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


T = TypeVar("T", bound="InverterOutputModel")


@_attrs_define
class InverterOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        max_power (float | Unset):
        external_id (str | Unset):
        last_set_production_capacity (int | Unset):
        info (MeterReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    max_power: float | Unset = UNSET
    external_id: str | Unset = UNSET
    last_set_production_capacity: int | Unset = UNSET
    info: MeterReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meter_reference_model import MeterReferenceModel

        resource_uri = self.resource_uri

        max_power = self.max_power

        external_id = self.external_id

        last_set_production_capacity = self.last_set_production_capacity

        info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if max_power is not UNSET:
            field_dict["maxPower"] = max_power
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if last_set_production_capacity is not UNSET:
            field_dict["lastSetProductionCapacity"] = last_set_production_capacity
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meter_reference_model import MeterReferenceModel

        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

        max_power = d.pop("maxPower", UNSET)

        external_id = d.pop("externalId", UNSET)

        last_set_production_capacity = d.pop("lastSetProductionCapacity", UNSET)

        _info = d.pop("info", UNSET)
        info: MeterReferenceModel | Unset
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = MeterReferenceModel.from_dict(_info)

        inverter_output_model = cls(
            resource_uri=resource_uri,
            max_power=max_power,
            external_id=external_id,
            last_set_production_capacity=last_set_production_capacity,
            info=info,
        )

        inverter_output_model.additional_properties = d
        return inverter_output_model

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
