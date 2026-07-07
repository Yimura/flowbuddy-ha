from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.api_meter_output_model import ApiMeterOutputModel


T = TypeVar("T", bound="ApiMeterOutputListModel")


@_attrs_define
class ApiMeterOutputListModel:
    """
    Attributes:
        api_meters (list[ApiMeterOutputModel] | Unset):
    """

    api_meters: list[ApiMeterOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_meter_output_model import ApiMeterOutputModel

        api_meters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.api_meters, Unset):
            api_meters = []
            for api_meters_item_data in self.api_meters:
                api_meters_item = api_meters_item_data.to_dict()
                api_meters.append(api_meters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_meters is not UNSET:
            field_dict["apiMeters"] = api_meters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_meter_output_model import ApiMeterOutputModel

        d = dict(src_dict)
        _api_meters = d.pop("apiMeters", UNSET)
        api_meters: list[ApiMeterOutputModel] | Unset = UNSET
        if _api_meters is not UNSET:
            api_meters = []
            for api_meters_item_data in _api_meters:
                api_meters_item = ApiMeterOutputModel.from_dict(api_meters_item_data)

                api_meters.append(api_meters_item)

        api_meter_output_list_model = cls(
            api_meters=api_meters,
        )

        api_meter_output_list_model.additional_properties = d
        return api_meter_output_list_model

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
