from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.api_meter_type_output_model import ApiMeterTypeOutputModel


T = TypeVar("T", bound="ApiMeterTypeOutputListModel")


@_attrs_define
class ApiMeterTypeOutputListModel:
    """
    Attributes:
        api_meter_types (list[ApiMeterTypeOutputModel] | Unset):
    """

    api_meter_types: list[ApiMeterTypeOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_meter_type_output_model import ApiMeterTypeOutputModel

        api_meter_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.api_meter_types, Unset):
            api_meter_types = []
            for api_meter_types_item_data in self.api_meter_types:
                api_meter_types_item = api_meter_types_item_data.to_dict()
                api_meter_types.append(api_meter_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_meter_types is not UNSET:
            field_dict["apiMeterTypes"] = api_meter_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_meter_type_output_model import ApiMeterTypeOutputModel

        d = dict(src_dict)
        _api_meter_types = d.pop("apiMeterTypes", UNSET)
        api_meter_types: list[ApiMeterTypeOutputModel] | Unset = UNSET
        if _api_meter_types is not UNSET:
            api_meter_types = []
            for api_meter_types_item_data in _api_meter_types:
                api_meter_types_item = ApiMeterTypeOutputModel.from_dict(api_meter_types_item_data)

                api_meter_types.append(api_meter_types_item)

        api_meter_type_output_list_model = cls(
            api_meter_types=api_meter_types,
        )

        api_meter_type_output_list_model.additional_properties = d
        return api_meter_type_output_list_model

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
