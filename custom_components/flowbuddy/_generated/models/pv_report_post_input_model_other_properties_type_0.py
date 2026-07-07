from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.pv_report_post_input_model_other_properties_type_0_additional_property import (
        PvReportPostInputModelOtherPropertiesType0AdditionalProperty,
    )


T = TypeVar("T", bound="PvReportPostInputModelOtherPropertiesType0")


@_attrs_define
class PvReportPostInputModelOtherPropertiesType0:
    """ """

    additional_properties: dict[
        str, PvReportPostInputModelOtherPropertiesType0AdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pv_report_post_input_model_other_properties_type_0_additional_property import (
            PvReportPostInputModelOtherPropertiesType0AdditionalProperty,
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pv_report_post_input_model_other_properties_type_0_additional_property import (
            PvReportPostInputModelOtherPropertiesType0AdditionalProperty,
        )

        d = dict(src_dict)
        pv_report_post_input_model_other_properties_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                PvReportPostInputModelOtherPropertiesType0AdditionalProperty.from_dict(prop_dict)
            )

            additional_properties[prop_name] = additional_property

        pv_report_post_input_model_other_properties_type_0.additional_properties = (
            additional_properties
        )
        return pv_report_post_input_model_other_properties_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> PvReportPostInputModelOtherPropertiesType0AdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: PvReportPostInputModelOtherPropertiesType0AdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
