from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.measurement_type_output_model import MeasurementTypeOutputModel


T = TypeVar("T", bound="MeasurementTypeOutputListModel")


@_attrs_define
class MeasurementTypeOutputListModel:
    """
    Attributes:
        measurement_types (list[MeasurementTypeOutputModel] | Unset):
    """

    measurement_types: list[MeasurementTypeOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.measurement_type_output_model import MeasurementTypeOutputModel

        measurement_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.measurement_types, Unset):
            measurement_types = []
            for measurement_types_item_data in self.measurement_types:
                measurement_types_item = measurement_types_item_data.to_dict()
                measurement_types.append(measurement_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_types is not UNSET:
            field_dict["measurementTypes"] = measurement_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurement_type_output_model import MeasurementTypeOutputModel

        d = dict(src_dict)
        _measurement_types = d.pop("measurementTypes", UNSET)
        measurement_types: list[MeasurementTypeOutputModel] | Unset = UNSET
        if _measurement_types is not UNSET:
            measurement_types = []
            for measurement_types_item_data in _measurement_types:
                measurement_types_item = MeasurementTypeOutputModel.from_dict(
                    measurement_types_item_data
                )

                measurement_types.append(measurement_types_item)

        measurement_type_output_list_model = cls(
            measurement_types=measurement_types,
        )

        measurement_type_output_list_model.additional_properties = d
        return measurement_type_output_list_model

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
