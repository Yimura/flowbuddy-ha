"""Tests for climate platform (HVAC heat/cool setpoint control)."""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest
from homeassistant.components.climate import ClimateEntityFeature, HVACMode
from homeassistant.exceptions import HomeAssistantError

from custom_components.flowbuddy.climate import FlowBuddyHvac


def _make_hvac(*, hvac_mode: HVACMode | None = None):
    coord = MagicMock()
    api = AsyncMock()
    hvac = MagicMock(
        resource_uri="/hvacs/h-1",
        external_id="HVAC-1",
        last_set_cool_temperature=24.0,
        last_set_heat_temperature=20.0,
        info=MagicMock(resource_uri="/meters/m-hvac-1"),
    )
    meter = MagicMock(serial_number="TEST-SN-HVAC-1")
    installation = MagicMock(uuid="00000000-0000-0000-0000-000000000001")

    entity = FlowBuddyHvac(
        coordinator=coord, api=api, hvac=hvac, meter=meter, installation=installation,
    )
    if hvac_mode is not None:
        entity._attr_hvac_mode = hvac_mode
    return entity, api


def test_climate_supported_features():
    entity, _ = _make_hvac()

    assert entity.hvac_modes == [HVACMode.HEAT, HVACMode.COOL, HVACMode.OFF]
    assert entity.temperature_unit == "°C"
    assert entity.supported_features == ClimateEntityFeature.TARGET_TEMPERATURE
    # No live mode field exists on HVACOutputModel — safe default is OFF.
    assert entity.hvac_mode == HVACMode.OFF


async def test_set_temperature_heat_mode():
    entity, api = _make_hvac(hvac_mode=HVACMode.HEAT)

    await entity.async_set_temperature(temperature=22.0)

    api.set_hvac_heat.assert_awaited_once_with("HVAC-1", 22.0)
    api.set_hvac_cool.assert_not_awaited()


async def test_set_temperature_cool_mode():
    entity, api = _make_hvac(hvac_mode=HVACMode.COOL)

    await entity.async_set_temperature(temperature=18.0)

    api.set_hvac_cool.assert_awaited_once_with("HVAC-1", 18.0)
    api.set_hvac_heat.assert_not_awaited()


async def test_set_temperature_off_raises():
    entity, api = _make_hvac(hvac_mode=HVACMode.OFF)

    with pytest.raises(HomeAssistantError):
        await entity.async_set_temperature(temperature=21.0)

    api.set_hvac_heat.assert_not_awaited()
    api.set_hvac_cool.assert_not_awaited()
