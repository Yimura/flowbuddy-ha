from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.measuring_device_output_model import MeasuringDeviceOutputModel


T = TypeVar("T", bound="MeasuringDeviceOutputListModel")


@_attrs_define
class MeasuringDeviceOutputListModel:
    """
    Attributes:
        measuring_devices (list[MeasuringDeviceOutputModel] | Unset):
    """

    measuring_devices: list[MeasuringDeviceOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.measuring_device_output_model import MeasuringDeviceOutputModel

        measuring_devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.measuring_devices, Unset):
            measuring_devices = []
            for measuring_devices_item_data in self.measuring_devices:
                measuring_devices_item = measuring_devices_item_data.to_dict()
                measuring_devices.append(measuring_devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measuring_devices is not UNSET:
            field_dict["measuringDevices"] = measuring_devices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measuring_device_output_model import MeasuringDeviceOutputModel

        d = dict(src_dict)
        _measuring_devices = d.pop("measuringDevices", UNSET)
        measuring_devices: list[MeasuringDeviceOutputModel] | Unset = UNSET
        if _measuring_devices is not UNSET:
            measuring_devices = []
            for measuring_devices_item_data in _measuring_devices:
                measuring_devices_item = MeasuringDeviceOutputModel.from_dict(
                    measuring_devices_item_data
                )

                measuring_devices.append(measuring_devices_item)

        measuring_device_output_list_model = cls(
            measuring_devices=measuring_devices,
        )

        measuring_device_output_list_model.additional_properties = d
        return measuring_device_output_list_model

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
