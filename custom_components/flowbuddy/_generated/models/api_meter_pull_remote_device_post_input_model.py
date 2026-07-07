from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.api_meter_pull_remote_device_post_input_model_other_properties import (
        ApiMeterPullRemoteDevicePostInputModelOtherProperties,
    )


T = TypeVar("T", bound="ApiMeterPullRemoteDevicePostInputModel")


@_attrs_define
class ApiMeterPullRemoteDevicePostInputModel:
    """
    Attributes:
        plant_id (str | Unset): The technical reference in the remote portal
        api_meter_type (str | Unset): SolarEdge or Fluvius
        api_account (str | Unset): The account to be used to connect to the API
        other_properties (ApiMeterPullRemoteDevicePostInputModelOtherProperties | Unset):
    """

    plant_id: str | Unset = UNSET
    api_meter_type: str | Unset = UNSET
    api_account: str | Unset = UNSET
    other_properties: ApiMeterPullRemoteDevicePostInputModelOtherProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_meter_pull_remote_device_post_input_model_other_properties import (
            ApiMeterPullRemoteDevicePostInputModelOtherProperties,
        )

        plant_id = self.plant_id

        api_meter_type = self.api_meter_type

        api_account = self.api_account

        other_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_properties, Unset):
            other_properties = self.other_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plant_id is not UNSET:
            field_dict["plantId"] = plant_id
        if api_meter_type is not UNSET:
            field_dict["apiMeterType"] = api_meter_type
        if api_account is not UNSET:
            field_dict["apiAccount"] = api_account
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_meter_pull_remote_device_post_input_model_other_properties import (
            ApiMeterPullRemoteDevicePostInputModelOtherProperties,
        )

        d = dict(src_dict)
        plant_id = d.pop("plantId", UNSET)

        api_meter_type = d.pop("apiMeterType", UNSET)

        api_account = d.pop("apiAccount", UNSET)

        _other_properties = d.pop("otherProperties", UNSET)
        other_properties: ApiMeterPullRemoteDevicePostInputModelOtherProperties | Unset
        if isinstance(_other_properties, Unset):
            other_properties = UNSET
        else:
            other_properties = ApiMeterPullRemoteDevicePostInputModelOtherProperties.from_dict(
                _other_properties
            )

        api_meter_pull_remote_device_post_input_model = cls(
            plant_id=plant_id,
            api_meter_type=api_meter_type,
            api_account=api_account,
            other_properties=other_properties,
        )

        api_meter_pull_remote_device_post_input_model.additional_properties = d
        return api_meter_pull_remote_device_post_input_model

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
