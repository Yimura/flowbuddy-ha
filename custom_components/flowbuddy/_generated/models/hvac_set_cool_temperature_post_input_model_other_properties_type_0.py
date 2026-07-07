from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.hvac_set_cool_temperature_post_input_model_other_properties_type_0_additional_property import (
        HVACSetCoolTemperaturePostInputModelOtherPropertiesType0AdditionalProperty,
    )


T = TypeVar("T", bound="HVACSetCoolTemperaturePostInputModelOtherPropertiesType0")


@_attrs_define
class HVACSetCoolTemperaturePostInputModelOtherPropertiesType0:
    """ """

    additional_properties: dict[
        str, HVACSetCoolTemperaturePostInputModelOtherPropertiesType0AdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hvac_set_cool_temperature_post_input_model_other_properties_type_0_additional_property import (
            HVACSetCoolTemperaturePostInputModelOtherPropertiesType0AdditionalProperty,
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hvac_set_cool_temperature_post_input_model_other_properties_type_0_additional_property import (
            HVACSetCoolTemperaturePostInputModelOtherPropertiesType0AdditionalProperty,
        )

        d = dict(src_dict)
        hvac_set_cool_temperature_post_input_model_other_properties_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = HVACSetCoolTemperaturePostInputModelOtherPropertiesType0AdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        hvac_set_cool_temperature_post_input_model_other_properties_type_0.additional_properties = (
            additional_properties
        )
        return hvac_set_cool_temperature_post_input_model_other_properties_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> HVACSetCoolTemperaturePostInputModelOtherPropertiesType0AdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: HVACSetCoolTemperaturePostInputModelOtherPropertiesType0AdditionalProperty,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
