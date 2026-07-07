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


T = TypeVar("T", bound="CommunicatorVerificationOutputModel")


@_attrs_define
class CommunicatorVerificationOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        signal_strength (int | Unset):
        result_code (int | Unset):
        result_message (str | Unset):
        performed_on (datetime.datetime | Unset):
        external_id (str | Unset):
        communicator (CommunicatorReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    signal_strength: int | Unset = UNSET
    result_code: int | Unset = UNSET
    result_message: str | Unset = UNSET
    performed_on: datetime.datetime | Unset = UNSET
    external_id: str | Unset = UNSET
    communicator: CommunicatorReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_reference_model import CommunicatorReferenceModel

        resource_uri = self.resource_uri

        signal_strength = self.signal_strength

        result_code = self.result_code

        result_message = self.result_message

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
        if signal_strength is not UNSET:
            field_dict["signalStrength"] = signal_strength
        if result_code is not UNSET:
            field_dict["resultCode"] = result_code
        if result_message is not UNSET:
            field_dict["resultMessage"] = result_message
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

        signal_strength = d.pop("signalStrength", UNSET)

        result_code = d.pop("resultCode", UNSET)

        result_message = d.pop("resultMessage", UNSET)

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

        communicator_verification_output_model = cls(
            resource_uri=resource_uri,
            signal_strength=signal_strength,
            result_code=result_code,
            result_message=result_message,
            performed_on=performed_on,
            external_id=external_id,
            communicator=communicator,
        )

        communicator_verification_output_model.additional_properties = d
        return communicator_verification_output_model

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
