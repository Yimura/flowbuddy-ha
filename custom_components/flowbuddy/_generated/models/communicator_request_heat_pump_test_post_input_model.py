from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.communicator_request_heat_pump_test_post_input_model_other_properties_type_0 import (
        CommunicatorRequestHeatPumpTestPostInputModelOtherPropertiesType0,
    )


T = TypeVar("T", bound="CommunicatorRequestHeatPumpTestPostInputModel")


@_attrs_define
class CommunicatorRequestHeatPumpTestPostInputModel:
    """
    Attributes:
        test_duration_per_mode (int | None | Unset): The duration per mode expressed in minutes
        other_properties (CommunicatorRequestHeatPumpTestPostInputModelOtherPropertiesType0 | None | Unset):
    """

    test_duration_per_mode: int | None | Unset = UNSET
    other_properties: (
        CommunicatorRequestHeatPumpTestPostInputModelOtherPropertiesType0 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_request_heat_pump_test_post_input_model_other_properties_type_0 import (
            CommunicatorRequestHeatPumpTestPostInputModelOtherPropertiesType0,
        )

        test_duration_per_mode: int | None | Unset
        if isinstance(self.test_duration_per_mode, Unset):
            test_duration_per_mode = UNSET
        else:
            test_duration_per_mode = self.test_duration_per_mode

        other_properties: dict[str, Any] | None | Unset
        if isinstance(self.other_properties, Unset):
            other_properties = UNSET
        elif isinstance(
            self.other_properties, CommunicatorRequestHeatPumpTestPostInputModelOtherPropertiesType0
        ):
            other_properties = self.other_properties.to_dict()
        else:
            other_properties = self.other_properties

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
        from ..models.communicator_request_heat_pump_test_post_input_model_other_properties_type_0 import (
            CommunicatorRequestHeatPumpTestPostInputModelOtherPropertiesType0,
        )

        d = dict(src_dict)

        def _parse_test_duration_per_mode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        test_duration_per_mode = _parse_test_duration_per_mode(d.pop("testDurationPerMode", UNSET))

        def _parse_other_properties(
            data: object,
        ) -> CommunicatorRequestHeatPumpTestPostInputModelOtherPropertiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_properties_type_0 = (
                    CommunicatorRequestHeatPumpTestPostInputModelOtherPropertiesType0.from_dict(
                        data
                    )
                )

                return other_properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CommunicatorRequestHeatPumpTestPostInputModelOtherPropertiesType0 | None | Unset,
                data,
            )

        other_properties = _parse_other_properties(d.pop("otherProperties", UNSET))

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
