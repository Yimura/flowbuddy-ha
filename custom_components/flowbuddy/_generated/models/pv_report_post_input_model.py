from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.pv_report_post_input_model_other_properties_type_0 import (
        PvReportPostInputModelOtherPropertiesType0,
    )


T = TypeVar("T", bound="PvReportPostInputModel")


@_attrs_define
class PvReportPostInputModel:
    """
    Attributes:
        installation (str):
        template (str):
        create_report (None | str | Unset):
        other_properties (None | PvReportPostInputModelOtherPropertiesType0 | Unset):
    """

    installation: str
    template: str
    create_report: None | str | Unset = UNSET
    other_properties: None | PvReportPostInputModelOtherPropertiesType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pv_report_post_input_model_other_properties_type_0 import (
            PvReportPostInputModelOtherPropertiesType0,
        )

        installation = self.installation

        template = self.template

        create_report: None | str | Unset
        if isinstance(self.create_report, Unset):
            create_report = UNSET
        else:
            create_report = self.create_report

        other_properties: dict[str, Any] | None | Unset
        if isinstance(self.other_properties, Unset):
            other_properties = UNSET
        elif isinstance(self.other_properties, PvReportPostInputModelOtherPropertiesType0):
            other_properties = self.other_properties.to_dict()
        else:
            other_properties = self.other_properties

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
        from ..models.pv_report_post_input_model_other_properties_type_0 import (
            PvReportPostInputModelOtherPropertiesType0,
        )

        d = dict(src_dict)
        installation = d.pop("installation")

        template = d.pop("template")

        def _parse_create_report(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        create_report = _parse_create_report(d.pop("createReport", UNSET))

        def _parse_other_properties(
            data: object,
        ) -> None | PvReportPostInputModelOtherPropertiesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_properties_type_0 = PvReportPostInputModelOtherPropertiesType0.from_dict(data)

                return other_properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PvReportPostInputModelOtherPropertiesType0 | Unset, data)

        other_properties = _parse_other_properties(d.pop("otherProperties", UNSET))

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
