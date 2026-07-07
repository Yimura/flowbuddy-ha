from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.installation_pool_signal_output_model import InstallationPoolSignalOutputModel


T = TypeVar("T", bound="InstallationPoolSignalOutputListModel")


@_attrs_define
class InstallationPoolSignalOutputListModel:
    """
    Attributes:
        installation_pool_signals (list[InstallationPoolSignalOutputModel] | Unset):
    """

    installation_pool_signals: list[InstallationPoolSignalOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_pool_signal_output_model import InstallationPoolSignalOutputModel

        installation_pool_signals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.installation_pool_signals, Unset):
            installation_pool_signals = []
            for installation_pool_signals_item_data in self.installation_pool_signals:
                installation_pool_signals_item = installation_pool_signals_item_data.to_dict()
                installation_pool_signals.append(installation_pool_signals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if installation_pool_signals is not UNSET:
            field_dict["installationPoolSignals"] = installation_pool_signals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.installation_pool_signal_output_model import InstallationPoolSignalOutputModel

        d = dict(src_dict)
        _installation_pool_signals = d.pop("installationPoolSignals", UNSET)
        installation_pool_signals: list[InstallationPoolSignalOutputModel] | Unset = UNSET
        if _installation_pool_signals is not UNSET:
            installation_pool_signals = []
            for installation_pool_signals_item_data in _installation_pool_signals:
                installation_pool_signals_item = InstallationPoolSignalOutputModel.from_dict(
                    installation_pool_signals_item_data
                )

                installation_pool_signals.append(installation_pool_signals_item)

        installation_pool_signal_output_list_model = cls(
            installation_pool_signals=installation_pool_signals,
        )

        installation_pool_signal_output_list_model.additional_properties = d
        return installation_pool_signal_output_list_model

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
