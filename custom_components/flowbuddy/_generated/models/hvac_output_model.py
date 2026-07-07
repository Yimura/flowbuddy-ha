from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.meter_reference_model import MeterReferenceModel


T = TypeVar("T", bound="HVACOutputModel")


@_attrs_define
class HVACOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        last_set_cool_temperature (float | None | Unset):
        last_set_heat_temperature (float | None | Unset):
        external_id (None | str | Unset):
        info (MeterReferenceModel | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    last_set_cool_temperature: float | None | Unset = UNSET
    last_set_heat_temperature: float | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    info: MeterReferenceModel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meter_reference_model import MeterReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        last_set_cool_temperature: float | None | Unset
        if isinstance(self.last_set_cool_temperature, Unset):
            last_set_cool_temperature = UNSET
        else:
            last_set_cool_temperature = self.last_set_cool_temperature

        last_set_heat_temperature: float | None | Unset
        if isinstance(self.last_set_heat_temperature, Unset):
            last_set_heat_temperature = UNSET
        else:
            last_set_heat_temperature = self.last_set_heat_temperature

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        info: dict[str, Any] | None | Unset
        if isinstance(self.info, Unset):
            info = UNSET
        elif isinstance(self.info, MeterReferenceModel):
            info = self.info.to_dict()
        else:
            info = self.info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if last_set_cool_temperature is not UNSET:
            field_dict["lastSetCoolTemperature"] = last_set_cool_temperature
        if last_set_heat_temperature is not UNSET:
            field_dict["lastSetHeatTemperature"] = last_set_heat_temperature
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meter_reference_model import MeterReferenceModel

        d = dict(src_dict)

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

        def _parse_last_set_cool_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        last_set_cool_temperature = _parse_last_set_cool_temperature(
            d.pop("lastSetCoolTemperature", UNSET)
        )

        def _parse_last_set_heat_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        last_set_heat_temperature = _parse_last_set_heat_temperature(
            d.pop("lastSetHeatTemperature", UNSET)
        )

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_info(data: object) -> MeterReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                info_type_1 = MeterReferenceModel.from_dict(data)

                return info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MeterReferenceModel | None | Unset, data)

        info = _parse_info(d.pop("info", UNSET))

        hvac_output_model = cls(
            resource_uri=resource_uri,
            last_set_cool_temperature=last_set_cool_temperature,
            last_set_heat_temperature=last_set_heat_temperature,
            external_id=external_id,
            info=info,
        )

        hvac_output_model.additional_properties = d
        return hvac_output_model

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
