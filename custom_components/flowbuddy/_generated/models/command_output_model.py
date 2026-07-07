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
    from ..models.installation_reference_model import InstallationReferenceModel
    from ..models.measurement_reference_model import MeasurementReferenceModel
    from ..models.meter_reference_model import MeterReferenceModel


T = TypeVar("T", bound="CommandOutputModel")


@_attrs_define
class CommandOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        type_ (None | str | Unset): Type of command
        status (None | str | Unset): Status of command
        result (None | str | Unset): Result of command
        entered_on (datetime.datetime | None | Unset): When the command was initiated
        performed_on (datetime.datetime | None | Unset): When the command was executed
        external_id (None | str | Unset):
        installation (InstallationReferenceModel | None | Unset):
        meter (MeterReferenceModel | None | Unset):
        measurement (MeasurementReferenceModel | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    result: None | str | Unset = UNSET
    entered_on: datetime.datetime | None | Unset = UNSET
    performed_on: datetime.datetime | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    installation: InstallationReferenceModel | None | Unset = UNSET
    meter: MeterReferenceModel | None | Unset = UNSET
    measurement: MeasurementReferenceModel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_reference_model import InstallationReferenceModel
        from ..models.measurement_reference_model import MeasurementReferenceModel
        from ..models.meter_reference_model import MeterReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        result: None | str | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        else:
            result = self.result

        entered_on: None | str | Unset
        if isinstance(self.entered_on, Unset):
            entered_on = UNSET
        elif isinstance(self.entered_on, datetime.datetime):
            entered_on = self.entered_on.isoformat()
        else:
            entered_on = self.entered_on

        performed_on: None | str | Unset
        if isinstance(self.performed_on, Unset):
            performed_on = UNSET
        elif isinstance(self.performed_on, datetime.datetime):
            performed_on = self.performed_on.isoformat()
        else:
            performed_on = self.performed_on

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if result is not UNSET:
            field_dict["result"] = result
        if entered_on is not UNSET:
            field_dict["enteredOn"] = entered_on
        if performed_on is not UNSET:
            field_dict["performedOn"] = performed_on
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if installation is not UNSET:
            field_dict["installation"] = installation
        if meter is not UNSET:
            field_dict["meter"] = meter
        if measurement is not UNSET:
            field_dict["measurement"] = measurement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_result(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result = _parse_result(d.pop("result", UNSET))

        def _parse_entered_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                entered_on_type_0 = datetime.datetime.fromisoformat(data)

                return entered_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        entered_on = _parse_entered_on(d.pop("enteredOn", UNSET))

        def _parse_performed_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                performed_on_type_0 = datetime.datetime.fromisoformat(data)

                return performed_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        performed_on = _parse_performed_on(d.pop("performedOn", UNSET))

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

        command_output_model = cls(
            resource_uri=resource_uri,
            type_=type_,
            status=status,
            result=result,
            entered_on=entered_on,
            performed_on=performed_on,
            external_id=external_id,
            installation=installation,
            meter=meter,
            measurement=measurement,
        )

        command_output_model.additional_properties = d
        return command_output_model

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
