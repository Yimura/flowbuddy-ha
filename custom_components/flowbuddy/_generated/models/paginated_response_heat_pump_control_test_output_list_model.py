from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.heat_pump_control_test_output_list_model import HeatPumpControlTestOutputListModel
    from ..models.links_model import LinksModel
    from ..models.page_model import PageModel


T = TypeVar("T", bound="PaginatedResponseHeatPumpControlTestOutputListModel")


@_attrs_define
class PaginatedResponseHeatPumpControlTestOutputListModel:
    """
    Attributes:
        field_embedded (HeatPumpControlTestOutputListModel | Unset):
        field_links (LinksModel | Unset):
        field_page (PageModel | Unset):
    """

    field_embedded: HeatPumpControlTestOutputListModel | Unset = UNSET
    field_links: LinksModel | Unset = UNSET
    field_page: PageModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.heat_pump_control_test_output_list_model import (
            HeatPumpControlTestOutputListModel,
        )
        from ..models.links_model import LinksModel
        from ..models.page_model import PageModel

        field_embedded: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_page: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_page, Unset):
            field_page = self.field_page.to_dict()

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
        from ..models.heat_pump_control_test_output_list_model import (
            HeatPumpControlTestOutputListModel,
        )
        from ..models.links_model import LinksModel
        from ..models.page_model import PageModel

        d = dict(src_dict)
        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: HeatPumpControlTestOutputListModel | Unset
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = HeatPumpControlTestOutputListModel.from_dict(_field_embedded)

        _field_links = d.pop("_links", UNSET)
        field_links: LinksModel | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = LinksModel.from_dict(_field_links)

        _field_page = d.pop("_page", UNSET)
        field_page: PageModel | Unset
        if isinstance(_field_page, Unset):
            field_page = UNSET
        else:
            field_page = PageModel.from_dict(_field_page)

        paginated_response_heat_pump_control_test_output_list_model = cls(
            field_embedded=field_embedded,
            field_links=field_links,
            field_page=field_page,
        )

        paginated_response_heat_pump_control_test_output_list_model.additional_properties = d
        return paginated_response_heat_pump_control_test_output_list_model

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
