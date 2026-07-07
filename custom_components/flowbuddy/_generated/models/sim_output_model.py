from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="SimOutputModel")


@_attrs_define
class SimOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        service_provider (str | Unset): The service provider of the sim card (1NCE or Sim Services)
        operator (str | Unset): The network operator
        icc_id (str | Unset): Unique serial number of the sim card
        ip_address (str | Unset): The IP Address to reach the sim card
        network_status (str | Unset): The status of the sim on the network
        external_id (str | Unset):
    """

    resource_uri: str | Unset = UNSET
    service_provider: str | Unset = UNSET
    operator: str | Unset = UNSET
    icc_id: str | Unset = UNSET
    ip_address: str | Unset = UNSET
    network_status: str | Unset = UNSET
    external_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_uri = self.resource_uri

        service_provider = self.service_provider

        operator = self.operator

        icc_id = self.icc_id

        ip_address = self.ip_address

        network_status = self.network_status

        external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if service_provider is not UNSET:
            field_dict["serviceProvider"] = service_provider
        if operator is not UNSET:
            field_dict["operator"] = operator
        if icc_id is not UNSET:
            field_dict["iccId"] = icc_id
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if network_status is not UNSET:
            field_dict["networkStatus"] = network_status
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

        service_provider = d.pop("serviceProvider", UNSET)

        operator = d.pop("operator", UNSET)

        icc_id = d.pop("iccId", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        network_status = d.pop("networkStatus", UNSET)

        external_id = d.pop("externalId", UNSET)

        sim_output_model = cls(
            resource_uri=resource_uri,
            service_provider=service_provider,
            operator=operator,
            icc_id=icc_id,
            ip_address=ip_address,
            network_status=network_status,
            external_id=external_id,
        )

        sim_output_model.additional_properties = d
        return sim_output_model

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
