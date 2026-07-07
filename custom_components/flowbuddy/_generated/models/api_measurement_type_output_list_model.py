from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.api_measurement_type_output_model import ApiMeasurementTypeOutputModel


T = TypeVar("T", bound="ApiMeasurementTypeOutputListModel")


@_attrs_define
class ApiMeasurementTypeOutputListModel:
    """
    Attributes:
        api_measurement_types (list[ApiMeasurementTypeOutputModel] | Unset):
    """

    api_measurement_types: list[ApiMeasurementTypeOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_measurement_type_output_model import ApiMeasurementTypeOutputModel

        api_measurement_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.api_measurement_types, Unset):
            api_measurement_types = []
            for api_measurement_types_item_data in self.api_measurement_types:
                api_measurement_types_item = api_measurement_types_item_data.to_dict()
                api_measurement_types.append(api_measurement_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_measurement_types is not UNSET:
            field_dict["apiMeasurementTypes"] = api_measurement_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_measurement_type_output_model import ApiMeasurementTypeOutputModel

        d = dict(src_dict)
        _api_measurement_types = d.pop("apiMeasurementTypes", UNSET)
        api_measurement_types: list[ApiMeasurementTypeOutputModel] | Unset = UNSET
        if _api_measurement_types is not UNSET:
            api_measurement_types = []
            for api_measurement_types_item_data in _api_measurement_types:
                api_measurement_types_item = ApiMeasurementTypeOutputModel.from_dict(
                    api_measurement_types_item_data
                )

                api_measurement_types.append(api_measurement_types_item)

        api_measurement_type_output_list_model = cls(
            api_measurement_types=api_measurement_types,
        )

        api_measurement_type_output_list_model.additional_properties = d
        return api_measurement_type_output_list_model

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
