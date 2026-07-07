"""Tests for the FlowBuddyClient facade."""

from __future__ import annotations

import json
from datetime import date

import httpx
import pytest

from custom_components.flowbuddy.api import (
    FlowBuddyClient,
    PollingLimitExceededError,
)
from custom_components.flowbuddy.auth import KeycloakTokenProvider
from custom_components.flowbuddy.const import API_BASE_URL, KEYCLOAK_TOKEN_URL


@pytest.fixture
async def client(load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    http = httpx.AsyncClient()
    provider = KeycloakTokenProvider(
        mode="client_credentials",
        http=http,
        client_id="cid",
        client_secret="secret",
    )
    yield FlowBuddyClient(http=http, token_provider=provider)
    await http.aclose()


async def test_list_installations(client, load_fixture, respx_mock):
    respx_mock.get(f"{API_BASE_URL}/installations").mock(
        return_value=httpx.Response(200, json=load_fixture("installations.json"))
    )
    installations = await client.list_installations()
    assert len(installations) == 2
    assert installations[0].uuid == "00000000-0000-0000-0000-000000000001"
    assert installations[0].identification == "TEST-INST-1"


async def test_list_installations_tolerates_null_date_fields(
    client, load_fixture, respx_mock
):
    """Regression test: live tenant returns null for installationDate /
    dashboardCreatedOn when values are not set. Vendor spec declares those
    fields as string+date-time without nullable=true, so the generator's
    from_dict called datetime.fromisoformat(None) -> TypeError.

    Spec (openapi/flexmon-v1.json) is now patched to add nullable=true on
    every date-time field, so from_dict now returns None. This test locks
    that behavior in so a future regen against a re-fetched upstream spec
    (which would drop our nullable patch) fails loudly here instead of
    only on the live tenant.
    """
    respx_mock.get(f"{API_BASE_URL}/installations").mock(
        return_value=httpx.Response(200, json=load_fixture("installations.json"))
    )
    installations = await client.list_installations()
    inst_1 = next(i for i in installations if i.uuid.endswith("000001"))
    assert inst_1.installation_date is None
    assert inst_1.dashboard_created_on is None
    # Nested $ref properties also arrive null on the wire even though the
    # vendor spec doesn't declare them nullable — spec now patches every
    # $ref property with nullable=true (see openapi/flexmon-v1.json).
    assert inst_1.location is None
    assert inst_1.communicator is None
    assert inst_1.client_user_group is None
    assert inst_1.energy_tariff is None
    assert inst_1.installation_pool is None


async def test_get_instant_values(client, load_fixture, respx_mock):
    # NOTE: InstantValueOutputModel only formally types `resource_uri` in
    # the generated spec — `measurement`, `measurementType`, `value`, and
    # `timestart` land in `additional_properties` (dict-style access via
    # __getitem__) rather than as typed attributes. See report for detail.
    respx_mock.get(f"{API_BASE_URL}/realtimevalues").mock(
        return_value=httpx.Response(200, json=load_fixture("realtimevalues.json"))
    )
    iid = "00000000-0000-0000-0000-000000000001"
    values = await client.get_instant_values(iid)
    assert len(values) == 4
    pv_power = next(v for v in values if v["measurement"]["resourceUri"].endswith("m-pv-power"))
    assert pv_power["value"] == 1500.0


async def test_get_instant_values_filters_by_installation(client, load_fixture, respx_mock):
    """Client-side filter drops values belonging to other installations
    (upstream /realtimevalues has no installation filter -- see spec §5 Q7)."""
    respx_mock.get(f"{API_BASE_URL}/realtimevalues").mock(
        return_value=httpx.Response(200, json=load_fixture("realtimevalues.json"))
    )
    iid = "00000000-0000-0000-0000-000000000001"
    values = await client.get_instant_values(iid)
    # Fixture ships 4 values for ...000001 + 1 for ...000002; expect only 4.
    assert len(values) == 4
    for v in values:
        # Verify not the ...000002 sentinel
        assert v["value"] != 999.0


async def test_list_meters(client, load_fixture, respx_mock):
    respx_mock.get(f"{API_BASE_URL}/meters").mock(
        return_value=httpx.Response(200, json=load_fixture("meters.json"))
    )
    iid = "00000000-0000-0000-0000-000000000001"
    meters = await client.list_meters(iid)
    assert len(meters) == 3
    pv_meter = next(m for m in meters if m.name == "PV Inverter")
    assert pv_meter.serial_number == "TEST-SN-PV-1"
    assert pv_meter.meter_type == "PV"
    assert respx_mock.calls.last.request.url.params["installation"] == iid


async def test_list_measurementtypes(client, load_fixture, respx_mock):
    respx_mock.get(f"{API_BASE_URL}/measurementtypes").mock(
        return_value=httpx.Response(200, json=load_fixture("measurementtypes.json"))
    )
    mtypes = await client.list_measurementtypes()
    assert len(mtypes) == 14
    pv_power = next(m for m in mtypes if m.code == "PV_POWER")
    assert pv_power.unit == "W"
    assert pv_power.is_incremental is False


async def test_get_day_aggregations(client, load_fixture, respx_mock):
    respx_mock.get(f"{API_BASE_URL}/aggregationdayvalues").mock(
        return_value=httpx.Response(200, json=load_fixture("aggregationdayvalues.json"))
    )
    iid = "00000000-0000-0000-0000-000000000001"
    values = await client.get_day_aggregations(iid, date(2026, 7, 7))
    assert len(values) == 3
    pv_energy = next(v for v in values if v.measurement.resource_uri.endswith("m-pv-energy"))
    assert pv_energy.value == 8.5
    assert pv_energy.sum_ == 8.5
    assert pv_energy.count == 96

    params = respx_mock.calls.last.request.url.params
    assert params["installation"] == iid
    assert params["fromPeriodStart"].startswith("2026-07-07")
    assert params["toPeriodStart"].startswith("2026-07-08")


async def test_list_open_alarms(client, load_fixture, respx_mock):
    respx_mock.get(f"{API_BASE_URL}/alarms").mock(
        return_value=httpx.Response(200, json=load_fixture("alarms_open.json"))
    )
    iid = "00000000-0000-0000-0000-000000000001"
    alarms = await client.list_open_alarms(iid)
    assert len(alarms) == 1
    assert alarms[0].priority == "HIGH"
    assert alarms[0].status == "OPEN"

    params = respx_mock.calls.last.request.url.params
    assert params["installation"] == iid
    assert params["status"] == "OPEN"


async def test_set_battery_charge_power(client, respx_mock):
    route = respx_mock.post(f"{API_BASE_URL}/batteries/battery-1/setChargePower").mock(
        return_value=httpx.Response(204)
    )
    await client.set_battery_charge_power("battery-1", 2500)
    assert route.called
    body = json.loads(respx_mock.calls.last.request.content)
    assert body == {"value": 2500}


async def test_limit_inverter(client, respx_mock):
    route = respx_mock.post(f"{API_BASE_URL}/inverters/inverter-1/limitProduction").mock(
        return_value=httpx.Response(204)
    )
    await client.limit_inverter("inverter-1", 3000)
    assert route.called
    body = json.loads(respx_mock.calls.last.request.content)
    assert body == {"value": 3000}


async def test_set_hvac_cool(client, respx_mock):
    route = respx_mock.post(f"{API_BASE_URL}/hvacs/hvac-1/setCoolTemperature").mock(
        return_value=httpx.Response(204)
    )
    await client.set_hvac_cool("hvac-1", 21.5)
    assert route.called
    body = json.loads(respx_mock.calls.last.request.content)
    assert body == {"value": 21.5}


async def test_set_hvac_heat(client, respx_mock):
    route = respx_mock.post(f"{API_BASE_URL}/hvacs/hvac-1/setHeatTemperature").mock(
        return_value=httpx.Response(204)
    )
    await client.set_hvac_heat("hvac-1", 19.0)
    assert route.called
    body = json.loads(respx_mock.calls.last.request.content)
    assert body == {"value": 19.0}


async def test_close_alarm_without_comment(client, respx_mock):
    route = respx_mock.post(f"{API_BASE_URL}/alarms/alarm-1/setToClosed").mock(
        return_value=httpx.Response(204)
    )
    await client.close_alarm("alarm-1")
    assert route.called
    assert json.loads(respx_mock.calls.last.request.content) == {}


async def test_close_alarm_with_comment(client, respx_mock):
    comment_route = respx_mock.post(f"{API_BASE_URL}/alarms/alarm-1/addComment").mock(
        return_value=httpx.Response(204)
    )
    close_route = respx_mock.post(f"{API_BASE_URL}/alarms/alarm-1/setToClosed").mock(
        return_value=httpx.Response(204)
    )
    await client.close_alarm("alarm-1", comment="Resolved on-site")
    assert comment_route.called
    assert close_route.called
    comment_body = json.loads(comment_route.calls.last.request.content)
    assert comment_body == {"newComment": "Resolved on-site"}
    # The comment must be posted before the alarm is closed. (calls[-3] is
    # the token fetch made by the `client` fixture on first use.)
    assert respx_mock.calls[-2].request.url.path.endswith("/addComment")
    assert respx_mock.calls[-1].request.url.path.endswith("/setToClosed")


async def test_activate_continuous_processing_success(client, respx_mock):
    iid = "00000000-0000-0000-0000-000000000001"
    route = respx_mock.post(
        f"{API_BASE_URL}/installations/{iid}/activateContinuousProcessing"
    ).mock(return_value=httpx.Response(202))
    await client.activate_continuous_processing(iid)
    assert route.called
    assert route.calls.last.request.headers["Authorization"] == "Bearer test-access-token-abc123"


async def test_activate_continuous_processing_rate_limit(client, respx_mock, load_fixture):
    iid = "00000000-0000-0000-0000-000000000001"
    respx_mock.post(f"{API_BASE_URL}/installations/{iid}/activateContinuousProcessing").mock(
        return_value=httpx.Response(
            429, json={"code": "RL001", "extraInfo": {"message": "PollingLimitExceeded"}}
        )
    )
    with pytest.raises(PollingLimitExceededError):
        await client.activate_continuous_processing(iid)


async def test_activate_continuous_processing_rate_limit_via_body(client, respx_mock):
    """Vendor may signal PollingLimitExceeded via 4xx-with-body rather than 429."""
    iid = "00000000-0000-0000-0000-000000000001"
    respx_mock.post(f"{API_BASE_URL}/installations/{iid}/activateContinuousProcessing").mock(
        return_value=httpx.Response(
            400,
            json={
                "code": "RL001",
                "extraInfo": {"message": "PollingLimitExceeded on installation"},
            },
        )
    )
    with pytest.raises(PollingLimitExceededError):
        await client.activate_continuous_processing(iid)


async def test_request_connection_test(client, respx_mock):
    route = respx_mock.post(f"{API_BASE_URL}/communicators/comm-1/requestConnectionTest").mock(
        return_value=httpx.Response(204)
    )
    await client.request_connection_test("comm-1")
    assert route.called


async def test_list_batteries(client, load_fixture, respx_mock):
    respx_mock.get(f"{API_BASE_URL}/batteries").mock(
        return_value=httpx.Response(200, json=load_fixture("batteries.json"))
    )
    iid = "00000000-0000-0000-0000-000000000001"
    batteries = await client.list_batteries(iid)
    assert len(batteries) == 1
    assert batteries[0].external_id == "BAT-1"
    assert batteries[0].max_charge_power == 5000.0
    assert batteries[0].info.resource_uri == "/meters/meter-batt-1"


async def test_list_inverters(client, load_fixture, respx_mock):
    respx_mock.get(f"{API_BASE_URL}/inverters").mock(
        return_value=httpx.Response(200, json=load_fixture("inverters.json"))
    )
    iid = "00000000-0000-0000-0000-000000000001"
    inverters = await client.list_inverters(iid)
    assert len(inverters) == 1
    assert inverters[0].external_id == "INV-1"
    assert inverters[0].max_power == 8000.0
    assert inverters[0].info.resource_uri == "/meters/meter-pv-1"


async def test_list_hvacs(client, load_fixture, respx_mock):
    respx_mock.get(f"{API_BASE_URL}/hvacs").mock(
        return_value=httpx.Response(200, json=load_fixture("hvacs.json"))
    )
    iid = "00000000-0000-0000-0000-000000000001"
    hvacs = await client.list_hvacs(iid)
    assert len(hvacs) == 1
    assert hvacs[0].external_id == "HVAC-1"
    assert hvacs[0].last_set_cool_temperature == 21.5
    assert hvacs[0].info.resource_uri == "/meters/meter-grid-1"


async def test_list_communicators(client, load_fixture, respx_mock):
    respx_mock.get(f"{API_BASE_URL}/communicators").mock(
        return_value=httpx.Response(200, json=load_fixture("communicators.json"))
    )
    iid = "00000000-0000-0000-0000-000000000001"
    communicators = await client.list_communicators(iid)
    assert len(communicators) == 1
    assert communicators[0].logical_device_name == "COMM-1"
    assert communicators[0].external_id == "comm-1"


async def test_list_measurements(client, load_fixture, respx_mock):
    respx_mock.get(f"{API_BASE_URL}/measurements").mock(
        return_value=httpx.Response(200, json=load_fixture("measurements.json"))
    )
    iid = "00000000-0000-0000-0000-000000000001"
    measurements = await client.list_measurements(iid)
    assert len(measurements) == 6
    pv_power = next(m for m in measurements if m.resource_uri == "/measurements/m-pv-power")
    assert pv_power.meter.resource_uri == "/meters/meter-pv-1"
    assert pv_power.measurement_type.resource_uri == "/measurementtypes/pv-power"
    assert respx_mock.calls.last.request.url.params["installation"] == iid


async def test_aclose_is_noop_ha_owns_client_lifecycle(client):
    # HA's create_async_httpx_client returns an auto-cleaned shared client;
    # FlowBuddyClient.aclose() must NOT close it, otherwise integration
    # reload tears down a client HA still uses (frame.py:350 warning).
    await client.aclose()
    assert not client._http.is_closed
