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


T = TypeVar("T", bound="AggregationYearValueOutputModel")


@_attrs_define
class AggregationYearValueOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        period_start (datetime.datetime | None | Unset):
        timestart (datetime.datetime | None | Unset):
        timestop (datetime.datetime | None | Unset):
        value (float | Unset):
        sum_ (float | Unset):
        count (int | Unset):
        max_ (float | Unset):
        measurement (MeasurementReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    period_start: datetime.datetime | None | Unset = UNSET
    timestart: datetime.datetime | None | Unset = UNSET
    timestop: datetime.datetime | None | Unset = UNSET
    value: float | Unset = UNSET
    sum_: float | Unset = UNSET
    count: int | Unset = UNSET
    max_: float | Unset = UNSET
    measurement: MeasurementReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.measurement_reference_model import MeasurementReferenceModel

        resource_uri = self.resource_uri

        period_start: None | str | Unset
        if isinstance(self.period_start, Unset):
            period_start = UNSET
        elif isinstance(self.period_start, datetime.datetime):
            period_start = self.period_start.isoformat()
        else:
            period_start = self.period_start

        timestart: None | str | Unset
        if isinstance(self.timestart, Unset):
            timestart = UNSET
        elif isinstance(self.timestart, datetime.datetime):
            timestart = self.timestart.isoformat()
        else:
            timestart = self.timestart

        timestop: None | str | Unset
        if isinstance(self.timestop, Unset):
            timestop = UNSET
        elif isinstance(self.timestop, datetime.datetime):
            timestop = self.timestop.isoformat()
        else:
            timestop = self.timestop

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

        def _parse_period_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_start_type_0 = datetime.datetime.fromisoformat(data)

                return period_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        period_start = _parse_period_start(d.pop("periodStart", UNSET))

        def _parse_timestart(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timestart_type_0 = datetime.datetime.fromisoformat(data)

                return timestart_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        timestart = _parse_timestart(d.pop("timestart", UNSET))

        def _parse_timestop(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timestop_type_0 = datetime.datetime.fromisoformat(data)

                return timestop_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        timestop = _parse_timestop(d.pop("timestop", UNSET))

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

        aggregation_year_value_output_model = cls(
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

        aggregation_year_value_output_model.additional_properties = d
        return aggregation_year_value_output_model

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
