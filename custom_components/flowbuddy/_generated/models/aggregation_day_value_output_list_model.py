from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.aggregation_day_value_output_model import AggregationDayValueOutputModel


T = TypeVar("T", bound="AggregationDayValueOutputListModel")


@_attrs_define
class AggregationDayValueOutputListModel:
    """
    Attributes:
        aggregation_day_values (list[AggregationDayValueOutputModel] | Unset):
    """

    aggregation_day_values: list[AggregationDayValueOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.aggregation_day_value_output_model import AggregationDayValueOutputModel

        aggregation_day_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aggregation_day_values, Unset):
            aggregation_day_values = []
            for aggregation_day_values_item_data in self.aggregation_day_values:
                aggregation_day_values_item = aggregation_day_values_item_data.to_dict()
                aggregation_day_values.append(aggregation_day_values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregation_day_values is not UNSET:
            field_dict["aggregationDayValues"] = aggregation_day_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aggregation_day_value_output_model import AggregationDayValueOutputModel

        d = dict(src_dict)
        _aggregation_day_values = d.pop("aggregationDayValues", UNSET)
        aggregation_day_values: list[AggregationDayValueOutputModel] | Unset = UNSET
        if _aggregation_day_values is not UNSET:
            aggregation_day_values = []
            for aggregation_day_values_item_data in _aggregation_day_values:
                aggregation_day_values_item = AggregationDayValueOutputModel.from_dict(
                    aggregation_day_values_item_data
                )

                aggregation_day_values.append(aggregation_day_values_item)

        aggregation_day_value_output_list_model = cls(
            aggregation_day_values=aggregation_day_values,
        )

        aggregation_day_value_output_list_model.additional_properties = d
        return aggregation_day_value_output_list_model

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
