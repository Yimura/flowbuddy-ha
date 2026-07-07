from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.battery_output_model import BatteryOutputModel


T = TypeVar("T", bound="BatteryOutputListModel")


@_attrs_define
class BatteryOutputListModel:
    """
    Attributes:
        batteries (list[BatteryOutputModel] | Unset):
    """

    batteries: list[BatteryOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.battery_output_model import BatteryOutputModel

        batteries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.batteries, Unset):
            batteries = []
            for batteries_item_data in self.batteries:
                batteries_item = batteries_item_data.to_dict()
                batteries.append(batteries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batteries is not UNSET:
            field_dict["batteries"] = batteries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.battery_output_model import BatteryOutputModel

        d = dict(src_dict)
        _batteries = d.pop("batteries", UNSET)
        batteries: list[BatteryOutputModel] | Unset = UNSET
        if _batteries is not UNSET:
            batteries = []
            for batteries_item_data in _batteries:
                batteries_item = BatteryOutputModel.from_dict(batteries_item_data)

                batteries.append(batteries_item)

        battery_output_list_model = cls(
            batteries=batteries,
        )

        battery_output_list_model.additional_properties = d
        return battery_output_list_model

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
