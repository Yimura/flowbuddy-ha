"""Tests for sensor platform."""

from types import SimpleNamespace
from unittest.mock import MagicMock

from custom_components.flowbuddy.const import DOMAIN
from custom_components.flowbuddy.sensor import FlowBuddySensor, async_setup_entry


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
        installation_uuid="i",
        meter=MagicMock(serial_number="s"),
        installation=MagicMock(uuid="i"),
        measurement=meas,
        measurement_type=mt,
    )
    assert s.native_value is None


async def test_setup_entry_skips_measurements_with_null_measurement_type_or_meter(hass):
    """Spec (openapi/flexmon-v1.json) marks every $ref property nullable, and
    the live tenant does return null measurement_type/meter links on some
    rows. async_setup_entry must skip those instead of raising
    AttributeError on `.resource_uri` and failing the whole platform."""
    coord = MagicMock()
    coord.data = {"/measurements/m-pv": 1500.0}
    installation = MagicMock(uuid="00000000-0000-0000-0000-000000000001")
    meter = MagicMock(serial_number="TEST-SN-PV-1")
    mt = MagicMock(code="PV_POWER", name="PV Power", unit="W", is_incremental=False)

    good = SimpleNamespace(
        resource_uri="/measurements/m-pv",
        measurement_type=SimpleNamespace(resource_uri="/measurementtypes/pv-power"),
        meter=SimpleNamespace(resource_uri="/meters/m-pv-1"),
    )
    null_type = SimpleNamespace(
        resource_uri="/measurements/m-null-type",
        measurement_type=None,
        meter=SimpleNamespace(resource_uri="/meters/m-pv-1"),
    )
    null_meter = SimpleNamespace(
        resource_uri="/measurements/m-null-meter",
        measurement_type=SimpleNamespace(resource_uri="/measurementtypes/pv-power"),
        meter=None,
    )

    entry = SimpleNamespace(entry_id="entry1")
    hass.data[DOMAIN] = {
        entry.entry_id: {
            "installation": installation,
            "measurements": [good, null_type, null_meter],
            "measurementtypes_by_uri": {"/measurementtypes/pv-power": mt},
            "meters_by_uri": {"/meters/m-pv-1": meter},
            "instant_coord": coord,
        }
    }

    added: list = []

    def _add_entities(entities):
        added.extend(entities)

    await async_setup_entry(hass, entry, _add_entities)

    assert len(added) == 1
    assert added[0].unique_id == "00000000-0000-0000-0000-000000000001:/measurements/m-pv"
