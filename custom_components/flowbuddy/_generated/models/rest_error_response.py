from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.rest_error_response_extra_info import RestErrorResponseExtraInfo


T = TypeVar("T", bound="RestErrorResponse")


@_attrs_define
class RestErrorResponse:
    """
    Attributes:
        type_ (str | Unset):
        title (str | Unset):
        status (int | Unset):
        identifier (str | Unset):
        code (str | Unset):
        extra_info (RestErrorResponseExtraInfo | Unset):
    """

    type_: str | Unset = UNSET
    title: str | Unset = UNSET
    status: int | Unset = UNSET
    identifier: str | Unset = UNSET
    code: str | Unset = UNSET
    extra_info: RestErrorResponseExtraInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_error_response_extra_info import RestErrorResponseExtraInfo

        type_ = self.type_

        title = self.title

        status = self.status

        identifier = self.identifier

        code = self.code

        extra_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra_info, Unset):
            extra_info = self.extra_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if code is not UNSET:
            field_dict["code"] = code
        if extra_info is not UNSET:
            field_dict["extraInfo"] = extra_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_error_response_extra_info import RestErrorResponseExtraInfo

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        title = d.pop("title", UNSET)

        status = d.pop("status", UNSET)

        identifier = d.pop("identifier", UNSET)

        code = d.pop("code", UNSET)

        _extra_info = d.pop("extraInfo", UNSET)
        extra_info: RestErrorResponseExtraInfo | Unset
        if isinstance(_extra_info, Unset):
            extra_info = UNSET
        else:
            extra_info = RestErrorResponseExtraInfo.from_dict(_extra_info)

        rest_error_response = cls(
            type_=type_,
            title=title,
            status=status,
            identifier=identifier,
            code=code,
            extra_info=extra_info,
        )

        rest_error_response.additional_properties = d
        return rest_error_response

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
