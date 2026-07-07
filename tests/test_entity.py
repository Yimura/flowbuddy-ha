"""Tests for entity base + DeviceInfo helpers."""
from unittest.mock import MagicMock

from custom_components.flowbuddy.const import DOMAIN
from custom_components.flowbuddy.entity import (
    installation_device_info,
    meter_device_info,
)


def test_installation_device_info():
    inst = MagicMock(uuid="00000000-0000-0000-0000-000000000001",
                     identification="TEST-INST-1", city="Testville")
    inst.installation_type.name = "Residential PV+Battery"
    di = installation_device_info(inst)
    assert di["identifiers"] == {(DOMAIN, "00000000-0000-0000-0000-000000000001")}
    assert di["name"] == "TEST-INST-1"
    assert di["model"] == "Residential PV+Battery"


def test_meter_device_info_via_installation():
    inst = MagicMock(uuid="00000000-0000-0000-0000-000000000001")
    meter = MagicMock(serial_number="TEST-SN-PV-1", name="PV Inverter",
                      manufacturer="TestInverterCo", meter_type="PV")
    di = meter_device_info(meter, inst)
    assert di["identifiers"] == {(DOMAIN, "TEST-SN-PV-1")}
    assert di["via_device"] == (DOMAIN, "00000000-0000-0000-0000-000000000001")
    assert di["manufacturer"] == "TestInverterCo"
