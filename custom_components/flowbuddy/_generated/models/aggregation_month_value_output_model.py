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


T = TypeVar("T", bound="AggregationMonthValueOutputModel")


@_attrs_define
class AggregationMonthValueOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        period_start (datetime.datetime | None | Unset):
        timestart (datetime.datetime | None | Unset):
        timestop (datetime.datetime | None | Unset):
        value (float | None | Unset):
        sum_ (float | None | Unset):
        count (int | None | Unset):
        max_ (float | None | Unset):
        measurement (MeasurementReferenceModel | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    period_start: datetime.datetime | None | Unset = UNSET
    timestart: datetime.datetime | None | Unset = UNSET
    timestop: datetime.datetime | None | Unset = UNSET
    value: float | None | Unset = UNSET
    sum_: float | None | Unset = UNSET
    count: int | None | Unset = UNSET
    max_: float | None | Unset = UNSET
    measurement: MeasurementReferenceModel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.measurement_reference_model import MeasurementReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
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

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        sum_: float | None | Unset
        if isinstance(self.sum_, Unset):
            sum_ = UNSET
        else:
            sum_ = self.sum_

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        max_: float | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        measurement: dict[str, Any] | None | Unset
        if isinstance(self.measurement, Unset):
            measurement = UNSET
        elif isinstance(self.measurement, MeasurementReferenceModel):
            measurement = self.measurement.to_dict()
        else:
            measurement = self.measurement

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

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

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

        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_sum_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sum_ = _parse_sum_(d.pop("sum", UNSET))

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        def _parse_max_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

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

        aggregation_month_value_output_model = cls(
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

        aggregation_month_value_output_model.additional_properties = d
        return aggregation_month_value_output_model

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
