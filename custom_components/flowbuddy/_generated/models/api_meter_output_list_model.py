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
        api_meters (list[ApiMeterOutputModel] | None | Unset):
    """

    api_meters: list[ApiMeterOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_meter_output_model import ApiMeterOutputModel

        api_meters: list[dict[str, Any]] | None | Unset
        if isinstance(self.api_meters, Unset):
            api_meters = UNSET
        elif isinstance(self.api_meters, list):
            api_meters = []
            for api_meters_type_0_item_data in self.api_meters:
                api_meters_type_0_item = api_meters_type_0_item_data.to_dict()
                api_meters.append(api_meters_type_0_item)

        else:
            api_meters = self.api_meters

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

        def _parse_api_meters(data: object) -> list[ApiMeterOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                api_meters_type_0 = []
                _api_meters_type_0 = data
                for api_meters_type_0_item_data in _api_meters_type_0:
                    api_meters_type_0_item = ApiMeterOutputModel.from_dict(
                        api_meters_type_0_item_data
                    )

                    api_meters_type_0.append(api_meters_type_0_item)

                return api_meters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ApiMeterOutputModel] | None | Unset, data)

        api_meters = _parse_api_meters(d.pop("apiMeters", UNSET))

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
