from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.send_ct_ratio_output_model import SendCtRatioOutputModel


T = TypeVar("T", bound="SendCtRatioOutputListModel")


@_attrs_define
class SendCtRatioOutputListModel:
    """
    Attributes:
        send_ct_ratios (list[SendCtRatioOutputModel] | None | Unset):
    """

    send_ct_ratios: list[SendCtRatioOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.send_ct_ratio_output_model import SendCtRatioOutputModel

        send_ct_ratios: list[dict[str, Any]] | None | Unset
        if isinstance(self.send_ct_ratios, Unset):
            send_ct_ratios = UNSET
        elif isinstance(self.send_ct_ratios, list):
            send_ct_ratios = []
            for send_ct_ratios_type_0_item_data in self.send_ct_ratios:
                send_ct_ratios_type_0_item = send_ct_ratios_type_0_item_data.to_dict()
                send_ct_ratios.append(send_ct_ratios_type_0_item)

        else:
            send_ct_ratios = self.send_ct_ratios

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if send_ct_ratios is not UNSET:
            field_dict["sendCtRatios"] = send_ct_ratios

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_ct_ratio_output_model import SendCtRatioOutputModel

        d = dict(src_dict)

        def _parse_send_ct_ratios(data: object) -> list[SendCtRatioOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                send_ct_ratios_type_0 = []
                _send_ct_ratios_type_0 = data
                for send_ct_ratios_type_0_item_data in _send_ct_ratios_type_0:
                    send_ct_ratios_type_0_item = SendCtRatioOutputModel.from_dict(
                        send_ct_ratios_type_0_item_data
                    )

                    send_ct_ratios_type_0.append(send_ct_ratios_type_0_item)

                return send_ct_ratios_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SendCtRatioOutputModel] | None | Unset, data)

        send_ct_ratios = _parse_send_ct_ratios(d.pop("sendCtRatios", UNSET))

        send_ct_ratio_output_list_model = cls(
            send_ct_ratios=send_ct_ratios,
        )

        send_ct_ratio_output_list_model.additional_properties = d
        return send_ct_ratio_output_list_model

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
