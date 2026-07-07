from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="SimOutputModel")


@_attrs_define
class SimOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        service_provider (None | str | Unset): The service provider of the sim card (1NCE or Sim Services)
        operator (None | str | Unset): The network operator
        icc_id (None | str | Unset): Unique serial number of the sim card
        ip_address (None | str | Unset): The IP Address to reach the sim card
        network_status (None | str | Unset): The status of the sim on the network
        external_id (None | str | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    service_provider: None | str | Unset = UNSET
    operator: None | str | Unset = UNSET
    icc_id: None | str | Unset = UNSET
    ip_address: None | str | Unset = UNSET
    network_status: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        service_provider: None | str | Unset
        if isinstance(self.service_provider, Unset):
            service_provider = UNSET
        else:
            service_provider = self.service_provider

        operator: None | str | Unset
        if isinstance(self.operator, Unset):
            operator = UNSET
        else:
            operator = self.operator

        icc_id: None | str | Unset
        if isinstance(self.icc_id, Unset):
            icc_id = UNSET
        else:
            icc_id = self.icc_id

        ip_address: None | str | Unset
        if isinstance(self.ip_address, Unset):
            ip_address = UNSET
        else:
            ip_address = self.ip_address

        network_status: None | str | Unset
        if isinstance(self.network_status, Unset):
            network_status = UNSET
        else:
            network_status = self.network_status

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
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

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

        def _parse_service_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_provider = _parse_service_provider(d.pop("serviceProvider", UNSET))

        def _parse_operator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operator = _parse_operator(d.pop("operator", UNSET))

        def _parse_icc_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icc_id = _parse_icc_id(d.pop("iccId", UNSET))

        def _parse_ip_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_address = _parse_ip_address(d.pop("ipAddress", UNSET))

        def _parse_network_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        network_status = _parse_network_status(d.pop("networkStatus", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

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
