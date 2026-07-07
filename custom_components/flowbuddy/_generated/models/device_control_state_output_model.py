from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.control_type_reference_model import ControlTypeReferenceModel
    from ..models.modbus_device_reference_model import ModbusDeviceReferenceModel


T = TypeVar("T", bound="DeviceControlStateOutputModel")


@_attrs_define
class DeviceControlStateOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        last_applied_value (str | Unset):
        timestamp (datetime.datetime | None | Unset):
        external_id (str | Unset):
        modbus_device (ModbusDeviceReferenceModel | Unset):
        control_type (ControlTypeReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    last_applied_value: str | Unset = UNSET
    timestamp: datetime.datetime | None | Unset = UNSET
    external_id: str | Unset = UNSET
    modbus_device: ModbusDeviceReferenceModel | Unset = UNSET
    control_type: ControlTypeReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.control_type_reference_model import ControlTypeReferenceModel
        from ..models.modbus_device_reference_model import ModbusDeviceReferenceModel

        resource_uri = self.resource_uri

        last_applied_value = self.last_applied_value

        timestamp: None | str | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        elif isinstance(self.timestamp, datetime.datetime):
            timestamp = self.timestamp.isoformat()
        else:
            timestamp = self.timestamp

        external_id = self.external_id

        modbus_device: dict[str, Any] | Unset = UNSET
        if not isinstance(self.modbus_device, Unset):
            modbus_device = self.modbus_device.to_dict()

        control_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.control_type, Unset):
            control_type = self.control_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if last_applied_value is not UNSET:
            field_dict["lastAppliedValue"] = last_applied_value
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if modbus_device is not UNSET:
            field_dict["modbusDevice"] = modbus_device
        if control_type is not UNSET:
            field_dict["controlType"] = control_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.control_type_reference_model import ControlTypeReferenceModel
        from ..models.modbus_device_reference_model import ModbusDeviceReferenceModel

        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

        last_applied_value = d.pop("lastAppliedValue", UNSET)

        def _parse_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timestamp_type_0 = datetime.datetime.fromisoformat(data)

                return timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        external_id = d.pop("externalId", UNSET)

        _modbus_device = d.pop("modbusDevice", UNSET)
        modbus_device: ModbusDeviceReferenceModel | Unset
        if isinstance(_modbus_device, Unset):
            modbus_device = UNSET
        else:
            modbus_device = ModbusDeviceReferenceModel.from_dict(_modbus_device)

        _control_type = d.pop("controlType", UNSET)
        control_type: ControlTypeReferenceModel | Unset
        if isinstance(_control_type, Unset):
            control_type = UNSET
        else:
            control_type = ControlTypeReferenceModel.from_dict(_control_type)

        device_control_state_output_model = cls(
            resource_uri=resource_uri,
            last_applied_value=last_applied_value,
            timestamp=timestamp,
            external_id=external_id,
            modbus_device=modbus_device,
            control_type=control_type,
        )

        device_control_state_output_model.additional_properties = d
        return device_control_state_output_model

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
