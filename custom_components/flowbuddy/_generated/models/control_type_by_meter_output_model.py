from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.unit_output_model import UnitOutputModel


T = TypeVar("T", bound="ControlTypeByMeterOutputModel")


@_attrs_define
class ControlTypeByMeterOutputModel:
    """
    Attributes:
        name (str | Unset):
        code (str | Unset):
        unit (UnitOutputModel | Unset):
        external_id (str | Unset):
    """

    name: str | Unset = UNSET
    code: str | Unset = UNSET
    unit: UnitOutputModel | Unset = UNSET
    external_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.unit_output_model import UnitOutputModel

        name = self.name

        code = self.code

        unit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.to_dict()

        external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if unit is not UNSET:
            field_dict["unit"] = unit
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unit_output_model import UnitOutputModel

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: UnitOutputModel | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = UnitOutputModel.from_dict(_unit)

        external_id = d.pop("externalId", UNSET)

        control_type_by_meter_output_model = cls(
            name=name,
            code=code,
            unit=unit,
            external_id=external_id,
        )

        control_type_by_meter_output_model.additional_properties = d
        return control_type_by_meter_output_model

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
