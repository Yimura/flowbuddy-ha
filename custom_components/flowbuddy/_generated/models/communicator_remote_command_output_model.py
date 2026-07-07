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


T = TypeVar("T", bound="CommunicatorRemoteCommandOutputModel")


@_attrs_define
class CommunicatorRemoteCommandOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        type_ (None | str | Unset): The type will indicate which action was requested (e.g. `connectiontest`)
        timestamp (datetime.datetime | None | Unset):
        status (None | str | Unset): Initial = The command is waiting for execution. Dispatching = We are trying to
            connect to the module. Dispatched = The action was executed.
        result (None | str | Unset): Failure or Success. A failure is often caused by a connection issue and can be
            solved by a retry at a later moment.
        result_message (None | str | Unset):
        entered_on (datetime.datetime | None | Unset):
        performed_on (datetime.datetime | None | Unset):
        external_id (None | str | Unset):
        communicator (CommunicatorReferenceModel | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    timestamp: datetime.datetime | None | Unset = UNSET
    status: None | str | Unset = UNSET
    result: None | str | Unset = UNSET
    result_message: None | str | Unset = UNSET
    entered_on: datetime.datetime | None | Unset = UNSET
    performed_on: datetime.datetime | None | Unset = UNSET
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

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        timestamp: None | str | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        elif isinstance(self.timestamp, datetime.datetime):
            timestamp = self.timestamp.isoformat()
        else:
            timestamp = self.timestamp

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

        result_message: None | str | Unset
        if isinstance(self.result_message, Unset):
            result_message = UNSET
        else:
            result_message = self.result_message

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
        if type_ is not UNSET:
            field_dict["type"] = type_
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if status is not UNSET:
            field_dict["status"] = status
        if result is not UNSET:
            field_dict["result"] = result
        if result_message is not UNSET:
            field_dict["resultMessage"] = result_message
        if entered_on is not UNSET:
            field_dict["enteredOn"] = entered_on
        if performed_on is not UNSET:
            field_dict["performedOn"] = performed_on
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

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timestamp_type_0 = datetime.datetime.fromisoformat(data)

                return timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

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

        def _parse_result_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result_message = _parse_result_message(d.pop("resultMessage", UNSET))

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

        communicator_remote_command_output_model = cls(
            resource_uri=resource_uri,
            type_=type_,
            timestamp=timestamp,
            status=status,
            result=result,
            result_message=result_message,
            entered_on=entered_on,
            performed_on=performed_on,
            external_id=external_id,
            communicator=communicator,
        )

        communicator_remote_command_output_model.additional_properties = d
        return communicator_remote_command_output_model

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
