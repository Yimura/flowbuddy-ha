from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.rest_error_response_extra_info_type_0 import RestErrorResponseExtraInfoType0


T = TypeVar("T", bound="RestErrorResponse")


@_attrs_define
class RestErrorResponse:
    """
    Attributes:
        type_ (None | str | Unset):
        title (None | str | Unset):
        status (int | None | Unset):
        identifier (None | str | Unset):
        code (None | str | Unset):
        extra_info (None | RestErrorResponseExtraInfoType0 | Unset):
    """

    type_: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    status: int | None | Unset = UNSET
    identifier: None | str | Unset = UNSET
    code: None | str | Unset = UNSET
    extra_info: None | RestErrorResponseExtraInfoType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_error_response_extra_info_type_0 import RestErrorResponseExtraInfoType0

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        status: int | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        identifier: None | str | Unset
        if isinstance(self.identifier, Unset):
            identifier = UNSET
        else:
            identifier = self.identifier

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        extra_info: dict[str, Any] | None | Unset
        if isinstance(self.extra_info, Unset):
            extra_info = UNSET
        elif isinstance(self.extra_info, RestErrorResponseExtraInfoType0):
            extra_info = self.extra_info.to_dict()
        else:
            extra_info = self.extra_info

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
        from ..models.rest_error_response_extra_info_type_0 import RestErrorResponseExtraInfoType0

        d = dict(src_dict)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identifier = _parse_identifier(d.pop("identifier", UNSET))

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_extra_info(data: object) -> None | RestErrorResponseExtraInfoType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_info_type_0 = RestErrorResponseExtraInfoType0.from_dict(data)

                return extra_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RestErrorResponseExtraInfoType0 | Unset, data)

        extra_info = _parse_extra_info(d.pop("extraInfo", UNSET))

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
