from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.instant_value_output_model import InstantValueOutputModel


T = TypeVar("T", bound="InstantValueOutputListModel")


@_attrs_define
class InstantValueOutputListModel:
    """
    Attributes:
        instant_values (list[InstantValueOutputModel] | None | Unset):
    """

    instant_values: list[InstantValueOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.instant_value_output_model import InstantValueOutputModel

        instant_values: list[dict[str, Any]] | None | Unset
        if isinstance(self.instant_values, Unset):
            instant_values = UNSET
        elif isinstance(self.instant_values, list):
            instant_values = []
            for instant_values_type_0_item_data in self.instant_values:
                instant_values_type_0_item = instant_values_type_0_item_data.to_dict()
                instant_values.append(instant_values_type_0_item)

        else:
            instant_values = self.instant_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instant_values is not UNSET:
            field_dict["instantValues"] = instant_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instant_value_output_model import InstantValueOutputModel

        d = dict(src_dict)

        def _parse_instant_values(data: object) -> list[InstantValueOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                instant_values_type_0 = []
                _instant_values_type_0 = data
                for instant_values_type_0_item_data in _instant_values_type_0:
                    instant_values_type_0_item = InstantValueOutputModel.from_dict(
                        instant_values_type_0_item_data
                    )

                    instant_values_type_0.append(instant_values_type_0_item)

                return instant_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InstantValueOutputModel] | None | Unset, data)

        instant_values = _parse_instant_values(d.pop("instantValues", UNSET))

        instant_value_output_list_model = cls(
            instant_values=instant_values,
        )

        instant_value_output_list_model.additional_properties = d
        return instant_value_output_list_model

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
