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


T = TypeVar("T", bound="AggregationDayValueOutputModel")


@_attrs_define
class AggregationDayValueOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        period_start (datetime.datetime | Unset):
        timestart (datetime.datetime | Unset):
        timestop (datetime.datetime | Unset):
        value (float | Unset):
        sum_ (float | Unset):
        count (int | Unset):
        max_ (float | Unset):
        measurement (MeasurementReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    period_start: datetime.datetime | Unset = UNSET
    timestart: datetime.datetime | Unset = UNSET
    timestop: datetime.datetime | Unset = UNSET
    value: float | Unset = UNSET
    sum_: float | Unset = UNSET
    count: int | Unset = UNSET
    max_: float | Unset = UNSET
    measurement: MeasurementReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.measurement_reference_model import MeasurementReferenceModel

        resource_uri = self.resource_uri

        period_start: str | Unset = UNSET
        if not isinstance(self.period_start, Unset):
            period_start = self.period_start.isoformat()

        timestart: str | Unset = UNSET
        if not isinstance(self.timestart, Unset):
            timestart = self.timestart.isoformat()

        timestop: str | Unset = UNSET
        if not isinstance(self.timestop, Unset):
            timestop = self.timestop.isoformat()

        value = self.value

        sum_ = self.sum_

        count = self.count

        max_ = self.max_

        measurement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.measurement, Unset):
            measurement = self.measurement.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if period_start is not UNSET:
            field_dict["periodStart"] = period_start
        if timestart is not UNSET:
            field_dict["timestart"] = timestart
        if timestop is not UNSET:
            field_dict["timestop"] = timestop
        if value is not UNSET:
            field_dict["value"] = value
        if sum_ is not UNSET:
            field_dict["sum"] = sum_
        if count is not UNSET:
            field_dict["count"] = count
        if max_ is not UNSET:
            field_dict["max"] = max_
        if measurement is not UNSET:
            field_dict["measurement"] = measurement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurement_reference_model import MeasurementReferenceModel

        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

        _period_start = d.pop("periodStart", UNSET)
        period_start: datetime.datetime | Unset
        if isinstance(_period_start, Unset):
            period_start = UNSET
        else:
            period_start = datetime.datetime.fromisoformat(_period_start)

        _timestart = d.pop("timestart", UNSET)
        timestart: datetime.datetime | Unset
        if isinstance(_timestart, Unset):
            timestart = UNSET
        else:
            timestart = datetime.datetime.fromisoformat(_timestart)

        _timestop = d.pop("timestop", UNSET)
        timestop: datetime.datetime | Unset
        if isinstance(_timestop, Unset):
            timestop = UNSET
        else:
            timestop = datetime.datetime.fromisoformat(_timestop)

        value = d.pop("value", UNSET)

        sum_ = d.pop("sum", UNSET)

        count = d.pop("count", UNSET)

        max_ = d.pop("max", UNSET)

        _measurement = d.pop("measurement", UNSET)
        measurement: MeasurementReferenceModel | Unset
        if isinstance(_measurement, Unset):
            measurement = UNSET
        else:
            measurement = MeasurementReferenceModel.from_dict(_measurement)

        aggregation_day_value_output_model = cls(
            resource_uri=resource_uri,
            period_start=period_start,
            timestart=timestart,
            timestop=timestop,
            value=value,
            sum_=sum_,
            count=count,
            max_=max_,
            measurement=measurement,
        )

        aggregation_day_value_output_model.additional_properties = d
        return aggregation_day_value_output_model

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
