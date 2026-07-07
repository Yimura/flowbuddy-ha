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
        resource_uri (str | Unset):
        identifier (str | Unset): Unique identifier for the device. This is only used for Fluvius connections and equals
            the EAN code of the meter
        plant_id (str | Unset): A technical reference to the API meter
        serial_number (str | Unset): The serialNumber of the device
        external_id (str | Unset):
        status (str | Unset): The status of the ApiMeter
        status_message (str | Unset): Additional info regarding the status
        api_meter_type (ApiMeterTypeReferenceModel | Unset):
        api_account (ApiAccountReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    identifier: str | Unset = UNSET
    plant_id: str | Unset = UNSET
    serial_number: str | Unset = UNSET
    external_id: str | Unset = UNSET
    status: str | Unset = UNSET
    status_message: str | Unset = UNSET
    api_meter_type: ApiMeterTypeReferenceModel | Unset = UNSET
    api_account: ApiAccountReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_account_reference_model import ApiAccountReferenceModel
        from ..models.api_meter_type_reference_model import ApiMeterTypeReferenceModel

        resource_uri = self.resource_uri

        identifier = self.identifier

        plant_id = self.plant_id

        serial_number = self.serial_number

        external_id = self.external_id

        status = self.status

        status_message = self.status_message

        api_meter_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.api_meter_type, Unset):
            api_meter_type = self.api_meter_type.to_dict()

        api_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.api_account, Unset):
            api_account = self.api_account.to_dict()

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
        resource_uri = d.pop("resourceUri", UNSET)

        identifier = d.pop("identifier", UNSET)

        plant_id = d.pop("plantId", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        external_id = d.pop("externalId", UNSET)

        status = d.pop("status", UNSET)

        status_message = d.pop("statusMessage", UNSET)

        _api_meter_type = d.pop("apiMeterType", UNSET)
        api_meter_type: ApiMeterTypeReferenceModel | Unset
        if isinstance(_api_meter_type, Unset):
            api_meter_type = UNSET
        else:
            api_meter_type = ApiMeterTypeReferenceModel.from_dict(_api_meter_type)

        _api_account = d.pop("apiAccount", UNSET)
        api_account: ApiAccountReferenceModel | Unset
        if isinstance(_api_account, Unset):
            api_account = UNSET
        else:
            api_account = ApiAccountReferenceModel.from_dict(_api_account)

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
