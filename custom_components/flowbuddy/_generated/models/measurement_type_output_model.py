from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="MeasurementTypeOutputModel")


@_attrs_define
class MeasurementTypeOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        name (None | str | Unset): Description of the type
        aggregation_type (None | str | Unset): Indicaties how data is aggregated (e.g. sum, avg, max, min)
        code (None | str | Unset):
        is_incremental (bool | None | Unset):
        external_id (None | str | Unset):
        interval (None | str | Unset):
        unit (None | str | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    aggregation_type: None | str | Unset = UNSET
    code: None | str | Unset = UNSET
    is_incremental: bool | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    interval: None | str | Unset = UNSET
    unit: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        aggregation_type: None | str | Unset
        if isinstance(self.aggregation_type, Unset):
            aggregation_type = UNSET
        else:
            aggregation_type = self.aggregation_type

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        is_incremental: bool | None | Unset
        if isinstance(self.is_incremental, Unset):
            is_incremental = UNSET
        else:
            is_incremental = self.is_incremental

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        interval: None | str | Unset
        if isinstance(self.interval, Unset):
            interval = UNSET
        else:
            interval = self.interval

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
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

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_aggregation_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aggregation_type = _parse_aggregation_type(d.pop("aggregationType", UNSET))

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_is_incremental(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_incremental = _parse_is_incremental(d.pop("isIncremental", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_interval(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        interval = _parse_interval(d.pop("interval", UNSET))

        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))

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
