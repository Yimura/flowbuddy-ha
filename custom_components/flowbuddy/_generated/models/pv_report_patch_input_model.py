from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.pv_report_patch_input_model_other_properties_type_0 import (
        PvReportPatchInputModelOtherPropertiesType0,
    )


T = TypeVar("T", bound="PvReportPatchInputModel")


@_attrs_define
class PvReportPatchInputModel:
    """
    Attributes:
        installation (None | str | Unset):
        template (None | str | Unset):
        create_report (None | str | Unset):
        other_properties (None | PvReportPatchInputModelOtherPropertiesType0 | Unset):
    """

    installation: None | str | Unset = UNSET
    template: None | str | Unset = UNSET
    create_report: None | str | Unset = UNSET
    other_properties: None | PvReportPatchInputModelOtherPropertiesType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pv_report_patch_input_model_other_properties_type_0 import (
            PvReportPatchInputModelOtherPropertiesType0,
        )

        installation: None | str | Unset
        if isinstance(self.installation, Unset):
            installation = UNSET
        else:
            installation = self.installation

        template: None | str | Unset
        if isinstance(self.template, Unset):
            template = UNSET
        else:
            template = self.template

        create_report: None | str | Unset
        if isinstance(self.create_report, Unset):
            create_report = UNSET
        else:
            create_report = self.create_report

        other_properties: dict[str, Any] | None | Unset
        if isinstance(self.other_properties, Unset):
            other_properties = UNSET
        elif isinstance(self.other_properties, PvReportPatchInputModelOtherPropertiesType0):
            other_properties = self.other_properties.to_dict()
        else:
            other_properties = self.other_properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if installation is not UNSET:
            field_dict["installation"] = installation
        if template is not UNSET:
            field_dict["template"] = template
        if create_report is not UNSET:
            field_dict["createReport"] = create_report
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pv_report_patch_input_model_other_properties_type_0 import (
            PvReportPatchInputModelOtherPropertiesType0,
        )

        d = dict(src_dict)

        def _parse_installation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        installation = _parse_installation(d.pop("installation", UNSET))

        def _parse_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template = _parse_template(d.pop("template", UNSET))

        def _parse_create_report(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        create_report = _parse_create_report(d.pop("createReport", UNSET))

        def _parse_other_properties(
            data: object,
        ) -> None | PvReportPatchInputModelOtherPropertiesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_properties_type_0 = PvReportPatchInputModelOtherPropertiesType0.from_dict(
                    data
                )

                return other_properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PvReportPatchInputModelOtherPropertiesType0 | Unset, data)

        other_properties = _parse_other_properties(d.pop("otherProperties", UNSET))

        pv_report_patch_input_model = cls(
            installation=installation,
            template=template,
            create_report=create_report,
            other_properties=other_properties,
        )

        pv_report_patch_input_model.additional_properties = d
        return pv_report_patch_input_model

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
