from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.hvac_set_cool_temperature_post_input_model_other_properties_type_0 import (
        HVACSetCoolTemperaturePostInputModelOtherPropertiesType0,
    )


T = TypeVar("T", bound="HVACSetCoolTemperaturePostInputModel")


@_attrs_define
class HVACSetCoolTemperaturePostInputModel:
    """
    Attributes:
        value (float | None | Unset):
        other_properties (HVACSetCoolTemperaturePostInputModelOtherPropertiesType0 | None | Unset):
    """

    value: float | None | Unset = UNSET
    other_properties: HVACSetCoolTemperaturePostInputModelOtherPropertiesType0 | None | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hvac_set_cool_temperature_post_input_model_other_properties_type_0 import (
            HVACSetCoolTemperaturePostInputModelOtherPropertiesType0,
        )

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        other_properties: dict[str, Any] | None | Unset
        if isinstance(self.other_properties, Unset):
            other_properties = UNSET
        elif isinstance(
            self.other_properties, HVACSetCoolTemperaturePostInputModelOtherPropertiesType0
        ):
            other_properties = self.other_properties.to_dict()
        else:
            other_properties = self.other_properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hvac_set_cool_temperature_post_input_model_other_properties_type_0 import (
            HVACSetCoolTemperaturePostInputModelOtherPropertiesType0,
        )

        d = dict(src_dict)

        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_other_properties(
            data: object,
        ) -> HVACSetCoolTemperaturePostInputModelOtherPropertiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_properties_type_0 = (
                    HVACSetCoolTemperaturePostInputModelOtherPropertiesType0.from_dict(data)
                )

                return other_properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                HVACSetCoolTemperaturePostInputModelOtherPropertiesType0 | None | Unset, data
            )

        other_properties = _parse_other_properties(d.pop("otherProperties", UNSET))

        hvac_set_cool_temperature_post_input_model = cls(
            value=value,
            other_properties=other_properties,
        )

        hvac_set_cool_temperature_post_input_model.additional_properties = d
        return hvac_set_cool_temperature_post_input_model

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
