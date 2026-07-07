from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.inverter_limit_production_post_input_model_other_properties_additional_property import (
        InverterLimitProductionPostInputModelOtherPropertiesAdditionalProperty,
    )


T = TypeVar("T", bound="InverterLimitProductionPostInputModelOtherProperties")


@_attrs_define
class InverterLimitProductionPostInputModelOtherProperties:
    """ """

    additional_properties: dict[
        str, InverterLimitProductionPostInputModelOtherPropertiesAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.inverter_limit_production_post_input_model_other_properties_additional_property import (
            InverterLimitProductionPostInputModelOtherPropertiesAdditionalProperty,
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inverter_limit_production_post_input_model_other_properties_additional_property import (
            InverterLimitProductionPostInputModelOtherPropertiesAdditionalProperty,
        )

        d = dict(src_dict)
        inverter_limit_production_post_input_model_other_properties = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                InverterLimitProductionPostInputModelOtherPropertiesAdditionalProperty.from_dict(
                    prop_dict
                )
            )

            additional_properties[prop_name] = additional_property

        inverter_limit_production_post_input_model_other_properties.additional_properties = (
            additional_properties
        )
        return inverter_limit_production_post_input_model_other_properties

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> InverterLimitProductionPostInputModelOtherPropertiesAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: InverterLimitProductionPostInputModelOtherPropertiesAdditionalProperty,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
