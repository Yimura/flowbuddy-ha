from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.communicator_type_output_model import CommunicatorTypeOutputModel


T = TypeVar("T", bound="CommunicatorTypeOutputListModel")


@_attrs_define
class CommunicatorTypeOutputListModel:
    """
    Attributes:
        communicator_types (list[CommunicatorTypeOutputModel] | Unset):
    """

    communicator_types: list[CommunicatorTypeOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_type_output_model import CommunicatorTypeOutputModel

        communicator_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.communicator_types, Unset):
            communicator_types = []
            for communicator_types_item_data in self.communicator_types:
                communicator_types_item = communicator_types_item_data.to_dict()
                communicator_types.append(communicator_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if communicator_types is not UNSET:
            field_dict["communicatorTypes"] = communicator_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communicator_type_output_model import CommunicatorTypeOutputModel

        d = dict(src_dict)
        _communicator_types = d.pop("communicatorTypes", UNSET)
        communicator_types: list[CommunicatorTypeOutputModel] | Unset = UNSET
        if _communicator_types is not UNSET:
            communicator_types = []
            for communicator_types_item_data in _communicator_types:
                communicator_types_item = CommunicatorTypeOutputModel.from_dict(
                    communicator_types_item_data
                )

                communicator_types.append(communicator_types_item)

        communicator_type_output_list_model = cls(
            communicator_types=communicator_types,
        )

        communicator_type_output_list_model.additional_properties = d
        return communicator_type_output_list_model

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
