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
        self_ (HrefModel | None | Unset):
        first (HrefModel | None | Unset):
        last (HrefModel | None | Unset):
        prev (HrefModel | None | Unset):
        next_ (HrefModel | None | Unset):
    """

    self_: HrefModel | None | Unset = UNSET
    first: HrefModel | None | Unset = UNSET
    last: HrefModel | None | Unset = UNSET
    prev: HrefModel | None | Unset = UNSET
    next_: HrefModel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.href_model import HrefModel

        self_: dict[str, Any] | None | Unset
        if isinstance(self.self_, Unset):
            self_ = UNSET
        elif isinstance(self.self_, HrefModel):
            self_ = self.self_.to_dict()
        else:
            self_ = self.self_

        first: dict[str, Any] | None | Unset
        if isinstance(self.first, Unset):
            first = UNSET
        elif isinstance(self.first, HrefModel):
            first = self.first.to_dict()
        else:
            first = self.first

        last: dict[str, Any] | None | Unset
        if isinstance(self.last, Unset):
            last = UNSET
        elif isinstance(self.last, HrefModel):
            last = self.last.to_dict()
        else:
            last = self.last

        prev: dict[str, Any] | None | Unset
        if isinstance(self.prev, Unset):
            prev = UNSET
        elif isinstance(self.prev, HrefModel):
            prev = self.prev.to_dict()
        else:
            prev = self.prev

        next_: dict[str, Any] | None | Unset
        if isinstance(self.next_, Unset):
            next_ = UNSET
        elif isinstance(self.next_, HrefModel):
            next_ = self.next_.to_dict()
        else:
            next_ = self.next_

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

        def _parse_self_(data: object) -> HrefModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                self_type_1 = HrefModel.from_dict(data)

                return self_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HrefModel | None | Unset, data)

        self_ = _parse_self_(d.pop("self", UNSET))

        def _parse_first(data: object) -> HrefModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                first_type_1 = HrefModel.from_dict(data)

                return first_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HrefModel | None | Unset, data)

        first = _parse_first(d.pop("first", UNSET))

        def _parse_last(data: object) -> HrefModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_type_1 = HrefModel.from_dict(data)

                return last_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HrefModel | None | Unset, data)

        last = _parse_last(d.pop("last", UNSET))

        def _parse_prev(data: object) -> HrefModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                prev_type_1 = HrefModel.from_dict(data)

                return prev_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HrefModel | None | Unset, data)

        prev = _parse_prev(d.pop("prev", UNSET))

        def _parse_next_(data: object) -> HrefModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                next_type_1 = HrefModel.from_dict(data)

                return next_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HrefModel | None | Unset, data)

        next_ = _parse_next_(d.pop("next", UNSET))

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
