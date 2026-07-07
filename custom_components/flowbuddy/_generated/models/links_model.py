from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.href_model import HrefModel


T = TypeVar("T", bound="LinksModel")


@_attrs_define
class LinksModel:
    """
    Attributes:
        self_ (HrefModel | Unset):
        first (HrefModel | Unset):
        last (HrefModel | Unset):
        prev (HrefModel | Unset):
        next_ (HrefModel | Unset):
    """

    self_: HrefModel | Unset = UNSET
    first: HrefModel | Unset = UNSET
    last: HrefModel | Unset = UNSET
    prev: HrefModel | Unset = UNSET
    next_: HrefModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.href_model import HrefModel

        self_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        first: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first, Unset):
            first = self.first.to_dict()

        last: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last, Unset):
            last = self.last.to_dict()

        prev: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prev, Unset):
            prev = self.prev.to_dict()

        next_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_, Unset):
            next_ = self.next_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if first is not UNSET:
            field_dict["first"] = first
        if last is not UNSET:
            field_dict["last"] = last
        if prev is not UNSET:
            field_dict["prev"] = prev
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.href_model import HrefModel

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: HrefModel | Unset
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = HrefModel.from_dict(_self_)

        _first = d.pop("first", UNSET)
        first: HrefModel | Unset
        if isinstance(_first, Unset):
            first = UNSET
        else:
            first = HrefModel.from_dict(_first)

        _last = d.pop("last", UNSET)
        last: HrefModel | Unset
        if isinstance(_last, Unset):
            last = UNSET
        else:
            last = HrefModel.from_dict(_last)

        _prev = d.pop("prev", UNSET)
        prev: HrefModel | Unset
        if isinstance(_prev, Unset):
            prev = UNSET
        else:
            prev = HrefModel.from_dict(_prev)

        _next_ = d.pop("next", UNSET)
        next_: HrefModel | Unset
        if isinstance(_next_, Unset):
            next_ = UNSET
        else:
            next_ = HrefModel.from_dict(_next_)

        links_model = cls(
            self_=self_,
            first=first,
            last=last,
            prev=prev,
            next_=next_,
        )

        links_model.additional_properties = d
        return links_model

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
