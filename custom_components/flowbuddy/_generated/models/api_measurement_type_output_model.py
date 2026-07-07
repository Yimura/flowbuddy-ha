from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.api_meter_type_reference_model import ApiMeterTypeReferenceModel


T = TypeVar("T", bound="ApiMeasurementTypeOutputModel")


@_attrs_define
class ApiMeasurementTypeOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        name (None | str | Unset):
        is_cumulative (bool | None | Unset):
        external_id (None | str | Unset):
        api_meter_type (ApiMeterTypeReferenceModel | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    is_cumulative: bool | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    api_meter_type: ApiMeterTypeReferenceModel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_meter_type_reference_model import ApiMeterTypeReferenceModel

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

        is_cumulative: bool | None | Unset
        if isinstance(self.is_cumulative, Unset):
            is_cumulative = UNSET
        else:
            is_cumulative = self.is_cumulative

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        api_meter_type: dict[str, Any] | None | Unset
        if isinstance(self.api_meter_type, Unset):
            api_meter_type = UNSET
        elif isinstance(self.api_meter_type, ApiMeterTypeReferenceModel):
            api_meter_type = self.api_meter_type.to_dict()
        else:
            api_meter_type = self.api_meter_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if name is not UNSET:
            field_dict["name"] = name
        if is_cumulative is not UNSET:
            field_dict["isCumulative"] = is_cumulative
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if api_meter_type is not UNSET:
            field_dict["apiMeterType"] = api_meter_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_meter_type_reference_model import ApiMeterTypeReferenceModel

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

        def _parse_is_cumulative(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_cumulative = _parse_is_cumulative(d.pop("isCumulative", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_api_meter_type(data: object) -> ApiMeterTypeReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                api_meter_type_type_1 = ApiMeterTypeReferenceModel.from_dict(data)

                return api_meter_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiMeterTypeReferenceModel | None | Unset, data)

        api_meter_type = _parse_api_meter_type(d.pop("apiMeterType", UNSET))

        api_measurement_type_output_model = cls(
            resource_uri=resource_uri,
            name=name,
            is_cumulative=is_cumulative,
            external_id=external_id,
            api_meter_type=api_meter_type,
        )

        api_measurement_type_output_model.additional_properties = d
        return api_measurement_type_output_model

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
