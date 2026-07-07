from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.measuring_device_reference_model import MeasuringDeviceReferenceModel


T = TypeVar("T", bound="ModbusDeviceOutputModel")


@_attrs_define
class ModbusDeviceOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        serial_number (str | Unset):
        address (str | Unset):
        tcp_port (int | Unset):
        result_code (int | Unset):
        external_id (str | Unset):
        measuring_device (MeasuringDeviceReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    serial_number: str | Unset = UNSET
    address: str | Unset = UNSET
    tcp_port: int | Unset = UNSET
    result_code: int | Unset = UNSET
    external_id: str | Unset = UNSET
    measuring_device: MeasuringDeviceReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.measuring_device_reference_model import MeasuringDeviceReferenceModel

        resource_uri = self.resource_uri

        serial_number = self.serial_number

        address = self.address

        tcp_port = self.tcp_port

        result_code = self.result_code

        external_id = self.external_id

        measuring_device: dict[str, Any] | Unset = UNSET
        if not isinstance(self.measuring_device, Unset):
            measuring_device = self.measuring_device.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if address is not UNSET:
            field_dict["address"] = address
        if tcp_port is not UNSET:
            field_dict["tcpPort"] = tcp_port
        if result_code is not UNSET:
            field_dict["resultCode"] = result_code
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if measuring_device is not UNSET:
            field_dict["measuringDevice"] = measuring_device

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measuring_device_reference_model import MeasuringDeviceReferenceModel

        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        address = d.pop("address", UNSET)

        tcp_port = d.pop("tcpPort", UNSET)

        result_code = d.pop("resultCode", UNSET)

        external_id = d.pop("externalId", UNSET)

        _measuring_device = d.pop("measuringDevice", UNSET)
        measuring_device: MeasuringDeviceReferenceModel | Unset
        if isinstance(_measuring_device, Unset):
            measuring_device = UNSET
        else:
            measuring_device = MeasuringDeviceReferenceModel.from_dict(_measuring_device)

        modbus_device_output_model = cls(
            resource_uri=resource_uri,
            serial_number=serial_number,
            address=address,
            tcp_port=tcp_port,
            result_code=result_code,
            external_id=external_id,
            measuring_device=measuring_device,
        )

        modbus_device_output_model.additional_properties = d
        return modbus_device_output_model

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
