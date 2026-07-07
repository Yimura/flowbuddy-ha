from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.command_output_model import CommandOutputModel


T = TypeVar("T", bound="CommandOutputListModel")


@_attrs_define
class CommandOutputListModel:
    """
    Attributes:
        commands (list[CommandOutputModel] | None | Unset):
    """

    commands: list[CommandOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.command_output_model import CommandOutputModel

        commands: list[dict[str, Any]] | None | Unset
        if isinstance(self.commands, Unset):
            commands = UNSET
        elif isinstance(self.commands, list):
            commands = []
            for commands_type_0_item_data in self.commands:
                commands_type_0_item = commands_type_0_item_data.to_dict()
                commands.append(commands_type_0_item)

        else:
            commands = self.commands

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commands is not UNSET:
            field_dict["commands"] = commands

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.command_output_model import CommandOutputModel

        d = dict(src_dict)

        def _parse_commands(data: object) -> list[CommandOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                commands_type_0 = []
                _commands_type_0 = data
                for commands_type_0_item_data in _commands_type_0:
                    commands_type_0_item = CommandOutputModel.from_dict(commands_type_0_item_data)

                    commands_type_0.append(commands_type_0_item)

                return commands_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CommandOutputModel] | None | Unset, data)

        commands = _parse_commands(d.pop("commands", UNSET))

        command_output_list_model = cls(
            commands=commands,
        )

        command_output_list_model.additional_properties = d
        return command_output_list_model

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
