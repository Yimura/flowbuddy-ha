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
        layouts (list[LayoutOutputModel] | None | Unset):
    """

    layouts: list[LayoutOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.layout_output_model import LayoutOutputModel

        layouts: list[dict[str, Any]] | None | Unset
        if isinstance(self.layouts, Unset):
            layouts = UNSET
        elif isinstance(self.layouts, list):
            layouts = []
            for layouts_type_0_item_data in self.layouts:
                layouts_type_0_item = layouts_type_0_item_data.to_dict()
                layouts.append(layouts_type_0_item)

        else:
            layouts = self.layouts

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

        def _parse_layouts(data: object) -> list[LayoutOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                layouts_type_0 = []
                _layouts_type_0 = data
                for layouts_type_0_item_data in _layouts_type_0:
                    layouts_type_0_item = LayoutOutputModel.from_dict(layouts_type_0_item_data)

                    layouts_type_0.append(layouts_type_0_item)

                return layouts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LayoutOutputModel] | None | Unset, data)

        layouts = _parse_layouts(d.pop("layouts", UNSET))

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
