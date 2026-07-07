from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.device_control_state_output_model import DeviceControlStateOutputModel


T = TypeVar("T", bound="DeviceControlStateOutputListModel")


@_attrs_define
class DeviceControlStateOutputListModel:
    """
    Attributes:
        device_control_states (list[DeviceControlStateOutputModel] | Unset):
    """

    device_control_states: list[DeviceControlStateOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.device_control_state_output_model import DeviceControlStateOutputModel

        device_control_states: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_control_states, Unset):
            device_control_states = []
            for device_control_states_item_data in self.device_control_states:
                device_control_states_item = device_control_states_item_data.to_dict()
                device_control_states.append(device_control_states_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_control_states is not UNSET:
            field_dict["deviceControlStates"] = device_control_states

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_control_state_output_model import DeviceControlStateOutputModel

        d = dict(src_dict)
        _device_control_states = d.pop("deviceControlStates", UNSET)
        device_control_states: list[DeviceControlStateOutputModel] | Unset = UNSET
        if _device_control_states is not UNSET:
            device_control_states = []
            for device_control_states_item_data in _device_control_states:
                device_control_states_item = DeviceControlStateOutputModel.from_dict(
                    device_control_states_item_data
                )

                device_control_states.append(device_control_states_item)

        device_control_state_output_list_model = cls(
            device_control_states=device_control_states,
        )

        device_control_state_output_list_model.additional_properties = d
        return device_control_state_output_list_model

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
