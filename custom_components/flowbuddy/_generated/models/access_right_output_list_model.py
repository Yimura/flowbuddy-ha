from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.access_right_output_model import AccessRightOutputModel


T = TypeVar("T", bound="AccessRightOutputListModel")


@_attrs_define
class AccessRightOutputListModel:
    """
    Attributes:
        access_rights (list[AccessRightOutputModel] | Unset):
    """

    access_rights: list[AccessRightOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.access_right_output_model import AccessRightOutputModel

        access_rights: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.access_rights, Unset):
            access_rights = []
            for access_rights_item_data in self.access_rights:
                access_rights_item = access_rights_item_data.to_dict()
                access_rights.append(access_rights_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_rights is not UNSET:
            field_dict["accessRights"] = access_rights

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.access_right_output_model import AccessRightOutputModel

        d = dict(src_dict)
        _access_rights = d.pop("accessRights", UNSET)
        access_rights: list[AccessRightOutputModel] | Unset = UNSET
        if _access_rights is not UNSET:
            access_rights = []
            for access_rights_item_data in _access_rights:
                access_rights_item = AccessRightOutputModel.from_dict(access_rights_item_data)

                access_rights.append(access_rights_item)

        access_right_output_list_model = cls(
            access_rights=access_rights,
        )

        access_right_output_list_model.additional_properties = d
        return access_right_output_list_model

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
