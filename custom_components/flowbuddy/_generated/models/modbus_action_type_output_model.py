from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.communicator_type_reference_model import CommunicatorTypeReferenceModel


T = TypeVar("T", bound="ModbusActionTypeOutputModel")


@_attrs_define
class ModbusActionTypeOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        name (None | str | Unset):
        function_code (None | str | Unset):
        slave_address (int | None | Unset):
        register_address (int | None | Unset):
        register_length (int | None | Unset):
        value (None | str | Unset):
        is_value_required (bool | None | Unset):
        is_fixed_value (bool | None | Unset):
        protocol (None | str | Unset):
        external_id (None | str | Unset):
        communicator_type (CommunicatorTypeReferenceModel | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    function_code: None | str | Unset = UNSET
    slave_address: int | None | Unset = UNSET
    register_address: int | None | Unset = UNSET
    register_length: int | None | Unset = UNSET
    value: None | str | Unset = UNSET
    is_value_required: bool | None | Unset = UNSET
    is_fixed_value: bool | None | Unset = UNSET
    protocol: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    communicator_type: CommunicatorTypeReferenceModel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_type_reference_model import CommunicatorTypeReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        function_code: None | str | Unset
        if isinstance(self.function_code, Unset):
            function_code = UNSET
        else:
            function_code = self.function_code

        slave_address: int | None | Unset
        if isinstance(self.slave_address, Unset):
            slave_address = UNSET
        else:
            slave_address = self.slave_address

        register_address: int | None | Unset
        if isinstance(self.register_address, Unset):
            register_address = UNSET
        else:
            register_address = self.register_address

        register_length: int | None | Unset
        if isinstance(self.register_length, Unset):
            register_length = UNSET
        else:
            register_length = self.register_length

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        is_value_required: bool | None | Unset
        if isinstance(self.is_value_required, Unset):
            is_value_required = UNSET
        else:
            is_value_required = self.is_value_required

        is_fixed_value: bool | None | Unset
        if isinstance(self.is_fixed_value, Unset):
            is_fixed_value = UNSET
        else:
            is_fixed_value = self.is_fixed_value

        protocol: None | str | Unset
        if isinstance(self.protocol, Unset):
            protocol = UNSET
        else:
            protocol = self.protocol

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        communicator_type: dict[str, Any] | None | Unset
        if isinstance(self.communicator_type, Unset):
            communicator_type = UNSET
        elif isinstance(self.communicator_type, CommunicatorTypeReferenceModel):
            communicator_type = self.communicator_type.to_dict()
        else:
            communicator_type = self.communicator_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if name is not UNSET:
            field_dict["name"] = name
        if function_code is not UNSET:
            field_dict["functionCode"] = function_code
        if slave_address is not UNSET:
            field_dict["slaveAddress"] = slave_address
        if register_address is not UNSET:
            field_dict["registerAddress"] = register_address
        if register_length is not UNSET:
            field_dict["registerLength"] = register_length
        if value is not UNSET:
            field_dict["value"] = value
        if is_value_required is not UNSET:
            field_dict["isValueRequired"] = is_value_required
        if is_fixed_value is not UNSET:
            field_dict["isFixedValue"] = is_fixed_value
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if communicator_type is not UNSET:
            field_dict["communicatorType"] = communicator_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communicator_type_reference_model import CommunicatorTypeReferenceModel

        d = dict(src_dict)

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_function_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        function_code = _parse_function_code(d.pop("functionCode", UNSET))

        def _parse_slave_address(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        slave_address = _parse_slave_address(d.pop("slaveAddress", UNSET))

        def _parse_register_address(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        register_address = _parse_register_address(d.pop("registerAddress", UNSET))

        def _parse_register_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        register_length = _parse_register_length(d.pop("registerLength", UNSET))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_is_value_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_value_required = _parse_is_value_required(d.pop("isValueRequired", UNSET))

        def _parse_is_fixed_value(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_fixed_value = _parse_is_fixed_value(d.pop("isFixedValue", UNSET))

        def _parse_protocol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        protocol = _parse_protocol(d.pop("protocol", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_communicator_type(data: object) -> CommunicatorTypeReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                communicator_type_type_1 = CommunicatorTypeReferenceModel.from_dict(data)

                return communicator_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CommunicatorTypeReferenceModel | None | Unset, data)

        communicator_type = _parse_communicator_type(d.pop("communicatorType", UNSET))

        modbus_action_type_output_model = cls(
            resource_uri=resource_uri,
            name=name,
            function_code=function_code,
            slave_address=slave_address,
            register_address=register_address,
            register_length=register_length,
            value=value,
            is_value_required=is_value_required,
            is_fixed_value=is_fixed_value,
            protocol=protocol,
            external_id=external_id,
            communicator_type=communicator_type,
        )

        modbus_action_type_output_model.additional_properties = d
        return modbus_action_type_output_model

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
