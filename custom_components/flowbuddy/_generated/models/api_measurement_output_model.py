from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.api_measurement_type_reference_model import ApiMeasurementTypeReferenceModel
    from ..models.api_meter_reference_model import ApiMeterReferenceModel


T = TypeVar("T", bound="ApiMeasurementOutputModel")


@_attrs_define
class ApiMeasurementOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        name (None | str | Unset):
        external_id (None | str | Unset):
        api_measurement_type (ApiMeasurementTypeReferenceModel | None | Unset):
        api_meter (ApiMeterReferenceModel | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    api_measurement_type: ApiMeasurementTypeReferenceModel | None | Unset = UNSET
    api_meter: ApiMeterReferenceModel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_measurement_type_reference_model import ApiMeasurementTypeReferenceModel
        from ..models.api_meter_reference_model import ApiMeterReferenceModel

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

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        api_measurement_type: dict[str, Any] | None | Unset
        if isinstance(self.api_measurement_type, Unset):
            api_measurement_type = UNSET
        elif isinstance(self.api_measurement_type, ApiMeasurementTypeReferenceModel):
            api_measurement_type = self.api_measurement_type.to_dict()
        else:
            api_measurement_type = self.api_measurement_type

        api_meter: dict[str, Any] | None | Unset
        if isinstance(self.api_meter, Unset):
            api_meter = UNSET
        elif isinstance(self.api_meter, ApiMeterReferenceModel):
            api_meter = self.api_meter.to_dict()
        else:
            api_meter = self.api_meter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if name is not UNSET:
            field_dict["name"] = name
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if api_measurement_type is not UNSET:
            field_dict["apiMeasurementType"] = api_measurement_type
        if api_meter is not UNSET:
            field_dict["apiMeter"] = api_meter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_measurement_type_reference_model import ApiMeasurementTypeReferenceModel
        from ..models.api_meter_reference_model import ApiMeterReferenceModel

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

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_api_measurement_type(
            data: object,
        ) -> ApiMeasurementTypeReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                api_measurement_type_type_1 = ApiMeasurementTypeReferenceModel.from_dict(data)

                return api_measurement_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiMeasurementTypeReferenceModel | None | Unset, data)

        api_measurement_type = _parse_api_measurement_type(d.pop("apiMeasurementType", UNSET))

        def _parse_api_meter(data: object) -> ApiMeterReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                api_meter_type_1 = ApiMeterReferenceModel.from_dict(data)

                return api_meter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiMeterReferenceModel | None | Unset, data)

        api_meter = _parse_api_meter(d.pop("apiMeter", UNSET))

        api_measurement_output_model = cls(
            resource_uri=resource_uri,
            name=name,
            external_id=external_id,
            api_measurement_type=api_measurement_type,
            api_meter=api_meter,
        )

        api_measurement_output_model.additional_properties = d
        return api_measurement_output_model

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
