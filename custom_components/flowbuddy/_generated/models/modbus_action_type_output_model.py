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
        resource_uri (str | Unset):
        name (str | Unset):
        function_code (str | Unset):
        slave_address (int | Unset):
        register_address (int | Unset):
        register_length (int | Unset):
        value (str | Unset):
        is_value_required (bool | Unset):
        is_fixed_value (bool | Unset):
        protocol (str | Unset):
        external_id (str | Unset):
        communicator_type (CommunicatorTypeReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    name: str | Unset = UNSET
    function_code: str | Unset = UNSET
    slave_address: int | Unset = UNSET
    register_address: int | Unset = UNSET
    register_length: int | Unset = UNSET
    value: str | Unset = UNSET
    is_value_required: bool | Unset = UNSET
    is_fixed_value: bool | Unset = UNSET
    protocol: str | Unset = UNSET
    external_id: str | Unset = UNSET
    communicator_type: CommunicatorTypeReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_type_reference_model import CommunicatorTypeReferenceModel

        resource_uri = self.resource_uri

        name = self.name

        function_code = self.function_code

        slave_address = self.slave_address

        register_address = self.register_address

        register_length = self.register_length

        value = self.value

        is_value_required = self.is_value_required

        is_fixed_value = self.is_fixed_value

        protocol = self.protocol

        external_id = self.external_id

        communicator_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.communicator_type, Unset):
            communicator_type = self.communicator_type.to_dict()

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
        resource_uri = d.pop("resourceUri", UNSET)

        name = d.pop("name", UNSET)

        function_code = d.pop("functionCode", UNSET)

        slave_address = d.pop("slaveAddress", UNSET)

        register_address = d.pop("registerAddress", UNSET)

        register_length = d.pop("registerLength", UNSET)

        value = d.pop("value", UNSET)

        is_value_required = d.pop("isValueRequired", UNSET)

        is_fixed_value = d.pop("isFixedValue", UNSET)

        protocol = d.pop("protocol", UNSET)

        external_id = d.pop("externalId", UNSET)

        _communicator_type = d.pop("communicatorType", UNSET)
        communicator_type: CommunicatorTypeReferenceModel | Unset
        if isinstance(_communicator_type, Unset):
            communicator_type = UNSET
        else:
            communicator_type = CommunicatorTypeReferenceModel.from_dict(_communicator_type)

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
