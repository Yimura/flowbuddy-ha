from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.communicator_verification_output_model import CommunicatorVerificationOutputModel


T = TypeVar("T", bound="CommunicatorVerificationOutputListModel")


@_attrs_define
class CommunicatorVerificationOutputListModel:
    """
    Attributes:
        communicator_verifications (list[CommunicatorVerificationOutputModel] | Unset):
    """

    communicator_verifications: list[CommunicatorVerificationOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_verification_output_model import (
            CommunicatorVerificationOutputModel,
        )

        communicator_verifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.communicator_verifications, Unset):
            communicator_verifications = []
            for communicator_verifications_item_data in self.communicator_verifications:
                communicator_verifications_item = communicator_verifications_item_data.to_dict()
                communicator_verifications.append(communicator_verifications_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if communicator_verifications is not UNSET:
            field_dict["communicatorVerifications"] = communicator_verifications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communicator_verification_output_model import (
            CommunicatorVerificationOutputModel,
        )

        d = dict(src_dict)
        _communicator_verifications = d.pop("communicatorVerifications", UNSET)
        communicator_verifications: list[CommunicatorVerificationOutputModel] | Unset = UNSET
        if _communicator_verifications is not UNSET:
            communicator_verifications = []
            for communicator_verifications_item_data in _communicator_verifications:
                communicator_verifications_item = CommunicatorVerificationOutputModel.from_dict(
                    communicator_verifications_item_data
                )

                communicator_verifications.append(communicator_verifications_item)

        communicator_verification_output_list_model = cls(
            communicator_verifications=communicator_verifications,
        )

        communicator_verification_output_list_model.additional_properties = d
        return communicator_verification_output_list_model

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
