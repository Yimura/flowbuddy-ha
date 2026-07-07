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
        access_rights (list[AccessRightOutputModel] | None | Unset):
    """

    access_rights: list[AccessRightOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.access_right_output_model import AccessRightOutputModel

        access_rights: list[dict[str, Any]] | None | Unset
        if isinstance(self.access_rights, Unset):
            access_rights = UNSET
        elif isinstance(self.access_rights, list):
            access_rights = []
            for access_rights_type_0_item_data in self.access_rights:
                access_rights_type_0_item = access_rights_type_0_item_data.to_dict()
                access_rights.append(access_rights_type_0_item)

        else:
            access_rights = self.access_rights

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

        def _parse_access_rights(data: object) -> list[AccessRightOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_rights_type_0 = []
                _access_rights_type_0 = data
                for access_rights_type_0_item_data in _access_rights_type_0:
                    access_rights_type_0_item = AccessRightOutputModel.from_dict(
                        access_rights_type_0_item_data
                    )

                    access_rights_type_0.append(access_rights_type_0_item)

                return access_rights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AccessRightOutputModel] | None | Unset, data)

        access_rights = _parse_access_rights(d.pop("accessRights", UNSET))

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
