from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.communicator_output_model import CommunicatorOutputModel


T = TypeVar("T", bound="CommunicatorOutputListModel")


@_attrs_define
class CommunicatorOutputListModel:
    """
    Attributes:
        communicators (list[CommunicatorOutputModel] | None | Unset):
    """

    communicators: list[CommunicatorOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_output_model import CommunicatorOutputModel

        communicators: list[dict[str, Any]] | None | Unset
        if isinstance(self.communicators, Unset):
            communicators = UNSET
        elif isinstance(self.communicators, list):
            communicators = []
            for communicators_type_0_item_data in self.communicators:
                communicators_type_0_item = communicators_type_0_item_data.to_dict()
                communicators.append(communicators_type_0_item)

        else:
            communicators = self.communicators

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if communicators is not UNSET:
            field_dict["communicators"] = communicators

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communicator_output_model import CommunicatorOutputModel

        d = dict(src_dict)

        def _parse_communicators(data: object) -> list[CommunicatorOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                communicators_type_0 = []
                _communicators_type_0 = data
                for communicators_type_0_item_data in _communicators_type_0:
                    communicators_type_0_item = CommunicatorOutputModel.from_dict(
                        communicators_type_0_item_data
                    )

                    communicators_type_0.append(communicators_type_0_item)

                return communicators_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CommunicatorOutputModel] | None | Unset, data)

        communicators = _parse_communicators(d.pop("communicators", UNSET))

        communicator_output_list_model = cls(
            communicators=communicators,
        )

        communicator_output_list_model.additional_properties = d
        return communicator_output_list_model

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
