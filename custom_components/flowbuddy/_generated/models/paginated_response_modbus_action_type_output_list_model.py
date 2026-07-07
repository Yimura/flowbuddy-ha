from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.links_model import LinksModel
    from ..models.modbus_action_type_output_list_model import ModbusActionTypeOutputListModel
    from ..models.page_model import PageModel


T = TypeVar("T", bound="PaginatedResponseModbusActionTypeOutputListModel")


@_attrs_define
class PaginatedResponseModbusActionTypeOutputListModel:
    """
    Attributes:
        field_embedded (ModbusActionTypeOutputListModel | None | Unset):
        field_links (LinksModel | None | Unset):
        field_page (None | PageModel | Unset):
    """

    field_embedded: ModbusActionTypeOutputListModel | None | Unset = UNSET
    field_links: LinksModel | None | Unset = UNSET
    field_page: None | PageModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_model import LinksModel
        from ..models.modbus_action_type_output_list_model import ModbusActionTypeOutputListModel
        from ..models.page_model import PageModel

        field_embedded: dict[str, Any] | None | Unset
        if isinstance(self.field_embedded, Unset):
            field_embedded = UNSET
        elif isinstance(self.field_embedded, ModbusActionTypeOutputListModel):
            field_embedded = self.field_embedded.to_dict()
        else:
            field_embedded = self.field_embedded

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksModel):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_page: dict[str, Any] | None | Unset
        if isinstance(self.field_page, Unset):
            field_page = UNSET
        elif isinstance(self.field_page, PageModel):
            field_page = self.field_page.to_dict()
        else:
            field_page = self.field_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_page is not UNSET:
            field_dict["_page"] = field_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_model import LinksModel
        from ..models.modbus_action_type_output_list_model import ModbusActionTypeOutputListModel
        from ..models.page_model import PageModel

        d = dict(src_dict)

        def _parse_field_embedded(data: object) -> ModbusActionTypeOutputListModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_embedded_type_1 = ModbusActionTypeOutputListModel.from_dict(data)

                return field_embedded_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModbusActionTypeOutputListModel | None | Unset, data)

        field_embedded = _parse_field_embedded(d.pop("_embedded", UNSET))

        def _parse_field_links(data: object) -> LinksModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_links_type_1 = LinksModel.from_dict(data)

                return field_links_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinksModel | None | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        def _parse_field_page(data: object) -> None | PageModel | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_page_type_1 = PageModel.from_dict(data)

                return field_page_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PageModel | Unset, data)

        field_page = _parse_field_page(d.pop("_page", UNSET))

        paginated_response_modbus_action_type_output_list_model = cls(
            field_embedded=field_embedded,
            field_links=field_links,
            field_page=field_page,
        )

        paginated_response_modbus_action_type_output_list_model.additional_properties = d
        return paginated_response_modbus_action_type_output_list_model

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
