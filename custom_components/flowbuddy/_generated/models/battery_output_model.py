from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.meter_reference_model import MeterReferenceModel


T = TypeVar("T", bound="BatteryOutputModel")


@_attrs_define
class BatteryOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        capacity (float | Unset):
        max_charge_power (float | Unset):
        max_discharge_power (float | Unset):
        last_set_charge_power (float | Unset):
        external_id (str | Unset):
        info (MeterReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    capacity: float | Unset = UNSET
    max_charge_power: float | Unset = UNSET
    max_discharge_power: float | Unset = UNSET
    last_set_charge_power: float | Unset = UNSET
    external_id: str | Unset = UNSET
    info: MeterReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meter_reference_model import MeterReferenceModel

        resource_uri = self.resource_uri

        capacity = self.capacity

        max_charge_power = self.max_charge_power

        max_discharge_power = self.max_discharge_power

        last_set_charge_power = self.last_set_charge_power

        external_id = self.external_id

        info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if max_charge_power is not UNSET:
            field_dict["maxChargePower"] = max_charge_power
        if max_discharge_power is not UNSET:
            field_dict["maxDischargePower"] = max_discharge_power
        if last_set_charge_power is not UNSET:
            field_dict["lastSetChargePower"] = last_set_charge_power
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meter_reference_model import MeterReferenceModel

        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

        capacity = d.pop("capacity", UNSET)

        max_charge_power = d.pop("maxChargePower", UNSET)

        max_discharge_power = d.pop("maxDischargePower", UNSET)

        last_set_charge_power = d.pop("lastSetChargePower", UNSET)

        external_id = d.pop("externalId", UNSET)

        _info = d.pop("info", UNSET)
        info: MeterReferenceModel | Unset
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = MeterReferenceModel.from_dict(_info)

        battery_output_model = cls(
            resource_uri=resource_uri,
            capacity=capacity,
            max_charge_power=max_charge_power,
            max_discharge_power=max_discharge_power,
            last_set_charge_power=last_set_charge_power,
            external_id=external_id,
            info=info,
        )

        battery_output_model.additional_properties = d
        return battery_output_model

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
