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
        name (None | str | Unset):
        code (None | str | Unset):
        unit (None | UnitOutputModel | Unset):
        external_id (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    code: None | str | Unset = UNSET
    unit: None | UnitOutputModel | Unset = UNSET
    external_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.unit_output_model import UnitOutputModel

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        unit: dict[str, Any] | None | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        elif isinstance(self.unit, UnitOutputModel):
            unit = self.unit.to_dict()
        else:
            unit = self.unit

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_unit(data: object) -> None | UnitOutputModel | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                unit_type_1 = UnitOutputModel.from_dict(data)

                return unit_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UnitOutputModel | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

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
