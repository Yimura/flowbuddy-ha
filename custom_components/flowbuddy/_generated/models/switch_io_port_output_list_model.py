from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.switch_io_port_output_model import SwitchIoPortOutputModel


T = TypeVar("T", bound="SwitchIoPortOutputListModel")


@_attrs_define
class SwitchIoPortOutputListModel:
    """
    Attributes:
        switch_io_ports (list[SwitchIoPortOutputModel] | Unset):
    """

    switch_io_ports: list[SwitchIoPortOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.switch_io_port_output_model import SwitchIoPortOutputModel

        switch_io_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.switch_io_ports, Unset):
            switch_io_ports = []
            for switch_io_ports_item_data in self.switch_io_ports:
                switch_io_ports_item = switch_io_ports_item_data.to_dict()
                switch_io_ports.append(switch_io_ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if switch_io_ports is not UNSET:
            field_dict["switchIoPorts"] = switch_io_ports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.switch_io_port_output_model import SwitchIoPortOutputModel

        d = dict(src_dict)
        _switch_io_ports = d.pop("switchIoPorts", UNSET)
        switch_io_ports: list[SwitchIoPortOutputModel] | Unset = UNSET
        if _switch_io_ports is not UNSET:
            switch_io_ports = []
            for switch_io_ports_item_data in _switch_io_ports:
                switch_io_ports_item = SwitchIoPortOutputModel.from_dict(switch_io_ports_item_data)

                switch_io_ports.append(switch_io_ports_item)

        switch_io_port_output_list_model = cls(
            switch_io_ports=switch_io_ports,
        )

        switch_io_port_output_list_model.additional_properties = d
        return switch_io_port_output_list_model

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
