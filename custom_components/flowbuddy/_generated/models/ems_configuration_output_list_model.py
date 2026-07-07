from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.ems_configuration_output_model import EmsConfigurationOutputModel


T = TypeVar("T", bound="EmsConfigurationOutputListModel")


@_attrs_define
class EmsConfigurationOutputListModel:
    """
    Attributes:
        ems_configurations (list[EmsConfigurationOutputModel] | Unset):
    """

    ems_configurations: list[EmsConfigurationOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ems_configuration_output_model import EmsConfigurationOutputModel

        ems_configurations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ems_configurations, Unset):
            ems_configurations = []
            for ems_configurations_item_data in self.ems_configurations:
                ems_configurations_item = ems_configurations_item_data.to_dict()
                ems_configurations.append(ems_configurations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ems_configurations is not UNSET:
            field_dict["emsConfigurations"] = ems_configurations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ems_configuration_output_model import EmsConfigurationOutputModel

        d = dict(src_dict)
        _ems_configurations = d.pop("emsConfigurations", UNSET)
        ems_configurations: list[EmsConfigurationOutputModel] | Unset = UNSET
        if _ems_configurations is not UNSET:
            ems_configurations = []
            for ems_configurations_item_data in _ems_configurations:
                ems_configurations_item = EmsConfigurationOutputModel.from_dict(
                    ems_configurations_item_data
                )

                ems_configurations.append(ems_configurations_item)

        ems_configuration_output_list_model = cls(
            ems_configurations=ems_configurations,
        )

        ems_configuration_output_list_model.additional_properties = d
        return ems_configuration_output_list_model

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
