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
        client_user_groups (list[ClientUserGroupOutputModel] | None | Unset):
    """

    client_user_groups: list[ClientUserGroupOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.client_user_group_output_model import ClientUserGroupOutputModel

        client_user_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.client_user_groups, Unset):
            client_user_groups = UNSET
        elif isinstance(self.client_user_groups, list):
            client_user_groups = []
            for client_user_groups_type_0_item_data in self.client_user_groups:
                client_user_groups_type_0_item = client_user_groups_type_0_item_data.to_dict()
                client_user_groups.append(client_user_groups_type_0_item)

        else:
            client_user_groups = self.client_user_groups

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

        def _parse_client_user_groups(
            data: object,
        ) -> list[ClientUserGroupOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                client_user_groups_type_0 = []
                _client_user_groups_type_0 = data
                for client_user_groups_type_0_item_data in _client_user_groups_type_0:
                    client_user_groups_type_0_item = ClientUserGroupOutputModel.from_dict(
                        client_user_groups_type_0_item_data
                    )

                    client_user_groups_type_0.append(client_user_groups_type_0_item)

                return client_user_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClientUserGroupOutputModel] | None | Unset, data)

        client_user_groups = _parse_client_user_groups(d.pop("clientUserGroups", UNSET))

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
