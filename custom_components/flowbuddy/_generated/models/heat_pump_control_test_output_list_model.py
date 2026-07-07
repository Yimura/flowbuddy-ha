from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.heat_pump_control_test_output_model import HeatPumpControlTestOutputModel


T = TypeVar("T", bound="HeatPumpControlTestOutputListModel")


@_attrs_define
class HeatPumpControlTestOutputListModel:
    """
    Attributes:
        heat_pump_control_tests (list[HeatPumpControlTestOutputModel] | Unset):
    """

    heat_pump_control_tests: list[HeatPumpControlTestOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.heat_pump_control_test_output_model import HeatPumpControlTestOutputModel

        heat_pump_control_tests: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.heat_pump_control_tests, Unset):
            heat_pump_control_tests = []
            for heat_pump_control_tests_item_data in self.heat_pump_control_tests:
                heat_pump_control_tests_item = heat_pump_control_tests_item_data.to_dict()
                heat_pump_control_tests.append(heat_pump_control_tests_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if heat_pump_control_tests is not UNSET:
            field_dict["heatPumpControlTests"] = heat_pump_control_tests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.heat_pump_control_test_output_model import HeatPumpControlTestOutputModel

        d = dict(src_dict)
        _heat_pump_control_tests = d.pop("heatPumpControlTests", UNSET)
        heat_pump_control_tests: list[HeatPumpControlTestOutputModel] | Unset = UNSET
        if _heat_pump_control_tests is not UNSET:
            heat_pump_control_tests = []
            for heat_pump_control_tests_item_data in _heat_pump_control_tests:
                heat_pump_control_tests_item = HeatPumpControlTestOutputModel.from_dict(
                    heat_pump_control_tests_item_data
                )

                heat_pump_control_tests.append(heat_pump_control_tests_item)

        heat_pump_control_test_output_list_model = cls(
            heat_pump_control_tests=heat_pump_control_tests,
        )

        heat_pump_control_test_output_list_model.additional_properties = d
        return heat_pump_control_test_output_list_model

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
