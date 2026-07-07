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


T = TypeVar("T", bound="ConnectionTestOutputModel")


@_attrs_define
class ConnectionTestOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        entered_on (datetime.datetime | Unset):
        status (str | Unset):
        result_message (str | Unset):
        signal_strength (int | Unset):
        lan_connection_successful (bool | Unset):
        external_id (str | Unset):
        communicator (CommunicatorReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    entered_on: datetime.datetime | Unset = UNSET
    status: str | Unset = UNSET
    result_message: str | Unset = UNSET
    signal_strength: int | Unset = UNSET
    lan_connection_successful: bool | Unset = UNSET
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

        signal_strength = self.signal_strength

        lan_connection_successful = self.lan_connection_successful

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
        if signal_strength is not UNSET:
            field_dict["signalStrength"] = signal_strength
        if lan_connection_successful is not UNSET:
            field_dict["lanConnectionSuccessful"] = lan_connection_successful
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

        signal_strength = d.pop("signalStrength", UNSET)

        lan_connection_successful = d.pop("lanConnectionSuccessful", UNSET)

        external_id = d.pop("externalId", UNSET)

        _communicator = d.pop("communicator", UNSET)
        communicator: CommunicatorReferenceModel | Unset
        if isinstance(_communicator, Unset):
            communicator = UNSET
        else:
            communicator = CommunicatorReferenceModel.from_dict(_communicator)

        connection_test_output_model = cls(
            resource_uri=resource_uri,
            entered_on=entered_on,
            status=status,
            result_message=result_message,
            signal_strength=signal_strength,
            lan_connection_successful=lan_connection_successful,
            external_id=external_id,
            communicator=communicator,
        )

        connection_test_output_model.additional_properties = d
        return connection_test_output_model

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
