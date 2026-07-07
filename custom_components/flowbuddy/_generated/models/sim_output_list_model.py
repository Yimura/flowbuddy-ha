from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.sim_output_model import SimOutputModel


T = TypeVar("T", bound="SimOutputListModel")


@_attrs_define
class SimOutputListModel:
    """
    Attributes:
        sims (list[SimOutputModel] | Unset):
    """

    sims: list[SimOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sim_output_model import SimOutputModel

        sims: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sims, Unset):
            sims = []
            for sims_item_data in self.sims:
                sims_item = sims_item_data.to_dict()
                sims.append(sims_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sims is not UNSET:
            field_dict["sims"] = sims

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sim_output_model import SimOutputModel

        d = dict(src_dict)
        _sims = d.pop("sims", UNSET)
        sims: list[SimOutputModel] | Unset = UNSET
        if _sims is not UNSET:
            sims = []
            for sims_item_data in _sims:
                sims_item = SimOutputModel.from_dict(sims_item_data)

                sims.append(sims_item)

        sim_output_list_model = cls(
            sims=sims,
        )

        sim_output_list_model.additional_properties = d
        return sim_output_list_model

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
