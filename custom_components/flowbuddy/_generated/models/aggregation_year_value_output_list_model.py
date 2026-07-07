from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.aggregation_year_value_output_model import AggregationYearValueOutputModel


T = TypeVar("T", bound="AggregationYearValueOutputListModel")


@_attrs_define
class AggregationYearValueOutputListModel:
    """
    Attributes:
        aggregation_year_values (list[AggregationYearValueOutputModel] | None | Unset):
    """

    aggregation_year_values: list[AggregationYearValueOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.aggregation_year_value_output_model import AggregationYearValueOutputModel

        aggregation_year_values: list[dict[str, Any]] | None | Unset
        if isinstance(self.aggregation_year_values, Unset):
            aggregation_year_values = UNSET
        elif isinstance(self.aggregation_year_values, list):
            aggregation_year_values = []
            for aggregation_year_values_type_0_item_data in self.aggregation_year_values:
                aggregation_year_values_type_0_item = (
                    aggregation_year_values_type_0_item_data.to_dict()
                )
                aggregation_year_values.append(aggregation_year_values_type_0_item)

        else:
            aggregation_year_values = self.aggregation_year_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregation_year_values is not UNSET:
            field_dict["aggregationYearValues"] = aggregation_year_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aggregation_year_value_output_model import AggregationYearValueOutputModel

        d = dict(src_dict)

        def _parse_aggregation_year_values(
            data: object,
        ) -> list[AggregationYearValueOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aggregation_year_values_type_0 = []
                _aggregation_year_values_type_0 = data
                for aggregation_year_values_type_0_item_data in _aggregation_year_values_type_0:
                    aggregation_year_values_type_0_item = AggregationYearValueOutputModel.from_dict(
                        aggregation_year_values_type_0_item_data
                    )

                    aggregation_year_values_type_0.append(aggregation_year_values_type_0_item)

                return aggregation_year_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AggregationYearValueOutputModel] | None | Unset, data)

        aggregation_year_values = _parse_aggregation_year_values(
            d.pop("aggregationYearValues", UNSET)
        )

        aggregation_year_value_output_list_model = cls(
            aggregation_year_values=aggregation_year_values,
        )

        aggregation_year_value_output_list_model.additional_properties = d
        return aggregation_year_value_output_list_model

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
