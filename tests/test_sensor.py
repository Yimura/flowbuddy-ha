"""Tests for sensor platform."""

from types import SimpleNamespace
from unittest.mock import MagicMock

from custom_components.flowbuddy.const import DOMAIN
from custom_components.flowbuddy.sensor import (
    FlowBuddyIntegratedEnergySensor,
    FlowBuddySensor,
    async_setup_entry,
)


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

    # 1 raw PV power sensor + 1 auto-derived integrator (no PV energy peer on
    # the same meter -> the integrator kicks in automatically). The two
    # null-linked measurements are skipped as before.
    raw = [e for e in added if isinstance(e, FlowBuddySensor)]
    assert len(raw) == 1
    assert raw[0].unique_id == "00000000-0000-0000-0000-000000000001:/measurements/m-pv"


async def test_setup_entry_adds_pv_integrator_when_no_pv_energy_peer(hass):
    """PV power sensor with no PV kWh peer on the same meter -> integrator
    MUST be added so the HA Energy dashboard Solar card has a data source."""
    coord = MagicMock()
    coord.data = {"/measurements/m-pv-power": 1500.0}
    coord.update_interval = None
    installation = MagicMock(uuid="00000000-0000-0000-0000-000000000001")
    meter = MagicMock(serial_number="TEST-SN-PV-1", resource_uri="/meters/m-pv-1")
    pv_power_mt = MagicMock(
        code="EMS_PV_POWER", name="EMS PV power", unit="W", is_incremental=False
    )
    pv_power_meas = SimpleNamespace(
        resource_uri="/measurements/m-pv-power",
        measurement_type=SimpleNamespace(resource_uri="/mt/pv-power"),
        meter=SimpleNamespace(resource_uri="/meters/m-pv-1"),
    )

    entry = SimpleNamespace(entry_id="e-1")
    hass.data[DOMAIN] = {
        entry.entry_id: {
            "installation": installation,
            "measurements": [pv_power_meas],
            "measurementtypes_by_uri": {"/mt/pv-power": pv_power_mt},
            "meters_by_uri": {"/meters/m-pv-1": meter},
            "instant_coord": coord,
        }
    }

    added: list = []
    await async_setup_entry(hass, entry, lambda e: added.extend(e))

    integrators = [e for e in added if isinstance(e, FlowBuddyIntegratedEnergySensor)]
    assert len(integrators) == 1
    assert integrators[0].unique_id.endswith(":integrated_energy")


async def test_setup_entry_suppresses_pv_integrator_when_pv_energy_peer_exists(hass):
    """If the vendor ever emits a PV kWh measurement on the same meter,
    the integrator is redundant and must NOT be added -- otherwise the
    Energy dashboard double-counts."""
    coord = MagicMock()
    coord.data = {}
    coord.update_interval = None
    installation = MagicMock(uuid="i-1")
    meter = MagicMock(serial_number="m", resource_uri="/meters/m-pv-1")

    pv_power_mt = MagicMock(
        code="EMS_PV_POWER", name="EMS PV power", unit="W", is_incremental=False
    )
    pv_energy_mt = MagicMock(
        code="EMS_PV_ENERGY", name="EMS PV energy", unit="kWh", is_incremental=True
    )
    pv_power = SimpleNamespace(
        resource_uri="/measurements/pv-power",
        measurement_type=SimpleNamespace(resource_uri="/mt/pv-power"),
        meter=SimpleNamespace(resource_uri="/meters/m-pv-1"),
    )
    pv_energy = SimpleNamespace(
        resource_uri="/measurements/pv-energy",
        measurement_type=SimpleNamespace(resource_uri="/mt/pv-energy"),
        meter=SimpleNamespace(resource_uri="/meters/m-pv-1"),
    )

    entry = SimpleNamespace(entry_id="e-1")
    hass.data[DOMAIN] = {
        entry.entry_id: {
            "installation": installation,
            "measurements": [pv_power, pv_energy],
            "measurementtypes_by_uri": {
                "/mt/pv-power": pv_power_mt,
                "/mt/pv-energy": pv_energy_mt,
            },
            "meters_by_uri": {"/meters/m-pv-1": meter},
            "instant_coord": coord,
        }
    }

    added: list = []
    await async_setup_entry(hass, entry, lambda e: added.extend(e))

    integrators = [e for e in added if isinstance(e, FlowBuddyIntegratedEnergySensor)]
    assert integrators == []


async def test_setup_entry_pv_detection_is_case_insensitive(hass):
    """Vendor spells PV codes inconsistently across tenants (EMS_PV_POWER,
    ems_pv_power, EMS PV Power). Detection must match on any casing so
    a naming quirk doesn't require a new release."""
    coord = MagicMock()
    coord.data = {}
    coord.update_interval = None
    installation = MagicMock(uuid="i-1")
    meter = MagicMock(serial_number="m", resource_uri="/meters/m-pv-1")
    pv_mt = MagicMock(
        code="ems_pv_power",  # lowercase
        name="Solar Panel Power",  # only "pv" substring in code, not name
        unit="W",
        is_incremental=False,
    )
    pv_meas = SimpleNamespace(
        resource_uri="/measurements/pv",
        measurement_type=SimpleNamespace(resource_uri="/mt/pv"),
        meter=SimpleNamespace(resource_uri="/meters/m-pv-1"),
    )

    entry = SimpleNamespace(entry_id="e-1")
    hass.data[DOMAIN] = {
        entry.entry_id: {
            "installation": installation,
            "measurements": [pv_meas],
            "measurementtypes_by_uri": {"/mt/pv": pv_mt},
            "meters_by_uri": {"/meters/m-pv-1": meter},
            "instant_coord": coord,
        }
    }

    added: list = []
    await async_setup_entry(hass, entry, lambda e: added.extend(e))

    integrators = [e for e in added if isinstance(e, FlowBuddyIntegratedEnergySensor)]
    assert len(integrators) == 1
