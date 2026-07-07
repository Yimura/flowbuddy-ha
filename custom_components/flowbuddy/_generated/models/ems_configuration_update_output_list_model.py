from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.ems_configuration_update_output_model import EmsConfigurationUpdateOutputModel


T = TypeVar("T", bound="EmsConfigurationUpdateOutputListModel")


@_attrs_define
class EmsConfigurationUpdateOutputListModel:
    """
    Attributes:
        ems_configuration_updates (list[EmsConfigurationUpdateOutputModel] | None | Unset):
    """

    ems_configuration_updates: list[EmsConfigurationUpdateOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ems_configuration_update_output_model import EmsConfigurationUpdateOutputModel

        ems_configuration_updates: list[dict[str, Any]] | None | Unset
        if isinstance(self.ems_configuration_updates, Unset):
            ems_configuration_updates = UNSET
        elif isinstance(self.ems_configuration_updates, list):
            ems_configuration_updates = []
            for ems_configuration_updates_type_0_item_data in self.ems_configuration_updates:
                ems_configuration_updates_type_0_item = (
                    ems_configuration_updates_type_0_item_data.to_dict()
                )
                ems_configuration_updates.append(ems_configuration_updates_type_0_item)

        else:
            ems_configuration_updates = self.ems_configuration_updates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ems_configuration_updates is not UNSET:
            field_dict["emsConfigurationUpdates"] = ems_configuration_updates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ems_configuration_update_output_model import EmsConfigurationUpdateOutputModel

        d = dict(src_dict)

        def _parse_ems_configuration_updates(
            data: object,
        ) -> list[EmsConfigurationUpdateOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ems_configuration_updates_type_0 = []
                _ems_configuration_updates_type_0 = data
                for ems_configuration_updates_type_0_item_data in _ems_configuration_updates_type_0:
                    ems_configuration_updates_type_0_item = (
                        EmsConfigurationUpdateOutputModel.from_dict(
                            ems_configuration_updates_type_0_item_data
                        )
                    )

                    ems_configuration_updates_type_0.append(ems_configuration_updates_type_0_item)

                return ems_configuration_updates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EmsConfigurationUpdateOutputModel] | None | Unset, data)

        ems_configuration_updates = _parse_ems_configuration_updates(
            d.pop("emsConfigurationUpdates", UNSET)
        )

        ems_configuration_update_output_list_model = cls(
            ems_configuration_updates=ems_configuration_updates,
        )

        ems_configuration_update_output_list_model.additional_properties = d
        return ems_configuration_update_output_list_model

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
