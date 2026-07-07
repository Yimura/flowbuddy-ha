from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.switch_breaker_output_model import SwitchBreakerOutputModel


T = TypeVar("T", bound="SwitchBreakerOutputListModel")


@_attrs_define
class SwitchBreakerOutputListModel:
    """
    Attributes:
        switch_breakers (list[SwitchBreakerOutputModel] | None | Unset):
    """

    switch_breakers: list[SwitchBreakerOutputModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.switch_breaker_output_model import SwitchBreakerOutputModel

        switch_breakers: list[dict[str, Any]] | None | Unset
        if isinstance(self.switch_breakers, Unset):
            switch_breakers = UNSET
        elif isinstance(self.switch_breakers, list):
            switch_breakers = []
            for switch_breakers_type_0_item_data in self.switch_breakers:
                switch_breakers_type_0_item = switch_breakers_type_0_item_data.to_dict()
                switch_breakers.append(switch_breakers_type_0_item)

        else:
            switch_breakers = self.switch_breakers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if switch_breakers is not UNSET:
            field_dict["switchBreakers"] = switch_breakers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.switch_breaker_output_model import SwitchBreakerOutputModel

        d = dict(src_dict)

        def _parse_switch_breakers(data: object) -> list[SwitchBreakerOutputModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                switch_breakers_type_0 = []
                _switch_breakers_type_0 = data
                for switch_breakers_type_0_item_data in _switch_breakers_type_0:
                    switch_breakers_type_0_item = SwitchBreakerOutputModel.from_dict(
                        switch_breakers_type_0_item_data
                    )

                    switch_breakers_type_0.append(switch_breakers_type_0_item)

                return switch_breakers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SwitchBreakerOutputModel] | None | Unset, data)

        switch_breakers = _parse_switch_breakers(d.pop("switchBreakers", UNSET))

        switch_breaker_output_list_model = cls(
            switch_breakers=switch_breakers,
        )

        switch_breaker_output_list_model.additional_properties = d
        return switch_breaker_output_list_model

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
