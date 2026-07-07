from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.installation_type_output_model import InstallationTypeOutputModel


T = TypeVar("T", bound="InstallationTypeOutputListModel")


@_attrs_define
class InstallationTypeOutputListModel:
    """
    Attributes:
        installation_types (list[InstallationTypeOutputModel] | None | Unset):
    """

    installation_types: list[InstallationTypeOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_type_output_model import InstallationTypeOutputModel

        installation_types: list[dict[str, Any]] | None | Unset
        if isinstance(self.installation_types, Unset):
            installation_types = UNSET
        elif isinstance(self.installation_types, list):
            installation_types = []
            for installation_types_type_0_item_data in self.installation_types:
                installation_types_type_0_item = installation_types_type_0_item_data.to_dict()
                installation_types.append(installation_types_type_0_item)

        else:
            installation_types = self.installation_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if installation_types is not UNSET:
            field_dict["installationTypes"] = installation_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.installation_type_output_model import InstallationTypeOutputModel

        d = dict(src_dict)

        def _parse_installation_types(
            data: object,
        ) -> list[InstallationTypeOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                installation_types_type_0 = []
                _installation_types_type_0 = data
                for installation_types_type_0_item_data in _installation_types_type_0:
                    installation_types_type_0_item = InstallationTypeOutputModel.from_dict(
                        installation_types_type_0_item_data
                    )

                    installation_types_type_0.append(installation_types_type_0_item)

                return installation_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InstallationTypeOutputModel] | None | Unset, data)

        installation_types = _parse_installation_types(d.pop("installationTypes", UNSET))

        installation_type_output_list_model = cls(
            installation_types=installation_types,
        )

        installation_type_output_list_model.additional_properties = d
        return installation_type_output_list_model

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
