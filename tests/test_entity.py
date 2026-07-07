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
    inst = MagicMock(uuid="00000000-0000-0000-0000-000000000001",
                     resource_uri="/installations/00000000-0000-0000-0000-000000000001",
                     external_id=None)
    meter = MagicMock(serial_number="TEST-SN-PV-1", name="PV Inverter",
                      manufacturer="TestInverterCo", meter_type="PV",
                      resource_uri="/meters/pv-1")
    di = meter_device_info(meter, inst)
    assert di["identifiers"] == {(DOMAIN, "TEST-SN-PV-1")}
    assert di["via_device"] == (DOMAIN, "00000000-0000-0000-0000-000000000001")
    assert di["manufacturer"] == "TestInverterCo"


def test_meter_device_info_survives_null_fields():
    """Live tenant returned meter with serial_number/name/manufacturer/
    meter_type ALL null and inst.uuid null. Previously produced
    via_device=(DOMAIN, None) which HA logs as a frame warning and will
    hard-fail in HA 2025.12. Fallback chain must synthesize serial via
    resource_uri and skip via_device entirely when uuid is missing.
    """
    inst = MagicMock(uuid=None, resource_uri=None, external_id=None)
    meter = MagicMock(serial_number=None, name=None, manufacturer=None,
                      meter_type=None, resource_uri="/meters/1031030229250246")
    di = meter_device_info(meter, inst)
    # Serial derived from resource_uri last segment.
    assert di["identifiers"] == {(DOMAIN, "1031030229250246")}
    # No via_device wired when installation has no id (prevents
    # frame.py:348 warning that becomes a hard error in HA 2025.12).
    assert "via_device" not in di
    # Human-readable fallbacks so entities don't render as blank rows.
    assert di["name"] and di["name"] != ""
    assert di["manufacturer"] == "FlowBuddy"
    assert di["model"] == "Meter"


def test_installation_device_info_survives_null_fields():
    """Same class of bug for installation: null uuid + null identification
    + null customer_name + null installation_type -> must synthesize."""
    inst = MagicMock(
        uuid=None, resource_uri="/installations/b3af1fd3-a09d-46b5-9a7c-6f3ee60d55c1",
        external_id=None, identification=None, customer_name=None, installation_type=None,
    )
    di = installation_device_info(inst)
    assert di["identifiers"] == {(DOMAIN, "b3af1fd3-a09d-46b5-9a7c-6f3ee60d55c1")}
    assert di["name"].startswith("FlowBuddy ")
    assert di["model"] == "Installation"
