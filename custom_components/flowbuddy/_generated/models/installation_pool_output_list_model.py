from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.installation_pool_output_model import InstallationPoolOutputModel


T = TypeVar("T", bound="InstallationPoolOutputListModel")


@_attrs_define
class InstallationPoolOutputListModel:
    """
    Attributes:
        installation_pools (list[InstallationPoolOutputModel] | Unset):
    """

    installation_pools: list[InstallationPoolOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_pool_output_model import InstallationPoolOutputModel

        installation_pools: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.installation_pools, Unset):
            installation_pools = []
            for installation_pools_item_data in self.installation_pools:
                installation_pools_item = installation_pools_item_data.to_dict()
                installation_pools.append(installation_pools_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if installation_pools is not UNSET:
            field_dict["installationPools"] = installation_pools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.installation_pool_output_model import InstallationPoolOutputModel

        d = dict(src_dict)
        _installation_pools = d.pop("installationPools", UNSET)
        installation_pools: list[InstallationPoolOutputModel] | Unset = UNSET
        if _installation_pools is not UNSET:
            installation_pools = []
            for installation_pools_item_data in _installation_pools:
                installation_pools_item = InstallationPoolOutputModel.from_dict(
                    installation_pools_item_data
                )

                installation_pools.append(installation_pools_item)

        installation_pool_output_list_model = cls(
            installation_pools=installation_pools,
        )

        installation_pool_output_list_model.additional_properties = d
        return installation_pool_output_list_model

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
