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
    from ..models.installation_pool_control_post_input_model_other_properties import (
        InstallationPoolControlPostInputModelOtherProperties,
    )


T = TypeVar("T", bound="InstallationPoolControlPostInputModel")


@_attrs_define
class InstallationPoolControlPostInputModel:
    """
    Attributes:
        control_type (str | Unset):
        timestamp (datetime.datetime | Unset):
        value (str | Unset):
        other_properties (InstallationPoolControlPostInputModelOtherProperties | Unset):
    """

    control_type: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    value: str | Unset = UNSET
    other_properties: InstallationPoolControlPostInputModelOtherProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_pool_control_post_input_model_other_properties import (
            InstallationPoolControlPostInputModelOtherProperties,
        )

        control_type = self.control_type

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        value = self.value

        other_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_properties, Unset):
            other_properties = self.other_properties.to_dict()

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
        from ..models.installation_pool_control_post_input_model_other_properties import (
            InstallationPoolControlPostInputModelOtherProperties,
        )

        d = dict(src_dict)
        control_type = d.pop("controlType", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        value = d.pop("value", UNSET)

        _other_properties = d.pop("otherProperties", UNSET)
        other_properties: InstallationPoolControlPostInputModelOtherProperties | Unset
        if isinstance(_other_properties, Unset):
            other_properties = UNSET
        else:
            other_properties = InstallationPoolControlPostInputModelOtherProperties.from_dict(
                _other_properties
            )

        installation_pool_control_post_input_model = cls(
            control_type=control_type,
            timestamp=timestamp,
            value=value,
            other_properties=other_properties,
        )

        installation_pool_control_post_input_model.additional_properties = d
        return installation_pool_control_post_input_model

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
