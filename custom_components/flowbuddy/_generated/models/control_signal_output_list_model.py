from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.control_signal_output_model import ControlSignalOutputModel


T = TypeVar("T", bound="ControlSignalOutputListModel")


@_attrs_define
class ControlSignalOutputListModel:
    """
    Attributes:
        control_signals (list[ControlSignalOutputModel] | Unset):
    """

    control_signals: list[ControlSignalOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.control_signal_output_model import ControlSignalOutputModel

        control_signals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.control_signals, Unset):
            control_signals = []
            for control_signals_item_data in self.control_signals:
                control_signals_item = control_signals_item_data.to_dict()
                control_signals.append(control_signals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_signals is not UNSET:
            field_dict["controlSignals"] = control_signals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.control_signal_output_model import ControlSignalOutputModel

        d = dict(src_dict)
        _control_signals = d.pop("controlSignals", UNSET)
        control_signals: list[ControlSignalOutputModel] | Unset = UNSET
        if _control_signals is not UNSET:
            control_signals = []
            for control_signals_item_data in _control_signals:
                control_signals_item = ControlSignalOutputModel.from_dict(control_signals_item_data)

                control_signals.append(control_signals_item)

        control_signal_output_list_model = cls(
            control_signals=control_signals,
        )

        control_signal_output_list_model.additional_properties = d
        return control_signal_output_list_model

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
