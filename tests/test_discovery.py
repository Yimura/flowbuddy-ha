"""Tests for discovery.describe — one per row of the spec §4.3 mapping table."""
from unittest.mock import MagicMock

import pytest
from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import (
    PERCENTAGE,
    UnitOfApparentPower,
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfFrequency,
    UnitOfPower,
    UnitOfReactivePower,
    UnitOfTemperature,
)

from custom_components.flowbuddy.discovery import describe


def _mt(code, unit, incremental):
    m = MagicMock()
    m.code = code; m.unit = unit; m.is_incremental = incremental; m.name = code
    return m


@pytest.mark.parametrize("unit_in,unit_expected", [("W", UnitOfPower.WATT), ("kW", UnitOfPower.WATT)])
def test_power_measurement(unit_in, unit_expected):
    d = describe(_mt("PV_POWER", unit_in, False))
    assert d.device_class == SensorDeviceClass.POWER
    assert d.state_class == SensorStateClass.MEASUREMENT
    assert d.native_unit_of_measurement == unit_expected


@pytest.mark.parametrize("unit_in,unit_expected", [("Wh", UnitOfEnergy.KILO_WATT_HOUR), ("kWh", UnitOfEnergy.KILO_WATT_HOUR)])
def test_energy_incremental(unit_in, unit_expected):
    d = describe(_mt("PV_ENERGY", unit_in, True))
    assert d.device_class == SensorDeviceClass.ENERGY
    assert d.state_class == SensorStateClass.TOTAL_INCREASING
    assert d.native_unit_of_measurement == unit_expected


def test_voltage():
    d = describe(_mt("V_LINE", "V", False))
    assert d.device_class == SensorDeviceClass.VOLTAGE
    assert d.native_unit_of_measurement == UnitOfElectricPotential.VOLT


def test_current():
    d = describe(_mt("I_LINE", "A", False))
    assert d.device_class == SensorDeviceClass.CURRENT
    assert d.native_unit_of_measurement == UnitOfElectricCurrent.AMPERE


def test_battery_soc_by_code_hint():
    d = describe(_mt("BATTERY_SOC", "%", False))
    assert d.device_class == SensorDeviceClass.BATTERY
    assert d.native_unit_of_measurement == PERCENTAGE


def test_generic_percent_not_soc():
    d = describe(_mt("PERF_INDEX", "%", False))
    assert d.device_class is None
    assert d.native_unit_of_measurement == PERCENTAGE


def test_temperature():
    d = describe(_mt("HVAC_TEMP", "°C", False))
    assert d.device_class == SensorDeviceClass.TEMPERATURE
    assert d.native_unit_of_measurement == UnitOfTemperature.CELSIUS


def test_frequency():
    d = describe(_mt("GRID_FREQ", "Hz", False))
    assert d.device_class == SensorDeviceClass.FREQUENCY
    assert d.native_unit_of_measurement == UnitOfFrequency.HERTZ


def test_apparent_power():
    d = describe(_mt("APPARENT_POWER", "VA", False))
    assert d.device_class == SensorDeviceClass.APPARENT_POWER
    assert d.native_unit_of_measurement == UnitOfApparentPower.VOLT_AMPERE


def test_reactive_power():
    d = describe(_mt("REACTIVE_POWER", "var", False))
    assert d.device_class == SensorDeviceClass.REACTIVE_POWER
    assert d.native_unit_of_measurement == UnitOfReactivePower.VOLT_AMPERE_REACTIVE


def test_unknown_unit_still_creates_sensor():
    d = describe(_mt("UNKNOWN", "wombats", False))
    assert d.device_class is None
    assert d.native_unit_of_measurement == "wombats"
    assert d.state_class == SensorStateClass.MEASUREMENT


def test_scale_kw_input_returns_watt():
    d = describe(_mt("PV_POWER", "kW", False))
    # Value transformer: kW input -> W output (× 1000)
    assert d.value_transformer(1.5) == 1500.0


def test_scale_wh_input_returns_kwh():
    d = describe(_mt("PV_ENERGY", "Wh", True))
    assert d.value_transformer(15230.5) == pytest.approx(15.2305)


def test_soc_with_vendor_typo_unit_Whpercent():
    """Real vendor ships SoC with unit="Wh%" (typo) + isIncremental=True.
    Confirmed against live tenant 2026-07-07 (EMS BAT SOC percentage,
    code=Soc_bat). Must still map to BATTERY device_class + % unit."""
    d = describe(_mt("Soc_bat", "Wh%", True))
    assert d.device_class == SensorDeviceClass.BATTERY
    assert d.native_unit_of_measurement == PERCENTAGE
    # SoC is a snapshot -> MEASUREMENT, not TOTAL_INCREASING, despite
    # vendor's isIncremental=True.
    assert d.state_class == SensorStateClass.MEASUREMENT


def test_monetary_savings_euro():
    """Vendor emits savings with unit="€" + isIncremental=True (cumulative
    savings over the lifetime of the installation)."""
    from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
    d = describe(_mt("Savings_pv", "€", True))
    assert d.device_class == SensorDeviceClass.MONETARY
    assert d.state_class == SensorStateClass.TOTAL_INCREASING
    assert d.native_unit_of_measurement == "EUR"


def test_unitless_direction_enum():
    """Vendor emits unit="_Unitless_" for enum-like measurements
    (EMS BAT Charge Direction: 0=idle, positive=charge, negative=discharge).
    Must not carry a wrong device_class or fake unit."""
    d = describe(_mt("P_bat_dir", "_Unitless_", False))
    assert d.device_class is None
    assert d.native_unit_of_measurement is None
    assert d.state_class == SensorStateClass.MEASUREMENT
