"""The FlowBuddy integration.

``async_setup`` registers the five FlowBuddy services (see spec §4.5 /
``services.yaml``) exactly once, independent of any config entry -- service
handlers look up the right API client / coordinator at call time via
``hass.data[DOMAIN]``, which ``async_setup_entry`` populates per config entry
with the shape documented on ``PLATFORMS``/below (mirroring what
``number.py``/``button.py``/``sensor.py``/``binary_sensor.py``/``climate.py``
already rely on).

``async_setup_entry`` authenticates against Keycloak, runs installation +
meter/measurement/battery/inverter/hvac/communicator discovery, creates and
primes the three coordinators, stores everything in
``hass.data[DOMAIN][entry.entry_id]``, then forwards to the five platforms.
"""

from __future__ import annotations

import asyncio
import logging
import time
from typing import TYPE_CHECKING, Any

import voluptuous as vol
from homeassistant.exceptions import (
    ConfigEntryAuthFailed,
    ConfigEntryNotReady,
    ServiceValidationError,
)
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import issue_registry as ir
from homeassistant.helpers.httpx_client import create_async_httpx_client

from .api import FlowBuddyClient, PollingLimitExceededError
from .api import installation_id as _installation_id
from .auth import InvalidCredentialsError, KeycloakTokenProvider
from .const import (
    AUTH_MODE_PASSWORD,
    CONF_AUTH_MODE,
    CONF_INSTALLATION_ID,
    DOMAIN,
    POLLING_LIMIT_BLOCK_S,
)
from .coordinator import (
    FlowBuddyAlarmsCoordinator,
    FlowBuddyDailyCoordinator,
    FlowBuddyInstantCoordinator,
)
from .entity import communicator_device_info

if TYPE_CHECKING:
    from collections.abc import Mapping

    import httpx
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.core import HomeAssistant, ServiceCall
    from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

# Platforms forwarded by every FlowBuddy config entry; shared between
# async_setup_entry (forward) and async_unload_entry (unload) so the two
# lists can never drift apart.
PLATFORMS: list[str] = ["sensor", "binary_sensor", "number", "climate", "button"]

SERVICE_SET_BATTERY_CHARGE_POWER = "set_battery_charge_power"
SERVICE_LIMIT_INVERTER = "limit_inverter"
SERVICE_ACK_ALARM = "ack_alarm"
SERVICE_REQUEST_CONNECTION_TEST = "request_connection_test"
SERVICE_ENABLE_REALTIME = "enable_realtime"

_SET_BATTERY_CHARGE_POWER_SCHEMA = vol.Schema(
    {
        vol.Required("entity_id"): cv.entity_id,
        vol.Required("watts"): vol.Coerce(int),
    }
)

_LIMIT_INVERTER_SCHEMA = vol.Schema(
    {
        vol.Required("entity_id"): cv.entity_id,
        vol.Required("watts"): vol.Coerce(int),
    }
)

_ACK_ALARM_SCHEMA = vol.Schema(
    {
        vol.Required("alarm_id"): cv.string,
        vol.Optional("comment"): cv.string,
    }
)

_REQUEST_CONNECTION_TEST_SCHEMA = vol.Schema(
    {
        vol.Required("communicator_id"): cv.string,
    }
)

_ENABLE_REALTIME_SCHEMA = vol.Schema(
    {
        vol.Required("installation_id"): cv.string,
        vol.Optional("duration_minutes", default=5): vol.All(
            vol.Coerce(int), vol.Range(min=1, max=5)
        ),
    }
)


def _entries(hass: HomeAssistant) -> dict[str, dict[str, Any]]:
    """Return the per-config-entry data dicts populated by async_setup_entry."""
    domain_data: dict[str, dict[str, Any]] = hass.data.get(DOMAIN, {})
    return domain_data


def _find_entry_by_installation(hass: HomeAssistant, installation_id: str) -> dict[str, Any] | None:
    """Find the config-entry data dict whose installation id matches.

    Uses ``installation_id()`` (with the same ``or "unknown"`` fallback every
    entity's unique_id already applies) rather than raw ``installation.uuid``
    -- the vendor can return ``uuid=null`` for a tenant, in which case every
    entity was built keyed off the fallback string, and service resolution
    must match that same string or it can never find the entry.
    """
    for data in _entries(hass).values():
        installation = data.get("installation")
        if (
            installation is not None
            and (_installation_id(installation) or "unknown") == installation_id
        ):
            return data
    return None


