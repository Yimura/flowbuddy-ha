from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.hvac_set_heat_temperature_post_input_model_other_properties import (
        HVACSetHeatTemperaturePostInputModelOtherProperties,
    )


T = TypeVar("T", bound="HVACSetHeatTemperaturePostInputModel")


@_attrs_define
class HVACSetHeatTemperaturePostInputModel:
    """
    Attributes:
        value (float | Unset):
        other_properties (HVACSetHeatTemperaturePostInputModelOtherProperties | Unset):
    """

    value: float | Unset = UNSET
    other_properties: HVACSetHeatTemperaturePostInputModelOtherProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hvac_set_heat_temperature_post_input_model_other_properties import (
            HVACSetHeatTemperaturePostInputModelOtherProperties,
        )

        value = self.value

        other_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_properties, Unset):
            other_properties = self.other_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hvac_set_heat_temperature_post_input_model_other_properties import (
            HVACSetHeatTemperaturePostInputModelOtherProperties,
        )

        d = dict(src_dict)
        value = d.pop("value", UNSET)

        _other_properties = d.pop("otherProperties", UNSET)
        other_properties: HVACSetHeatTemperaturePostInputModelOtherProperties | Unset
        if isinstance(_other_properties, Unset):
            other_properties = UNSET
        else:
            other_properties = HVACSetHeatTemperaturePostInputModelOtherProperties.from_dict(
                _other_properties
            )

        hvac_set_heat_temperature_post_input_model = cls(
            value=value,
            other_properties=other_properties,
        )

        hvac_set_heat_temperature_post_input_model.additional_properties = d
        return hvac_set_heat_temperature_post_input_model

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
