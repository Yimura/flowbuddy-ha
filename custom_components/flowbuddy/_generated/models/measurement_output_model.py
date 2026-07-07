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
    from ..models.measurement_type_reference_model import MeasurementTypeReferenceModel
    from ..models.meter_reference_model import MeterReferenceModel


T = TypeVar("T", bound="MeasurementOutputModel")


@_attrs_define
class MeasurementOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        status (str | Unset): Registration status of Measurement
        first_registered_on (datetime.datetime | Unset): First time when measurement was linked to an meter
        polling (bool | Unset): Indicates if data is processed for this measurement (overrule from meter)
        last_polled_value (float | Unset): Last valid meter reading. (correspondig to the latest cumulative value
            registered by the physical device)
        last_polled_time_stamp (datetime.datetime | Unset): Last timestamp that was processed
        last_aggregation_on (datetime.datetime | Unset): Last timestamp that was aggregated
        validating_quality (bool | Unset):
        last_run_measurement_quality_engine_on (datetime.datetime | Unset):
        alarm_status (str | Unset):
        last_polled_realtime_value (float | Unset): Last realtime value that was processed
        last_polled_realtime_time_stamp (datetime.datetime | Unset): Last realtime timestamp that was processed
        external_id (str | Unset):
        meter (MeterReferenceModel | Unset):
        measurement_type (MeasurementTypeReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    status: str | Unset = UNSET
    first_registered_on: datetime.datetime | Unset = UNSET
    polling: bool | Unset = UNSET
    last_polled_value: float | Unset = UNSET
    last_polled_time_stamp: datetime.datetime | Unset = UNSET
    last_aggregation_on: datetime.datetime | Unset = UNSET
    validating_quality: bool | Unset = UNSET
    last_run_measurement_quality_engine_on: datetime.datetime | Unset = UNSET
    alarm_status: str | Unset = UNSET
    last_polled_realtime_value: float | Unset = UNSET
    last_polled_realtime_time_stamp: datetime.datetime | Unset = UNSET
    external_id: str | Unset = UNSET
    meter: MeterReferenceModel | Unset = UNSET
    measurement_type: MeasurementTypeReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.measurement_type_reference_model import MeasurementTypeReferenceModel
        from ..models.meter_reference_model import MeterReferenceModel

        resource_uri = self.resource_uri

        status = self.status

        first_registered_on: str | Unset = UNSET
        if not isinstance(self.first_registered_on, Unset):
            first_registered_on = self.first_registered_on.isoformat()

        polling = self.polling

        last_polled_value = self.last_polled_value

        last_polled_time_stamp: str | Unset = UNSET
        if not isinstance(self.last_polled_time_stamp, Unset):
            last_polled_time_stamp = self.last_polled_time_stamp.isoformat()

        last_aggregation_on: str | Unset = UNSET
        if not isinstance(self.last_aggregation_on, Unset):
            last_aggregation_on = self.last_aggregation_on.isoformat()

        validating_quality = self.validating_quality

        last_run_measurement_quality_engine_on: str | Unset = UNSET
        if not isinstance(self.last_run_measurement_quality_engine_on, Unset):
            last_run_measurement_quality_engine_on = (
                self.last_run_measurement_quality_engine_on.isoformat()
            )

        alarm_status = self.alarm_status

        last_polled_realtime_value = self.last_polled_realtime_value

        last_polled_realtime_time_stamp: str | Unset = UNSET
        if not isinstance(self.last_polled_realtime_time_stamp, Unset):
            last_polled_realtime_time_stamp = self.last_polled_realtime_time_stamp.isoformat()

        external_id = self.external_id

        meter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meter, Unset):
            meter = self.meter.to_dict()

        measurement_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.measurement_type, Unset):
            measurement_type = self.measurement_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if status is not UNSET:
            field_dict["status"] = status
        if first_registered_on is not UNSET:
            field_dict["firstRegisteredOn"] = first_registered_on
        if polling is not UNSET:
            field_dict["polling"] = polling
        if last_polled_value is not UNSET:
            field_dict["lastPolledValue"] = last_polled_value
        if last_polled_time_stamp is not UNSET:
            field_dict["lastPolledTimeStamp"] = last_polled_time_stamp
        if last_aggregation_on is not UNSET:
            field_dict["lastAggregationOn"] = last_aggregation_on
        if validating_quality is not UNSET:
            field_dict["validatingQuality"] = validating_quality
        if last_run_measurement_quality_engine_on is not UNSET:
            field_dict["lastRunMeasurementQualityEngineOn"] = last_run_measurement_quality_engine_on
        if alarm_status is not UNSET:
            field_dict["alarmStatus"] = alarm_status
        if last_polled_realtime_value is not UNSET:
            field_dict["lastPolledRealtimeValue"] = last_polled_realtime_value
        if last_polled_realtime_time_stamp is not UNSET:
            field_dict["lastPolledRealtimeTimeStamp"] = last_polled_realtime_time_stamp
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if meter is not UNSET:
            field_dict["meter"] = meter
        if measurement_type is not UNSET:
            field_dict["measurementType"] = measurement_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurement_type_reference_model import MeasurementTypeReferenceModel
        from ..models.meter_reference_model import MeterReferenceModel

        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

        status = d.pop("status", UNSET)

        _first_registered_on = d.pop("firstRegisteredOn", UNSET)
        first_registered_on: datetime.datetime | Unset
        if isinstance(_first_registered_on, Unset):
            first_registered_on = UNSET
        else:
            first_registered_on = datetime.datetime.fromisoformat(_first_registered_on)

        polling = d.pop("polling", UNSET)

        last_polled_value = d.pop("lastPolledValue", UNSET)

        _last_polled_time_stamp = d.pop("lastPolledTimeStamp", UNSET)
        last_polled_time_stamp: datetime.datetime | Unset
        if isinstance(_last_polled_time_stamp, Unset):
            last_polled_time_stamp = UNSET
        else:
            last_polled_time_stamp = datetime.datetime.fromisoformat(_last_polled_time_stamp)

        _last_aggregation_on = d.pop("lastAggregationOn", UNSET)
        last_aggregation_on: datetime.datetime | Unset
        if isinstance(_last_aggregation_on, Unset):
            last_aggregation_on = UNSET
        else:
            last_aggregation_on = datetime.datetime.fromisoformat(_last_aggregation_on)

        validating_quality = d.pop("validatingQuality", UNSET)

        _last_run_measurement_quality_engine_on = d.pop("lastRunMeasurementQualityEngineOn", UNSET)
        last_run_measurement_quality_engine_on: datetime.datetime | Unset
        if isinstance(_last_run_measurement_quality_engine_on, Unset):
            last_run_measurement_quality_engine_on = UNSET
        else:
            last_run_measurement_quality_engine_on = datetime.datetime.fromisoformat(
                _last_run_measurement_quality_engine_on
            )

        alarm_status = d.pop("alarmStatus", UNSET)

        last_polled_realtime_value = d.pop("lastPolledRealtimeValue", UNSET)

        _last_polled_realtime_time_stamp = d.pop("lastPolledRealtimeTimeStamp", UNSET)
        last_polled_realtime_time_stamp: datetime.datetime | Unset
        if isinstance(_last_polled_realtime_time_stamp, Unset):
            last_polled_realtime_time_stamp = UNSET
        else:
            last_polled_realtime_time_stamp = datetime.datetime.fromisoformat(
                _last_polled_realtime_time_stamp
            )

        external_id = d.pop("externalId", UNSET)

        _meter = d.pop("meter", UNSET)
        meter: MeterReferenceModel | Unset
        if isinstance(_meter, Unset):
            meter = UNSET
        else:
            meter = MeterReferenceModel.from_dict(_meter)

        _measurement_type = d.pop("measurementType", UNSET)
        measurement_type: MeasurementTypeReferenceModel | Unset
        if isinstance(_measurement_type, Unset):
            measurement_type = UNSET
        else:
            measurement_type = MeasurementTypeReferenceModel.from_dict(_measurement_type)

        measurement_output_model = cls(
            resource_uri=resource_uri,
            status=status,
            first_registered_on=first_registered_on,
            polling=polling,
            last_polled_value=last_polled_value,
            last_polled_time_stamp=last_polled_time_stamp,
            last_aggregation_on=last_aggregation_on,
            validating_quality=validating_quality,
            last_run_measurement_quality_engine_on=last_run_measurement_quality_engine_on,
            alarm_status=alarm_status,
            last_polled_realtime_value=last_polled_realtime_value,
            last_polled_realtime_time_stamp=last_polled_realtime_time_stamp,
            external_id=external_id,
            meter=meter,
            measurement_type=measurement_type,
        )

        measurement_output_model.additional_properties = d
        return measurement_output_model

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
