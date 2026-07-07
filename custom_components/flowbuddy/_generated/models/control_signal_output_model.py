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
        resource_uri (str | Unset):
        time_stamp (datetime.datetime | Unset):
        value (str | Unset):
        status (str | Unset):
        result_message (str | Unset):
        external_id (str | Unset):
        meter (MeterReferenceModel | Unset):
        control_type (ControlTypeReferenceModel | Unset):
        created (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
    """

    resource_uri: str | Unset = UNSET
    time_stamp: datetime.datetime | Unset = UNSET
    value: str | Unset = UNSET
    status: str | Unset = UNSET
    result_message: str | Unset = UNSET
    external_id: str | Unset = UNSET
    meter: MeterReferenceModel | Unset = UNSET
    control_type: ControlTypeReferenceModel | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    last_modified: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.control_type_reference_model import ControlTypeReferenceModel
        from ..models.meter_reference_model import MeterReferenceModel

        resource_uri = self.resource_uri

        time_stamp: str | Unset = UNSET
        if not isinstance(self.time_stamp, Unset):
            time_stamp = self.time_stamp.isoformat()

        value = self.value

        status = self.status

        result_message = self.result_message

        external_id = self.external_id

        meter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meter, Unset):
            meter = self.meter.to_dict()

        control_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.control_type, Unset):
            control_type = self.control_type.to_dict()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        last_modified: str | Unset = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

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
        resource_uri = d.pop("resourceUri", UNSET)

        _time_stamp = d.pop("timeStamp", UNSET)
        time_stamp: datetime.datetime | Unset
        if isinstance(_time_stamp, Unset):
            time_stamp = UNSET
        else:
            time_stamp = datetime.datetime.fromisoformat(_time_stamp)

        value = d.pop("value", UNSET)

        status = d.pop("status", UNSET)

        result_message = d.pop("resultMessage", UNSET)

        external_id = d.pop("externalId", UNSET)

        _meter = d.pop("meter", UNSET)
        meter: MeterReferenceModel | Unset
        if isinstance(_meter, Unset):
            meter = UNSET
        else:
            meter = MeterReferenceModel.from_dict(_meter)

        _control_type = d.pop("controlType", UNSET)
        control_type: ControlTypeReferenceModel | Unset
        if isinstance(_control_type, Unset):
            control_type = UNSET
        else:
            control_type = ControlTypeReferenceModel.from_dict(_control_type)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: datetime.datetime | Unset
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = datetime.datetime.fromisoformat(_last_modified)

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
