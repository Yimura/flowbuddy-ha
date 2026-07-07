from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.hvac_output_model import HVACOutputModel


T = TypeVar("T", bound="HVACOutputListModel")


@_attrs_define
class HVACOutputListModel:
    """
    Attributes:
        hvacs (list[HVACOutputModel] | None | Unset):
    """

    hvacs: list[HVACOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hvac_output_model import HVACOutputModel

        hvacs: list[dict[str, Any]] | None | Unset
        if isinstance(self.hvacs, Unset):
            hvacs = UNSET
        elif isinstance(self.hvacs, list):
            hvacs = []
            for hvacs_type_0_item_data in self.hvacs:
                hvacs_type_0_item = hvacs_type_0_item_data.to_dict()
                hvacs.append(hvacs_type_0_item)

        else:
            hvacs = self.hvacs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hvacs is not UNSET:
            field_dict["hvacs"] = hvacs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hvac_output_model import HVACOutputModel

        d = dict(src_dict)

        def _parse_hvacs(data: object) -> list[HVACOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hvacs_type_0 = []
                _hvacs_type_0 = data
                for hvacs_type_0_item_data in _hvacs_type_0:
                    hvacs_type_0_item = HVACOutputModel.from_dict(hvacs_type_0_item_data)

                    hvacs_type_0.append(hvacs_type_0_item)

                return hvacs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HVACOutputModel] | None | Unset, data)

        hvacs = _parse_hvacs(d.pop("hvacs", UNSET))

        hvac_output_list_model = cls(
            hvacs=hvacs,
        )

        hvac_output_list_model.additional_properties = d
        return hvac_output_list_model

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
