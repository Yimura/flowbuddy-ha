from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.api_account_reference_model import ApiAccountReferenceModel
    from ..models.api_meter_type_reference_model import ApiMeterTypeReferenceModel


T = TypeVar("T", bound="ApiMeterOutputModel")


@_attrs_define
class ApiMeterOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        identifier (None | str | Unset): Unique identifier for the device. This is only used for Fluvius connections and
            equals the EAN code of the meter
        plant_id (None | str | Unset): A technical reference to the API meter
        serial_number (None | str | Unset): The serialNumber of the device
        external_id (None | str | Unset):
        status (None | str | Unset): The status of the ApiMeter
        status_message (None | str | Unset): Additional info regarding the status
        api_meter_type (ApiMeterTypeReferenceModel | None | Unset):
        api_account (ApiAccountReferenceModel | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    identifier: None | str | Unset = UNSET
    plant_id: None | str | Unset = UNSET
    serial_number: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    status_message: None | str | Unset = UNSET
    api_meter_type: ApiMeterTypeReferenceModel | None | Unset = UNSET
    api_account: ApiAccountReferenceModel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_account_reference_model import ApiAccountReferenceModel
        from ..models.api_meter_type_reference_model import ApiMeterTypeReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        identifier: None | str | Unset
        if isinstance(self.identifier, Unset):
            identifier = UNSET
        else:
            identifier = self.identifier

        plant_id: None | str | Unset
        if isinstance(self.plant_id, Unset):
            plant_id = UNSET
        else:
            plant_id = self.plant_id

        serial_number: None | str | Unset
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        status_message: None | str | Unset
        if isinstance(self.status_message, Unset):
            status_message = UNSET
        else:
            status_message = self.status_message

        api_meter_type: dict[str, Any] | None | Unset
        if isinstance(self.api_meter_type, Unset):
            api_meter_type = UNSET
        elif isinstance(self.api_meter_type, ApiMeterTypeReferenceModel):
            api_meter_type = self.api_meter_type.to_dict()
        else:
            api_meter_type = self.api_meter_type

        api_account: dict[str, Any] | None | Unset
        if isinstance(self.api_account, Unset):
            api_account = UNSET
        elif isinstance(self.api_account, ApiAccountReferenceModel):
            api_account = self.api_account.to_dict()
        else:
            api_account = self.api_account

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if plant_id is not UNSET:
            field_dict["plantId"] = plant_id
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if status is not UNSET:
            field_dict["status"] = status
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message
        if api_meter_type is not UNSET:
            field_dict["apiMeterType"] = api_meter_type
        if api_account is not UNSET:
            field_dict["apiAccount"] = api_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_account_reference_model import ApiAccountReferenceModel
        from ..models.api_meter_type_reference_model import ApiMeterTypeReferenceModel

        d = dict(src_dict)

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

        def _parse_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identifier = _parse_identifier(d.pop("identifier", UNSET))

        def _parse_plant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plant_id = _parse_plant_id(d.pop("plantId", UNSET))

        def _parse_serial_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        serial_number = _parse_serial_number(d.pop("serialNumber", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_status_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_message = _parse_status_message(d.pop("statusMessage", UNSET))

        def _parse_api_meter_type(data: object) -> ApiMeterTypeReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                api_meter_type_type_1 = ApiMeterTypeReferenceModel.from_dict(data)

                return api_meter_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiMeterTypeReferenceModel | None | Unset, data)

        api_meter_type = _parse_api_meter_type(d.pop("apiMeterType", UNSET))

        def _parse_api_account(data: object) -> ApiAccountReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                api_account_type_1 = ApiAccountReferenceModel.from_dict(data)

                return api_account_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiAccountReferenceModel | None | Unset, data)

        api_account = _parse_api_account(d.pop("apiAccount", UNSET))

        api_meter_output_model = cls(
            resource_uri=resource_uri,
            identifier=identifier,
            plant_id=plant_id,
            serial_number=serial_number,
            external_id=external_id,
            status=status,
            status_message=status_message,
            api_meter_type=api_meter_type,
            api_account=api_account,
        )

        api_meter_output_model.additional_properties = d
        return api_meter_output_model

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
