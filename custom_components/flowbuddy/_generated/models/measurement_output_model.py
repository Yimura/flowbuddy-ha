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
        resource_uri (None | str | Unset):
        status (None | str | Unset): Registration status of Measurement
        first_registered_on (datetime.datetime | None | Unset): First time when measurement was linked to an meter
        polling (bool | None | Unset): Indicates if data is processed for this measurement (overrule from meter)
        last_polled_value (float | None | Unset): Last valid meter reading. (correspondig to the latest cumulative value
            registered by the physical device)
        last_polled_time_stamp (datetime.datetime | None | Unset): Last timestamp that was processed
        last_aggregation_on (datetime.datetime | None | Unset): Last timestamp that was aggregated
        validating_quality (bool | None | Unset):
        last_run_measurement_quality_engine_on (datetime.datetime | None | Unset):
        alarm_status (None | str | Unset):
        last_polled_realtime_value (float | None | Unset): Last realtime value that was processed
        last_polled_realtime_time_stamp (datetime.datetime | None | Unset): Last realtime timestamp that was processed
        external_id (None | str | Unset):
        meter (MeterReferenceModel | None | Unset):
        measurement_type (MeasurementTypeReferenceModel | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    first_registered_on: datetime.datetime | None | Unset = UNSET
    polling: bool | None | Unset = UNSET
    last_polled_value: float | None | Unset = UNSET
    last_polled_time_stamp: datetime.datetime | None | Unset = UNSET
    last_aggregation_on: datetime.datetime | None | Unset = UNSET
    validating_quality: bool | None | Unset = UNSET
    last_run_measurement_quality_engine_on: datetime.datetime | None | Unset = UNSET
    alarm_status: None | str | Unset = UNSET
    last_polled_realtime_value: float | None | Unset = UNSET
    last_polled_realtime_time_stamp: datetime.datetime | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    meter: MeterReferenceModel | None | Unset = UNSET
    measurement_type: MeasurementTypeReferenceModel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.measurement_type_reference_model import MeasurementTypeReferenceModel
        from ..models.meter_reference_model import MeterReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        first_registered_on: None | str | Unset
        if isinstance(self.first_registered_on, Unset):
            first_registered_on = UNSET
        elif isinstance(self.first_registered_on, datetime.datetime):
            first_registered_on = self.first_registered_on.isoformat()
        else:
            first_registered_on = self.first_registered_on

        polling: bool | None | Unset
        if isinstance(self.polling, Unset):
            polling = UNSET
        else:
            polling = self.polling

        last_polled_value: float | None | Unset
        if isinstance(self.last_polled_value, Unset):
            last_polled_value = UNSET
        else:
            last_polled_value = self.last_polled_value

        last_polled_time_stamp: None | str | Unset
        if isinstance(self.last_polled_time_stamp, Unset):
            last_polled_time_stamp = UNSET
        elif isinstance(self.last_polled_time_stamp, datetime.datetime):
            last_polled_time_stamp = self.last_polled_time_stamp.isoformat()
        else:
            last_polled_time_stamp = self.last_polled_time_stamp

        last_aggregation_on: None | str | Unset
        if isinstance(self.last_aggregation_on, Unset):
            last_aggregation_on = UNSET
        elif isinstance(self.last_aggregation_on, datetime.datetime):
            last_aggregation_on = self.last_aggregation_on.isoformat()
        else:
            last_aggregation_on = self.last_aggregation_on

        validating_quality: bool | None | Unset
        if isinstance(self.validating_quality, Unset):
            validating_quality = UNSET
        else:
            validating_quality = self.validating_quality

        last_run_measurement_quality_engine_on: None | str | Unset
        if isinstance(self.last_run_measurement_quality_engine_on, Unset):
            last_run_measurement_quality_engine_on = UNSET
        elif isinstance(self.last_run_measurement_quality_engine_on, datetime.datetime):
            last_run_measurement_quality_engine_on = (
                self.last_run_measurement_quality_engine_on.isoformat()
            )
        else:
            last_run_measurement_quality_engine_on = self.last_run_measurement_quality_engine_on

        alarm_status: None | str | Unset
        if isinstance(self.alarm_status, Unset):
            alarm_status = UNSET
        else:
            alarm_status = self.alarm_status

        last_polled_realtime_value: float | None | Unset
        if isinstance(self.last_polled_realtime_value, Unset):
            last_polled_realtime_value = UNSET
        else:
            last_polled_realtime_value = self.last_polled_realtime_value

        last_polled_realtime_time_stamp: None | str | Unset
        if isinstance(self.last_polled_realtime_time_stamp, Unset):
            last_polled_realtime_time_stamp = UNSET
        elif isinstance(self.last_polled_realtime_time_stamp, datetime.datetime):
            last_polled_realtime_time_stamp = self.last_polled_realtime_time_stamp.isoformat()
        else:
            last_polled_realtime_time_stamp = self.last_polled_realtime_time_stamp

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

        measurement_type: dict[str, Any] | None | Unset
        if isinstance(self.measurement_type, Unset):
            measurement_type = UNSET
        elif isinstance(self.measurement_type, MeasurementTypeReferenceModel):
            measurement_type = self.measurement_type.to_dict()
        else:
            measurement_type = self.measurement_type

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

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_first_registered_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_registered_on_type_0 = datetime.datetime.fromisoformat(data)

                return first_registered_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_registered_on = _parse_first_registered_on(d.pop("firstRegisteredOn", UNSET))

        def _parse_polling(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        polling = _parse_polling(d.pop("polling", UNSET))

        def _parse_last_polled_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        last_polled_value = _parse_last_polled_value(d.pop("lastPolledValue", UNSET))

        def _parse_last_polled_time_stamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_polled_time_stamp_type_0 = datetime.datetime.fromisoformat(data)

                return last_polled_time_stamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_polled_time_stamp = _parse_last_polled_time_stamp(d.pop("lastPolledTimeStamp", UNSET))

        def _parse_last_aggregation_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_aggregation_on_type_0 = datetime.datetime.fromisoformat(data)

                return last_aggregation_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_aggregation_on = _parse_last_aggregation_on(d.pop("lastAggregationOn", UNSET))

        def _parse_validating_quality(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        validating_quality = _parse_validating_quality(d.pop("validatingQuality", UNSET))

        def _parse_last_run_measurement_quality_engine_on(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_measurement_quality_engine_on_type_0 = datetime.datetime.fromisoformat(
                    data
                )

                return last_run_measurement_quality_engine_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_run_measurement_quality_engine_on = _parse_last_run_measurement_quality_engine_on(
            d.pop("lastRunMeasurementQualityEngineOn", UNSET)
        )

        def _parse_alarm_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alarm_status = _parse_alarm_status(d.pop("alarmStatus", UNSET))

        def _parse_last_polled_realtime_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        last_polled_realtime_value = _parse_last_polled_realtime_value(
            d.pop("lastPolledRealtimeValue", UNSET)
        )

        def _parse_last_polled_realtime_time_stamp(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_polled_realtime_time_stamp_type_0 = datetime.datetime.fromisoformat(data)

                return last_polled_realtime_time_stamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_polled_realtime_time_stamp = _parse_last_polled_realtime_time_stamp(
            d.pop("lastPolledRealtimeTimeStamp", UNSET)
        )

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

        def _parse_measurement_type(data: object) -> MeasurementTypeReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                measurement_type_type_1 = MeasurementTypeReferenceModel.from_dict(data)

                return measurement_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MeasurementTypeReferenceModel | None | Unset, data)

        measurement_type = _parse_measurement_type(d.pop("measurementType", UNSET))

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
