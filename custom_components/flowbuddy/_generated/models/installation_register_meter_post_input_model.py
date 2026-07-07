from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.installation_register_meter_post_input_model_other_properties import (
        InstallationRegisterMeterPostInputModelOtherProperties,
    )


T = TypeVar("T", bound="InstallationRegisterMeterPostInputModel")


@_attrs_define
class InstallationRegisterMeterPostInputModel:
    """
    Attributes:
        measuring_device (str | Unset):
        description (str | Unset): Custom name that will be used to fill in Meter Type
        initial_polling (str | Unset): You can choose which data to process for this particular device. All data (whole
            period) or only the data read after registration.
        other_properties (InstallationRegisterMeterPostInputModelOtherProperties | Unset):
    """

    measuring_device: str | Unset = UNSET
    description: str | Unset = UNSET
    initial_polling: str | Unset = UNSET
    other_properties: InstallationRegisterMeterPostInputModelOtherProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_register_meter_post_input_model_other_properties import (
            InstallationRegisterMeterPostInputModelOtherProperties,
        )

        measuring_device = self.measuring_device

        description = self.description

        initial_polling = self.initial_polling

        other_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_properties, Unset):
            other_properties = self.other_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measuring_device is not UNSET:
            field_dict["measuringDevice"] = measuring_device
        if description is not UNSET:
            field_dict["description"] = description
        if initial_polling is not UNSET:
            field_dict["initialPolling"] = initial_polling
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.installation_register_meter_post_input_model_other_properties import (
            InstallationRegisterMeterPostInputModelOtherProperties,
        )

        d = dict(src_dict)
        measuring_device = d.pop("measuringDevice", UNSET)

        description = d.pop("description", UNSET)

        initial_polling = d.pop("initialPolling", UNSET)

        _other_properties = d.pop("otherProperties", UNSET)
        other_properties: InstallationRegisterMeterPostInputModelOtherProperties | Unset
        if isinstance(_other_properties, Unset):
            other_properties = UNSET
        else:
            other_properties = InstallationRegisterMeterPostInputModelOtherProperties.from_dict(
                _other_properties
            )

        installation_register_meter_post_input_model = cls(
            measuring_device=measuring_device,
            description=description,
            initial_polling=initial_polling,
            other_properties=other_properties,
        )

        installation_register_meter_post_input_model.additional_properties = d
        return installation_register_meter_post_input_model

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
