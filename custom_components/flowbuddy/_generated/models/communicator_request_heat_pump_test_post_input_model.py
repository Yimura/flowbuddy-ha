from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.communicator_request_heat_pump_test_post_input_model_other_properties import (
        CommunicatorRequestHeatPumpTestPostInputModelOtherProperties,
    )


T = TypeVar("T", bound="CommunicatorRequestHeatPumpTestPostInputModel")


@_attrs_define
class CommunicatorRequestHeatPumpTestPostInputModel:
    """
    Attributes:
        test_duration_per_mode (int | Unset): The duration per mode expressed in minutes
        other_properties (CommunicatorRequestHeatPumpTestPostInputModelOtherProperties | Unset):
    """

    test_duration_per_mode: int | Unset = UNSET
    other_properties: CommunicatorRequestHeatPumpTestPostInputModelOtherProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_request_heat_pump_test_post_input_model_other_properties import (
            CommunicatorRequestHeatPumpTestPostInputModelOtherProperties,
        )

        test_duration_per_mode = self.test_duration_per_mode

        other_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_properties, Unset):
            other_properties = self.other_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if test_duration_per_mode is not UNSET:
            field_dict["testDurationPerMode"] = test_duration_per_mode
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communicator_request_heat_pump_test_post_input_model_other_properties import (
            CommunicatorRequestHeatPumpTestPostInputModelOtherProperties,
        )

        d = dict(src_dict)
        test_duration_per_mode = d.pop("testDurationPerMode", UNSET)

        _other_properties = d.pop("otherProperties", UNSET)
        other_properties: CommunicatorRequestHeatPumpTestPostInputModelOtherProperties | Unset
        if isinstance(_other_properties, Unset):
            other_properties = UNSET
        else:
            other_properties = (
                CommunicatorRequestHeatPumpTestPostInputModelOtherProperties.from_dict(
                    _other_properties
                )
            )

        communicator_request_heat_pump_test_post_input_model = cls(
            test_duration_per_mode=test_duration_per_mode,
            other_properties=other_properties,
        )

        communicator_request_heat_pump_test_post_input_model.additional_properties = d
        return communicator_request_heat_pump_test_post_input_model

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
