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
        communicator_verifications (list[CommunicatorVerificationOutputModel] | None | Unset):
    """

    communicator_verifications: list[CommunicatorVerificationOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_verification_output_model import (
            CommunicatorVerificationOutputModel,
        )

        communicator_verifications: list[dict[str, Any]] | None | Unset
        if isinstance(self.communicator_verifications, Unset):
            communicator_verifications = UNSET
        elif isinstance(self.communicator_verifications, list):
            communicator_verifications = []
            for communicator_verifications_type_0_item_data in self.communicator_verifications:
                communicator_verifications_type_0_item = (
                    communicator_verifications_type_0_item_data.to_dict()
                )
                communicator_verifications.append(communicator_verifications_type_0_item)

        else:
            communicator_verifications = self.communicator_verifications

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

        def _parse_communicator_verifications(
            data: object,
        ) -> list[CommunicatorVerificationOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                communicator_verifications_type_0 = []
                _communicator_verifications_type_0 = data
                for (
                    communicator_verifications_type_0_item_data
                ) in _communicator_verifications_type_0:
                    communicator_verifications_type_0_item = (
                        CommunicatorVerificationOutputModel.from_dict(
                            communicator_verifications_type_0_item_data
                        )
                    )

                    communicator_verifications_type_0.append(communicator_verifications_type_0_item)

                return communicator_verifications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CommunicatorVerificationOutputModel] | None | Unset, data)

        communicator_verifications = _parse_communicator_verifications(
            d.pop("communicatorVerifications", UNSET)
        )

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
