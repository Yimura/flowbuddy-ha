"""Tests for async_setup_entry / async_unload_entry (config-entry wiring).

These exercise the full discovery -> coordinator-priming -> platform-forward
pipeline against fixtures, mirroring the respx-mocking style already used by
tests/test_config_flow.py. The happy path deliberately runs *real* platform
setup (sensor/binary_sensor/number/climate/button) rather than mocking
``async_forward_entry_setups`` away, so this test doubles as an end-to-end
check that the ``hass.data[DOMAIN][entry_id]`` shape this task builds is
actually consumable by every platform that depends on it.
"""

from __future__ import annotations

import asyncio
import contextlib

import httpx
import pytest
from homeassistant.config_entries import ConfigEntryState
from homeassistant.exceptions import ConfigEntryAuthFailed, ConfigEntryNotReady
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.flowbuddy import async_setup_entry
from custom_components.flowbuddy.const import (
    AUTH_MODE_CLIENT_CREDS,
    CONF_AUTH_MODE,
    CONF_INSTALLATION_ID,
    DOMAIN,
    KEYCLOAK_TOKEN_URL,
)

API_BASE = "https://izen.cast4all.energy/flexMon/v1"
IID = "00000000-0000-0000-0000-000000000001"


def _entry_data() -> dict:
    return {
        CONF_AUTH_MODE: AUTH_MODE_CLIENT_CREDS,
        "client_id": "cid",
        "client_secret": "secret",
        CONF_INSTALLATION_ID: IID,
    }


def _mock_full_discovery(respx_mock, load_fixture) -> None:
    """Mock every endpoint touched by a successful async_setup_entry run."""
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    respx_mock.get(f"{API_BASE}/installations").mock(
        return_value=httpx.Response(200, json=load_fixture("installations.json"))
    )
    respx_mock.get(f"{API_BASE}/meters").mock(
        return_value=httpx.Response(200, json=load_fixture("meters.json"))
    )
    respx_mock.get(f"{API_BASE}/measurementtypes").mock(
        return_value=httpx.Response(200, json=load_fixture("measurementtypes.json"))
    )
    respx_mock.get(f"{API_BASE}/measurements").mock(
        return_value=httpx.Response(200, json=load_fixture("measurements.json"))
    )
    respx_mock.get(f"{API_BASE}/batteries").mock(
        return_value=httpx.Response(200, json=load_fixture("batteries.json"))
    )
    respx_mock.get(f"{API_BASE}/inverters").mock(
        return_value=httpx.Response(200, json=load_fixture("inverters.json"))
    )
    respx_mock.get(f"{API_BASE}/hvacs").mock(
        return_value=httpx.Response(200, json=load_fixture("hvacs.json"))
    )
    respx_mock.get(f"{API_BASE}/communicators").mock(
        return_value=httpx.Response(200, json=load_fixture("communicators.json"))
    )
    respx_mock.get(f"{API_BASE}/realtimevalues").mock(
        return_value=httpx.Response(200, json=load_fixture("realtimevalues.json"))
    )
    respx_mock.get(f"{API_BASE}/aggregationdayvalues").mock(
        return_value=httpx.Response(200, json=load_fixture("aggregationdayvalues.json"))
    )
    respx_mock.get(f"{API_BASE}/alarms").mock(
        return_value=httpx.Response(200, json=load_fixture("alarms_open.json"))
    )


async def test_setup_entry_happy_path(hass, load_fixture, respx_mock):
    _mock_full_discovery(respx_mock, load_fixture)
    entry = MockConfigEntry(domain=DOMAIN, unique_id=IID, data=_entry_data())
    entry.add_to_hass(hass)

    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert entry.state is ConfigEntryState.LOADED
    data = hass.data[DOMAIN][entry.entry_id]

    # -- discovery data wired in ------------------------------------------------
    assert data["installation"].uuid == IID
    assert data["api"] is not None
    assert len(data["meters"]) == 3
    assert set(data["meters_by_uri"]) == {m.resource_uri for m in data["meters"]}
    assert len(data["measurements"]) == 6
    assert {mt.resource_uri for mt in data["measurementtypes_by_uri"].values()} == set(
        data["measurementtypes_by_uri"]
    )
    assert len(data["batteries"]) == 1
    assert len(data["inverters"]) == 1
    assert len(data["hvacs"]) == 1
    assert len(data["communicators"]) == 1
    assert data["communicators"][0].logical_device_name == "COMM-1"

    # -- coordinators created + primed (first refresh already ran) --------------
    assert data["instant_coord"].data
    assert data["daily_coord"].data
    assert data["alarms_coord"].data is not None
    assert len(data["alarms_coord"].data) == 1

    # -- all 5 platforms actually forwarded + created entities -------------------
    assert len(hass.states.async_entity_ids("sensor")) == 6
    assert len(hass.states.async_entity_ids("binary_sensor")) == 1
    assert len(hass.states.async_entity_ids("number")) == 2
    assert len(hass.states.async_entity_ids("climate")) == 1
    # 1 alarm-ack button + 1 connection-test button (from populated communicators fixture)
    assert len(hass.states.async_entity_ids("button")) == 2


