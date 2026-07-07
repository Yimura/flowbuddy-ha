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
        resource_uri (None | str | Unset):
        timestamp (datetime.datetime | None | Unset): Time when alarm was detected
        description (None | str | Unset): Description of alarm
        resolution (None | str | Unset): Predefined list of solutions that can be linked to an alarm when solved
        cause (None | str | Unset): Predefined list of causes that can be linked to an alarm
        action (None | str | Unset): Predefined list of action types that can be linked to an alarm
        priority (None | str | Unset): Predefined list of priorities to rank the importance of an alarm
        status (None | str | Unset): Status of alarm (e.g. open or closed)
        closed_by (None | str | Unset): Indicates which user closed ticket
        closed_on (datetime.datetime | None | Unset): When ticket was closed
        external_id (None | str | Unset):
        installation (InstallationReferenceModel | None | Unset):
        meter (MeterReferenceModel | None | Unset):
        measurement (MeasurementReferenceModel | None | Unset):
        event_type (EventTypeReferenceModel | None | Unset):
        comment (None | str | Unset): List of comments that were added to alarm
        created (datetime.datetime | None | Unset): Time when alarm was created in application
    """

    resource_uri: None | str | Unset = UNSET
    timestamp: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    resolution: None | str | Unset = UNSET
    cause: None | str | Unset = UNSET
    action: None | str | Unset = UNSET
    priority: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    closed_by: None | str | Unset = UNSET
    closed_on: datetime.datetime | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    installation: InstallationReferenceModel | None | Unset = UNSET
    meter: MeterReferenceModel | None | Unset = UNSET
    measurement: MeasurementReferenceModel | None | Unset = UNSET
    event_type: EventTypeReferenceModel | None | Unset = UNSET
    comment: None | str | Unset = UNSET
    created: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_type_reference_model import EventTypeReferenceModel
        from ..models.installation_reference_model import InstallationReferenceModel
        from ..models.measurement_reference_model import MeasurementReferenceModel
        from ..models.meter_reference_model import MeterReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        timestamp: None | str | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        elif isinstance(self.timestamp, datetime.datetime):
            timestamp = self.timestamp.isoformat()
        else:
            timestamp = self.timestamp

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        resolution: None | str | Unset
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        else:
            resolution = self.resolution

        cause: None | str | Unset
        if isinstance(self.cause, Unset):
            cause = UNSET
        else:
            cause = self.cause

        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        else:
            action = self.action

        priority: None | str | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        closed_by: None | str | Unset
        if isinstance(self.closed_by, Unset):
            closed_by = UNSET
        else:
            closed_by = self.closed_by

        closed_on: None | str | Unset
        if isinstance(self.closed_on, Unset):
            closed_on = UNSET
        elif isinstance(self.closed_on, datetime.datetime):
            closed_on = self.closed_on.isoformat()
        else:
            closed_on = self.closed_on

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

        meter: dict[str, Any] | None | Unset
        if isinstance(self.meter, Unset):
            meter = UNSET
        elif isinstance(self.meter, MeterReferenceModel):
            meter = self.meter.to_dict()
        else:
            meter = self.meter

        measurement: dict[str, Any] | None | Unset
        if isinstance(self.measurement, Unset):
            measurement = UNSET
        elif isinstance(self.measurement, MeasurementReferenceModel):
            measurement = self.measurement.to_dict()
        else:
            measurement = self.measurement

        event_type: dict[str, Any] | None | Unset
        if isinstance(self.event_type, Unset):
            event_type = UNSET
        elif isinstance(self.event_type, EventTypeReferenceModel):
            event_type = self.event_type.to_dict()
        else:
            event_type = self.event_type

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

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

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_resolution(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        def _parse_cause(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cause = _parse_cause(d.pop("cause", UNSET))

        def _parse_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action = _parse_action(d.pop("action", UNSET))

        def _parse_priority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_closed_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        closed_by = _parse_closed_by(d.pop("closedBy", UNSET))

        def _parse_closed_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_on_type_0 = datetime.datetime.fromisoformat(data)

                return closed_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closed_on = _parse_closed_on(d.pop("closedOn", UNSET))

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

        def _parse_meter(data: object) -> MeterReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meter_type_1 = MeterReferenceModel.from_dict(data)

                return meter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MeterReferenceModel | None | Unset, data)

        meter = _parse_meter(d.pop("meter", UNSET))

        def _parse_measurement(data: object) -> MeasurementReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                measurement_type_1 = MeasurementReferenceModel.from_dict(data)

                return measurement_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MeasurementReferenceModel | None | Unset, data)

        measurement = _parse_measurement(d.pop("measurement", UNSET))

        def _parse_event_type(data: object) -> EventTypeReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                event_type_type_1 = EventTypeReferenceModel.from_dict(data)

                return event_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventTypeReferenceModel | None | Unset, data)

        event_type = _parse_event_type(d.pop("eventType", UNSET))

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

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
