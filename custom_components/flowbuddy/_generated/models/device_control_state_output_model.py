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
        resource_uri (None | str | Unset):
        last_applied_value (None | str | Unset):
        timestamp (datetime.datetime | None | Unset):
        external_id (None | str | Unset):
        modbus_device (ModbusDeviceReferenceModel | None | Unset):
        control_type (ControlTypeReferenceModel | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    last_applied_value: None | str | Unset = UNSET
    timestamp: datetime.datetime | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    modbus_device: ModbusDeviceReferenceModel | None | Unset = UNSET
    control_type: ControlTypeReferenceModel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.control_type_reference_model import ControlTypeReferenceModel
        from ..models.modbus_device_reference_model import ModbusDeviceReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        last_applied_value: None | str | Unset
        if isinstance(self.last_applied_value, Unset):
            last_applied_value = UNSET
        else:
            last_applied_value = self.last_applied_value

        timestamp: None | str | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        elif isinstance(self.timestamp, datetime.datetime):
            timestamp = self.timestamp.isoformat()
        else:
            timestamp = self.timestamp

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        modbus_device: dict[str, Any] | None | Unset
        if isinstance(self.modbus_device, Unset):
            modbus_device = UNSET
        elif isinstance(self.modbus_device, ModbusDeviceReferenceModel):
            modbus_device = self.modbus_device.to_dict()
        else:
            modbus_device = self.modbus_device

        control_type: dict[str, Any] | None | Unset
        if isinstance(self.control_type, Unset):
            control_type = UNSET
        elif isinstance(self.control_type, ControlTypeReferenceModel):
            control_type = self.control_type.to_dict()
        else:
            control_type = self.control_type

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

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

        def _parse_last_applied_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_applied_value = _parse_last_applied_value(d.pop("lastAppliedValue", UNSET))

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

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_modbus_device(data: object) -> ModbusDeviceReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                modbus_device_type_1 = ModbusDeviceReferenceModel.from_dict(data)

                return modbus_device_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModbusDeviceReferenceModel | None | Unset, data)

        modbus_device = _parse_modbus_device(d.pop("modbusDevice", UNSET))

        def _parse_control_type(data: object) -> ControlTypeReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                control_type_type_1 = ControlTypeReferenceModel.from_dict(data)

                return control_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ControlTypeReferenceModel | None | Unset, data)

        control_type = _parse_control_type(d.pop("controlType", UNSET))

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
