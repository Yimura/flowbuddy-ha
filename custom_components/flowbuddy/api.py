"""Thin facade over the generated FlexMon v1 client."""

from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING, Any

from ._generated import client as _gen_client
from ._generated.api.aggregation_day_value_apis import (
    get_aggregation_day_value_details_list,
)
from ._generated.api.alarm_apis import add_comment, get_alarm_details_list, set_to_closed
from ._generated.api.battery_apis import set_charge_power
from ._generated.api.hvac_apis import set_cool_temperature, set_heat_temperature
from ._generated.api.installation_apis import get_installation_details_list
from ._generated.api.instant_value_apis import get_instant_value_details_list
from ._generated.api.inverter_apis import limit_production
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
    InstallationOutputModel as Installation,
)
from ._generated.models import (
    InstantValueOutputModel as InstantValue,
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


class FlowBuddyClient:
    """Facade over the generated FlexMon v1 client + our Keycloak auth."""

    def __init__(self, *, http: httpx.AsyncClient, token_provider: KeycloakTokenProvider) -> None:
        self._http = http
        self._token = token_provider
        # The bearer token is injected per-request via our httpx.Auth
        # adapter (httpx_args={"auth": ...}); the static `token=` value is
        # a placeholder immediately overwritten by that auth flow.
        self._client = _gen_client.AuthenticatedClient(
            base_url=API_BASE_URL,
            token="unused-injected-by-httpx-auth",
            httpx_args={"auth": token_provider.httpx_auth()},
        )

    async def list_installations(self) -> list[Installation]:
        result = await get_installation_details_list.asyncio(
            client=self._client, pagesize=_LIST_PAGESIZE
        )
        return _embedded_list(result, "installations", "installations", Installation)

    async def get_instant_values(self, installation_id: str) -> list[InstantValue]:
        # NOTE: the generated /instantvalues endpoint has no `installation`
        # filter param in the public spec — FlexMon scopes instant values
        # implicitly to the authenticated client credentials.
        # installation_id is kept in the signature per the facade's
        # interface contract but is not forwarded as a query param.
        result = await get_instant_value_details_list.asyncio(
            client=self._client, pagesize=_LIST_PAGESIZE
        )
        return _embedded_list(result, "instant_values", "instantvalues", InstantValue)

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
