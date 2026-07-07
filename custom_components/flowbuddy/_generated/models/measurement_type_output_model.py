from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="MeasurementTypeOutputModel")


@_attrs_define
class MeasurementTypeOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        name (str | Unset): Description of the type
        aggregation_type (str | Unset): Indicaties how data is aggregated (e.g. sum, avg, max, min)
        code (str | Unset):
        is_incremental (bool | Unset):
        external_id (str | Unset):
        interval (str | Unset):
        unit (str | Unset):
    """

    resource_uri: str | Unset = UNSET
    name: str | Unset = UNSET
    aggregation_type: str | Unset = UNSET
    code: str | Unset = UNSET
    is_incremental: bool | Unset = UNSET
    external_id: str | Unset = UNSET
    interval: str | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_uri = self.resource_uri

        name = self.name

        aggregation_type = self.aggregation_type

        code = self.code

        is_incremental = self.is_incremental

        external_id = self.external_id

        interval = self.interval

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if name is not UNSET:
            field_dict["name"] = name
        if aggregation_type is not UNSET:
            field_dict["aggregationType"] = aggregation_type
        if code is not UNSET:
            field_dict["code"] = code
        if is_incremental is not UNSET:
            field_dict["isIncremental"] = is_incremental
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if interval is not UNSET:
            field_dict["interval"] = interval
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

        name = d.pop("name", UNSET)

        aggregation_type = d.pop("aggregationType", UNSET)

        code = d.pop("code", UNSET)

        is_incremental = d.pop("isIncremental", UNSET)

        external_id = d.pop("externalId", UNSET)

        interval = d.pop("interval", UNSET)

        unit = d.pop("unit", UNSET)

        measurement_type_output_model = cls(
            resource_uri=resource_uri,
            name=name,
            aggregation_type=aggregation_type,
            code=code,
            is_incremental=is_incremental,
            external_id=external_id,
            interval=interval,
            unit=unit,
        )

        measurement_type_output_model.additional_properties = d
        return measurement_type_output_model

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
