"""Tests for the PV Riemann integrator sensor."""

from __future__ import annotations

import datetime as dt
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest
from homeassistant.core import State

from custom_components.flowbuddy.sensor import FlowBuddyIntegratedEnergySensor


def _make_sensor(coord_data, max_gap_s=540.0):
    coord = MagicMock()
    coord.data = coord_data
    installation = MagicMock(uuid="i-1")
    meter = MagicMock(serial_number="m-1", resource_uri="/meters/m-1")
    source = SimpleNamespace(resource_uri="/measurements/pv-power")
    return FlowBuddyIntegratedEnergySensor(
        coordinator=coord,
        installation_uuid="i-1",
        meter=meter,
        installation=installation,
        source_measurement=source,
        source_name="EMS PV power",
        max_gap_s=max_gap_s,
    )


def _advance(sensor, watts_now, seconds_since_last):
    """Simulate one coordinator tick at ``seconds_since_last`` after the previous."""
    base = dt.datetime(2026, 1, 1, tzinfo=dt.UTC)
    if not hasattr(sensor, "_test_clock"):
        sensor._test_clock = base
    sensor._test_clock += dt.timedelta(seconds=seconds_since_last)
    sensor.coordinator.data["/measurements/pv-power"] = watts_now
    with patch.object(FlowBuddyIntegratedEnergySensor, "_now", return_value=sensor._test_clock):
        sensor._accumulate_from_coordinator()


def test_integrator_accumulates_trapezoidal():
    """Two 1000 W samples 3600s apart -> avg 1000 W over 1 hour = 1 kWh.

    Uses an inflated max_gap so the 1-hour dt doesn't trip the gap guard
    -- that behavior has its own test (`_skips_when_gap_exceeds_threshold`).
    """
    sensor = _make_sensor({"/measurements/pv-power": None}, max_gap_s=7200.0)
    _advance(sensor, 1000.0, 0.0)  # first tick seeds _last_watts, no accumulation
    assert sensor.native_value == 0.0

    _advance(sensor, 1000.0, 3600.0)  # avg 1000 W * 1h / 1000 = 1 kWh
    assert sensor.native_value == pytest.approx(1.0, abs=1e-9)


def test_integrator_trapezoidal_averages_rising_edge():
    """Rising power 500 -> 1500 W over 60s -> avg 1000 W = 60000/3_600_000 kWh."""
    sensor = _make_sensor({"/measurements/pv-power": None})
    _advance(sensor, 500.0, 0.0)
    _advance(sensor, 1500.0, 60.0)
    assert sensor.native_value == pytest.approx(60_000.0 / 3_600_000.0, abs=1e-9)


def test_integrator_skips_when_gap_exceeds_threshold():
    """A dt larger than max_gap_s must NOT accumulate; _last_ts still moves
    forward so the next tick has a fresh baseline."""
    sensor = _make_sensor({"/measurements/pv-power": None}, max_gap_s=540.0)
    _advance(sensor, 1000.0, 0.0)
    _advance(sensor, 1000.0, 300.0)  # dt < 540 -> accumulates
    # 5 minutes at 1000W = 1000*300/3_600_000 = 0.08333... kWh
    assert sensor.native_value == pytest.approx(300_000.0 / 3_600_000.0, abs=1e-9)

    baseline = sensor.native_value
    _advance(sensor, 1000.0, 10_000.0)  # dt > max_gap_s -> no accumulation
    assert sensor.native_value == pytest.approx(baseline)


def test_integrator_skips_when_source_is_none():
    """Missing source reading -> skip the tick entirely (do not advance
    _last_ts either)."""
    sensor = _make_sensor({})
    _advance(sensor, None, 0.0)
    assert sensor.native_value == 0.0


async def test_integrator_restores_previous_total_on_startup():
    """RestoreEntity contract: seed self._total from the last saved state so
    total_increasing statistics don't reset every HA restart."""
    sensor = _make_sensor({"/measurements/pv-power": None})
    with patch.object(
        FlowBuddyIntegratedEnergySensor,
        "async_get_last_state",
        return_value=State("sensor.derived_pv_energy", "12.345"),
    ):
        await sensor.async_added_to_hass()
    assert sensor.native_value == pytest.approx(12.345)

    # First post-restore tick must NOT accumulate (last_ts is None until
    # after the first update).
    _advance(sensor, 1000.0, 0.0)
    _advance(sensor, 1000.0, 60.0)
    expected = 12.345 + (60_000.0 / 3_600_000.0)
    assert sensor.native_value == pytest.approx(expected, abs=1e-9)


async def test_integrator_restore_handles_unknown_state():
    """Prior state might be 'unknown' / 'unavailable' / empty. Restore must
    not raise and must default to 0.0."""
    sensor = _make_sensor({"/measurements/pv-power": None})
    with patch.object(
        FlowBuddyIntegratedEnergySensor,
        "async_get_last_state",
        return_value=State("sensor.derived_pv_energy", "unknown"),
    ):
        await sensor.async_added_to_hass()
    assert sensor.native_value == 0.0


def test_integrator_has_correct_ha_metadata():
    """Sensor must present as ENERGY / TOTAL_INCREASING / kWh so it plugs
    into the HA Energy dashboard Solar card with no user configuration."""
    from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
    from homeassistant.const import UnitOfEnergy

    sensor = _make_sensor({"/measurements/pv-power": None})
    assert sensor.device_class == SensorDeviceClass.ENERGY
    assert sensor.state_class == SensorStateClass.TOTAL_INCREASING
    assert sensor.native_unit_of_measurement == UnitOfEnergy.KILO_WATT_HOUR
