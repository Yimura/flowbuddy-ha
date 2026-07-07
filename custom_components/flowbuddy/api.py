"""Thin facade over the generated FlexMon v1 client."""

from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING, Any

from ._generated import client as _gen_client
from ._generated.api.aggregation_day_value_apis import (
    get_aggregation_day_value_details_list,
)
from ._generated.api.alarm_apis import add_comment, get_alarm_details_list, set_to_closed
from ._generated.api.battery_apis import get_battery_details_list, set_charge_power
from ._generated.api.communicator_apis import (
    get_communicator_details_list,
    request_connection_test,
)
from ._generated.api.hvac_apis import (
    get_hvac_details_list,
    set_cool_temperature,
    set_heat_temperature,
)
from ._generated.api.installation_apis import get_installation_details_list
from ._generated.api.instant_value_apis import get_instant_value_details_list
from ._generated.api.inverter_apis import get_inverter_details_list, limit_production
from ._generated.api.measurement_apis import get_measurement_details_list
from ._generated.api.measurement_type_apis import get_measurement_type_details_list
from ._generated.api.meter_apis import get_meter_details_list
from ._generated.models import (
    AggregationDayValueOutputModel as AggregationDayValue,
)
from ._generated.models import (
    AlarmAddCommentPostInputModel,
    AlarmSetToClosedPostInputModel,
    BatterySetChargePowerPostInputModel,
    HVACSetCoolTemperaturePostInputModel,
    HVACSetHeatTemperaturePostInputModel,
    InverterLimitProductionPostInputModel,
)
from ._generated.models import (
    AlarmOutputModel as Alarm,
)
from ._generated.models import (
    BatteryOutputModel as Battery,
)
from ._generated.models import (
    CommunicatorOutputModel as Communicator,
)
from ._generated.models import (
    HVACOutputModel as Hvac,
)
from ._generated.models import (
    InstallationOutputModel as Installation,
)
from ._generated.models import (
    InstantValueOutputModel as InstantValue,
)
from ._generated.models import (
    InverterOutputModel as Inverter,
)
from ._generated.models import (
    MeasurementOutputModel as Measurement,
)
from ._generated.models import (
    MeasurementTypeOutputModel as MeasurementType,
)
from ._generated.models import (
    MeterOutputModel as Meter,
)
from ._generated.types import UNSET, Unset
from .const import API_BASE_URL

if TYPE_CHECKING:
    import httpx

    from .auth import KeycloakTokenProvider

_LIST_PAGESIZE = 500


class PollingLimitExceededError(Exception):
    """Raised when the vendor signals a per-installation polling block."""


def _embedded_list(
    result: object, typed_attr: str, raw_key: str, model_cls: type[Any]
) -> list[Any]:
    """Pull the embedded list out of a ``PaginatedResponse*Model``.

    Works around a vendor spec/runtime mismatch: some OpenAPI-declared
    embedded property names (e.g. ``instantValues``) are camelCase, but the
    live FlexMon API actually emits all-lowercase concatenated keys (e.g.
    ``instantvalues`` — matching the URL path segment). The generated
    ``from_dict`` only pops the spec-declared key, so on a genuine payload
    the typed attribute is left ``UNSET`` while the untouched raw list
    survives inside ``additional_properties``. Fall back to that.
    """
    embedded = getattr(result, "field_embedded", UNSET)
    if isinstance(embedded, Unset) or embedded is None:
        return []
    typed = getattr(embedded, typed_attr, UNSET)
    if not isinstance(typed, Unset) and typed is not None:
        return list(typed)
    raw = embedded.additional_properties.get(raw_key) or []
    return [model_cls.from_dict(item) for item in raw]


