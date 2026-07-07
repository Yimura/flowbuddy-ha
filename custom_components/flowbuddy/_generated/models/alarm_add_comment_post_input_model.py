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
    from ..models.alarm_add_comment_post_input_model_other_properties import (
        AlarmAddCommentPostInputModelOtherProperties,
    )


T = TypeVar("T", bound="AlarmAddCommentPostInputModel")


@_attrs_define
class AlarmAddCommentPostInputModel:
    """
    Attributes:
        type_ (str | Unset): The type of comment you want to add
        new_comment (str | Unset): The comment to add
        date (datetime.datetime | None | Unset): The date on which is logically coupled to the Comment
        other_properties (AlarmAddCommentPostInputModelOtherProperties | Unset):
    """

    type_: str | Unset = UNSET
    new_comment: str | Unset = UNSET
    date: datetime.datetime | None | Unset = UNSET
    other_properties: AlarmAddCommentPostInputModelOtherProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alarm_add_comment_post_input_model_other_properties import (
            AlarmAddCommentPostInputModelOtherProperties,
        )

        type_ = self.type_

        new_comment = self.new_comment

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        other_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_properties, Unset):
            other_properties = self.other_properties.to_dict()

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
        from ..models.alarm_add_comment_post_input_model_other_properties import (
            AlarmAddCommentPostInputModelOtherProperties,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        new_comment = d.pop("newComment", UNSET)

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

        _other_properties = d.pop("otherProperties", UNSET)
        other_properties: AlarmAddCommentPostInputModelOtherProperties | Unset
        if isinstance(_other_properties, Unset):
            other_properties = UNSET
        else:
            other_properties = AlarmAddCommentPostInputModelOtherProperties.from_dict(
                _other_properties
            )

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
