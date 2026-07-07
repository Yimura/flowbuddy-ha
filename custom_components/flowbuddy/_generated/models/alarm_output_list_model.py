from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.alarm_output_model import AlarmOutputModel


T = TypeVar("T", bound="AlarmOutputListModel")


@_attrs_define
class AlarmOutputListModel:
    """
    Attributes:
        alarms (list[AlarmOutputModel] | Unset):
    """

    alarms: list[AlarmOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alarm_output_model import AlarmOutputModel

        alarms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alarms, Unset):
            alarms = []
            for alarms_item_data in self.alarms:
                alarms_item = alarms_item_data.to_dict()
                alarms.append(alarms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alarms is not UNSET:
            field_dict["alarms"] = alarms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alarm_output_model import AlarmOutputModel

        d = dict(src_dict)
        _alarms = d.pop("alarms", UNSET)
        alarms: list[AlarmOutputModel] | Unset = UNSET
        if _alarms is not UNSET:
            alarms = []
            for alarms_item_data in _alarms:
                alarms_item = AlarmOutputModel.from_dict(alarms_item_data)

                alarms.append(alarms_item)

        alarm_output_list_model = cls(
            alarms=alarms,
        )

        alarm_output_list_model.additional_properties = d
        return alarm_output_list_model

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
