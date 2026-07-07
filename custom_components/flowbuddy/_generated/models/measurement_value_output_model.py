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
    from ..models.measurement_reference_model import MeasurementReferenceModel


T = TypeVar("T", bound="MeasurementValueOutputModel")


@_attrs_define
class MeasurementValueOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        timestart (datetime.datetime | Unset):
        value (float | Unset):
        created_on (datetime.datetime | Unset):
        measurement (MeasurementReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    timestart: datetime.datetime | Unset = UNSET
    value: float | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    measurement: MeasurementReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.measurement_reference_model import MeasurementReferenceModel

        resource_uri = self.resource_uri

        timestart: str | Unset = UNSET
        if not isinstance(self.timestart, Unset):
            timestart = self.timestart.isoformat()

        value = self.value

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        measurement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.measurement, Unset):
            measurement = self.measurement.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if timestart is not UNSET:
            field_dict["timestart"] = timestart
        if value is not UNSET:
            field_dict["value"] = value
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if measurement is not UNSET:
            field_dict["measurement"] = measurement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurement_reference_model import MeasurementReferenceModel

        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

        _timestart = d.pop("timestart", UNSET)
        timestart: datetime.datetime | Unset
        if isinstance(_timestart, Unset):
            timestart = UNSET
        else:
            timestart = datetime.datetime.fromisoformat(_timestart)

        value = d.pop("value", UNSET)

        _created_on = d.pop("createdOn", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = datetime.datetime.fromisoformat(_created_on)

        _measurement = d.pop("measurement", UNSET)
        measurement: MeasurementReferenceModel | Unset
        if isinstance(_measurement, Unset):
            measurement = UNSET
        else:
            measurement = MeasurementReferenceModel.from_dict(_measurement)

        measurement_value_output_model = cls(
            resource_uri=resource_uri,
            timestart=timestart,
            value=value,
            created_on=created_on,
            measurement=measurement,
        )

        measurement_value_output_model.additional_properties = d
        return measurement_value_output_model

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