def _find_number_target(
    hass: HomeAssistant, entity_id: str, *, kind: str, unique_id_suffix: str
) -> tuple[Any, str]:
    """Resolve a ``number.*`` entity_id to (api, external_id) for its battery/inverter.

    ``kind`` is ``"battery"`` or ``"inverter"`` and matches the segment used
    by ``number.py`` when it built each entity's unique_id
    (``f"{installation_id(installation) or 'unknown'}:{kind}:{item.resource_uri}:{unique_id_suffix}"``).
    We look the entity up in the entity registry to get its unique_id, then
    recompute that same unique_id for every battery/inverter cached in
    ``hass.data[DOMAIN]`` until we find the match -- this avoids depending on
    any HA-internal "get the live entity object" API.
    """
    registry = er.async_get(hass)
    registry_entry = registry.async_get(entity_id)
    unique_id = registry_entry.unique_id if registry_entry is not None else None
    list_key = "batteries" if kind == "battery" else "inverters"

    for data in _entries(hass).values():
        installation = data.get("installation")
        api = data.get("api")
        if installation is None or api is None:
            continue
        installation_uuid = _installation_id(installation) or "unknown"
        for item in data.get(list_key, []):
            candidate = f"{installation_uuid}:{kind}:{item.resource_uri}:{unique_id_suffix}"
            if unique_id is not None and candidate == unique_id:
                return api, item.external_id

    raise ServiceValidationError(f"Could not resolve {entity_id} to a FlowBuddy {kind}")


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Register FlowBuddy services once, independent of config entries."""

    async def handle_set_battery_charge_power(call: ServiceCall) -> None:
        api, battery_id = _find_number_target(
            hass, call.data["entity_id"], kind="battery", unique_id_suffix="charge_power"
        )
        await api.set_battery_charge_power(battery_id, call.data["watts"])

    async def handle_limit_inverter(call: ServiceCall) -> None:
        api, inverter_id = _find_number_target(
            hass, call.data["entity_id"], kind="inverter", unique_id_suffix="production_limit"
        )
        await api.limit_inverter(inverter_id, call.data["watts"])

    async def handle_ack_alarm(call: ServiceCall) -> None:
        alarm_id = call.data["alarm_id"]
        comment = call.data.get("comment")
        for data in _entries(hass).values():
            api = data.get("api")
            if api is not None:
                await api.close_alarm(alarm_id, comment)
                return
        raise ServiceValidationError("No configured FlowBuddy installation found")

    async def handle_request_connection_test(call: ServiceCall) -> None:
        communicator_id = call.data["communicator_id"]
        for data in _entries(hass).values():
            api = data.get("api")
            if api is not None:
                await api.request_connection_test(communicator_id)
                return
        raise ServiceValidationError("No configured FlowBuddy installation found")

    async def handle_enable_realtime(call: ServiceCall) -> None:
        installation_id = call.data["installation_id"]
        duration_minutes = call.data["duration_minutes"]
        data = _find_entry_by_installation(hass, installation_id)
        if data is None:
            raise ServiceValidationError(f"Unknown FlowBuddy installation {installation_id}")

        coord = data.get("instant_coord")
        if coord is None:
            raise ServiceValidationError(
                f"FlowBuddy installation {installation_id} has no live-polling coordinator"
            )
        try:
            await coord.boost(duration_minutes)
        except PollingLimitExceededError as exc:
            blocked_until = getattr(coord, "_blocked_until", None)
            block_remaining_s = (
                max(0, int(blocked_until - time.monotonic()))
                if blocked_until is not None
                else POLLING_LIMIT_BLOCK_S
            )
            ir.async_create_issue(
                hass,
                DOMAIN,
                f"polling_limit_{installation_id}",
                is_fixable=False,
                severity=ir.IssueSeverity.WARNING,
                translation_key="polling_limit_exceeded",
                translation_placeholders={
                    "installation_id": installation_id,
                    "retry_seconds": str(block_remaining_s),
                },
            )
            raise ServiceValidationError(
                f"FlowBuddy blocked live polling for installation {installation_id}. "
                f"Retry in {block_remaining_s} seconds."
            ) from exc

    hass.services.async_register(
        DOMAIN,
        SERVICE_SET_BATTERY_CHARGE_POWER,
        handle_set_battery_charge_power,
        schema=_SET_BATTERY_CHARGE_POWER_SCHEMA,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_LIMIT_INVERTER,
        handle_limit_inverter,
        schema=_LIMIT_INVERTER_SCHEMA,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_ACK_ALARM,
        handle_ack_alarm,
        schema=_ACK_ALARM_SCHEMA,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_REQUEST_CONNECTION_TEST,
        handle_request_connection_test,
        schema=_REQUEST_CONNECTION_TEST_SCHEMA,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_ENABLE_REALTIME,
        handle_enable_realtime,
        schema=_ENABLE_REALTIME_SCHEMA,
    )

    return True


def _build_token_provider(
    http: httpx.AsyncClient, data: Mapping[str, Any]
) -> KeycloakTokenProvider:
    """Build a KeycloakTokenProvider from a config entry's stored credentials.

    ``config_flow.py`` always writes a ``client_id`` into ``entry.data`` for
    both auth modes (defaulting it for the password grant -- see
    ``FlowBuddyConfigFlow._async_finish``), so no default is needed here.
    """
    if data.get(CONF_AUTH_MODE) == AUTH_MODE_PASSWORD:
        return KeycloakTokenProvider(
            mode="password",
            http=http,
            client_id=data["client_id"],
            username=data["email"],
            password=data["password"],
        )
    return KeycloakTokenProvider(
        mode="client_credentials",
        http=http,
        client_id=data["client_id"],
        client_secret=data["client_secret"],
    )


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up a FlowBuddy config entry.

    Creates the auth/API client, runs installation + fleet discovery,
    creates and primes the three coordinators, stores everything in
    ``hass.data[DOMAIN][entry.entry_id]`` and forwards to ``PLATFORMS``.
    """
    # Each config entry gets its own httpx.AsyncClient (and therefore its own
    # connection pool) rather than sharing one across entries. Spec §5 Q9
    # left this decision to P9.A; the call made at the P3 review was to
    # DEFER the shared-client refactor and ship the simpler private-pool
    # version first.
    #
    # Direct httpx.AsyncClient() calls ssl.SSLContext.load_verify_locations()
    # during __init__ — a blocking file read that HA's blocking-call detector
    # treats as an error inside the event loop. Use HA's helper which returns
    # a client backed by HA's pre-warmed shared SSL context.
    http = create_async_httpx_client(hass)
    api = FlowBuddyClient(http=http, token_provider=_build_token_provider(http, entry.data))
    installation_id = entry.data[CONF_INSTALLATION_ID]

    try:
        installations = await api.list_installations()
    except InvalidCredentialsError as exc:
        raise ConfigEntryAuthFailed(str(exc)) from exc
    except Exception as exc:
        raise ConfigEntryNotReady(f"Error communicating with FlowBuddy: {exc}") from exc

    installation = next((i for i in installations if _installation_id(i) == installation_id), None)
    if installation is None:
        raise ConfigEntryNotReady(
            f"Installation {installation_id} was not found for these credentials"
        )

    try:
        # asyncio.gather's typeshed overloads only cover a fixed number of
        # distinctly-typed arguments; beyond that arity it falls back to a
        # homogeneous signature, so mypy would otherwise infer each unpacked
        # name below as `object`. Route through an explicit `list[Any]` to
        # match what gather actually returns at runtime.
        results: list[Any] = await asyncio.gather(
            api.list_meters(installation_id),
            api.list_measurementtypes(),
            api.list_measurements(installation_id),
            api.list_batteries(installation_id),
            api.list_inverters(installation_id),
            api.list_hvacs(installation_id),
            api.list_communicators(installation_id),
        )
        (
            meters,
            measurementtypes,
            measurements,
            batteries,
            inverters,
            hvacs,
            communicators,
        ) = results
    except InvalidCredentialsError as exc:
        raise ConfigEntryAuthFailed(str(exc)) from exc
    except Exception as exc:
        raise ConfigEntryNotReady(f"Error communicating with FlowBuddy: {exc}") from exc

    entry_data: dict[str, Any] = {
        "api": api,
        "installation": installation,
        "meters": meters,
        "meters_by_uri": {m.resource_uri: m for m in meters},
        "measurements": measurements,
        "measurementtypes_by_uri": {mt.resource_uri: mt for mt in measurementtypes},
        "batteries": batteries,
        "inverters": inverters,
        "hvacs": hvacs,
        "communicators": communicators,
        "instant_coord": FlowBuddyInstantCoordinator(hass, api, installation_id),
        "daily_coord": FlowBuddyDailyCoordinator(hass, api, installation_id),
        "alarms_coord": FlowBuddyAlarmsCoordinator(hass, api, installation_id),
    }
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = entry_data

    # Register communicator devices eagerly so the Devices UI shows firmware
    # + serial as soon as discovery finishes -- independent of whether the
    # button platform manages to attach an entity to each communicator.
    dev_reg = dr.async_get(hass)
    for comm in communicators:
        dev_reg.async_get_or_create(
            config_entry_id=entry.entry_id,
            **communicator_device_info(comm, installation),
        )

    try:
        # Prime every coordinator before forwarding to platforms: button.py
        # and binary_sensor.py build their initial entity list directly from
        # alarms_coord.data, so it (and the others, for consistency) must
        # already hold data by the time platform setup runs.
        await entry_data["instant_coord"].async_config_entry_first_refresh()
        await entry_data["daily_coord"].async_config_entry_first_refresh()
        await entry_data["alarms_coord"].async_config_entry_first_refresh()
    except ConfigEntryNotReady:
        hass.data[DOMAIN].pop(entry.entry_id, None)
        raise

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a FlowBuddy config entry: unload platforms, then clean up."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        entry_data = hass.data[DOMAIN].pop(entry.entry_id)
        instant_coord = entry_data.get("instant_coord")
        boost_task = getattr(instant_coord, "_boost_task", None)
        if boost_task is not None and not boost_task.done():
            boost_task.cancel()
        api = entry_data.get("api")
        if api is not None:
            await api.aclose()
    return unload_ok