def _instant_value_installation_ref(item: InstantValue) -> str | None:
    """Best-effort extraction of an instant value's owning installation.

    ``InstantValueOutputModel`` is under-typed by the generator: only
    ``resource_uri`` is a real attribute, so ``measurement`` (and its
    nested ``installation``) lands as a raw dict inside
    ``additional_properties`` rather than as typed sub-models. Try the
    typed attribute path first in case a future codegen run types it,
    then fall back to raw dict access under both the camelCase spelling
    that the live API actually emits and the snake_case spelling used
    elsewhere in this codebase.
    """
    try:
        ref = item.measurement.installation.resource_uri  # type: ignore[attr-defined]
        if isinstance(ref, str):
            return ref
    except AttributeError:
        pass

    measurement = item.additional_properties.get("measurement")
    if not isinstance(measurement, dict):
        return None
    installation = measurement.get("installation")
    if not isinstance(installation, dict):
        return None
    ref = installation.get("resourceUri") or installation.get("resource_uri")
    return ref if isinstance(ref, str) else None


def installation_id(installation: Any) -> str | None:
    """Return a usable identifier for an Installation.

    Vendor sometimes returns ``uuid=null`` even though the installation
    obviously has one (it appears in ``resourceUri``). Fall back through
    ``resource_uri`` (last path segment) and ``external_id``. Returns
    None only if all three are null/empty.
    """
    for attr in ("uuid",):
        v = getattr(installation, attr, None)
        if isinstance(v, str) and v.strip():
            return v.strip()
    ru = getattr(installation, "resource_uri", None)
    if isinstance(ru, str) and "/" in ru:
        seg = ru.rstrip("/").rsplit("/", 1)[-1].strip()
        if seg:
            return seg
    ext = getattr(installation, "external_id", None)
    if isinstance(ext, str) and ext.strip():
        return ext.strip()
    return None


