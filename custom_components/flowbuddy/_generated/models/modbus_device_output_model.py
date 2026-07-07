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
        resource_uri (None | str | Unset):
        serial_number (None | str | Unset):
        address (None | str | Unset):
        tcp_port (int | None | Unset):
        result_code (int | None | Unset):
        external_id (None | str | Unset):
        measuring_device (MeasuringDeviceReferenceModel | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    serial_number: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    tcp_port: int | None | Unset = UNSET
    result_code: int | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    measuring_device: MeasuringDeviceReferenceModel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.measuring_device_reference_model import MeasuringDeviceReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        serial_number: None | str | Unset
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        tcp_port: int | None | Unset
        if isinstance(self.tcp_port, Unset):
            tcp_port = UNSET
        else:
            tcp_port = self.tcp_port

        result_code: int | None | Unset
        if isinstance(self.result_code, Unset):
            result_code = UNSET
        else:
            result_code = self.result_code

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        measuring_device: dict[str, Any] | None | Unset
        if isinstance(self.measuring_device, Unset):
            measuring_device = UNSET
        elif isinstance(self.measuring_device, MeasuringDeviceReferenceModel):
            measuring_device = self.measuring_device.to_dict()
        else:
            measuring_device = self.measuring_device

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

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

        def _parse_serial_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        serial_number = _parse_serial_number(d.pop("serialNumber", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_tcp_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tcp_port = _parse_tcp_port(d.pop("tcpPort", UNSET))

        def _parse_result_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        result_code = _parse_result_code(d.pop("resultCode", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_measuring_device(data: object) -> MeasuringDeviceReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                measuring_device_type_1 = MeasuringDeviceReferenceModel.from_dict(data)

                return measuring_device_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MeasuringDeviceReferenceModel | None | Unset, data)

        measuring_device = _parse_measuring_device(d.pop("measuringDevice", UNSET))

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
