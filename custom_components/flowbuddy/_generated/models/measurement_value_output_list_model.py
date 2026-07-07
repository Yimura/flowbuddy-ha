from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.measurement_value_output_model import MeasurementValueOutputModel


T = TypeVar("T", bound="MeasurementValueOutputListModel")


@_attrs_define
class MeasurementValueOutputListModel:
    """
    Attributes:
        measurement_values (list[MeasurementValueOutputModel] | None | Unset):
    """

    measurement_values: list[MeasurementValueOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.measurement_value_output_model import MeasurementValueOutputModel

        measurement_values: list[dict[str, Any]] | None | Unset
        if isinstance(self.measurement_values, Unset):
            measurement_values = UNSET
        elif isinstance(self.measurement_values, list):
            measurement_values = []
            for measurement_values_type_0_item_data in self.measurement_values:
                measurement_values_type_0_item = measurement_values_type_0_item_data.to_dict()
                measurement_values.append(measurement_values_type_0_item)

        else:
            measurement_values = self.measurement_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_values is not UNSET:
            field_dict["measurementValues"] = measurement_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurement_value_output_model import MeasurementValueOutputModel

        d = dict(src_dict)

        def _parse_measurement_values(
            data: object,
        ) -> list[MeasurementValueOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                measurement_values_type_0 = []
                _measurement_values_type_0 = data
                for measurement_values_type_0_item_data in _measurement_values_type_0:
                    measurement_values_type_0_item = MeasurementValueOutputModel.from_dict(
                        measurement_values_type_0_item_data
                    )

                    measurement_values_type_0.append(measurement_values_type_0_item)

                return measurement_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeasurementValueOutputModel] | None | Unset, data)

        measurement_values = _parse_measurement_values(d.pop("measurementValues", UNSET))

        measurement_value_output_list_model = cls(
            measurement_values=measurement_values,
        )

        measurement_value_output_list_model.additional_properties = d
        return measurement_value_output_list_model

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
