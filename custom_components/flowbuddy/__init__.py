"""The FlowBuddy integration.

``async_setup`` registers the five FlowBuddy services (see spec §4.5 /
``services.yaml``) exactly once, independent of any config entry -- service
handlers look up the right API client / coordinator at call time via
``hass.data[DOMAIN]``, which ``async_setup_entry`` (P9.A) populates per
config entry with at least ``installation``, ``api`` and ``instant_coord``
keys (mirroring the shape already relied on by ``number.py``/``button.py``).

``async_setup_entry`` here is a placeholder -- P9.A replaces it with the
real coordinator/data wiring (auth, coordinators, forwarding to platforms).
It must exist so config-entry setup does not fail while that work lands.
"""

from __future__ import annotations

import logging
import time
from typing import Any

import voluptuous as vol
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.exceptions import ServiceValidationError
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import issue_registry as ir
from homeassistant.helpers.typing import ConfigType

from .api import PollingLimitExceededError
from .const import DOMAIN, POLLING_LIMIT_BLOCK_S

_LOGGER = logging.getLogger(__name__)

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
    """Find the config-entry data dict whose installation.uuid matches."""
    for data in _entries(hass).values():
        installation = data.get("installation")
        if installation is not None and getattr(installation, "uuid", None) == installation_id:
            return data
    return None


def _find_number_target(
    hass: HomeAssistant, entity_id: str, *, kind: str, unique_id_suffix: str
) -> tuple[Any, str]:
    """Resolve a ``number.*`` entity_id to (api, external_id) for its battery/inverter.

    ``kind`` is ``"battery"`` or ``"inverter"`` and matches the segment used
    by ``number.py`` when it built each entity's unique_id
    (``f"{installation.uuid}:{kind}:{item.resource_uri}:{unique_id_suffix}"``).
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
        for item in data.get(list_key, []):
            candidate = f"{installation.uuid}:{kind}:{item.resource_uri}:{unique_id_suffix}"
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


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up a FlowBuddy config entry.

    PLACEHOLDER: real coordinator/API/data wiring lands in P9.A. This stub
    exists only so config-entry setup does not fail while services (this
    task) and the full entry setup (P9.A) are developed independently.
    """
    return True
