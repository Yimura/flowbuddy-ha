from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.pv_report_output_model import PvReportOutputModel


T = TypeVar("T", bound="PvReportOutputListModel")


@_attrs_define
class PvReportOutputListModel:
    """
    Attributes:
        pv_reports (list[PvReportOutputModel] | None | Unset):
    """

    pv_reports: list[PvReportOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pv_report_output_model import PvReportOutputModel

        pv_reports: list[dict[str, Any]] | None | Unset
        if isinstance(self.pv_reports, Unset):
            pv_reports = UNSET
        elif isinstance(self.pv_reports, list):
            pv_reports = []
            for pv_reports_type_0_item_data in self.pv_reports:
                pv_reports_type_0_item = pv_reports_type_0_item_data.to_dict()
                pv_reports.append(pv_reports_type_0_item)

        else:
            pv_reports = self.pv_reports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pv_reports is not UNSET:
            field_dict["pvReports"] = pv_reports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pv_report_output_model import PvReportOutputModel

        d = dict(src_dict)

        def _parse_pv_reports(data: object) -> list[PvReportOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pv_reports_type_0 = []
                _pv_reports_type_0 = data
                for pv_reports_type_0_item_data in _pv_reports_type_0:
                    pv_reports_type_0_item = PvReportOutputModel.from_dict(
                        pv_reports_type_0_item_data
                    )

                    pv_reports_type_0.append(pv_reports_type_0_item)

                return pv_reports_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PvReportOutputModel] | None | Unset, data)

        pv_reports = _parse_pv_reports(d.pop("pvReports", UNSET))

        pv_report_output_list_model = cls(
            pv_reports=pv_reports,
        )

        pv_report_output_list_model.additional_properties = d
        return pv_report_output_list_model

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
