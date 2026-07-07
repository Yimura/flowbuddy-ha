from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.client_user_group_output_model import ClientUserGroupOutputModel


T = TypeVar("T", bound="ClientUserGroupOutputListModel")


@_attrs_define
class ClientUserGroupOutputListModel:
    """
    Attributes:
        client_user_groups (list[ClientUserGroupOutputModel] | Unset):
    """

    client_user_groups: list[ClientUserGroupOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.client_user_group_output_model import ClientUserGroupOutputModel

        client_user_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.client_user_groups, Unset):
            client_user_groups = []
            for client_user_groups_item_data in self.client_user_groups:
                client_user_groups_item = client_user_groups_item_data.to_dict()
                client_user_groups.append(client_user_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_user_groups is not UNSET:
            field_dict["clientUserGroups"] = client_user_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.client_user_group_output_model import ClientUserGroupOutputModel

        d = dict(src_dict)
        _client_user_groups = d.pop("clientUserGroups", UNSET)
        client_user_groups: list[ClientUserGroupOutputModel] | Unset = UNSET
        if _client_user_groups is not UNSET:
            client_user_groups = []
            for client_user_groups_item_data in _client_user_groups:
                client_user_groups_item = ClientUserGroupOutputModel.from_dict(
                    client_user_groups_item_data
                )

                client_user_groups.append(client_user_groups_item)

        client_user_group_output_list_model = cls(
            client_user_groups=client_user_groups,
        )

        client_user_group_output_list_model.additional_properties = d
        return client_user_group_output_list_model

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
