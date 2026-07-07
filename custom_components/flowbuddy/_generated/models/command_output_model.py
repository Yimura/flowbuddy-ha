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
        resource_uri (str | Unset):
        type_ (str | Unset): Type of command
        status (str | Unset): Status of command
        result (str | Unset): Result of command
        entered_on (datetime.datetime | None | Unset): When the command was initiated
        performed_on (datetime.datetime | None | Unset): When the command was executed
        external_id (str | Unset):
        installation (InstallationReferenceModel | Unset):
        meter (MeterReferenceModel | Unset):
        measurement (MeasurementReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    type_: str | Unset = UNSET
    status: str | Unset = UNSET
    result: str | Unset = UNSET
    entered_on: datetime.datetime | None | Unset = UNSET
    performed_on: datetime.datetime | None | Unset = UNSET
    external_id: str | Unset = UNSET
    installation: InstallationReferenceModel | Unset = UNSET
    meter: MeterReferenceModel | Unset = UNSET
    measurement: MeasurementReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_reference_model import InstallationReferenceModel
        from ..models.measurement_reference_model import MeasurementReferenceModel
        from ..models.meter_reference_model import MeterReferenceModel

        resource_uri = self.resource_uri

        type_ = self.type_

        status = self.status

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

        external_id = self.external_id

        installation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.installation, Unset):
            installation = self.installation.to_dict()

        meter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meter, Unset):
            meter = self.meter.to_dict()

        measurement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.measurement, Unset):
            measurement = self.measurement.to_dict()

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
        resource_uri = d.pop("resourceUri", UNSET)

        type_ = d.pop("type", UNSET)

        status = d.pop("status", UNSET)

        result = d.pop("result", UNSET)

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

        external_id = d.pop("externalId", UNSET)

        _installation = d.pop("installation", UNSET)
        installation: InstallationReferenceModel | Unset
        if isinstance(_installation, Unset):
            installation = UNSET
        else:
            installation = InstallationReferenceModel.from_dict(_installation)

        _meter = d.pop("meter", UNSET)
        meter: MeterReferenceModel | Unset
        if isinstance(_meter, Unset):
            meter = UNSET
        else:
            meter = MeterReferenceModel.from_dict(_meter)

        _measurement = d.pop("measurement", UNSET)
        measurement: MeasurementReferenceModel | Unset
        if isinstance(_measurement, Unset):
            measurement = UNSET
        else:
            measurement = MeasurementReferenceModel.from_dict(_measurement)

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
