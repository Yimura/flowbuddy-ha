from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.communicator_request_switch_io_port_post_input_model_other_properties import (
        CommunicatorRequestSwitchIoPortPostInputModelOtherProperties,
    )


T = TypeVar("T", bound="CommunicatorRequestSwitchIoPortPostInputModel")


@_attrs_define
class CommunicatorRequestSwitchIoPortPostInputModel:
    """
    Attributes:
        port (int | Unset):
        port_on (bool | Unset):
        other_properties (CommunicatorRequestSwitchIoPortPostInputModelOtherProperties | Unset):
    """

    port: int | Unset = UNSET
    port_on: bool | Unset = UNSET
    other_properties: CommunicatorRequestSwitchIoPortPostInputModelOtherProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_request_switch_io_port_post_input_model_other_properties import (
            CommunicatorRequestSwitchIoPortPostInputModelOtherProperties,
        )

        port = self.port

        port_on = self.port_on

        other_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_properties, Unset):
            other_properties = self.other_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if port_on is not UNSET:
            field_dict["portOn"] = port_on
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communicator_request_switch_io_port_post_input_model_other_properties import (
            CommunicatorRequestSwitchIoPortPostInputModelOtherProperties,
        )

        d = dict(src_dict)
        port = d.pop("port", UNSET)

        port_on = d.pop("portOn", UNSET)

        _other_properties = d.pop("otherProperties", UNSET)
        other_properties: CommunicatorRequestSwitchIoPortPostInputModelOtherProperties | Unset
        if isinstance(_other_properties, Unset):
            other_properties = UNSET
        else:
            other_properties = (
                CommunicatorRequestSwitchIoPortPostInputModelOtherProperties.from_dict(
                    _other_properties
                )
            )

        communicator_request_switch_io_port_post_input_model = cls(
            port=port,
            port_on=port_on,
            other_properties=other_properties,
        )

        communicator_request_switch_io_port_post_input_model.additional_properties = d
        return communicator_request_switch_io_port_post_input_model

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
