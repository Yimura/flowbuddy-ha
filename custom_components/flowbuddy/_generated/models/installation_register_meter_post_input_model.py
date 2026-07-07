from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.installation_register_meter_post_input_model_other_properties_type_0 import (
        InstallationRegisterMeterPostInputModelOtherPropertiesType0,
    )


T = TypeVar("T", bound="InstallationRegisterMeterPostInputModel")


@_attrs_define
class InstallationRegisterMeterPostInputModel:
    """
    Attributes:
        measuring_device (None | str | Unset):
        description (None | str | Unset): Custom name that will be used to fill in Meter Type
        initial_polling (None | str | Unset): You can choose which data to process for this particular device. All data
            (whole period) or only the data read after registration.
        other_properties (InstallationRegisterMeterPostInputModelOtherPropertiesType0 | None | Unset):
    """

    measuring_device: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    initial_polling: None | str | Unset = UNSET
    other_properties: InstallationRegisterMeterPostInputModelOtherPropertiesType0 | None | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_register_meter_post_input_model_other_properties_type_0 import (
            InstallationRegisterMeterPostInputModelOtherPropertiesType0,
        )

        measuring_device: None | str | Unset
        if isinstance(self.measuring_device, Unset):
            measuring_device = UNSET
        else:
            measuring_device = self.measuring_device

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        initial_polling: None | str | Unset
        if isinstance(self.initial_polling, Unset):
            initial_polling = UNSET
        else:
            initial_polling = self.initial_polling

        other_properties: dict[str, Any] | None | Unset
        if isinstance(self.other_properties, Unset):
            other_properties = UNSET
        elif isinstance(
            self.other_properties, InstallationRegisterMeterPostInputModelOtherPropertiesType0
        ):
            other_properties = self.other_properties.to_dict()
        else:
            other_properties = self.other_properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measuring_device is not UNSET:
            field_dict["measuringDevice"] = measuring_device
        if description is not UNSET:
            field_dict["description"] = description
        if initial_polling is not UNSET:
            field_dict["initialPolling"] = initial_polling
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.installation_register_meter_post_input_model_other_properties_type_0 import (
            InstallationRegisterMeterPostInputModelOtherPropertiesType0,
        )

        d = dict(src_dict)

        def _parse_measuring_device(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        measuring_device = _parse_measuring_device(d.pop("measuringDevice", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_initial_polling(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        initial_polling = _parse_initial_polling(d.pop("initialPolling", UNSET))

        def _parse_other_properties(
            data: object,
        ) -> InstallationRegisterMeterPostInputModelOtherPropertiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_properties_type_0 = (
                    InstallationRegisterMeterPostInputModelOtherPropertiesType0.from_dict(data)
                )

                return other_properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InstallationRegisterMeterPostInputModelOtherPropertiesType0 | None | Unset, data
            )

        other_properties = _parse_other_properties(d.pop("otherProperties", UNSET))

        installation_register_meter_post_input_model = cls(
            measuring_device=measuring_device,
            description=description,
            initial_polling=initial_polling,
            other_properties=other_properties,
        )

        installation_register_meter_post_input_model.additional_properties = d
        return installation_register_meter_post_input_model

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
