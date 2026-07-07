from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.api_meter_type_output_model import ApiMeterTypeOutputModel


T = TypeVar("T", bound="ApiMeterTypeOutputListModel")


@_attrs_define
class ApiMeterTypeOutputListModel:
    """
    Attributes:
        api_meter_types (list[ApiMeterTypeOutputModel] | None | Unset):
    """

    api_meter_types: list[ApiMeterTypeOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_meter_type_output_model import ApiMeterTypeOutputModel

        api_meter_types: list[dict[str, Any]] | None | Unset
        if isinstance(self.api_meter_types, Unset):
            api_meter_types = UNSET
        elif isinstance(self.api_meter_types, list):
            api_meter_types = []
            for api_meter_types_type_0_item_data in self.api_meter_types:
                api_meter_types_type_0_item = api_meter_types_type_0_item_data.to_dict()
                api_meter_types.append(api_meter_types_type_0_item)

        else:
            api_meter_types = self.api_meter_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_meter_types is not UNSET:
            field_dict["apiMeterTypes"] = api_meter_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_meter_type_output_model import ApiMeterTypeOutputModel

        d = dict(src_dict)

        def _parse_api_meter_types(data: object) -> list[ApiMeterTypeOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                api_meter_types_type_0 = []
                _api_meter_types_type_0 = data
                for api_meter_types_type_0_item_data in _api_meter_types_type_0:
                    api_meter_types_type_0_item = ApiMeterTypeOutputModel.from_dict(
                        api_meter_types_type_0_item_data
                    )

                    api_meter_types_type_0.append(api_meter_types_type_0_item)

                return api_meter_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ApiMeterTypeOutputModel] | None | Unset, data)

        api_meter_types = _parse_api_meter_types(d.pop("apiMeterTypes", UNSET))

        api_meter_type_output_list_model = cls(
            api_meter_types=api_meter_types,
        )

        api_meter_type_output_list_model.additional_properties = d
        return api_meter_type_output_list_model

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
