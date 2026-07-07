from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.aggregation_month_value_output_model import AggregationMonthValueOutputModel


T = TypeVar("T", bound="AggregationMonthValueOutputListModel")


@_attrs_define
class AggregationMonthValueOutputListModel:
    """
    Attributes:
        aggregation_month_values (list[AggregationMonthValueOutputModel] | Unset):
    """

    aggregation_month_values: list[AggregationMonthValueOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.aggregation_month_value_output_model import AggregationMonthValueOutputModel

        aggregation_month_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aggregation_month_values, Unset):
            aggregation_month_values = []
            for aggregation_month_values_item_data in self.aggregation_month_values:
                aggregation_month_values_item = aggregation_month_values_item_data.to_dict()
                aggregation_month_values.append(aggregation_month_values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregation_month_values is not UNSET:
            field_dict["aggregationMonthValues"] = aggregation_month_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aggregation_month_value_output_model import AggregationMonthValueOutputModel

        d = dict(src_dict)
        _aggregation_month_values = d.pop("aggregationMonthValues", UNSET)
        aggregation_month_values: list[AggregationMonthValueOutputModel] | Unset = UNSET
        if _aggregation_month_values is not UNSET:
            aggregation_month_values = []
            for aggregation_month_values_item_data in _aggregation_month_values:
                aggregation_month_values_item = AggregationMonthValueOutputModel.from_dict(
                    aggregation_month_values_item_data
                )

                aggregation_month_values.append(aggregation_month_values_item)

        aggregation_month_value_output_list_model = cls(
            aggregation_month_values=aggregation_month_values,
        )

        aggregation_month_value_output_list_model.additional_properties = d
        return aggregation_month_value_output_list_model

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
