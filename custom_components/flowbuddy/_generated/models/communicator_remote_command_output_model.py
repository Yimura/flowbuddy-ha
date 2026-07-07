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
        resource_uri (str | Unset):
        type_ (str | Unset): The type will indicate which action was requested (e.g. `connectiontest`)
        timestamp (datetime.datetime | Unset):
        status (str | Unset): Initial = The command is waiting for execution. Dispatching = We are trying to connect to
            the module. Dispatched = The action was executed.
        result (str | Unset): Failure or Success. A failure is often caused by a connection issue and can be solved by a
            retry at a later moment.
        result_message (str | Unset):
        entered_on (datetime.datetime | Unset):
        performed_on (datetime.datetime | Unset):
        external_id (str | Unset):
        communicator (CommunicatorReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    type_: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    status: str | Unset = UNSET
    result: str | Unset = UNSET
    result_message: str | Unset = UNSET
    entered_on: datetime.datetime | Unset = UNSET
    performed_on: datetime.datetime | Unset = UNSET
    external_id: str | Unset = UNSET
    communicator: CommunicatorReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_reference_model import CommunicatorReferenceModel

        resource_uri = self.resource_uri

        type_ = self.type_

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        status = self.status

        result = self.result

        result_message = self.result_message

        entered_on: str | Unset = UNSET
        if not isinstance(self.entered_on, Unset):
            entered_on = self.entered_on.isoformat()

        performed_on: str | Unset = UNSET
        if not isinstance(self.performed_on, Unset):
            performed_on = self.performed_on.isoformat()

        external_id = self.external_id

        communicator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.communicator, Unset):
            communicator = self.communicator.to_dict()

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
        resource_uri = d.pop("resourceUri", UNSET)

        type_ = d.pop("type", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        status = d.pop("status", UNSET)

        result = d.pop("result", UNSET)

        result_message = d.pop("resultMessage", UNSET)

        _entered_on = d.pop("enteredOn", UNSET)
        entered_on: datetime.datetime | Unset
        if isinstance(_entered_on, Unset):
            entered_on = UNSET
        else:
            entered_on = datetime.datetime.fromisoformat(_entered_on)

        _performed_on = d.pop("performedOn", UNSET)
        performed_on: datetime.datetime | Unset
        if isinstance(_performed_on, Unset):
            performed_on = UNSET
        else:
            performed_on = datetime.datetime.fromisoformat(_performed_on)

        external_id = d.pop("externalId", UNSET)

        _communicator = d.pop("communicator", UNSET)
        communicator: CommunicatorReferenceModel | Unset
        if isinstance(_communicator, Unset):
            communicator = UNSET
        else:
            communicator = CommunicatorReferenceModel.from_dict(_communicator)

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
