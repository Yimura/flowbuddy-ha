from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.communicator_request_modbus_action_post_input_model_other_properties import (
        CommunicatorRequestModbusActionPostInputModelOtherProperties,
    )


T = TypeVar("T", bound="CommunicatorRequestModbusActionPostInputModel")


@_attrs_define
class CommunicatorRequestModbusActionPostInputModel:
    """
    Attributes:
        modbus_action_type (str | Unset): A predefined lists of available modbus settings
        modbus_function_code (str | Unset): The Modbus protocol offers a number of functions that are used to read or
            write data
        protocol (str | Unset):
        slave_address (int | Unset): The master device addresses a specific slave device by using the address field.
            Valid RTU addresses are from 1-247
        ipv_4_address (str | Unset):
        port (int | Unset):
        unit_id (int | Unset):
        register_address (int | Unset): Modbus functions operate on register map registers to monitor, configure, and
            control module I/O. This value is often a 5-digit number (0xxxx,1xxxx,3xxxx,4xxxx)
        register_value (str | Unset): When executing a write function, the value to be written should be filled in.
        register_length (int | Unset): The amount of registers that will be read. In case of a larger datatype such as
            U32, multiple registers have to be read/written.
        other_properties (CommunicatorRequestModbusActionPostInputModelOtherProperties | Unset):
    """

    modbus_action_type: str | Unset = UNSET
    modbus_function_code: str | Unset = UNSET
    protocol: str | Unset = UNSET
    slave_address: int | Unset = UNSET
    ipv_4_address: str | Unset = UNSET
    port: int | Unset = UNSET
    unit_id: int | Unset = UNSET
    register_address: int | Unset = UNSET
    register_value: str | Unset = UNSET
    register_length: int | Unset = UNSET
    other_properties: CommunicatorRequestModbusActionPostInputModelOtherProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_request_modbus_action_post_input_model_other_properties import (
            CommunicatorRequestModbusActionPostInputModelOtherProperties,
        )

        modbus_action_type = self.modbus_action_type

        modbus_function_code = self.modbus_function_code

        protocol = self.protocol

        slave_address = self.slave_address

        ipv_4_address = self.ipv_4_address

        port = self.port

        unit_id = self.unit_id

        register_address = self.register_address

        register_value = self.register_value

        register_length = self.register_length

        other_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_properties, Unset):
            other_properties = self.other_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modbus_action_type is not UNSET:
            field_dict["modbusActionType"] = modbus_action_type
        if modbus_function_code is not UNSET:
            field_dict["modbusFunctionCode"] = modbus_function_code
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if slave_address is not UNSET:
            field_dict["slaveAddress"] = slave_address
        if ipv_4_address is not UNSET:
            field_dict["ipv4Address"] = ipv_4_address
        if port is not UNSET:
            field_dict["port"] = port
        if unit_id is not UNSET:
            field_dict["unitId"] = unit_id
        if register_address is not UNSET:
            field_dict["registerAddress"] = register_address
        if register_value is not UNSET:
            field_dict["registerValue"] = register_value
        if register_length is not UNSET:
            field_dict["registerLength"] = register_length
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communicator_request_modbus_action_post_input_model_other_properties import (
            CommunicatorRequestModbusActionPostInputModelOtherProperties,
        )

        d = dict(src_dict)
        modbus_action_type = d.pop("modbusActionType", UNSET)

        modbus_function_code = d.pop("modbusFunctionCode", UNSET)

        protocol = d.pop("protocol", UNSET)

        slave_address = d.pop("slaveAddress", UNSET)

        ipv_4_address = d.pop("ipv4Address", UNSET)

        port = d.pop("port", UNSET)

        unit_id = d.pop("unitId", UNSET)

        register_address = d.pop("registerAddress", UNSET)

        register_value = d.pop("registerValue", UNSET)

        register_length = d.pop("registerLength", UNSET)

        _other_properties = d.pop("otherProperties", UNSET)
        other_properties: CommunicatorRequestModbusActionPostInputModelOtherProperties | Unset
        if isinstance(_other_properties, Unset):
            other_properties = UNSET
        else:
            other_properties = (
                CommunicatorRequestModbusActionPostInputModelOtherProperties.from_dict(
                    _other_properties
                )
            )

        communicator_request_modbus_action_post_input_model = cls(
            modbus_action_type=modbus_action_type,
            modbus_function_code=modbus_function_code,
            protocol=protocol,
            slave_address=slave_address,
            ipv_4_address=ipv_4_address,
            port=port,
            unit_id=unit_id,
            register_address=register_address,
            register_value=register_value,
            register_length=register_length,
            other_properties=other_properties,
        )

        communicator_request_modbus_action_post_input_model.additional_properties = d
        return communicator_request_modbus_action_post_input_model

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
