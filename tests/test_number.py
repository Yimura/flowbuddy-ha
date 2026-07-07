"""Tests for number platform (battery charge power + inverter production limit)."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

from custom_components.flowbuddy.number import (
    BatteryChargePowerNumber,
    InverterProductionLimitNumber,
)


def test_battery_number_range():
    coord = MagicMock()
    api = AsyncMock()
    battery = MagicMock(
        resource_uri="/batteries/b-1",
        external_id="BAT-1",
        max_charge_power=5000.0,
        max_discharge_power=4000.0,
        last_set_charge_power=1200.0,
        info=MagicMock(resource_uri="/meters/m-bat-1"),
    )
    meter = MagicMock(serial_number="TEST-SN-BAT-1")
    installation = MagicMock(uuid="00000000-0000-0000-0000-000000000001")

    number = BatteryChargePowerNumber(
        coordinator=coord,
        api=api,
        battery=battery,
        meter=meter,
        installation=installation,
    )

    assert number.native_min_value == -4000.0
    assert number.native_max_value == 5000.0
    assert number.native_step == 100
    assert number.native_unit_of_measurement == "W"
    assert number.native_value == 1200.0


async def test_battery_set_calls_api():
    coord = MagicMock()
    api = AsyncMock()
    battery = MagicMock(
        resource_uri="/batteries/b-1",
        external_id="BAT-1",
        max_charge_power=5000.0,
        max_discharge_power=4000.0,
        last_set_charge_power=1200.0,
        info=MagicMock(resource_uri="/meters/m-bat-1"),
    )
    meter = MagicMock(serial_number="TEST-SN-BAT-1")
    installation = MagicMock(uuid="00000000-0000-0000-0000-000000000001")

    number = BatteryChargePowerNumber(
        coordinator=coord,
        api=api,
        battery=battery,
        meter=meter,
        installation=installation,
    )

    await number.async_set_native_value(1500)

    api.set_battery_charge_power.assert_awaited_once_with("BAT-1", 1500)


def test_inverter_number_range():
    coord = MagicMock()
    api = AsyncMock()
    inverter = MagicMock(
        resource_uri="/inverters/i-1",
        external_id="INV-1",
        max_power=8000.0,
        last_set_production_capacity=3000,
        info=MagicMock(resource_uri="/meters/m-inv-1"),
    )
    meter = MagicMock(serial_number="TEST-SN-INV-1")
    installation = MagicMock(uuid="00000000-0000-0000-0000-000000000001")

    number = InverterProductionLimitNumber(
        coordinator=coord,
        api=api,
        inverter=inverter,
        meter=meter,
        installation=installation,
    )

    assert number.native_min_value == 0
    assert number.native_max_value == 8000.0
    assert number.native_step == 100
    assert number.native_unit_of_measurement == "W"
    assert number.native_value == 3000


async def test_inverter_set_calls_api():
    coord = MagicMock()
    api = AsyncMock()
    inverter = MagicMock(
        resource_uri="/inverters/i-1",
        external_id="INV-1",
        max_power=8000.0,
        last_set_production_capacity=3000,
        info=MagicMock(resource_uri="/meters/m-inv-1"),
    )
    meter = MagicMock(serial_number="TEST-SN-INV-1")
    installation = MagicMock(uuid="00000000-0000-0000-0000-000000000001")

    number = InverterProductionLimitNumber(
        coordinator=coord,
        api=api,
        inverter=inverter,
        meter=meter,
        installation=installation,
    )

    await number.async_set_native_value(2000)

    api.limit_inverter.assert_awaited_once_with("INV-1", 2000)
