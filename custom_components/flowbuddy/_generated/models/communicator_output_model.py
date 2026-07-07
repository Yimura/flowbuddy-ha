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
    from ..models.communicator_type_reference_model import CommunicatorTypeReferenceModel
    from ..models.sim_reference_model import SimReferenceModel


T = TypeVar("T", bound="CommunicatorOutputModel")


@_attrs_define
class CommunicatorOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        logical_device_name (str | Unset): Unique identifier of communicator
        firm_ware_version (str | Unset): Version of the firmware of the device
        first_registered_on (datetime.datetime | None | Unset): Time the device was first registered
        status (str | Unset): Status of registration
        last_successful_polling_on (datetime.datetime | None | Unset): Time of last successful polling of the device
        last_polling_result (str | Unset): Result of last data retrieval
        last_successful_communication_on (datetime.datetime | None | Unset): Time of last successful communication
        last_communication_attempt_on (datetime.datetime | None | Unset): Time of last communication attempt
        last_time_sync (datetime.datetime | None | Unset): Last time synchronisation
        external_id (str | Unset):
        type_ (CommunicatorTypeReferenceModel | Unset):
        sim (SimReferenceModel | Unset): Connection which can be used for network communication
    """

    resource_uri: str | Unset = UNSET
    logical_device_name: str | Unset = UNSET
    firm_ware_version: str | Unset = UNSET
    first_registered_on: datetime.datetime | None | Unset = UNSET
    status: str | Unset = UNSET
    last_successful_polling_on: datetime.datetime | None | Unset = UNSET
    last_polling_result: str | Unset = UNSET
    last_successful_communication_on: datetime.datetime | None | Unset = UNSET
    last_communication_attempt_on: datetime.datetime | None | Unset = UNSET
    last_time_sync: datetime.datetime | None | Unset = UNSET
    external_id: str | Unset = UNSET
    type_: CommunicatorTypeReferenceModel | Unset = UNSET
    sim: SimReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_type_reference_model import CommunicatorTypeReferenceModel
        from ..models.sim_reference_model import SimReferenceModel

        resource_uri = self.resource_uri

        logical_device_name = self.logical_device_name

        firm_ware_version = self.firm_ware_version

        first_registered_on: None | str | Unset
        if isinstance(self.first_registered_on, Unset):
            first_registered_on = UNSET
        elif isinstance(self.first_registered_on, datetime.datetime):
            first_registered_on = self.first_registered_on.isoformat()
        else:
            first_registered_on = self.first_registered_on

        status = self.status

        last_successful_polling_on: None | str | Unset
        if isinstance(self.last_successful_polling_on, Unset):
            last_successful_polling_on = UNSET
        elif isinstance(self.last_successful_polling_on, datetime.datetime):
            last_successful_polling_on = self.last_successful_polling_on.isoformat()
        else:
            last_successful_polling_on = self.last_successful_polling_on

        last_polling_result = self.last_polling_result

        last_successful_communication_on: None | str | Unset
        if isinstance(self.last_successful_communication_on, Unset):
            last_successful_communication_on = UNSET
        elif isinstance(self.last_successful_communication_on, datetime.datetime):
            last_successful_communication_on = self.last_successful_communication_on.isoformat()
        else:
            last_successful_communication_on = self.last_successful_communication_on

        last_communication_attempt_on: None | str | Unset
        if isinstance(self.last_communication_attempt_on, Unset):
            last_communication_attempt_on = UNSET
        elif isinstance(self.last_communication_attempt_on, datetime.datetime):
            last_communication_attempt_on = self.last_communication_attempt_on.isoformat()
        else:
            last_communication_attempt_on = self.last_communication_attempt_on

        last_time_sync: None | str | Unset
        if isinstance(self.last_time_sync, Unset):
            last_time_sync = UNSET
        elif isinstance(self.last_time_sync, datetime.datetime):
            last_time_sync = self.last_time_sync.isoformat()
        else:
            last_time_sync = self.last_time_sync

        external_id = self.external_id

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        sim: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sim, Unset):
            sim = self.sim.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if logical_device_name is not UNSET:
            field_dict["logicalDeviceName"] = logical_device_name
        if firm_ware_version is not UNSET:
            field_dict["firmWareVersion"] = firm_ware_version
        if first_registered_on is not UNSET:
            field_dict["firstRegisteredOn"] = first_registered_on
        if status is not UNSET:
            field_dict["status"] = status
        if last_successful_polling_on is not UNSET:
            field_dict["lastSuccessfulPollingOn"] = last_successful_polling_on
        if last_polling_result is not UNSET:
            field_dict["lastPollingResult"] = last_polling_result
        if last_successful_communication_on is not UNSET:
            field_dict["lastSuccessfulCommunicationOn"] = last_successful_communication_on
        if last_communication_attempt_on is not UNSET:
            field_dict["lastCommunicationAttemptOn"] = last_communication_attempt_on
        if last_time_sync is not UNSET:
            field_dict["lastTimeSync"] = last_time_sync
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if sim is not UNSET:
            field_dict["sim"] = sim

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communicator_type_reference_model import CommunicatorTypeReferenceModel
        from ..models.sim_reference_model import SimReferenceModel

        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

        logical_device_name = d.pop("logicalDeviceName", UNSET)

        firm_ware_version = d.pop("firmWareVersion", UNSET)

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

        status = d.pop("status", UNSET)

        def _parse_last_successful_polling_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_successful_polling_on_type_0 = datetime.datetime.fromisoformat(data)

                return last_successful_polling_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_successful_polling_on = _parse_last_successful_polling_on(
            d.pop("lastSuccessfulPollingOn", UNSET)
        )

        last_polling_result = d.pop("lastPollingResult", UNSET)

        def _parse_last_successful_communication_on(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_successful_communication_on_type_0 = datetime.datetime.fromisoformat(data)

                return last_successful_communication_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_successful_communication_on = _parse_last_successful_communication_on(
            d.pop("lastSuccessfulCommunicationOn", UNSET)
        )

        def _parse_last_communication_attempt_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_communication_attempt_on_type_0 = datetime.datetime.fromisoformat(data)

                return last_communication_attempt_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_communication_attempt_on = _parse_last_communication_attempt_on(
            d.pop("lastCommunicationAttemptOn", UNSET)
        )

        def _parse_last_time_sync(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_time_sync_type_0 = datetime.datetime.fromisoformat(data)

                return last_time_sync_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_time_sync = _parse_last_time_sync(d.pop("lastTimeSync", UNSET))

        external_id = d.pop("externalId", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CommunicatorTypeReferenceModel | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CommunicatorTypeReferenceModel.from_dict(_type_)

        _sim = d.pop("sim", UNSET)
        sim: SimReferenceModel | Unset
        if isinstance(_sim, Unset):
            sim = UNSET
        else:
            sim = SimReferenceModel.from_dict(_sim)

        communicator_output_model = cls(
            resource_uri=resource_uri,
            logical_device_name=logical_device_name,
            firm_ware_version=firm_ware_version,
            first_registered_on=first_registered_on,
            status=status,
            last_successful_polling_on=last_successful_polling_on,
            last_polling_result=last_polling_result,
            last_successful_communication_on=last_successful_communication_on,
            last_communication_attempt_on=last_communication_attempt_on,
            last_time_sync=last_time_sync,
            external_id=external_id,
            type_=type_,
            sim=sim,
        )

        communicator_output_model.additional_properties = d
        return communicator_output_model

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
