from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.pv_report_post_input_model_other_properties import (
        PvReportPostInputModelOtherProperties,
    )


T = TypeVar("T", bound="PvReportPostInputModel")


@_attrs_define
class PvReportPostInputModel:
    """
    Attributes:
        installation (str):
        template (str):
        create_report (str | Unset):
        other_properties (PvReportPostInputModelOtherProperties | Unset):
    """

    installation: str
    template: str
    create_report: str | Unset = UNSET
    other_properties: PvReportPostInputModelOtherProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pv_report_post_input_model_other_properties import (
            PvReportPostInputModelOtherProperties,
        )

        installation = self.installation

        template = self.template

        create_report = self.create_report

        other_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_properties, Unset):
            other_properties = self.other_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "installation": installation,
                "template": template,
            }
        )
        if create_report is not UNSET:
            field_dict["createReport"] = create_report
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pv_report_post_input_model_other_properties import (
            PvReportPostInputModelOtherProperties,
        )

        d = dict(src_dict)
        installation = d.pop("installation")

        template = d.pop("template")

        create_report = d.pop("createReport", UNSET)

        _other_properties = d.pop("otherProperties", UNSET)
        other_properties: PvReportPostInputModelOtherProperties | Unset
        if isinstance(_other_properties, Unset):
            other_properties = UNSET
        else:
            other_properties = PvReportPostInputModelOtherProperties.from_dict(_other_properties)

        pv_report_post_input_model = cls(
            installation=installation,
            template=template,
            create_report=create_report,
            other_properties=other_properties,
        )

        pv_report_post_input_model.additional_properties = d
        return pv_report_post_input_model

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
