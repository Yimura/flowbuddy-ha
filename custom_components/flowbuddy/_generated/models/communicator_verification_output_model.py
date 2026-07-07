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
        resource_uri (None | str | Unset):
        signal_strength (int | None | Unset):
        result_code (int | None | Unset):
        result_message (None | str | Unset):
        performed_on (datetime.datetime | None | Unset):
        external_id (None | str | Unset):
        communicator (CommunicatorReferenceModel | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    signal_strength: int | None | Unset = UNSET
    result_code: int | None | Unset = UNSET
    result_message: None | str | Unset = UNSET
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

        signal_strength: int | None | Unset
        if isinstance(self.signal_strength, Unset):
            signal_strength = UNSET
        else:
            signal_strength = self.signal_strength

        result_code: int | None | Unset
        if isinstance(self.result_code, Unset):
            result_code = UNSET
        else:
            result_code = self.result_code

        result_message: None | str | Unset
        if isinstance(self.result_message, Unset):
            result_message = UNSET
        else:
            result_message = self.result_message

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

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

        def _parse_signal_strength(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        signal_strength = _parse_signal_strength(d.pop("signalStrength", UNSET))

        def _parse_result_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        result_code = _parse_result_code(d.pop("resultCode", UNSET))

        def _parse_result_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result_message = _parse_result_message(d.pop("resultMessage", UNSET))

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
