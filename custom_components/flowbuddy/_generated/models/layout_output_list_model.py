from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.layout_output_model import LayoutOutputModel


T = TypeVar("T", bound="LayoutOutputListModel")


@_attrs_define
class LayoutOutputListModel:
    """
    Attributes:
        layouts (list[LayoutOutputModel] | Unset):
    """

    layouts: list[LayoutOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.layout_output_model import LayoutOutputModel

        layouts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.layouts, Unset):
            layouts = []
            for layouts_item_data in self.layouts:
                layouts_item = layouts_item_data.to_dict()
                layouts.append(layouts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if layouts is not UNSET:
            field_dict["layouts"] = layouts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.layout_output_model import LayoutOutputModel

        d = dict(src_dict)
        _layouts = d.pop("layouts", UNSET)
        layouts: list[LayoutOutputModel] | Unset = UNSET
        if _layouts is not UNSET:
            layouts = []
            for layouts_item_data in _layouts:
                layouts_item = LayoutOutputModel.from_dict(layouts_item_data)

                layouts.append(layouts_item)

        layout_output_list_model = cls(
            layouts=layouts,
        )

        layout_output_list_model.additional_properties = d
        return layout_output_list_model

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
