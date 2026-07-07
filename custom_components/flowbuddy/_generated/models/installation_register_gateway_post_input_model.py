from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.installation_register_gateway_post_input_model_other_properties import (
        InstallationRegisterGatewayPostInputModelOtherProperties,
    )


T = TypeVar("T", bound="InstallationRegisterGatewayPostInputModel")


@_attrs_define
class InstallationRegisterGatewayPostInputModel:
    """
    Attributes:
        communicator (str | Unset): The communicator serial number starting with **XMX** or **IQ**. If no Communicator
            is selected, the linked Communicator field of Installation is used as input.
        initial_polling (str | Unset):
        other_properties (InstallationRegisterGatewayPostInputModelOtherProperties | Unset):
    """

    communicator: str | Unset = UNSET
    initial_polling: str | Unset = UNSET
    other_properties: InstallationRegisterGatewayPostInputModelOtherProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_register_gateway_post_input_model_other_properties import (
            InstallationRegisterGatewayPostInputModelOtherProperties,
        )

        communicator = self.communicator

        initial_polling = self.initial_polling

        other_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_properties, Unset):
            other_properties = self.other_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if communicator is not UNSET:
            field_dict["communicator"] = communicator
        if initial_polling is not UNSET:
            field_dict["initialPolling"] = initial_polling
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.installation_register_gateway_post_input_model_other_properties import (
            InstallationRegisterGatewayPostInputModelOtherProperties,
        )

        d = dict(src_dict)
        communicator = d.pop("communicator", UNSET)

        initial_polling = d.pop("initialPolling", UNSET)

        _other_properties = d.pop("otherProperties", UNSET)
        other_properties: InstallationRegisterGatewayPostInputModelOtherProperties | Unset
        if isinstance(_other_properties, Unset):
            other_properties = UNSET
        else:
            other_properties = InstallationRegisterGatewayPostInputModelOtherProperties.from_dict(
                _other_properties
            )

        installation_register_gateway_post_input_model = cls(
            communicator=communicator,
            initial_polling=initial_polling,
            other_properties=other_properties,
        )

        installation_register_gateway_post_input_model.additional_properties = d
        return installation_register_gateway_post_input_model

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
