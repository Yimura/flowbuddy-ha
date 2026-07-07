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
    from ..models.communicator_reference_model import CommunicatorReferenceModel


T = TypeVar("T", bound="PvProductionTestOutputModel")


@_attrs_define
class PvProductionTestOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        entered_on (datetime.datetime | None | Unset):
        status (None | str | Unset):
        result_message (None | str | Unset):
        test_start_on (datetime.datetime | None | Unset): Time of first connection with the `communicator` and start of
            test
        test_end_on (datetime.datetime | None | Unset):
        breaker_initial_status (None | str | Unset):
        start_export_value (float | None | Unset): Cumulative export value in Wh as reported on the display of
            `communicator`
        start_import_value (float | None | Unset): Cumulative import value in Wh as reported on the display of
            `communicator`. This value should be close to 0 and lower than the export value. If not, this might indicate
            incorrect wiring.
        next_export_value (float | None | Unset): Cumulative export value that was read from the `communicator` after
            several minutes. The difference between the start and next value is used to decide if a valid production was
            measured.
        next_import_value (float | None | Unset):
        average_voltage (float | None | Unset): Average voltage of the last 10 minutes at the moment of the
            productiontest. If this value is close to 253V, this might lead to over voltage which might to a shutdown of the
            inverter.
        instantaneous_active_power_import (float | None | Unset): imported power measured by the `communicator` at the
            moment of productiontest. If this value is greater as 0, the `communicator` might be wired incorrectly.
        instantaneous_active_power_export (float | None | Unset): exported power measured by the communicator at the
            moment of productiontest. If this value is greater as 0, the installation is working as expected.
        instantaneous_current (float | None | Unset):
        external_id (None | str | Unset):
        communicator (CommunicatorReferenceModel | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    entered_on: datetime.datetime | None | Unset = UNSET
    status: None | str | Unset = UNSET
    result_message: None | str | Unset = UNSET
    test_start_on: datetime.datetime | None | Unset = UNSET
    test_end_on: datetime.datetime | None | Unset = UNSET
    breaker_initial_status: None | str | Unset = UNSET
    start_export_value: float | None | Unset = UNSET
    start_import_value: float | None | Unset = UNSET
    next_export_value: float | None | Unset = UNSET
    next_import_value: float | None | Unset = UNSET
    average_voltage: float | None | Unset = UNSET
    instantaneous_active_power_import: float | None | Unset = UNSET
    instantaneous_active_power_export: float | None | Unset = UNSET
    instantaneous_current: float | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    communicator: CommunicatorReferenceModel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_reference_model import CommunicatorReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        entered_on: None | str | Unset
        if isinstance(self.entered_on, Unset):
            entered_on = UNSET
        elif isinstance(self.entered_on, datetime.datetime):
            entered_on = self.entered_on.isoformat()
        else:
            entered_on = self.entered_on

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

        test_start_on: None | str | Unset
        if isinstance(self.test_start_on, Unset):
            test_start_on = UNSET
        elif isinstance(self.test_start_on, datetime.datetime):
            test_start_on = self.test_start_on.isoformat()
        else:
            test_start_on = self.test_start_on

        test_end_on: None | str | Unset
        if isinstance(self.test_end_on, Unset):
            test_end_on = UNSET
        elif isinstance(self.test_end_on, datetime.datetime):
            test_end_on = self.test_end_on.isoformat()
        else:
            test_end_on = self.test_end_on

        breaker_initial_status: None | str | Unset
        if isinstance(self.breaker_initial_status, Unset):
            breaker_initial_status = UNSET
        else:
            breaker_initial_status = self.breaker_initial_status

        start_export_value: float | None | Unset
        if isinstance(self.start_export_value, Unset):
            start_export_value = UNSET
        else:
            start_export_value = self.start_export_value

        start_import_value: float | None | Unset
        if isinstance(self.start_import_value, Unset):
            start_import_value = UNSET
        else:
            start_import_value = self.start_import_value

        next_export_value: float | None | Unset
        if isinstance(self.next_export_value, Unset):
            next_export_value = UNSET
        else:
            next_export_value = self.next_export_value

        next_import_value: float | None | Unset
        if isinstance(self.next_import_value, Unset):
            next_import_value = UNSET
        else:
            next_import_value = self.next_import_value

        average_voltage: float | None | Unset
        if isinstance(self.average_voltage, Unset):
            average_voltage = UNSET
        else:
            average_voltage = self.average_voltage

        instantaneous_active_power_import: float | None | Unset
        if isinstance(self.instantaneous_active_power_import, Unset):
            instantaneous_active_power_import = UNSET
        else:
            instantaneous_active_power_import = self.instantaneous_active_power_import

        instantaneous_active_power_export: float | None | Unset
        if isinstance(self.instantaneous_active_power_export, Unset):
            instantaneous_active_power_export = UNSET
        else:
            instantaneous_active_power_export = self.instantaneous_active_power_export

        instantaneous_current: float | None | Unset
        if isinstance(self.instantaneous_current, Unset):
            instantaneous_current = UNSET
        else:
            instantaneous_current = self.instantaneous_current

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        communicator: dict[str, Any] | None | Unset
        if isinstance(self.communicator, Unset):
            communicator = UNSET
        elif isinstance(self.communicator, CommunicatorReferenceModel):
            communicator = self.communicator.to_dict()
        else:
            communicator = self.communicator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if entered_on is not UNSET:
            field_dict["enteredOn"] = entered_on
        if status is not UNSET:
            field_dict["status"] = status
        if result_message is not UNSET:
            field_dict["resultMessage"] = result_message
        if test_start_on is not UNSET:
            field_dict["testStartOn"] = test_start_on
        if test_end_on is not UNSET:
            field_dict["testEndOn"] = test_end_on
        if breaker_initial_status is not UNSET:
            field_dict["breakerInitialStatus"] = breaker_initial_status
        if start_export_value is not UNSET:
            field_dict["startExportValue"] = start_export_value
        if start_import_value is not UNSET:
            field_dict["startImportValue"] = start_import_value
        if next_export_value is not UNSET:
            field_dict["nextExportValue"] = next_export_value
        if next_import_value is not UNSET:
            field_dict["nextImportValue"] = next_import_value
        if average_voltage is not UNSET:
            field_dict["averageVoltage"] = average_voltage
        if instantaneous_active_power_import is not UNSET:
            field_dict["instantaneousActivePowerImport"] = instantaneous_active_power_import
        if instantaneous_active_power_export is not UNSET:
            field_dict["instantaneousActivePowerExport"] = instantaneous_active_power_export
        if instantaneous_current is not UNSET:
            field_dict["instantaneousCurrent"] = instantaneous_current
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if communicator is not UNSET:
            field_dict["communicator"] = communicator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communicator_reference_model import CommunicatorReferenceModel

        d = dict(src_dict)

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

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

        def _parse_test_start_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                test_start_on_type_0 = datetime.datetime.fromisoformat(data)

                return test_start_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        test_start_on = _parse_test_start_on(d.pop("testStartOn", UNSET))

        def _parse_test_end_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                test_end_on_type_0 = datetime.datetime.fromisoformat(data)

                return test_end_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        test_end_on = _parse_test_end_on(d.pop("testEndOn", UNSET))

        def _parse_breaker_initial_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        breaker_initial_status = _parse_breaker_initial_status(d.pop("breakerInitialStatus", UNSET))

        def _parse_start_export_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        start_export_value = _parse_start_export_value(d.pop("startExportValue", UNSET))

        def _parse_start_import_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        start_import_value = _parse_start_import_value(d.pop("startImportValue", UNSET))

        def _parse_next_export_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        next_export_value = _parse_next_export_value(d.pop("nextExportValue", UNSET))

        def _parse_next_import_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        next_import_value = _parse_next_import_value(d.pop("nextImportValue", UNSET))

        def _parse_average_voltage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        average_voltage = _parse_average_voltage(d.pop("averageVoltage", UNSET))

        def _parse_instantaneous_active_power_import(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        instantaneous_active_power_import = _parse_instantaneous_active_power_import(
            d.pop("instantaneousActivePowerImport", UNSET)
        )

        def _parse_instantaneous_active_power_export(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        instantaneous_active_power_export = _parse_instantaneous_active_power_export(
            d.pop("instantaneousActivePowerExport", UNSET)
        )

        def _parse_instantaneous_current(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        instantaneous_current = _parse_instantaneous_current(d.pop("instantaneousCurrent", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_communicator(data: object) -> CommunicatorReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                communicator_type_1 = CommunicatorReferenceModel.from_dict(data)

                return communicator_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CommunicatorReferenceModel | None | Unset, data)

        communicator = _parse_communicator(d.pop("communicator", UNSET))

        pv_production_test_output_model = cls(
            resource_uri=resource_uri,
            entered_on=entered_on,
            status=status,
            result_message=result_message,
            test_start_on=test_start_on,
            test_end_on=test_end_on,
            breaker_initial_status=breaker_initial_status,
            start_export_value=start_export_value,
            start_import_value=start_import_value,
            next_export_value=next_export_value,
            next_import_value=next_import_value,
            average_voltage=average_voltage,
            instantaneous_active_power_import=instantaneous_active_power_import,
            instantaneous_active_power_export=instantaneous_active_power_export,
            instantaneous_current=instantaneous_current,
            external_id=external_id,
            communicator=communicator,
        )

        pv_production_test_output_model.additional_properties = d
        return pv_production_test_output_model

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
