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
        sims (list[SimOutputModel] | None | Unset):
    """

    sims: list[SimOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sim_output_model import SimOutputModel

        sims: list[dict[str, Any]] | None | Unset
        if isinstance(self.sims, Unset):
            sims = UNSET
        elif isinstance(self.sims, list):
            sims = []
            for sims_type_0_item_data in self.sims:
                sims_type_0_item = sims_type_0_item_data.to_dict()
                sims.append(sims_type_0_item)

        else:
            sims = self.sims

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

        def _parse_sims(data: object) -> list[SimOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sims_type_0 = []
                _sims_type_0 = data
                for sims_type_0_item_data in _sims_type_0:
                    sims_type_0_item = SimOutputModel.from_dict(sims_type_0_item_data)

                    sims_type_0.append(sims_type_0_item)

                return sims_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SimOutputModel] | None | Unset, data)

        sims = _parse_sims(d.pop("sims", UNSET))

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
