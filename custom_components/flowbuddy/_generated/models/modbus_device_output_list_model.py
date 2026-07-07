from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.modbus_device_output_model import ModbusDeviceOutputModel


T = TypeVar("T", bound="ModbusDeviceOutputListModel")


@_attrs_define
class ModbusDeviceOutputListModel:
    """
    Attributes:
        modbus_devices (list[ModbusDeviceOutputModel] | Unset):
    """

    modbus_devices: list[ModbusDeviceOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.modbus_device_output_model import ModbusDeviceOutputModel

        modbus_devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.modbus_devices, Unset):
            modbus_devices = []
            for modbus_devices_item_data in self.modbus_devices:
                modbus_devices_item = modbus_devices_item_data.to_dict()
                modbus_devices.append(modbus_devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modbus_devices is not UNSET:
            field_dict["modbusDevices"] = modbus_devices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.modbus_device_output_model import ModbusDeviceOutputModel

        d = dict(src_dict)
        _modbus_devices = d.pop("modbusDevices", UNSET)
        modbus_devices: list[ModbusDeviceOutputModel] | Unset = UNSET
        if _modbus_devices is not UNSET:
            modbus_devices = []
            for modbus_devices_item_data in _modbus_devices:
                modbus_devices_item = ModbusDeviceOutputModel.from_dict(modbus_devices_item_data)

                modbus_devices.append(modbus_devices_item)

        modbus_device_output_list_model = cls(
            modbus_devices=modbus_devices,
        )

        modbus_device_output_list_model.additional_properties = d
        return modbus_device_output_list_model

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
