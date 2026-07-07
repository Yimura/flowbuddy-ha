from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.send_channel_type_definition_output_model import (
        SendChannelTypeDefinitionOutputModel,
    )


T = TypeVar("T", bound="SendChannelTypeDefinitionOutputListModel")


@_attrs_define
class SendChannelTypeDefinitionOutputListModel:
    """
    Attributes:
        send_channel_type_definitions (list[SendChannelTypeDefinitionOutputModel] | None | Unset):
    """

    send_channel_type_definitions: list[SendChannelTypeDefinitionOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.send_channel_type_definition_output_model import (
            SendChannelTypeDefinitionOutputModel,
        )

        send_channel_type_definitions: list[dict[str, Any]] | None | Unset
        if isinstance(self.send_channel_type_definitions, Unset):
            send_channel_type_definitions = UNSET
        elif isinstance(self.send_channel_type_definitions, list):
            send_channel_type_definitions = []
            for (
                send_channel_type_definitions_type_0_item_data
            ) in self.send_channel_type_definitions:
                send_channel_type_definitions_type_0_item = (
                    send_channel_type_definitions_type_0_item_data.to_dict()
                )
                send_channel_type_definitions.append(send_channel_type_definitions_type_0_item)

        else:
            send_channel_type_definitions = self.send_channel_type_definitions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if send_channel_type_definitions is not UNSET:
            field_dict["sendChannelTypeDefinitions"] = send_channel_type_definitions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_channel_type_definition_output_model import (
            SendChannelTypeDefinitionOutputModel,
        )

        d = dict(src_dict)

        def _parse_send_channel_type_definitions(
            data: object,
        ) -> list[SendChannelTypeDefinitionOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                send_channel_type_definitions_type_0 = []
                _send_channel_type_definitions_type_0 = data
                for (
                    send_channel_type_definitions_type_0_item_data
                ) in _send_channel_type_definitions_type_0:
                    send_channel_type_definitions_type_0_item = (
                        SendChannelTypeDefinitionOutputModel.from_dict(
                            send_channel_type_definitions_type_0_item_data
                        )
                    )

                    send_channel_type_definitions_type_0.append(
                        send_channel_type_definitions_type_0_item
                    )

                return send_channel_type_definitions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SendChannelTypeDefinitionOutputModel] | None | Unset, data)

        send_channel_type_definitions = _parse_send_channel_type_definitions(
            d.pop("sendChannelTypeDefinitions", UNSET)
        )

        send_channel_type_definition_output_list_model = cls(
            send_channel_type_definitions=send_channel_type_definitions,
        )

        send_channel_type_definition_output_list_model.additional_properties = d
        return send_channel_type_definition_output_list_model

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
