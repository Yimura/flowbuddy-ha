from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.inverter_output_model import InverterOutputModel


T = TypeVar("T", bound="InverterOutputListModel")


@_attrs_define
class InverterOutputListModel:
    """
    Attributes:
        inverters (list[InverterOutputModel] | Unset):
    """

    inverters: list[InverterOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.inverter_output_model import InverterOutputModel

        inverters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inverters, Unset):
            inverters = []
            for inverters_item_data in self.inverters:
                inverters_item = inverters_item_data.to_dict()
                inverters.append(inverters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inverters is not UNSET:
            field_dict["inverters"] = inverters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inverter_output_model import InverterOutputModel

        d = dict(src_dict)
        _inverters = d.pop("inverters", UNSET)
        inverters: list[InverterOutputModel] | Unset = UNSET
        if _inverters is not UNSET:
            inverters = []
            for inverters_item_data in _inverters:
                inverters_item = InverterOutputModel.from_dict(inverters_item_data)

                inverters.append(inverters_item)

        inverter_output_list_model = cls(
            inverters=inverters,
        )

        inverter_output_list_model.additional_properties = d
        return inverter_output_list_model

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
