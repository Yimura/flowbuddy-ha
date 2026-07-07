from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.pv_production_test_output_model import PvProductionTestOutputModel


T = TypeVar("T", bound="PvProductionTestOutputListModel")


@_attrs_define
class PvProductionTestOutputListModel:
    """
    Attributes:
        pv_production_tests (list[PvProductionTestOutputModel] | Unset):
    """

    pv_production_tests: list[PvProductionTestOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pv_production_test_output_model import PvProductionTestOutputModel

        pv_production_tests: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pv_production_tests, Unset):
            pv_production_tests = []
            for pv_production_tests_item_data in self.pv_production_tests:
                pv_production_tests_item = pv_production_tests_item_data.to_dict()
                pv_production_tests.append(pv_production_tests_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pv_production_tests is not UNSET:
            field_dict["pvProductionTests"] = pv_production_tests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pv_production_test_output_model import PvProductionTestOutputModel

        d = dict(src_dict)
        _pv_production_tests = d.pop("pvProductionTests", UNSET)
        pv_production_tests: list[PvProductionTestOutputModel] | Unset = UNSET
        if _pv_production_tests is not UNSET:
            pv_production_tests = []
            for pv_production_tests_item_data in _pv_production_tests:
                pv_production_tests_item = PvProductionTestOutputModel.from_dict(
                    pv_production_tests_item_data
                )

                pv_production_tests.append(pv_production_tests_item)

        pv_production_test_output_list_model = cls(
            pv_production_tests=pv_production_tests,
        )

        pv_production_test_output_list_model.additional_properties = d
        return pv_production_test_output_list_model

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
