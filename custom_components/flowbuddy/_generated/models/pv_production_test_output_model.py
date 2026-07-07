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
        resource_uri (str | Unset):
        entered_on (datetime.datetime | Unset):
        status (str | Unset):
        result_message (str | Unset):
        test_start_on (datetime.datetime | Unset): Time of first connection with the `communicator` and start of test
        test_end_on (datetime.datetime | Unset):
        breaker_initial_status (str | Unset):
        start_export_value (float | Unset): Cumulative export value in Wh as reported on the display of `communicator`
        start_import_value (float | Unset): Cumulative import value in Wh as reported on the display of `communicator`.
            This value should be close to 0 and lower than the export value. If not, this might indicate incorrect wiring.
        next_export_value (float | Unset): Cumulative export value that was read from the `communicator` after several
            minutes. The difference between the start and next value is used to decide if a valid production was measured.
        next_import_value (float | Unset):
        average_voltage (float | Unset): Average voltage of the last 10 minutes at the moment of the productiontest. If
            this value is close to 253V, this might lead to over voltage which might to a shutdown of the inverter.
        instantaneous_active_power_import (float | Unset): imported power measured by the `communicator` at the moment
            of productiontest. If this value is greater as 0, the `communicator` might be wired incorrectly.
        instantaneous_active_power_export (float | Unset): exported power measured by the communicator at the moment of
            productiontest. If this value is greater as 0, the installation is working as expected.
        instantaneous_current (float | Unset):
        external_id (str | Unset):
        communicator (CommunicatorReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    entered_on: datetime.datetime | Unset = UNSET
    status: str | Unset = UNSET
    result_message: str | Unset = UNSET
    test_start_on: datetime.datetime | Unset = UNSET
    test_end_on: datetime.datetime | Unset = UNSET
    breaker_initial_status: str | Unset = UNSET
    start_export_value: float | Unset = UNSET
    start_import_value: float | Unset = UNSET
    next_export_value: float | Unset = UNSET
    next_import_value: float | Unset = UNSET
    average_voltage: float | Unset = UNSET
    instantaneous_active_power_import: float | Unset = UNSET
    instantaneous_active_power_export: float | Unset = UNSET
    instantaneous_current: float | Unset = UNSET
    external_id: str | Unset = UNSET
    communicator: CommunicatorReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_reference_model import CommunicatorReferenceModel

        resource_uri = self.resource_uri

        entered_on: str | Unset = UNSET
        if not isinstance(self.entered_on, Unset):
            entered_on = self.entered_on.isoformat()

        status = self.status

        result_message = self.result_message

        test_start_on: str | Unset = UNSET
        if not isinstance(self.test_start_on, Unset):
            test_start_on = self.test_start_on.isoformat()

        test_end_on: str | Unset = UNSET
        if not isinstance(self.test_end_on, Unset):
            test_end_on = self.test_end_on.isoformat()

        breaker_initial_status = self.breaker_initial_status

        start_export_value = self.start_export_value

        start_import_value = self.start_import_value

        next_export_value = self.next_export_value

        next_import_value = self.next_import_value

        average_voltage = self.average_voltage

        instantaneous_active_power_import = self.instantaneous_active_power_import

        instantaneous_active_power_export = self.instantaneous_active_power_export

        instantaneous_current = self.instantaneous_current

        external_id = self.external_id

        communicator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.communicator, Unset):
            communicator = self.communicator.to_dict()

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
        resource_uri = d.pop("resourceUri", UNSET)

        _entered_on = d.pop("enteredOn", UNSET)
        entered_on: datetime.datetime | Unset
        if isinstance(_entered_on, Unset):
            entered_on = UNSET
        else:
            entered_on = datetime.datetime.fromisoformat(_entered_on)

        status = d.pop("status", UNSET)

        result_message = d.pop("resultMessage", UNSET)

        _test_start_on = d.pop("testStartOn", UNSET)
        test_start_on: datetime.datetime | Unset
        if isinstance(_test_start_on, Unset):
            test_start_on = UNSET
        else:
            test_start_on = datetime.datetime.fromisoformat(_test_start_on)

        _test_end_on = d.pop("testEndOn", UNSET)
        test_end_on: datetime.datetime | Unset
        if isinstance(_test_end_on, Unset):
            test_end_on = UNSET
        else:
            test_end_on = datetime.datetime.fromisoformat(_test_end_on)

        breaker_initial_status = d.pop("breakerInitialStatus", UNSET)

        start_export_value = d.pop("startExportValue", UNSET)

        start_import_value = d.pop("startImportValue", UNSET)

        next_export_value = d.pop("nextExportValue", UNSET)

        next_import_value = d.pop("nextImportValue", UNSET)

        average_voltage = d.pop("averageVoltage", UNSET)

        instantaneous_active_power_import = d.pop("instantaneousActivePowerImport", UNSET)

        instantaneous_active_power_export = d.pop("instantaneousActivePowerExport", UNSET)

        instantaneous_current = d.pop("instantaneousCurrent", UNSET)

        external_id = d.pop("externalId", UNSET)

        _communicator = d.pop("communicator", UNSET)
        communicator: CommunicatorReferenceModel | Unset
        if isinstance(_communicator, Unset):
            communicator = UNSET
        else:
            communicator = CommunicatorReferenceModel.from_dict(_communicator)

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
