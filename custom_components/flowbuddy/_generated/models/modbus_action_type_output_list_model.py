from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.modbus_action_type_output_model import ModbusActionTypeOutputModel


T = TypeVar("T", bound="ModbusActionTypeOutputListModel")


@_attrs_define
class ModbusActionTypeOutputListModel:
    """
    Attributes:
        modbus_action_types (list[ModbusActionTypeOutputModel] | Unset):
    """

    modbus_action_types: list[ModbusActionTypeOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.modbus_action_type_output_model import ModbusActionTypeOutputModel

        modbus_action_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.modbus_action_types, Unset):
            modbus_action_types = []
            for modbus_action_types_item_data in self.modbus_action_types:
                modbus_action_types_item = modbus_action_types_item_data.to_dict()
                modbus_action_types.append(modbus_action_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modbus_action_types is not UNSET:
            field_dict["modbusActionTypes"] = modbus_action_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.modbus_action_type_output_model import ModbusActionTypeOutputModel

        d = dict(src_dict)
        _modbus_action_types = d.pop("modbusActionTypes", UNSET)
        modbus_action_types: list[ModbusActionTypeOutputModel] | Unset = UNSET
        if _modbus_action_types is not UNSET:
            modbus_action_types = []
            for modbus_action_types_item_data in _modbus_action_types:
                modbus_action_types_item = ModbusActionTypeOutputModel.from_dict(
                    modbus_action_types_item_data
                )

                modbus_action_types.append(modbus_action_types_item)

        modbus_action_type_output_list_model = cls(
            modbus_action_types=modbus_action_types,
        )

        modbus_action_type_output_list_model.additional_properties = d
        return modbus_action_type_output_list_model

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