class FlowBuddyClient:
    """Facade over the generated FlexMon v1 client + our Keycloak auth."""

    def __init__(self, *, http: httpx.AsyncClient, token_provider: KeycloakTokenProvider) -> None:
        self._http = http
        self._token = token_provider
        # The bearer token is injected per-request via our httpx.Auth
        # adapter (httpx_args={"auth": ...}); the static `token=` value is
        # a placeholder immediately overwritten by that auth flow.
        #
        # The generated AuthenticatedClient lazily constructs its OWN
        # internal httpx.AsyncClient on first request. Passing verify=<ctx>
        # via httpx_args reuses HA's already-loaded SSL context (loaded off
        # the event loop at HA start) instead of triggering the blocking
        # ssl.SSLContext.load_verify_locations() the first time a request
        # is made -- otherwise HA's blocking-call detector fires from
        # inside get_async_httpx_client().
        verify_ssl: Any = True
        try:
            from homeassistant.util.ssl import get_default_context

            verify_ssl = get_default_context()
        except ImportError:
            # Running outside HA (unit tests without hass helpers). httpx
            # default `verify=True` is fine because respx intercepts at the
            # transport layer before any actual SSL handshake.
            pass
        self._client = _gen_client.AuthenticatedClient(
            base_url=API_BASE_URL,
            token="unused-injected-by-httpx-auth",
            verify_ssl=verify_ssl,
            httpx_args={"auth": token_provider.httpx_auth()},
        )

    async def list_installations(self) -> list[Installation]:
        result = await get_installation_details_list.asyncio(
            client=self._client, pagesize=_LIST_PAGESIZE
        )
        return _embedded_list(result, "installations", "installations", Installation)

    async def get_instant_values(self, installation_id: str) -> list[Any]:
        """Return live values for the given installation.

        Backed by ``GET /flexMon/v1/realtimevalues`` — the SPA's live-data
        endpoint. Spec §5 Q10 (Gate B live probe 2026-07-07) established
        that ``/instantvalues`` is installer-only (403 for residents) and
        the resident-scope replacement is ``/realtimevalues``. The path
        is not modelled in the vendored OpenAPI spec, so we bypass the
        generated client and call it directly via ``self._http``; auth is
        applied via the client-level ``auth`` hook attached at
        construction. Returns raw dict rows (no typed model exists) —
        callers should read ``resource_uri`` / ``measurement`` /
        ``value`` / ``timestamp`` via dict access.
        """
        url = f"{API_BASE_URL}/realtimevalues?pagesize={_LIST_PAGESIZE}"
        resp = await self._http.get(url, auth=self._token.httpx_auth())
        if resp.status_code == 403:
            # Installer-scope tenants may have moved the endpoint or the
            # user's credentials lack the resident realtime role. Treat as
            # "no data available" instead of failing setup.
            return []
        resp.raise_for_status()
        body = resp.json()
        embedded = body.get("_embedded", {}) if isinstance(body, dict) else {}
        # HAL+JSON multi-word keys are camelCase in real responses.
        rows = embedded.get("realtimeValues") or embedded.get("realtimevalues") or []
        suffix = f"/installations/{installation_id}"
        # Filter client-side by measurement.installation.resourceUri —
        # /realtimevalues has no per-installation filter param either.
        return [
            row for row in rows
            if isinstance(row, dict)
            and (
                (row.get("measurement", {}) or {})
                .get("installation", {}) or {}
            ).get("resourceUri", "").endswith(suffix)
        ]

    async def list_meters(self, installation_id: str) -> list[Meter]:
        result = await get_meter_details_list.asyncio(
            client=self._client, installation=installation_id, pagesize=_LIST_PAGESIZE
        )
        return _embedded_list(result, "meters", "meters", Meter)

    async def list_measurementtypes(self) -> list[MeasurementType]:
        result = await get_measurement_type_details_list.asyncio(
            client=self._client, pagesize=_LIST_PAGESIZE
        )
        return _embedded_list(result, "measurement_types", "measurementtypes", MeasurementType)

    async def get_day_aggregations(
        self, installation_id: str, day: dt.date
    ) -> list[AggregationDayValue]:
        start = dt.datetime.combine(day, dt.time.min, tzinfo=dt.UTC)
        stop = start + dt.timedelta(days=1)
        result = await get_aggregation_day_value_details_list.asyncio(
            client=self._client,
            installation=installation_id,
            from_period_start=start,
            to_period_start=stop,
            pagesize=_LIST_PAGESIZE,
        )
        return _embedded_list(
            result, "aggregation_day_values", "aggregationdayvalues", AggregationDayValue
        )

    async def list_open_alarms(self, installation_id: str) -> list[Alarm]:
        result = await get_alarm_details_list.asyncio(
            client=self._client,
            installation=installation_id,
            status="OPEN",
            pagesize=_LIST_PAGESIZE,
        )
        return _embedded_list(result, "alarms", "alarms", Alarm)

    async def set_battery_charge_power(self, battery_id: str, watts: int) -> None:
        await set_charge_power.asyncio(
            battery_id,
            client=self._client,
            body=BatterySetChargePowerPostInputModel(value=watts),
        )

    async def limit_inverter(self, inverter_id: str, watts: int) -> None:
        await limit_production.asyncio(
            inverter_id,
            client=self._client,
            body=InverterLimitProductionPostInputModel(value=watts),
        )

    async def set_hvac_cool(self, hvac_id: str, celsius: float) -> None:
        await set_cool_temperature.asyncio(
            hvac_id,
            client=self._client,
            body=HVACSetCoolTemperaturePostInputModel(value=celsius),
        )

    async def set_hvac_heat(self, hvac_id: str, celsius: float) -> None:
        await set_heat_temperature.asyncio(
            hvac_id,
            client=self._client,
            body=HVACSetHeatTemperaturePostInputModel(value=celsius),
        )

    async def close_alarm(self, alarm_id: str, comment: str | None = None) -> None:
        if comment is not None:
            await add_comment.asyncio(
                alarm_id,
                client=self._client,
                body=AlarmAddCommentPostInputModel(new_comment=comment),
            )
        await set_to_closed.asyncio(
            alarm_id, client=self._client, body=AlarmSetToClosedPostInputModel()
        )

    async def request_connection_test(self, communicator_id: str) -> None:
        await request_connection_test.asyncio(communicator_id, client=self._client)

    async def list_batteries(self, installation_id: str) -> list[Battery]:
        """Return all batteries visible to the credentialed account.

        NOTE: unlike ``/meters`` or ``/measurements``, the vendor's
        ``/batteries`` endpoint has no ``installation`` query parameter
        (confirmed against the generated client -- see
        ``_generated/api/battery_apis/get_battery_details_list.py``), and
        ``BatteryOutputModel`` carries no installation reference of its own
        to filter on client-side either -- only a link to its owning meter
        via ``info.resource_uri``. Downstream consumers (``number.py``)
        already narrow the result down implicitly by only matching
        batteries whose ``info.resource_uri`` appears in this
        installation's ``meters_by_uri``, so no filtering happens here.
        ``installation_id`` is accepted for symmetry with the other
        discovery facades and to leave room for a future server-side filter.
        """
        result = await get_battery_details_list.asyncio(
            client=self._client, pagesize=_LIST_PAGESIZE
        )
        return _embedded_list(result, "batteries", "batteries", Battery)

    async def list_inverters(self, installation_id: str) -> list[Inverter]:
        """Return all inverters visible to the credentialed account.

        See ``list_batteries`` -- ``/inverters`` has the same
        no-installation-filter limitation, worked around downstream the
        same way via each inverter's ``info.resource_uri`` meter link.
        """
        result = await get_inverter_details_list.asyncio(
            client=self._client, pagesize=_LIST_PAGESIZE
        )
        return _embedded_list(result, "inverters", "inverters", Inverter)

    async def list_hvacs(self, installation_id: str) -> list[Hvac]:
        """Return all HVAC units visible to the credentialed account.

        See ``list_batteries`` -- ``/hvacs`` has the same
        no-installation-filter limitation.
        """
        result = await get_hvac_details_list.asyncio(client=self._client, pagesize=_LIST_PAGESIZE)
        return _embedded_list(result, "hvacs", "hvacs", Hvac)

    async def list_communicators(self, installation_id: str) -> list[Communicator]:
        """Return all communicators visible to the credentialed account.

        Same ``/communicators``-has-no-installation-filter limitation as
        ``list_batteries``, except here there is not even a meter link to
        narrow down by client-side afterwards: ``CommunicatorOutputModel``
        carries no installation or meter reference at all.
        """
        result = await get_communicator_details_list.asyncio(
            client=self._client, pagesize=_LIST_PAGESIZE
        )
        return _embedded_list(result, "communicators", "communicators", Communicator)

    async def list_measurements(self, installation_id: str) -> list[Measurement]:
        """Return every measurement registered for the given installation.

        Unlike batteries/inverters/hvacs/communicators, ``/measurements``
        does accept a server-side ``installation`` filter (see
        ``_generated/api/measurement_apis/get_measurement_details_list.py``),
        so -- like ``list_meters`` -- no client-side filtering is needed.
        """
        result = await get_measurement_details_list.asyncio(
            client=self._client, installation=installation_id, pagesize=_LIST_PAGESIZE
        )
        return _embedded_list(result, "measurements", "measurements", Measurement)

    async def aclose(self) -> None:
        """No-op teardown hook.

        Since we now use ``homeassistant.helpers.httpx_client.create_async_httpx_client``,
        HA owns the client lifecycle (auto_cleanup=True). Closing it here
        would tear down a client HA reuses across integration reloads and
        trigger a ``frame.py:350`` warning. Kept as a stable method name so
        callers do not need to know about the ownership transfer.
        """
        return None

    async def activate_continuous_processing(self, installation_id: str) -> None:
        url = f"{API_BASE_URL}/installations/{installation_id}/activateContinuousProcessing"
        auth = self._token.httpx_auth()
        # Not in the public OpenAPI spec — call directly with our httpx client.
        resp = await self._http.post(url, auth=auth)
        if resp.status_code == 429 or (
            resp.status_code >= 400 and "PollingLimitExceeded" in resp.text
        ):
            raise PollingLimitExceededError(resp.text)
        resp.raise_for_status()
