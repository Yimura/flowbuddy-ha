from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.meter_register_measurement_post_input_model_other_properties import (
        MeterRegisterMeasurementPostInputModelOtherProperties,
    )


T = TypeVar("T", bound="MeterRegisterMeasurementPostInputModel")


@_attrs_define
class MeterRegisterMeasurementPostInputModel:
    """
    Attributes:
        measurement_type (str | Unset):
        force_polling (bool | Unset):
        initial_polling (str | Unset):
        other_properties (MeterRegisterMeasurementPostInputModelOtherProperties | Unset):
    """

    measurement_type: str | Unset = UNSET
    force_polling: bool | Unset = UNSET
    initial_polling: str | Unset = UNSET
    other_properties: MeterRegisterMeasurementPostInputModelOtherProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meter_register_measurement_post_input_model_other_properties import (
            MeterRegisterMeasurementPostInputModelOtherProperties,
        )

        measurement_type = self.measurement_type

        force_polling = self.force_polling

        initial_polling = self.initial_polling

        other_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_properties, Unset):
            other_properties = self.other_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_type is not UNSET:
            field_dict["measurementType"] = measurement_type
        if force_polling is not UNSET:
            field_dict["forcePolling"] = force_polling
        if initial_polling is not UNSET:
            field_dict["initialPolling"] = initial_polling
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meter_register_measurement_post_input_model_other_properties import (
            MeterRegisterMeasurementPostInputModelOtherProperties,
        )

        d = dict(src_dict)
        measurement_type = d.pop("measurementType", UNSET)

        force_polling = d.pop("forcePolling", UNSET)

        initial_polling = d.pop("initialPolling", UNSET)

        _other_properties = d.pop("otherProperties", UNSET)
        other_properties: MeterRegisterMeasurementPostInputModelOtherProperties | Unset
        if isinstance(_other_properties, Unset):
            other_properties = UNSET
        else:
            other_properties = MeterRegisterMeasurementPostInputModelOtherProperties.from_dict(
                _other_properties
            )

        meter_register_measurement_post_input_model = cls(
            measurement_type=measurement_type,
            force_polling=force_polling,
            initial_polling=initial_polling,
            other_properties=other_properties,
        )

        meter_register_measurement_post_input_model.additional_properties = d
        return meter_register_measurement_post_input_model

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
