from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.meter_register_measurement_post_input_model_other_properties_type_0 import (
        MeterRegisterMeasurementPostInputModelOtherPropertiesType0,
    )


T = TypeVar("T", bound="MeterRegisterMeasurementPostInputModel")


@_attrs_define
class MeterRegisterMeasurementPostInputModel:
    """
    Attributes:
        measurement_type (None | str | Unset):
        force_polling (bool | None | Unset):
        initial_polling (None | str | Unset):
        other_properties (MeterRegisterMeasurementPostInputModelOtherPropertiesType0 | None | Unset):
    """

    measurement_type: None | str | Unset = UNSET
    force_polling: bool | None | Unset = UNSET
    initial_polling: None | str | Unset = UNSET
    other_properties: MeterRegisterMeasurementPostInputModelOtherPropertiesType0 | None | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meter_register_measurement_post_input_model_other_properties_type_0 import (
            MeterRegisterMeasurementPostInputModelOtherPropertiesType0,
        )

        measurement_type: None | str | Unset
        if isinstance(self.measurement_type, Unset):
            measurement_type = UNSET
        else:
            measurement_type = self.measurement_type

        force_polling: bool | None | Unset
        if isinstance(self.force_polling, Unset):
            force_polling = UNSET
        else:
            force_polling = self.force_polling

        initial_polling: None | str | Unset
        if isinstance(self.initial_polling, Unset):
            initial_polling = UNSET
        else:
            initial_polling = self.initial_polling

        other_properties: dict[str, Any] | None | Unset
        if isinstance(self.other_properties, Unset):
            other_properties = UNSET
        elif isinstance(
            self.other_properties, MeterRegisterMeasurementPostInputModelOtherPropertiesType0
        ):
            other_properties = self.other_properties.to_dict()
        else:
            other_properties = self.other_properties

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
        from ..models.meter_register_measurement_post_input_model_other_properties_type_0 import (
            MeterRegisterMeasurementPostInputModelOtherPropertiesType0,
        )

        d = dict(src_dict)

        def _parse_measurement_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        measurement_type = _parse_measurement_type(d.pop("measurementType", UNSET))

        def _parse_force_polling(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        force_polling = _parse_force_polling(d.pop("forcePolling", UNSET))

        def _parse_initial_polling(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        initial_polling = _parse_initial_polling(d.pop("initialPolling", UNSET))

        def _parse_other_properties(
            data: object,
        ) -> MeterRegisterMeasurementPostInputModelOtherPropertiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_properties_type_0 = (
                    MeterRegisterMeasurementPostInputModelOtherPropertiesType0.from_dict(data)
                )

                return other_properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                MeterRegisterMeasurementPostInputModelOtherPropertiesType0 | None | Unset, data
            )

        other_properties = _parse_other_properties(d.pop("otherProperties", UNSET))

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