async def test_setup_entry_registers_communicator_device(hass, load_fixture, respx_mock):
    """After async_setup_entry, the HA device registry should already
    contain the communicator device row -- even before any entity gets
    a chance to attach to it -- so the Devices UI shows firmware +
    serial as soon as setup finishes."""
    from homeassistant.helpers import device_registry as dr

    _mock_full_discovery(respx_mock, load_fixture)
    entry = MockConfigEntry(domain=DOMAIN, unique_id=IID, data=_entry_data())
    entry.add_to_hass(hass)

    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    device_reg = dr.async_get(hass)
    comm_device = device_reg.async_get_device(identifiers={(DOMAIN, "communicator:comm-1")})
    assert comm_device is not None
    assert comm_device.sw_version == "XMX_EMSA_V0.8.4"
    assert comm_device.model == "Lewiz"
    assert comm_device.serial_number == "COMM-1"


async def test_setup_entry_registers_installation_device(hass, load_fixture, respx_mock):
    """Every downstream device (meter, communicator, alarm-ack, connection-
    test button) sets via_device=(DOMAIN, installation_id). HA 2025.12
    hard-fails when that points at a not-yet-registered device. Prior to
    v0.2.1 the installation device was created lazily via whichever entity
    happened to attach to installation_device_info first -- if no such
    entity exists (no alarms + comm-button moved off installation), the
    via_device link dangles."""
    from homeassistant.helpers import device_registry as dr

    _mock_full_discovery(respx_mock, load_fixture)
    entry = MockConfigEntry(domain=DOMAIN, unique_id=IID, data=_entry_data())
    entry.add_to_hass(hass)

    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    device_reg = dr.async_get(hass)
    inst_device = device_reg.async_get_device(identifiers={(DOMAIN, IID)})
    assert inst_device is not None
    assert inst_device.model == "Residential PV+Battery"


async def test_setup_entry_invalid_creds_raises_auth_failed(hass, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(401, json=load_fixture("token_invalid_grant.json"))
    )
    entry = MockConfigEntry(domain=DOMAIN, unique_id=IID, data=_entry_data())
    entry.add_to_hass(hass)

    with pytest.raises(ConfigEntryAuthFailed):
        await async_setup_entry(hass, entry)

    # No half-populated hass.data left behind.
    assert entry.entry_id not in hass.data.get(DOMAIN, {})


async def test_setup_entry_transport_error_raises_not_ready(hass, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    respx_mock.get(f"{API_BASE}/installations").mock(side_effect=httpx.ConnectError("refused"))
    entry = MockConfigEntry(domain=DOMAIN, unique_id=IID, data=_entry_data())
    entry.add_to_hass(hass)

    with pytest.raises(ConfigEntryNotReady):
        await async_setup_entry(hass, entry)

    assert entry.entry_id not in hass.data.get(DOMAIN, {})


async def test_unload_entry(hass, load_fixture, respx_mock):
    _mock_full_discovery(respx_mock, load_fixture)
    entry = MockConfigEntry(domain=DOMAIN, unique_id=IID, data=_entry_data())
    entry.add_to_hass(hass)

    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    api = hass.data[DOMAIN][entry.entry_id]["api"]
    instant_coord = hass.data[DOMAIN][entry.entry_id]["instant_coord"]
    # Simulate a boost() in flight so unload's cleanup has something to cancel.
    boost_task = hass.loop.create_task(asyncio.sleep(3600))
    instant_coord._boost_task = boost_task

    assert await hass.config_entries.async_unload(entry.entry_id)
    await hass.async_block_till_done()
    with contextlib.suppress(asyncio.CancelledError):
        await boost_task

    assert entry.state is ConfigEntryState.NOT_LOADED
    assert entry.entry_id not in hass.data.get(DOMAIN, {})
    # Unloading a platform marks its entities unavailable rather than
    # deleting them outright (standard HA teardown behavior).
    sensor_states = [hass.states.get(eid) for eid in hass.states.async_entity_ids("sensor")]
    assert sensor_states and all(s.state == "unavailable" for s in sensor_states)
    # HA owns the httpx client lifecycle via create_async_httpx_client;
    # FlowBuddyClient.aclose() is intentionally a no-op so we don't tear
    # down a client HA reuses across integration reloads.
    assert not api._http.is_closed
    assert boost_task.cancelled()
