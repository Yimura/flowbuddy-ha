from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.event_type_output_model import EventTypeOutputModel


T = TypeVar("T", bound="EventTypeOutputListModel")


@_attrs_define
class EventTypeOutputListModel:
    """
    Attributes:
        event_types (list[EventTypeOutputModel] | None | Unset):
    """

    event_types: list[EventTypeOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_type_output_model import EventTypeOutputModel

        event_types: list[dict[str, Any]] | None | Unset
        if isinstance(self.event_types, Unset):
            event_types = UNSET
        elif isinstance(self.event_types, list):
            event_types = []
            for event_types_type_0_item_data in self.event_types:
                event_types_type_0_item = event_types_type_0_item_data.to_dict()
                event_types.append(event_types_type_0_item)

        else:
            event_types = self.event_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_types is not UNSET:
            field_dict["eventTypes"] = event_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_type_output_model import EventTypeOutputModel

        d = dict(src_dict)

        def _parse_event_types(data: object) -> list[EventTypeOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_types_type_0 = []
                _event_types_type_0 = data
                for event_types_type_0_item_data in _event_types_type_0:
                    event_types_type_0_item = EventTypeOutputModel.from_dict(
                        event_types_type_0_item_data
                    )

                    event_types_type_0.append(event_types_type_0_item)

                return event_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EventTypeOutputModel] | None | Unset, data)

        event_types = _parse_event_types(d.pop("eventTypes", UNSET))

        event_type_output_list_model = cls(
            event_types=event_types,
        )

        event_type_output_list_model.additional_properties = d
        return event_type_output_list_model

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
