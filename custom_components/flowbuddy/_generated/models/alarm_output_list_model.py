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
        alarms (list[AlarmOutputModel] | None | Unset):
    """

    alarms: list[AlarmOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alarm_output_model import AlarmOutputModel

        alarms: list[dict[str, Any]] | None | Unset
        if isinstance(self.alarms, Unset):
            alarms = UNSET
        elif isinstance(self.alarms, list):
            alarms = []
            for alarms_type_0_item_data in self.alarms:
                alarms_type_0_item = alarms_type_0_item_data.to_dict()
                alarms.append(alarms_type_0_item)

        else:
            alarms = self.alarms

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

        def _parse_alarms(data: object) -> list[AlarmOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alarms_type_0 = []
                _alarms_type_0 = data
                for alarms_type_0_item_data in _alarms_type_0:
                    alarms_type_0_item = AlarmOutputModel.from_dict(alarms_type_0_item_data)

                    alarms_type_0.append(alarms_type_0_item)

                return alarms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AlarmOutputModel] | None | Unset, data)

        alarms = _parse_alarms(d.pop("alarms", UNSET))

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
