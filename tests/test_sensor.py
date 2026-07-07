"""Tests for sensor platform."""
from unittest.mock import MagicMock

from custom_components.flowbuddy.sensor import FlowBuddySensor


def test_sensor_reads_from_coordinator():
    coord = MagicMock()
    coord.data = {"/measurements/m-pv": 1500.0}
    mt = MagicMock(code="PV_POWER", name="PV Power", unit="W", is_incremental=False)
    meas = MagicMock(resource_uri="/measurements/m-pv")
    sensor = FlowBuddySensor(
        coordinator=coord,
        installation_uuid="00000000-0000-0000-0000-000000000001",
        meter=MagicMock(serial_number="TEST-SN-PV-1"),
        installation=MagicMock(uuid="00000000-0000-0000-0000-000000000001"),
        measurement=meas,
        measurement_type=mt,
    )
    assert sensor.native_value == 1500.0
    assert sensor.native_unit_of_measurement == "W"


def test_sensor_applies_value_transformer():
    coord = MagicMock()
    coord.data = {"/measurements/m-pv": 1.5}
    mt = MagicMock(code="PV_POWER", name="PV Power", unit="kW", is_incremental=False)
    meas = MagicMock(resource_uri="/measurements/m-pv")
    sensor = FlowBuddySensor(
        coordinator=coord,
        installation_uuid="00000000-0000-0000-0000-000000000001",
        meter=MagicMock(serial_number="TEST-SN-PV-1"),
        installation=MagicMock(uuid="00000000-0000-0000-0000-000000000001"),
        measurement=meas,
        measurement_type=mt,
    )
    # kW measurement -> raw W value after ×1000 transformer is applied.
    assert sensor.native_value == 1500.0
    assert sensor.native_unit_of_measurement == "W"


def test_sensor_returns_none_when_missing_from_coordinator():
    coord = MagicMock()
    coord.data = {}
    mt = MagicMock(code="PV_POWER", name="PV Power", unit="W", is_incremental=False)
    meas = MagicMock(resource_uri="/measurements/m-pv")
    s = FlowBuddySensor(
        coordinator=coord,
        installation_uuid="i", meter=MagicMock(serial_number="s"),
        installation=MagicMock(uuid="i"),
        measurement=meas, measurement_type=mt,
    )
    assert s.native_value is None
