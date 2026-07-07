"""Tests for entity base + DeviceInfo helpers."""

from unittest.mock import MagicMock

from custom_components.flowbuddy.const import DOMAIN
from custom_components.flowbuddy.entity import (
    communicator_device_info,
    installation_device_info,
    meter_device_info,
)


def test_installation_device_info():
    inst = MagicMock(
        uuid="00000000-0000-0000-0000-000000000001", identification="TEST-INST-1", city="Testville"
    )
    inst.installation_type.name = "Residential PV+Battery"
    di = installation_device_info(inst)
    assert di["identifiers"] == {(DOMAIN, "00000000-0000-0000-0000-000000000001")}
    assert di["name"] == "TEST-INST-1"
    assert di["model"] == "Residential PV+Battery"


def test_meter_device_info_via_installation():
    inst = MagicMock(
        uuid="00000000-0000-0000-0000-000000000001",
        resource_uri="/installations/00000000-0000-0000-0000-000000000001",
        external_id=None,
    )
    meter = MagicMock(
        serial_number="TEST-SN-PV-1",
        name="PV Inverter",
        manufacturer="TestInverterCo",
        meter_type="PV",
        resource_uri="/meters/pv-1",
    )
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
    meter = MagicMock(
        serial_number=None,
        name=None,
        manufacturer=None,
        meter_type=None,
        resource_uri="/meters/1031030229250246",
    )
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
        uuid=None,
        resource_uri="/installations/b3af1fd3-a09d-46b5-9a7c-6f3ee60d55c1",
        external_id=None,
        identification=None,
        customer_name=None,
        installation_type=None,
    )
    di = installation_device_info(inst)
    assert di["identifiers"] == {(DOMAIN, "b3af1fd3-a09d-46b5-9a7c-6f3ee60d55c1")}
    assert di["name"].startswith("FlowBuddy ")
    assert di["model"] == "Installation"


def test_meter_device_info_exposes_serial_number_field():
    """Serial number belongs on DeviceInfo.serial_number so the HA Devices
    UI can show it in the header slot -- not just embedded in the name."""
    inst = MagicMock(
        uuid="00000000-0000-0000-0000-000000000001",
        resource_uri="/installations/00000000-0000-0000-0000-000000000001",
        external_id=None,
    )
    meter = MagicMock(
        serial_number="TEST-SN-PV-1",
        name="PV Inverter",
        manufacturer="TestInverterCo",
        meter_type="PV",
        resource_uri="/meters/pv-1",
    )
    di = meter_device_info(meter, inst)
    assert di["serial_number"] == "TEST-SN-PV-1"


def test_meter_device_info_serial_number_uses_resource_uri_fallback():
    """When vendor sends serial_number=None (common on live tenant), the
    resource_uri last segment already becomes the identifier + name
    fallback -- serial_number must use the same fallback so the UI slot
    isn't blank."""
    inst = MagicMock(uuid=None, resource_uri=None, external_id=None)
    meter = MagicMock(
        serial_number=None,
        name=None,
        manufacturer=None,
        meter_type=None,
        resource_uri="/meters/1031030229250246",
    )
    di = meter_device_info(meter, inst)
    assert di["serial_number"] == "1031030229250246"


def test_communicator_device_info_populates_all_fields():
    """Full-payload communicator (matches live tenant XMXCTA0400002388,
    firmware XMX_EMSA_V0.8.4, type=Lewiz) -- every DeviceInfo field the
    HA UI can display must be wired up."""
    inst = MagicMock(
        uuid="00000000-0000-0000-0000-000000000001",
        resource_uri="/installations/00000000-0000-0000-0000-000000000001",
        external_id=None,
    )
    comm = MagicMock(
        external_id="comm-uuid-1",
        logical_device_name="XMXCTA0400002388",
        firm_ware_version="XMX_EMSA_V0.8.4",
    )
    comm.type_ = MagicMock()
    comm.type_.name = "Lewiz"
    di = communicator_device_info(comm, inst)
    assert di["identifiers"] == {(DOMAIN, "communicator:comm-uuid-1")}
    assert di["name"] == "XMXCTA0400002388"
    assert di["manufacturer"] == "FlowBuddy"
    assert di["model"] == "Lewiz"
    assert di["sw_version"] == "XMX_EMSA_V0.8.4"
    assert di["serial_number"] == "XMXCTA0400002388"
    assert di["via_device"] == (DOMAIN, "00000000-0000-0000-0000-000000000001")


def test_communicator_device_info_survives_null_fields():
    """Vendor spec is fully nullable. When every field is None the helper
    must still produce a valid DeviceInfo (no crash, no (DOMAIN, None)
    identifiers, no via_device wired to None)."""
    inst = MagicMock(uuid=None, resource_uri=None, external_id=None)
    comm = MagicMock(
        external_id=None,
        logical_device_name=None,
        firm_ware_version=None,
    )
    comm.type_ = None
    di = communicator_device_info(comm, inst)
    ident = next(iter(di["identifiers"]))
    assert ident[0] == DOMAIN
    assert ident[1].startswith("communicator:")
    assert len(ident[1]) > len("communicator:")
    assert di["model"] == "Communicator"
    assert di["manufacturer"] == "FlowBuddy"
    assert "via_device" not in di


def test_communicator_device_info_prefers_external_id_then_logical_name():
    """Identifier fallback chain: external_id -> logical_device_name ->
    synthetic. Verifies logical_device_name is used when external_id is
    None but logical_device_name is set (some tenants emit one but not
    the other on partial-registration rows)."""
    inst = MagicMock(uuid="i-1", resource_uri=None, external_id=None)
    comm = MagicMock(
        external_id=None,
        logical_device_name="XMX-BACKUP-1",
        firm_ware_version=None,
    )
    comm.type_ = None
    di = communicator_device_info(comm, inst)
    ident = next(iter(di["identifiers"]))
    assert ident == (DOMAIN, "communicator:XMX-BACKUP-1")
