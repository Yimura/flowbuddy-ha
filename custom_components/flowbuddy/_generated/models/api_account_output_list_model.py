from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.api_account_output_model import ApiAccountOutputModel


T = TypeVar("T", bound="ApiAccountOutputListModel")


@_attrs_define
class ApiAccountOutputListModel:
    """
    Attributes:
        api_accounts (list[ApiAccountOutputModel] | Unset):
    """

    api_accounts: list[ApiAccountOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_account_output_model import ApiAccountOutputModel

        api_accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.api_accounts, Unset):
            api_accounts = []
            for api_accounts_item_data in self.api_accounts:
                api_accounts_item = api_accounts_item_data.to_dict()
                api_accounts.append(api_accounts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_accounts is not UNSET:
            field_dict["apiAccounts"] = api_accounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_account_output_model import ApiAccountOutputModel

        d = dict(src_dict)
        _api_accounts = d.pop("apiAccounts", UNSET)
        api_accounts: list[ApiAccountOutputModel] | Unset = UNSET
        if _api_accounts is not UNSET:
            api_accounts = []
            for api_accounts_item_data in _api_accounts:
                api_accounts_item = ApiAccountOutputModel.from_dict(api_accounts_item_data)

                api_accounts.append(api_accounts_item)

        api_account_output_list_model = cls(
            api_accounts=api_accounts,
        )

        api_account_output_list_model.additional_properties = d
        return api_account_output_list_model

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
