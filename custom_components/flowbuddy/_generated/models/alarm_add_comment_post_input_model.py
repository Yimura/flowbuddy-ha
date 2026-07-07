from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.alarm_add_comment_post_input_model_other_properties_type_0 import (
        AlarmAddCommentPostInputModelOtherPropertiesType0,
    )


T = TypeVar("T", bound="AlarmAddCommentPostInputModel")


@_attrs_define
class AlarmAddCommentPostInputModel:
    """
    Attributes:
        type_ (None | str | Unset): The type of comment you want to add
        new_comment (None | str | Unset): The comment to add
        date (datetime.datetime | None | Unset): The date on which is logically coupled to the Comment
        other_properties (AlarmAddCommentPostInputModelOtherPropertiesType0 | None | Unset):
    """

    type_: None | str | Unset = UNSET
    new_comment: None | str | Unset = UNSET
    date: datetime.datetime | None | Unset = UNSET
    other_properties: AlarmAddCommentPostInputModelOtherPropertiesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alarm_add_comment_post_input_model_other_properties_type_0 import (
            AlarmAddCommentPostInputModelOtherPropertiesType0,
        )

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        new_comment: None | str | Unset
        if isinstance(self.new_comment, Unset):
            new_comment = UNSET
        else:
            new_comment = self.new_comment

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        other_properties: dict[str, Any] | None | Unset
        if isinstance(self.other_properties, Unset):
            other_properties = UNSET
        elif isinstance(self.other_properties, AlarmAddCommentPostInputModelOtherPropertiesType0):
            other_properties = self.other_properties.to_dict()
        else:
            other_properties = self.other_properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if new_comment is not UNSET:
            field_dict["newComment"] = new_comment
        if date is not UNSET:
            field_dict["date"] = date
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alarm_add_comment_post_input_model_other_properties_type_0 import (
            AlarmAddCommentPostInputModelOtherPropertiesType0,
        )

        d = dict(src_dict)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_new_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_comment = _parse_new_comment(d.pop("newComment", UNSET))

        def _parse_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = datetime.datetime.fromisoformat(data)

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_other_properties(
            data: object,
        ) -> AlarmAddCommentPostInputModelOtherPropertiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_properties_type_0 = (
                    AlarmAddCommentPostInputModelOtherPropertiesType0.from_dict(data)
                )

                return other_properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlarmAddCommentPostInputModelOtherPropertiesType0 | None | Unset, data)

        other_properties = _parse_other_properties(d.pop("otherProperties", UNSET))

        alarm_add_comment_post_input_model = cls(
            type_=type_,
            new_comment=new_comment,
            date=date,
            other_properties=other_properties,
        )

        alarm_add_comment_post_input_model.additional_properties = d
        return alarm_add_comment_post_input_model

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
