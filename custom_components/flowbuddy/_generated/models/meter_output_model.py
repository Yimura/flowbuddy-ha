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
        resource_uri (None | str | Unset):
        name (None | str | Unset): Description of the meter
        serial_number (None | str | Unset): Serial number of device
        manufacturer (None | str | Unset):
        type_ (None | str | Unset): Type of meter (e.g. Solar, Heating, ...)
        meter_type (None | str | Unset):
        status (None | str | Unset): Registration status of device
        first_registered_on (datetime.datetime | None | Unset): First time when meter was linked to an installation
        registered_on (datetime.datetime | None | Unset): Time when meter was linked to an installation (if meter was
            unregistered/re-registered this will be updated)
        last_communication_attempt_on (datetime.datetime | None | Unset): Last attempt of network communication with
            physical device
        last_successful_communication_on (datetime.datetime | None | Unset): Last successful network communication with
            physical device
        polling (None | str | Unset): Indicates whether the device is processing data (e.g. yes or no)
        last_polling_result (None | str | Unset): Indicates whether the last data processing was completed without
            errors (e.g. successful)
        last_successful_polling_on (datetime.datetime | None | Unset): Time when data was last processed for this device
        external_id (None | str | Unset):
        installation (InstallationReferenceModel | None | Unset):
        dlms_meter (MeasuringDeviceReferenceModel | None | Unset):
        api_meter (ApiMeterReferenceModel | None | Unset):
        created (datetime.datetime | None | Unset): Time when meter was created in the application
    """

    resource_uri: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    serial_number: None | str | Unset = UNSET
    manufacturer: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    meter_type: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    first_registered_on: datetime.datetime | None | Unset = UNSET
    registered_on: datetime.datetime | None | Unset = UNSET
    last_communication_attempt_on: datetime.datetime | None | Unset = UNSET
    last_successful_communication_on: datetime.datetime | None | Unset = UNSET
    polling: None | str | Unset = UNSET
    last_polling_result: None | str | Unset = UNSET
    last_successful_polling_on: datetime.datetime | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    installation: InstallationReferenceModel | None | Unset = UNSET
    dlms_meter: MeasuringDeviceReferenceModel | None | Unset = UNSET
    api_meter: ApiMeterReferenceModel | None | Unset = UNSET
    created: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_meter_reference_model import ApiMeterReferenceModel
        from ..models.installation_reference_model import InstallationReferenceModel
        from ..models.measuring_device_reference_model import MeasuringDeviceReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        serial_number: None | str | Unset
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        manufacturer: None | str | Unset
        if isinstance(self.manufacturer, Unset):
            manufacturer = UNSET
        else:
            manufacturer = self.manufacturer

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        meter_type: None | str | Unset
        if isinstance(self.meter_type, Unset):
            meter_type = UNSET
        else:
            meter_type = self.meter_type

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        first_registered_on: None | str | Unset
        if isinstance(self.first_registered_on, Unset):
            first_registered_on = UNSET
        elif isinstance(self.first_registered_on, datetime.datetime):
            first_registered_on = self.first_registered_on.isoformat()
        else:
            first_registered_on = self.first_registered_on

        registered_on: None | str | Unset
        if isinstance(self.registered_on, Unset):
            registered_on = UNSET
        elif isinstance(self.registered_on, datetime.datetime):
            registered_on = self.registered_on.isoformat()
        else:
            registered_on = self.registered_on

        last_communication_attempt_on: None | str | Unset
        if isinstance(self.last_communication_attempt_on, Unset):
            last_communication_attempt_on = UNSET
        elif isinstance(self.last_communication_attempt_on, datetime.datetime):
            last_communication_attempt_on = self.last_communication_attempt_on.isoformat()
        else:
            last_communication_attempt_on = self.last_communication_attempt_on

        last_successful_communication_on: None | str | Unset
        if isinstance(self.last_successful_communication_on, Unset):
            last_successful_communication_on = UNSET
        elif isinstance(self.last_successful_communication_on, datetime.datetime):
            last_successful_communication_on = self.last_successful_communication_on.isoformat()
        else:
            last_successful_communication_on = self.last_successful_communication_on

        polling: None | str | Unset
        if isinstance(self.polling, Unset):
            polling = UNSET
        else:
            polling = self.polling

        last_polling_result: None | str | Unset
        if isinstance(self.last_polling_result, Unset):
            last_polling_result = UNSET
        else:
            last_polling_result = self.last_polling_result

        last_successful_polling_on: None | str | Unset
        if isinstance(self.last_successful_polling_on, Unset):
            last_successful_polling_on = UNSET
        elif isinstance(self.last_successful_polling_on, datetime.datetime):
            last_successful_polling_on = self.last_successful_polling_on.isoformat()
        else:
            last_successful_polling_on = self.last_successful_polling_on

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        installation: dict[str, Any] | None | Unset
        if isinstance(self.installation, Unset):
            installation = UNSET
        elif isinstance(self.installation, InstallationReferenceModel):
            installation = self.installation.to_dict()
        else:
            installation = self.installation

        dlms_meter: dict[str, Any] | None | Unset
        if isinstance(self.dlms_meter, Unset):
            dlms_meter = UNSET
        elif isinstance(self.dlms_meter, MeasuringDeviceReferenceModel):
            dlms_meter = self.dlms_meter.to_dict()
        else:
            dlms_meter = self.dlms_meter

        api_meter: dict[str, Any] | None | Unset
        if isinstance(self.api_meter, Unset):
            api_meter = UNSET
        elif isinstance(self.api_meter, ApiMeterReferenceModel):
            api_meter = self.api_meter.to_dict()
        else:
            api_meter = self.api_meter

        created: None | str | Unset
        if isinstance(self.created, Unset):
            created = UNSET
        elif isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

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

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_serial_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        serial_number = _parse_serial_number(d.pop("serialNumber", UNSET))

        def _parse_manufacturer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        manufacturer = _parse_manufacturer(d.pop("manufacturer", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_meter_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meter_type = _parse_meter_type(d.pop("meterType", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_first_registered_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_registered_on_type_0 = datetime.datetime.fromisoformat(data)

                return first_registered_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_registered_on = _parse_first_registered_on(d.pop("firstRegisteredOn", UNSET))

        def _parse_registered_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registered_on_type_0 = datetime.datetime.fromisoformat(data)

                return registered_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        registered_on = _parse_registered_on(d.pop("registeredOn", UNSET))

        def _parse_last_communication_attempt_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_communication_attempt_on_type_0 = datetime.datetime.fromisoformat(data)

                return last_communication_attempt_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_communication_attempt_on = _parse_last_communication_attempt_on(
            d.pop("lastCommunicationAttemptOn", UNSET)
        )

        def _parse_last_successful_communication_on(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_successful_communication_on_type_0 = datetime.datetime.fromisoformat(data)

                return last_successful_communication_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_successful_communication_on = _parse_last_successful_communication_on(
            d.pop("lastSuccessfulCommunicationOn", UNSET)
        )

        def _parse_polling(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        polling = _parse_polling(d.pop("polling", UNSET))

        def _parse_last_polling_result(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_polling_result = _parse_last_polling_result(d.pop("lastPollingResult", UNSET))

        def _parse_last_successful_polling_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_successful_polling_on_type_0 = datetime.datetime.fromisoformat(data)

                return last_successful_polling_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_successful_polling_on = _parse_last_successful_polling_on(
            d.pop("lastSuccessfulPollingOn", UNSET)
        )

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_installation(data: object) -> InstallationReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                installation_type_1 = InstallationReferenceModel.from_dict(data)

                return installation_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InstallationReferenceModel | None | Unset, data)

        installation = _parse_installation(d.pop("installation", UNSET))

        def _parse_dlms_meter(data: object) -> MeasuringDeviceReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dlms_meter_type_1 = MeasuringDeviceReferenceModel.from_dict(data)

                return dlms_meter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MeasuringDeviceReferenceModel | None | Unset, data)

        dlms_meter = _parse_dlms_meter(d.pop("dlmsMeter", UNSET))

        def _parse_api_meter(data: object) -> ApiMeterReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                api_meter_type_1 = ApiMeterReferenceModel.from_dict(data)

                return api_meter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiMeterReferenceModel | None | Unset, data)

        api_meter = _parse_api_meter(d.pop("apiMeter", UNSET))

        def _parse_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = datetime.datetime.fromisoformat(data)

                return created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created = _parse_created(d.pop("created", UNSET))

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
