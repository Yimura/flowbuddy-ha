from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.control_type_by_meter_output_model import ControlTypeByMeterOutputModel


T = TypeVar("T", bound="ControlTypeByMeterOutputListModel")


@_attrs_define
class ControlTypeByMeterOutputListModel:
    """
    Attributes:
        control_types (list[ControlTypeByMeterOutputModel] | None | Unset):
    """

    control_types: list[ControlTypeByMeterOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.control_type_by_meter_output_model import ControlTypeByMeterOutputModel

        control_types: list[dict[str, Any]] | None | Unset
        if isinstance(self.control_types, Unset):
            control_types = UNSET
        elif isinstance(self.control_types, list):
            control_types = []
            for control_types_type_0_item_data in self.control_types:
                control_types_type_0_item = control_types_type_0_item_data.to_dict()
                control_types.append(control_types_type_0_item)

        else:
            control_types = self.control_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_types is not UNSET:
            field_dict["controlTypes"] = control_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.control_type_by_meter_output_model import ControlTypeByMeterOutputModel

        d = dict(src_dict)

        def _parse_control_types(
            data: object,
        ) -> list[ControlTypeByMeterOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                control_types_type_0 = []
                _control_types_type_0 = data
                for control_types_type_0_item_data in _control_types_type_0:
                    control_types_type_0_item = ControlTypeByMeterOutputModel.from_dict(
                        control_types_type_0_item_data
                    )

                    control_types_type_0.append(control_types_type_0_item)

                return control_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ControlTypeByMeterOutputModel] | None | Unset, data)

        control_types = _parse_control_types(d.pop("controlTypes", UNSET))

        control_type_by_meter_output_list_model = cls(
            control_types=control_types,
        )

        control_type_by_meter_output_list_model.additional_properties = d
        return control_type_by_meter_output_list_model

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
