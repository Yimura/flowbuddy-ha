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
    from ..models.event_type_reference_model import EventTypeReferenceModel
    from ..models.installation_reference_model import InstallationReferenceModel
    from ..models.measurement_reference_model import MeasurementReferenceModel
    from ..models.meter_reference_model import MeterReferenceModel


T = TypeVar("T", bound="EventOutputModel")


@_attrs_define
class EventOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        timestamp (datetime.datetime | None | Unset):
        description (str | Unset):
        created_on (datetime.datetime | None | Unset):
        external_id (str | Unset):
        installation (InstallationReferenceModel | Unset):
        meter (MeterReferenceModel | Unset):
        measurement (MeasurementReferenceModel | Unset):
        event_type (EventTypeReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    timestamp: datetime.datetime | None | Unset = UNSET
    description: str | Unset = UNSET
    created_on: datetime.datetime | None | Unset = UNSET
    external_id: str | Unset = UNSET
    installation: InstallationReferenceModel | Unset = UNSET
    meter: MeterReferenceModel | Unset = UNSET
    measurement: MeasurementReferenceModel | Unset = UNSET
    event_type: EventTypeReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_type_reference_model import EventTypeReferenceModel
        from ..models.installation_reference_model import InstallationReferenceModel
        from ..models.measurement_reference_model import MeasurementReferenceModel
        from ..models.meter_reference_model import MeterReferenceModel

        resource_uri = self.resource_uri

        timestamp: None | str | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        elif isinstance(self.timestamp, datetime.datetime):
            timestamp = self.timestamp.isoformat()
        else:
            timestamp = self.timestamp

        description = self.description

        created_on: None | str | Unset
        if isinstance(self.created_on, Unset):
            created_on = UNSET
        elif isinstance(self.created_on, datetime.datetime):
            created_on = self.created_on.isoformat()
        else:
            created_on = self.created_on

        external_id = self.external_id

        installation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.installation, Unset):
            installation = self.installation.to_dict()

        meter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meter, Unset):
            meter = self.meter.to_dict()

        measurement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.measurement, Unset):
            measurement = self.measurement.to_dict()

        event_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if description is not UNSET:
            field_dict["description"] = description
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if installation is not UNSET:
            field_dict["installation"] = installation
        if meter is not UNSET:
            field_dict["meter"] = meter
        if measurement is not UNSET:
            field_dict["measurement"] = measurement
        if event_type is not UNSET:
            field_dict["eventType"] = event_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_type_reference_model import EventTypeReferenceModel
        from ..models.installation_reference_model import InstallationReferenceModel
        from ..models.measurement_reference_model import MeasurementReferenceModel
        from ..models.meter_reference_model import MeterReferenceModel

        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

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

        description = d.pop("description", UNSET)

        def _parse_created_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_on_type_0 = datetime.datetime.fromisoformat(data)

                return created_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_on = _parse_created_on(d.pop("createdOn", UNSET))

        external_id = d.pop("externalId", UNSET)

        _installation = d.pop("installation", UNSET)
        installation: InstallationReferenceModel | Unset
        if isinstance(_installation, Unset):
            installation = UNSET
        else:
            installation = InstallationReferenceModel.from_dict(_installation)

        _meter = d.pop("meter", UNSET)
        meter: MeterReferenceModel | Unset
        if isinstance(_meter, Unset):
            meter = UNSET
        else:
            meter = MeterReferenceModel.from_dict(_meter)

        _measurement = d.pop("measurement", UNSET)
        measurement: MeasurementReferenceModel | Unset
        if isinstance(_measurement, Unset):
            measurement = UNSET
        else:
            measurement = MeasurementReferenceModel.from_dict(_measurement)

        _event_type = d.pop("eventType", UNSET)
        event_type: EventTypeReferenceModel | Unset
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = EventTypeReferenceModel.from_dict(_event_type)

        event_output_model = cls(
            resource_uri=resource_uri,
            timestamp=timestamp,
            description=description,
            created_on=created_on,
            external_id=external_id,
            installation=installation,
            meter=meter,
            measurement=measurement,
            event_type=event_type,
        )

        event_output_model.additional_properties = d
        return event_output_model

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
