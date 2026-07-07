from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.meter_output_model import MeterOutputModel


T = TypeVar("T", bound="MeterOutputListModel")


@_attrs_define
class MeterOutputListModel:
    """
    Attributes:
        meters (list[MeterOutputModel] | Unset):
    """

    meters: list[MeterOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meter_output_model import MeterOutputModel

        meters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.meters, Unset):
            meters = []
            for meters_item_data in self.meters:
                meters_item = meters_item_data.to_dict()
                meters.append(meters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meters is not UNSET:
            field_dict["meters"] = meters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meter_output_model import MeterOutputModel

        d = dict(src_dict)
        _meters = d.pop("meters", UNSET)
        meters: list[MeterOutputModel] | Unset = UNSET
        if _meters is not UNSET:
            meters = []
            for meters_item_data in _meters:
                meters_item = MeterOutputModel.from_dict(meters_item_data)

                meters.append(meters_item)

        meter_output_list_model = cls(
            meters=meters,
        )

        meter_output_list_model.additional_properties = d
        return meter_output_list_model

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
