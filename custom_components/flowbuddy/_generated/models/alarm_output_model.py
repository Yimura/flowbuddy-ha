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


T = TypeVar("T", bound="AlarmOutputModel")


@_attrs_define
class AlarmOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        timestamp (datetime.datetime | Unset): Time when alarm was detected
        description (str | Unset): Description of alarm
        resolution (str | Unset): Predefined list of solutions that can be linked to an alarm when solved
        cause (str | Unset): Predefined list of causes that can be linked to an alarm
        action (str | Unset): Predefined list of action types that can be linked to an alarm
        priority (str | Unset): Predefined list of priorities to rank the importance of an alarm
        status (str | Unset): Status of alarm (e.g. open or closed)
        closed_by (str | Unset): Indicates which user closed ticket
        closed_on (datetime.datetime | Unset): When ticket was closed
        external_id (str | Unset):
        installation (InstallationReferenceModel | Unset):
        meter (MeterReferenceModel | Unset):
        measurement (MeasurementReferenceModel | Unset):
        event_type (EventTypeReferenceModel | Unset):
        comment (str | Unset): List of comments that were added to alarm
        created (datetime.datetime | Unset): Time when alarm was created in application
    """

    resource_uri: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    resolution: str | Unset = UNSET
    cause: str | Unset = UNSET
    action: str | Unset = UNSET
    priority: str | Unset = UNSET
    status: str | Unset = UNSET
    closed_by: str | Unset = UNSET
    closed_on: datetime.datetime | Unset = UNSET
    external_id: str | Unset = UNSET
    installation: InstallationReferenceModel | Unset = UNSET
    meter: MeterReferenceModel | Unset = UNSET
    measurement: MeasurementReferenceModel | Unset = UNSET
    event_type: EventTypeReferenceModel | Unset = UNSET
    comment: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_type_reference_model import EventTypeReferenceModel
        from ..models.installation_reference_model import InstallationReferenceModel
        from ..models.measurement_reference_model import MeasurementReferenceModel
        from ..models.meter_reference_model import MeterReferenceModel

        resource_uri = self.resource_uri

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        description = self.description

        resolution = self.resolution

        cause = self.cause

        action = self.action

        priority = self.priority

        status = self.status

        closed_by = self.closed_by

        closed_on: str | Unset = UNSET
        if not isinstance(self.closed_on, Unset):
            closed_on = self.closed_on.isoformat()

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

        comment = self.comment

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if description is not UNSET:
            field_dict["description"] = description
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if cause is not UNSET:
            field_dict["cause"] = cause
        if action is not UNSET:
            field_dict["action"] = action
        if priority is not UNSET:
            field_dict["priority"] = priority
        if status is not UNSET:
            field_dict["status"] = status
        if closed_by is not UNSET:
            field_dict["closedBy"] = closed_by
        if closed_on is not UNSET:
            field_dict["closedOn"] = closed_on
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
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_type_reference_model import EventTypeReferenceModel
        from ..models.installation_reference_model import InstallationReferenceModel
        from ..models.measurement_reference_model import MeasurementReferenceModel
        from ..models.meter_reference_model import MeterReferenceModel

        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        description = d.pop("description", UNSET)

        resolution = d.pop("resolution", UNSET)

        cause = d.pop("cause", UNSET)

        action = d.pop("action", UNSET)

        priority = d.pop("priority", UNSET)

        status = d.pop("status", UNSET)

        closed_by = d.pop("closedBy", UNSET)

        _closed_on = d.pop("closedOn", UNSET)
        closed_on: datetime.datetime | Unset
        if isinstance(_closed_on, Unset):
            closed_on = UNSET
        else:
            closed_on = datetime.datetime.fromisoformat(_closed_on)

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

        comment = d.pop("comment", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        alarm_output_model = cls(
            resource_uri=resource_uri,
            timestamp=timestamp,
            description=description,
            resolution=resolution,
            cause=cause,
            action=action,
            priority=priority,
            status=status,
            closed_by=closed_by,
            closed_on=closed_on,
            external_id=external_id,
            installation=installation,
            meter=meter,
            measurement=measurement,
            event_type=event_type,
            comment=comment,
            created=created,
        )

        alarm_output_model.additional_properties = d
        return alarm_output_model

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
