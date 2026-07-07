"""Tests for FlowBuddy service registration and handlers."""

from __future__ import annotations

import time
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest
from homeassistant.exceptions import ServiceValidationError
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import issue_registry as ir

from custom_components.flowbuddy import DOMAIN, async_setup
from custom_components.flowbuddy.api import PollingLimitExceededError


def _installation(uuid: str) -> SimpleNamespace:
    return SimpleNamespace(uuid=uuid)


def _null_uuid_installation() -> SimpleNamespace:
    """An installation with the vendor's null-uuid quirk and no other
    identifying attribute -- ``installation_id()`` (see api.py) falls all
    the way through to returning None, so every entity/service lookup for
    this tenant is keyed off the ``"unknown"`` fallback string."""
    return SimpleNamespace(uuid=None)


@pytest.fixture
async def flowbuddy_hass(hass):
    """Register FlowBuddy's services on the test hass instance."""
    assert await async_setup(hass, {})
    return hass


async def test_enable_realtime_calls_boost(flowbuddy_hass):
    hass = flowbuddy_hass
    coord = AsyncMock()
    hass.data[DOMAIN] = {
        "entry1": {
            "installation": _installation("inst-1"),
            "api": AsyncMock(),
            "instant_coord": coord,
        }
    }

    await hass.services.async_call(
        DOMAIN,
        "enable_realtime",
        {"installation_id": "inst-1", "duration_minutes": 3},
        blocking=True,
    )

    coord.boost.assert_awaited_once_with(3)


async def test_enable_realtime_defaults_duration_to_five_minutes(flowbuddy_hass):
    hass = flowbuddy_hass
    coord = AsyncMock()
    hass.data[DOMAIN] = {
        "entry1": {
            "installation": _installation("inst-1"),
            "api": AsyncMock(),
            "instant_coord": coord,
        }
    }

    await hass.services.async_call(
        DOMAIN,
        "enable_realtime",
        {"installation_id": "inst-1"},
        blocking=True,
    )

    coord.boost.assert_awaited_once_with(5)


async def test_enable_realtime_polling_limit_raises_and_creates_issue(flowbuddy_hass):
    hass = flowbuddy_hass
    coord = AsyncMock()
    coord.boost.side_effect = PollingLimitExceededError("blocked")
    coord._blocked_until = time.monotonic() + 120
    hass.data[DOMAIN] = {
        "entry1": {
            "installation": _installation("inst-1"),
            "api": AsyncMock(),
            "instant_coord": coord,
        }
    }

    with pytest.raises(ServiceValidationError) as excinfo:
        await hass.services.async_call(
            DOMAIN,
            "enable_realtime",
            {"installation_id": "inst-1"},
            blocking=True,
        )

    assert "inst-1" in str(excinfo.value)

    registry = ir.async_get(hass)
    issue = registry.async_get_issue(DOMAIN, "polling_limit_inst-1")
    assert issue is not None


async def test_enable_realtime_resolves_via_installation_id_fallback_when_uuid_null(
    flowbuddy_hass,
):
    """Regression: installation.uuid=None must resolve via the same
    'unknown' fallback string that entity unique_ids use (api.installation_id()
    + `or "unknown"`), not raw installation.uuid comparison."""
    hass = flowbuddy_hass
    coord = AsyncMock()
    hass.data[DOMAIN] = {
        "entry1": {
            "installation": _null_uuid_installation(),
            "api": AsyncMock(),
            "instant_coord": coord,
        }
    }

    await hass.services.async_call(
        DOMAIN,
        "enable_realtime",
        {"installation_id": "unknown", "duration_minutes": 3},
        blocking=True,
    )

    coord.boost.assert_awaited_once_with(3)


async def test_enable_realtime_unknown_installation_raises(flowbuddy_hass):
    hass = flowbuddy_hass
    hass.data[DOMAIN] = {}

    with pytest.raises(ServiceValidationError):
        await hass.services.async_call(
            DOMAIN,
            "enable_realtime",
            {"installation_id": "does-not-exist"},
            blocking=True,
        )


async def test_ack_alarm_calls_api(flowbuddy_hass):
    hass = flowbuddy_hass
    api = AsyncMock()
    hass.data[DOMAIN] = {
        "entry1": {
            "installation": _installation("inst-1"),
            "api": api,
            "instant_coord": AsyncMock(),
        }
    }

    await hass.services.async_call(
        DOMAIN,
        "ack_alarm",
        {"alarm_id": "alarm-1", "comment": "handled"},
        blocking=True,
    )

    api.close_alarm.assert_awaited_once_with("alarm-1", "handled")


async def test_request_connection_test_calls_api(flowbuddy_hass):
    hass = flowbuddy_hass
    api = AsyncMock()
    hass.data[DOMAIN] = {
        "entry1": {
            "installation": _installation("inst-1"),
            "api": api,
            "instant_coord": AsyncMock(),
        }
    }

    await hass.services.async_call(
        DOMAIN,
        "request_connection_test",
        {"communicator_id": "comm-1"},
        blocking=True,
    )

    api.request_connection_test.assert_awaited_once_with("comm-1")


async def test_set_battery_charge_power_resolves_entity_and_calls_api(flowbuddy_hass):
    """Entity-lookup path: entity_id -> registry unique_id -> matching battery -> api call."""
    hass = flowbuddy_hass
    registry = er.async_get(hass)
    entry = registry.async_get_or_create(
        "number",
        DOMAIN,
        "inst-1:battery:/api/batteries/1:charge_power",
        suggested_object_id="test_battery_charge_power",
    )

    api = AsyncMock()
    battery = SimpleNamespace(resource_uri="/api/batteries/1", external_id="battery-ext-1")
    hass.data[DOMAIN] = {
        "entry1": {
            "installation": _installation("inst-1"),
            "api": api,
            "batteries": [battery],
        }
    }

    await hass.services.async_call(
        DOMAIN,
        "set_battery_charge_power",
        {"entity_id": entry.entity_id, "watts": 1500},
        blocking=True,
    )

    api.set_battery_charge_power.assert_awaited_once_with("battery-ext-1", 1500)


async def test_set_battery_charge_power_resolves_via_installation_id_fallback_when_uuid_null(
    flowbuddy_hass,
):
    """Regression: number-target resolution must recompute the candidate
    unique_id using installation_id() + 'unknown' fallback, matching what
    number.py actually stamped on the entity for a null-uuid tenant."""
    hass = flowbuddy_hass
    registry = er.async_get(hass)
    entry = registry.async_get_or_create(
        "number",
        DOMAIN,
        "unknown:battery:/api/batteries/1:charge_power",
        suggested_object_id="test_battery_charge_power_null_uuid",
    )

    api = AsyncMock()
    battery = SimpleNamespace(resource_uri="/api/batteries/1", external_id="battery-ext-1")
    hass.data[DOMAIN] = {
        "entry1": {
            "installation": _null_uuid_installation(),
            "api": api,
            "batteries": [battery],
        }
    }

    await hass.services.async_call(
        DOMAIN,
        "set_battery_charge_power",
        {"entity_id": entry.entity_id, "watts": 1500},
        blocking=True,
    )

    api.set_battery_charge_power.assert_awaited_once_with("battery-ext-1", 1500)


async def test_set_battery_charge_power_unknown_entity_raises(flowbuddy_hass):
    hass = flowbuddy_hass
    hass.data[DOMAIN] = {}

    with pytest.raises(ServiceValidationError):
        await hass.services.async_call(
            DOMAIN,
            "set_battery_charge_power",
            {"entity_id": "number.does_not_exist", "watts": 100},
            blocking=True,
        )
