from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.installation_output_model import InstallationOutputModel


T = TypeVar("T", bound="InstallationOutputListModel")


@_attrs_define
class InstallationOutputListModel:
    """
    Attributes:
        installations (list[InstallationOutputModel] | None | Unset):
    """

    installations: list[InstallationOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_output_model import InstallationOutputModel

        installations: list[dict[str, Any]] | None | Unset
        if isinstance(self.installations, Unset):
            installations = UNSET
        elif isinstance(self.installations, list):
            installations = []
            for installations_type_0_item_data in self.installations:
                installations_type_0_item = installations_type_0_item_data.to_dict()
                installations.append(installations_type_0_item)

        else:
            installations = self.installations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if installations is not UNSET:
            field_dict["installations"] = installations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.installation_output_model import InstallationOutputModel

        d = dict(src_dict)

        def _parse_installations(data: object) -> list[InstallationOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                installations_type_0 = []
                _installations_type_0 = data
                for installations_type_0_item_data in _installations_type_0:
                    installations_type_0_item = InstallationOutputModel.from_dict(
                        installations_type_0_item_data
                    )

                    installations_type_0.append(installations_type_0_item)

                return installations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InstallationOutputModel] | None | Unset, data)

        installations = _parse_installations(d.pop("installations", UNSET))

        installation_output_list_model = cls(
            installations=installations,
        )

        installation_output_list_model.additional_properties = d
        return installation_output_list_model

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
