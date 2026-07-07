from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.api_measurement_output_model import ApiMeasurementOutputModel


T = TypeVar("T", bound="ApiMeasurementOutputListModel")


@_attrs_define
class ApiMeasurementOutputListModel:
    """
    Attributes:
        api_measurements (list[ApiMeasurementOutputModel] | Unset):
    """

    api_measurements: list[ApiMeasurementOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_measurement_output_model import ApiMeasurementOutputModel

        api_measurements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.api_measurements, Unset):
            api_measurements = []
            for api_measurements_item_data in self.api_measurements:
                api_measurements_item = api_measurements_item_data.to_dict()
                api_measurements.append(api_measurements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_measurements is not UNSET:
            field_dict["apiMeasurements"] = api_measurements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_measurement_output_model import ApiMeasurementOutputModel

        d = dict(src_dict)
        _api_measurements = d.pop("apiMeasurements", UNSET)
        api_measurements: list[ApiMeasurementOutputModel] | Unset = UNSET
        if _api_measurements is not UNSET:
            api_measurements = []
            for api_measurements_item_data in _api_measurements:
                api_measurements_item = ApiMeasurementOutputModel.from_dict(
                    api_measurements_item_data
                )

                api_measurements.append(api_measurements_item)

        api_measurement_output_list_model = cls(
            api_measurements=api_measurements,
        )

        api_measurement_output_list_model.additional_properties = d
        return api_measurement_output_list_model

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
