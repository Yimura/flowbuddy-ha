from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.meter_control_post_input_model_other_properties_type_0 import (
        MeterControlPostInputModelOtherPropertiesType0,
    )


T = TypeVar("T", bound="MeterControlPostInputModel")


@_attrs_define
class MeterControlPostInputModel:
    """
    Attributes:
        control_type (None | str | Unset):
        timestamp (datetime.datetime | None | Unset):
        value (None | str | Unset):
        other_properties (MeterControlPostInputModelOtherPropertiesType0 | None | Unset):
    """

    control_type: None | str | Unset = UNSET
    timestamp: datetime.datetime | None | Unset = UNSET
    value: None | str | Unset = UNSET
    other_properties: MeterControlPostInputModelOtherPropertiesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meter_control_post_input_model_other_properties_type_0 import (
            MeterControlPostInputModelOtherPropertiesType0,
        )

        control_type: None | str | Unset
        if isinstance(self.control_type, Unset):
            control_type = UNSET
        else:
            control_type = self.control_type

        timestamp: None | str | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        elif isinstance(self.timestamp, datetime.datetime):
            timestamp = self.timestamp.isoformat()
        else:
            timestamp = self.timestamp

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        other_properties: dict[str, Any] | None | Unset
        if isinstance(self.other_properties, Unset):
            other_properties = UNSET
        elif isinstance(self.other_properties, MeterControlPostInputModelOtherPropertiesType0):
            other_properties = self.other_properties.to_dict()
        else:
            other_properties = self.other_properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_type is not UNSET:
            field_dict["controlType"] = control_type
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if value is not UNSET:
            field_dict["value"] = value
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meter_control_post_input_model_other_properties_type_0 import (
            MeterControlPostInputModelOtherPropertiesType0,
        )

        d = dict(src_dict)

        def _parse_control_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        control_type = _parse_control_type(d.pop("controlType", UNSET))

        def _parse_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timestamp_type_0 = datetime.datetime.fromisoformat(data)

                return timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_other_properties(
            data: object,
        ) -> MeterControlPostInputModelOtherPropertiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_properties_type_0 = MeterControlPostInputModelOtherPropertiesType0.from_dict(
                    data
                )

                return other_properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MeterControlPostInputModelOtherPropertiesType0 | None | Unset, data)

        other_properties = _parse_other_properties(d.pop("otherProperties", UNSET))

        meter_control_post_input_model = cls(
            control_type=control_type,
            timestamp=timestamp,
            value=value,
            other_properties=other_properties,
        )

        meter_control_post_input_model.additional_properties = d
        return meter_control_post_input_model

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
