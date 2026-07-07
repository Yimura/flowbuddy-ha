from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.communicator_remote_command_output_model import (
        CommunicatorRemoteCommandOutputModel,
    )


T = TypeVar("T", bound="CommunicatorRemoteCommandOutputListModel")


@_attrs_define
class CommunicatorRemoteCommandOutputListModel:
    """
    Attributes:
        communicator_remote_commands (list[CommunicatorRemoteCommandOutputModel] | Unset):
    """

    communicator_remote_commands: list[CommunicatorRemoteCommandOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_remote_command_output_model import (
            CommunicatorRemoteCommandOutputModel,
        )

        communicator_remote_commands: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.communicator_remote_commands, Unset):
            communicator_remote_commands = []
            for communicator_remote_commands_item_data in self.communicator_remote_commands:
                communicator_remote_commands_item = communicator_remote_commands_item_data.to_dict()
                communicator_remote_commands.append(communicator_remote_commands_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if communicator_remote_commands is not UNSET:
            field_dict["communicatorRemoteCommands"] = communicator_remote_commands

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communicator_remote_command_output_model import (
            CommunicatorRemoteCommandOutputModel,
        )

        d = dict(src_dict)
        _communicator_remote_commands = d.pop("communicatorRemoteCommands", UNSET)
        communicator_remote_commands: list[CommunicatorRemoteCommandOutputModel] | Unset = UNSET
        if _communicator_remote_commands is not UNSET:
            communicator_remote_commands = []
            for communicator_remote_commands_item_data in _communicator_remote_commands:
                communicator_remote_commands_item = CommunicatorRemoteCommandOutputModel.from_dict(
                    communicator_remote_commands_item_data
                )

                communicator_remote_commands.append(communicator_remote_commands_item)

        communicator_remote_command_output_list_model = cls(
            communicator_remote_commands=communicator_remote_commands,
        )

        communicator_remote_command_output_list_model.additional_properties = d
        return communicator_remote_command_output_list_model

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
