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
    from ..models.api_meter_reference_model import ApiMeterReferenceModel
    from ..models.installation_reference_model import InstallationReferenceModel
    from ..models.measuring_device_reference_model import MeasuringDeviceReferenceModel


T = TypeVar("T", bound="MeterOutputModel")


@_attrs_define
class MeterOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        name (str | Unset): Description of the meter
        serial_number (str | Unset): Serial number of device
        manufacturer (str | Unset):
        type_ (str | Unset): Type of meter (e.g. Solar, Heating, ...)
        meter_type (str | Unset):
        status (str | Unset): Registration status of device
        first_registered_on (datetime.datetime | Unset): First time when meter was linked to an installation
        registered_on (datetime.datetime | Unset): Time when meter was linked to an installation (if meter was
            unregistered/re-registered this will be updated)
        last_communication_attempt_on (datetime.datetime | Unset): Last attempt of network communication with physical
            device
        last_successful_communication_on (datetime.datetime | Unset): Last successful network communication with
            physical device
        polling (str | Unset): Indicates whether the device is processing data (e.g. yes or no)
        last_polling_result (str | Unset): Indicates whether the last data processing was completed without errors (e.g.
            successful)
        last_successful_polling_on (datetime.datetime | Unset): Time when data was last processed for this device
        external_id (str | Unset):
        installation (InstallationReferenceModel | Unset):
        dlms_meter (MeasuringDeviceReferenceModel | Unset):
        api_meter (ApiMeterReferenceModel | Unset):
        created (datetime.datetime | Unset): Time when meter was created in the application
    """

    resource_uri: str | Unset = UNSET
    name: str | Unset = UNSET
    serial_number: str | Unset = UNSET
    manufacturer: str | Unset = UNSET
    type_: str | Unset = UNSET
    meter_type: str | Unset = UNSET
    status: str | Unset = UNSET
    first_registered_on: datetime.datetime | Unset = UNSET
    registered_on: datetime.datetime | Unset = UNSET
    last_communication_attempt_on: datetime.datetime | Unset = UNSET
    last_successful_communication_on: datetime.datetime | Unset = UNSET
    polling: str | Unset = UNSET
    last_polling_result: str | Unset = UNSET
    last_successful_polling_on: datetime.datetime | Unset = UNSET
    external_id: str | Unset = UNSET
    installation: InstallationReferenceModel | Unset = UNSET
    dlms_meter: MeasuringDeviceReferenceModel | Unset = UNSET
    api_meter: ApiMeterReferenceModel | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_meter_reference_model import ApiMeterReferenceModel
        from ..models.installation_reference_model import InstallationReferenceModel
        from ..models.measuring_device_reference_model import MeasuringDeviceReferenceModel

        resource_uri = self.resource_uri

        name = self.name

        serial_number = self.serial_number

        manufacturer = self.manufacturer

        type_ = self.type_

        meter_type = self.meter_type

        status = self.status

        first_registered_on: str | Unset = UNSET
        if not isinstance(self.first_registered_on, Unset):
            first_registered_on = self.first_registered_on.isoformat()

        registered_on: str | Unset = UNSET
        if not isinstance(self.registered_on, Unset):
            registered_on = self.registered_on.isoformat()

        last_communication_attempt_on: str | Unset = UNSET
        if not isinstance(self.last_communication_attempt_on, Unset):
            last_communication_attempt_on = self.last_communication_attempt_on.isoformat()

        last_successful_communication_on: str | Unset = UNSET
        if not isinstance(self.last_successful_communication_on, Unset):
            last_successful_communication_on = self.last_successful_communication_on.isoformat()

        polling = self.polling

        last_polling_result = self.last_polling_result

        last_successful_polling_on: str | Unset = UNSET
        if not isinstance(self.last_successful_polling_on, Unset):
            last_successful_polling_on = self.last_successful_polling_on.isoformat()

        external_id = self.external_id

        installation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.installation, Unset):
            installation = self.installation.to_dict()

        dlms_meter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dlms_meter, Unset):
            dlms_meter = self.dlms_meter.to_dict()

        api_meter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.api_meter, Unset):
            api_meter = self.api_meter.to_dict()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if name is not UNSET:
            field_dict["name"] = name
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if type_ is not UNSET:
            field_dict["type"] = type_
        if meter_type is not UNSET:
            field_dict["meterType"] = meter_type
        if status is not UNSET:
            field_dict["status"] = status
        if first_registered_on is not UNSET:
            field_dict["firstRegisteredOn"] = first_registered_on
        if registered_on is not UNSET:
            field_dict["registeredOn"] = registered_on
        if last_communication_attempt_on is not UNSET:
            field_dict["lastCommunicationAttemptOn"] = last_communication_attempt_on
        if last_successful_communication_on is not UNSET:
            field_dict["lastSuccessfulCommunicationOn"] = last_successful_communication_on
        if polling is not UNSET:
            field_dict["polling"] = polling
        if last_polling_result is not UNSET:
            field_dict["lastPollingResult"] = last_polling_result
        if last_successful_polling_on is not UNSET:
            field_dict["lastSuccessfulPollingOn"] = last_successful_polling_on
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if installation is not UNSET:
            field_dict["installation"] = installation
        if dlms_meter is not UNSET:
            field_dict["dlmsMeter"] = dlms_meter
        if api_meter is not UNSET:
            field_dict["apiMeter"] = api_meter
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_meter_reference_model import ApiMeterReferenceModel
        from ..models.installation_reference_model import InstallationReferenceModel
        from ..models.measuring_device_reference_model import MeasuringDeviceReferenceModel

        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

        name = d.pop("name", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        type_ = d.pop("type", UNSET)

        meter_type = d.pop("meterType", UNSET)

        status = d.pop("status", UNSET)

        _first_registered_on = d.pop("firstRegisteredOn", UNSET)
        first_registered_on: datetime.datetime | Unset
        if isinstance(_first_registered_on, Unset):
            first_registered_on = UNSET
        else:
            first_registered_on = datetime.datetime.fromisoformat(_first_registered_on)

        _registered_on = d.pop("registeredOn", UNSET)
        registered_on: datetime.datetime | Unset
        if isinstance(_registered_on, Unset):
            registered_on = UNSET
        else:
            registered_on = datetime.datetime.fromisoformat(_registered_on)

        _last_communication_attempt_on = d.pop("lastCommunicationAttemptOn", UNSET)
        last_communication_attempt_on: datetime.datetime | Unset
        if isinstance(_last_communication_attempt_on, Unset):
            last_communication_attempt_on = UNSET
        else:
            last_communication_attempt_on = datetime.datetime.fromisoformat(
                _last_communication_attempt_on
            )

        _last_successful_communication_on = d.pop("lastSuccessfulCommunicationOn", UNSET)
        last_successful_communication_on: datetime.datetime | Unset
        if isinstance(_last_successful_communication_on, Unset):
            last_successful_communication_on = UNSET
        else:
            last_successful_communication_on = datetime.datetime.fromisoformat(
                _last_successful_communication_on
            )

        polling = d.pop("polling", UNSET)

        last_polling_result = d.pop("lastPollingResult", UNSET)

        _last_successful_polling_on = d.pop("lastSuccessfulPollingOn", UNSET)
        last_successful_polling_on: datetime.datetime | Unset
        if isinstance(_last_successful_polling_on, Unset):
            last_successful_polling_on = UNSET
        else:
            last_successful_polling_on = datetime.datetime.fromisoformat(
                _last_successful_polling_on
            )

        external_id = d.pop("externalId", UNSET)

        _installation = d.pop("installation", UNSET)
        installation: InstallationReferenceModel | Unset
        if isinstance(_installation, Unset):
            installation = UNSET
        else:
            installation = InstallationReferenceModel.from_dict(_installation)

        _dlms_meter = d.pop("dlmsMeter", UNSET)
        dlms_meter: MeasuringDeviceReferenceModel | Unset
        if isinstance(_dlms_meter, Unset):
            dlms_meter = UNSET
        else:
            dlms_meter = MeasuringDeviceReferenceModel.from_dict(_dlms_meter)

        _api_meter = d.pop("apiMeter", UNSET)
        api_meter: ApiMeterReferenceModel | Unset
        if isinstance(_api_meter, Unset):
            api_meter = UNSET
        else:
            api_meter = ApiMeterReferenceModel.from_dict(_api_meter)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        meter_output_model = cls(
            resource_uri=resource_uri,
            name=name,
            serial_number=serial_number,
            manufacturer=manufacturer,
            type_=type_,
            meter_type=meter_type,
            status=status,
            first_registered_on=first_registered_on,
            registered_on=registered_on,
            last_communication_attempt_on=last_communication_attempt_on,
            last_successful_communication_on=last_successful_communication_on,
            polling=polling,
            last_polling_result=last_polling_result,
            last_successful_polling_on=last_successful_polling_on,
            external_id=external_id,
            installation=installation,
            dlms_meter=dlms_meter,
            api_meter=api_meter,
            created=created,
        )

        meter_output_model.additional_properties = d
        return meter_output_model

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
