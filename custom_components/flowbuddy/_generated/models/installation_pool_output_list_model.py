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
        installation_pools (list[InstallationPoolOutputModel] | None | Unset):
    """

    installation_pools: list[InstallationPoolOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_pool_output_model import InstallationPoolOutputModel

        installation_pools: list[dict[str, Any]] | None | Unset
        if isinstance(self.installation_pools, Unset):
            installation_pools = UNSET
        elif isinstance(self.installation_pools, list):
            installation_pools = []
            for installation_pools_type_0_item_data in self.installation_pools:
                installation_pools_type_0_item = installation_pools_type_0_item_data.to_dict()
                installation_pools.append(installation_pools_type_0_item)

        else:
            installation_pools = self.installation_pools

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

        def _parse_installation_pools(
            data: object,
        ) -> list[InstallationPoolOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                installation_pools_type_0 = []
                _installation_pools_type_0 = data
                for installation_pools_type_0_item_data in _installation_pools_type_0:
                    installation_pools_type_0_item = InstallationPoolOutputModel.from_dict(
                        installation_pools_type_0_item_data
                    )

                    installation_pools_type_0.append(installation_pools_type_0_item)

                return installation_pools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InstallationPoolOutputModel] | None | Unset, data)

        installation_pools = _parse_installation_pools(d.pop("installationPools", UNSET))

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
