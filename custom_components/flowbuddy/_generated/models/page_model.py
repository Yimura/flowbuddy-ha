from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="PageModel")


@_attrs_define
class PageModel:
    """
    Attributes:
        size (int | Unset):
        total_elements (int | Unset):
        total_pages (int | Unset):
        number (int | Unset):
    """

    size: int | Unset = UNSET
    total_elements: int | Unset = UNSET
    total_pages: int | Unset = UNSET
    number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        size = self.size

        total_elements = self.total_elements

        total_pages = self.total_pages

        number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if size is not UNSET:
            field_dict["size"] = size
        if total_elements is not UNSET:
            field_dict["totalElements"] = total_elements
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        size = d.pop("size", UNSET)

        total_elements = d.pop("totalElements", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        number = d.pop("number", UNSET)

        page_model = cls(
            size=size,
            total_elements=total_elements,
            total_pages=total_pages,
            number=number,
        )

        page_model.additional_properties = d
        return page_model

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
