from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.api_meter_create_remote_device_post_input_model_other_properties_type_0 import (
        ApiMeterCreateRemoteDevicePostInputModelOtherPropertiesType0,
    )


T = TypeVar("T", bound="ApiMeterCreateRemoteDevicePostInputModel")


@_attrs_define
class ApiMeterCreateRemoteDevicePostInputModel:
    """
    Attributes:
        serial_number (None | str | Unset): EAN code for Fluvius, Inverter serialNumber for SolarEdge
        email_address (None | str | Unset): E-mailadres to send the mandate request to (Fluvius)
        api_meter_type (None | str | Unset): SolarEdge or Fluvius
        api_account (None | str | Unset): The account to be used to connect to the API
        other_properties (ApiMeterCreateRemoteDevicePostInputModelOtherPropertiesType0 | None | Unset):
    """

    serial_number: None | str | Unset = UNSET
    email_address: None | str | Unset = UNSET
    api_meter_type: None | str | Unset = UNSET
    api_account: None | str | Unset = UNSET
    other_properties: (
        ApiMeterCreateRemoteDevicePostInputModelOtherPropertiesType0 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_meter_create_remote_device_post_input_model_other_properties_type_0 import (
            ApiMeterCreateRemoteDevicePostInputModelOtherPropertiesType0,
        )

        serial_number: None | str | Unset
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        email_address: None | str | Unset
        if isinstance(self.email_address, Unset):
            email_address = UNSET
        else:
            email_address = self.email_address

        api_meter_type: None | str | Unset
        if isinstance(self.api_meter_type, Unset):
            api_meter_type = UNSET
        else:
            api_meter_type = self.api_meter_type

        api_account: None | str | Unset
        if isinstance(self.api_account, Unset):
            api_account = UNSET
        else:
            api_account = self.api_account

        other_properties: dict[str, Any] | None | Unset
        if isinstance(self.other_properties, Unset):
            other_properties = UNSET
        elif isinstance(
            self.other_properties, ApiMeterCreateRemoteDevicePostInputModelOtherPropertiesType0
        ):
            other_properties = self.other_properties.to_dict()
        else:
            other_properties = self.other_properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if api_meter_type is not UNSET:
            field_dict["apiMeterType"] = api_meter_type
        if api_account is not UNSET:
            field_dict["apiAccount"] = api_account
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_meter_create_remote_device_post_input_model_other_properties_type_0 import (
            ApiMeterCreateRemoteDevicePostInputModelOtherPropertiesType0,
        )

        d = dict(src_dict)

        def _parse_serial_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        serial_number = _parse_serial_number(d.pop("serialNumber", UNSET))

        def _parse_email_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address = _parse_email_address(d.pop("emailAddress", UNSET))

        def _parse_api_meter_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_meter_type = _parse_api_meter_type(d.pop("apiMeterType", UNSET))

        def _parse_api_account(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_account = _parse_api_account(d.pop("apiAccount", UNSET))

        def _parse_other_properties(
            data: object,
        ) -> ApiMeterCreateRemoteDevicePostInputModelOtherPropertiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_properties_type_0 = (
                    ApiMeterCreateRemoteDevicePostInputModelOtherPropertiesType0.from_dict(data)
                )

                return other_properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ApiMeterCreateRemoteDevicePostInputModelOtherPropertiesType0 | None | Unset, data
            )

        other_properties = _parse_other_properties(d.pop("otherProperties", UNSET))

        api_meter_create_remote_device_post_input_model = cls(
            serial_number=serial_number,
            email_address=email_address,
            api_meter_type=api_meter_type,
            api_account=api_account,
            other_properties=other_properties,
        )

        api_meter_create_remote_device_post_input_model.additional_properties = d
        return api_meter_create_remote_device_post_input_model

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
