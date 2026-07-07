from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.communicator_request_modbus_action_post_input_model_other_properties_type_0 import (
        CommunicatorRequestModbusActionPostInputModelOtherPropertiesType0,
    )


T = TypeVar("T", bound="CommunicatorRequestModbusActionPostInputModel")


@_attrs_define
class CommunicatorRequestModbusActionPostInputModel:
    """
    Attributes:
        modbus_action_type (None | str | Unset): A predefined lists of available modbus settings
        modbus_function_code (None | str | Unset): The Modbus protocol offers a number of functions that are used to
            read or write data
        protocol (None | str | Unset):
        slave_address (int | None | Unset): The master device addresses a specific slave device by using the address
            field. Valid RTU addresses are from 1-247
        ipv_4_address (None | str | Unset):
        port (int | None | Unset):
        unit_id (int | None | Unset):
        register_address (int | None | Unset): Modbus functions operate on register map registers to monitor, configure,
            and control module I/O. This value is often a 5-digit number (0xxxx,1xxxx,3xxxx,4xxxx)
        register_value (None | str | Unset): When executing a write function, the value to be written should be filled
            in.
        register_length (int | None | Unset): The amount of registers that will be read. In case of a larger datatype
            such as U32, multiple registers have to be read/written.
        other_properties (CommunicatorRequestModbusActionPostInputModelOtherPropertiesType0 | None | Unset):
    """

    modbus_action_type: None | str | Unset = UNSET
    modbus_function_code: None | str | Unset = UNSET
    protocol: None | str | Unset = UNSET
    slave_address: int | None | Unset = UNSET
    ipv_4_address: None | str | Unset = UNSET
    port: int | None | Unset = UNSET
    unit_id: int | None | Unset = UNSET
    register_address: int | None | Unset = UNSET
    register_value: None | str | Unset = UNSET
    register_length: int | None | Unset = UNSET
    other_properties: (
        CommunicatorRequestModbusActionPostInputModelOtherPropertiesType0 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_request_modbus_action_post_input_model_other_properties_type_0 import (
            CommunicatorRequestModbusActionPostInputModelOtherPropertiesType0,
        )

        modbus_action_type: None | str | Unset
        if isinstance(self.modbus_action_type, Unset):
            modbus_action_type = UNSET
        else:
            modbus_action_type = self.modbus_action_type

        modbus_function_code: None | str | Unset
        if isinstance(self.modbus_function_code, Unset):
            modbus_function_code = UNSET
        else:
            modbus_function_code = self.modbus_function_code

        protocol: None | str | Unset
        if isinstance(self.protocol, Unset):
            protocol = UNSET
        else:
            protocol = self.protocol

        slave_address: int | None | Unset
        if isinstance(self.slave_address, Unset):
            slave_address = UNSET
        else:
            slave_address = self.slave_address

        ipv_4_address: None | str | Unset
        if isinstance(self.ipv_4_address, Unset):
            ipv_4_address = UNSET
        else:
            ipv_4_address = self.ipv_4_address

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        unit_id: int | None | Unset
        if isinstance(self.unit_id, Unset):
            unit_id = UNSET
        else:
            unit_id = self.unit_id

        register_address: int | None | Unset
        if isinstance(self.register_address, Unset):
            register_address = UNSET
        else:
            register_address = self.register_address

        register_value: None | str | Unset
        if isinstance(self.register_value, Unset):
            register_value = UNSET
        else:
            register_value = self.register_value

        register_length: int | None | Unset
        if isinstance(self.register_length, Unset):
            register_length = UNSET
        else:
            register_length = self.register_length

        other_properties: dict[str, Any] | None | Unset
        if isinstance(self.other_properties, Unset):
            other_properties = UNSET
        elif isinstance(
            self.other_properties, CommunicatorRequestModbusActionPostInputModelOtherPropertiesType0
        ):
            other_properties = self.other_properties.to_dict()
        else:
            other_properties = self.other_properties

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
        from ..models.communicator_request_modbus_action_post_input_model_other_properties_type_0 import (
            CommunicatorRequestModbusActionPostInputModelOtherPropertiesType0,
        )

        d = dict(src_dict)

        def _parse_modbus_action_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        modbus_action_type = _parse_modbus_action_type(d.pop("modbusActionType", UNSET))

        def _parse_modbus_function_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        modbus_function_code = _parse_modbus_function_code(d.pop("modbusFunctionCode", UNSET))

        def _parse_protocol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        protocol = _parse_protocol(d.pop("protocol", UNSET))

        def _parse_slave_address(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        slave_address = _parse_slave_address(d.pop("slaveAddress", UNSET))

        def _parse_ipv_4_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ipv_4_address = _parse_ipv_4_address(d.pop("ipv4Address", UNSET))

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_unit_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unit_id = _parse_unit_id(d.pop("unitId", UNSET))

        def _parse_register_address(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        register_address = _parse_register_address(d.pop("registerAddress", UNSET))

        def _parse_register_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        register_value = _parse_register_value(d.pop("registerValue", UNSET))

        def _parse_register_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        register_length = _parse_register_length(d.pop("registerLength", UNSET))

        def _parse_other_properties(
            data: object,
        ) -> CommunicatorRequestModbusActionPostInputModelOtherPropertiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_properties_type_0 = (
                    CommunicatorRequestModbusActionPostInputModelOtherPropertiesType0.from_dict(
                        data
                    )
                )

                return other_properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CommunicatorRequestModbusActionPostInputModelOtherPropertiesType0 | None | Unset,
                data,
            )

        other_properties = _parse_other_properties(d.pop("otherProperties", UNSET))

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
