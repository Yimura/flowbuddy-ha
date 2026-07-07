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
    from ..models.control_type_reference_model import ControlTypeReferenceModel
    from ..models.meter_reference_model import MeterReferenceModel


T = TypeVar("T", bound="ControlSignalOutputModel")


@_attrs_define
class ControlSignalOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        time_stamp (datetime.datetime | None | Unset):
        value (None | str | Unset):
        status (None | str | Unset):
        result_message (None | str | Unset):
        external_id (None | str | Unset):
        meter (MeterReferenceModel | None | Unset):
        control_type (ControlTypeReferenceModel | None | Unset):
        created (datetime.datetime | None | Unset):
        last_modified (datetime.datetime | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    time_stamp: datetime.datetime | None | Unset = UNSET
    value: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    result_message: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    meter: MeterReferenceModel | None | Unset = UNSET
    control_type: ControlTypeReferenceModel | None | Unset = UNSET
    created: datetime.datetime | None | Unset = UNSET
    last_modified: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.control_type_reference_model import ControlTypeReferenceModel
        from ..models.meter_reference_model import MeterReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        time_stamp: None | str | Unset
        if isinstance(self.time_stamp, Unset):
            time_stamp = UNSET
        elif isinstance(self.time_stamp, datetime.datetime):
            time_stamp = self.time_stamp.isoformat()
        else:
            time_stamp = self.time_stamp

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        result_message: None | str | Unset
        if isinstance(self.result_message, Unset):
            result_message = UNSET
        else:
            result_message = self.result_message

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        meter: dict[str, Any] | None | Unset
        if isinstance(self.meter, Unset):
            meter = UNSET
        elif isinstance(self.meter, MeterReferenceModel):
            meter = self.meter.to_dict()
        else:
            meter = self.meter

        control_type: dict[str, Any] | None | Unset
        if isinstance(self.control_type, Unset):
            control_type = UNSET
        elif isinstance(self.control_type, ControlTypeReferenceModel):
            control_type = self.control_type.to_dict()
        else:
            control_type = self.control_type

        created: None | str | Unset
        if isinstance(self.created, Unset):
            created = UNSET
        elif isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        last_modified: None | str | Unset
        if isinstance(self.last_modified, Unset):
            last_modified = UNSET
        elif isinstance(self.last_modified, datetime.datetime):
            last_modified = self.last_modified.isoformat()
        else:
            last_modified = self.last_modified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if time_stamp is not UNSET:
            field_dict["timeStamp"] = time_stamp
        if value is not UNSET:
            field_dict["value"] = value
        if status is not UNSET:
            field_dict["status"] = status
        if result_message is not UNSET:
            field_dict["resultMessage"] = result_message
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if meter is not UNSET:
            field_dict["meter"] = meter
        if control_type is not UNSET:
            field_dict["controlType"] = control_type
        if created is not UNSET:
            field_dict["created"] = created
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.control_type_reference_model import ControlTypeReferenceModel
        from ..models.meter_reference_model import MeterReferenceModel

        d = dict(src_dict)

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

        def _parse_time_stamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_stamp_type_0 = datetime.datetime.fromisoformat(data)

                return time_stamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_stamp = _parse_time_stamp(d.pop("timeStamp", UNSET))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_result_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result_message = _parse_result_message(d.pop("resultMessage", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

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

        def _parse_control_type(data: object) -> ControlTypeReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                control_type_type_1 = ControlTypeReferenceModel.from_dict(data)

                return control_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ControlTypeReferenceModel | None | Unset, data)

        control_type = _parse_control_type(d.pop("controlType", UNSET))

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

        def _parse_last_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_modified_type_0 = datetime.datetime.fromisoformat(data)

                return last_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_modified = _parse_last_modified(d.pop("lastModified", UNSET))

        control_signal_output_model = cls(
            resource_uri=resource_uri,
            time_stamp=time_stamp,
            value=value,
            status=status,
            result_message=result_message,
            external_id=external_id,
            meter=meter,
            control_type=control_type,
            created=created,
            last_modified=last_modified,
        )

        control_signal_output_model.additional_properties = d
        return control_signal_output_model

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
