"""Tests for binary_sensor platform (open alarms as PROBLEM binary sensors)."""
from __future__ import annotations

from unittest.mock import MagicMock

from homeassistant.components.binary_sensor import BinarySensorDeviceClass

from custom_components.flowbuddy._generated.models.alarm_output_model import (
    AlarmOutputModel,
)
from custom_components.flowbuddy.binary_sensor import FlowBuddyAlarmBinarySensor
from custom_components.flowbuddy.const import DOMAIN


def _alarm_from_fixture(load_fixture) -> AlarmOutputModel:
    """Decode the fixture's single open alarm the same way FlowBuddyClient does."""
    raw = load_fixture("alarms_open.json")["_embedded"]["alarms"][0]
    return AlarmOutputModel.from_dict(raw)


def test_alarm_binary_sensor_is_on_with_correct_identity(load_fixture):
    coord = MagicMock()
    installation = MagicMock(uuid="00000000-0000-0000-0000-000000000001")
    alarm = _alarm_from_fixture(load_fixture)

    sensor = FlowBuddyAlarmBinarySensor(
        coordinator=coord, installation=installation, alarm=alarm,
    )

    assert sensor.is_on is True
    assert sensor.device_class == BinarySensorDeviceClass.PROBLEM
    assert sensor.unique_id == "00000000-0000-0000-0000-000000000001:alarm:alarm-1"


def test_alarm_binary_sensor_extra_state_attributes(load_fixture):
    coord = MagicMock()
    installation = MagicMock(uuid="00000000-0000-0000-0000-000000000001")
    alarm = _alarm_from_fixture(load_fixture)

    sensor = FlowBuddyAlarmBinarySensor(
        coordinator=coord, installation=installation, alarm=alarm,
    )

    # priority is a typed AlarmOutputModel field; message/raisedOn are only
    # present in additional_properties (see binary_sensor.py's fallback).
    assert sensor.extra_state_attributes == {
        "priority": "HIGH",
        "message": "Communicator offline",
        "raisedOn": "2026-07-07T10:00:00Z",
    }


def test_alarm_binary_sensor_attaches_to_installation_not_meter(load_fixture):
    coord = MagicMock()
    installation = MagicMock(
        uuid="00000000-0000-0000-0000-000000000001",
        identification="TEST-INST-1",
    )
    installation.installation_type.name = "Residential PV+Battery"
    alarm = _alarm_from_fixture(load_fixture)

    sensor = FlowBuddyAlarmBinarySensor(
        coordinator=coord, installation=installation, alarm=alarm,
    )

    assert sensor.device_info["identifiers"] == {
        (DOMAIN, "00000000-0000-0000-0000-000000000001")
    }
    # Meter-scoped entities set via_device; installation-scoped ones must not.
    assert "via_device" not in sensor.device_info
