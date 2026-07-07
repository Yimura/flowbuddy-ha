from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.communicator_reference_model import CommunicatorReferenceModel


T = TypeVar("T", bound="MeasuringDeviceOutputModel")


@_attrs_define
class MeasuringDeviceOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        serial_number (str | Unset):
        status (str | Unset):
        external_id (str | Unset):
        communicator (CommunicatorReferenceModel | Unset):
        is_communicator_device (bool | Unset):
    """

    resource_uri: str | Unset = UNSET
    serial_number: str | Unset = UNSET
    status: str | Unset = UNSET
    external_id: str | Unset = UNSET
    communicator: CommunicatorReferenceModel | Unset = UNSET
    is_communicator_device: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_reference_model import CommunicatorReferenceModel

        resource_uri = self.resource_uri

        serial_number = self.serial_number

        status = self.status

        external_id = self.external_id

        communicator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.communicator, Unset):
            communicator = self.communicator.to_dict()

        is_communicator_device = self.is_communicator_device

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if status is not UNSET:
            field_dict["status"] = status
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if communicator is not UNSET:
            field_dict["communicator"] = communicator
        if is_communicator_device is not UNSET:
            field_dict["isCommunicatorDevice"] = is_communicator_device

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communicator_reference_model import CommunicatorReferenceModel

        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        status = d.pop("status", UNSET)

        external_id = d.pop("externalId", UNSET)

        _communicator = d.pop("communicator", UNSET)
        communicator: CommunicatorReferenceModel | Unset
        if isinstance(_communicator, Unset):
            communicator = UNSET
        else:
            communicator = CommunicatorReferenceModel.from_dict(_communicator)

        is_communicator_device = d.pop("isCommunicatorDevice", UNSET)

        measuring_device_output_model = cls(
            resource_uri=resource_uri,
            serial_number=serial_number,
            status=status,
            external_id=external_id,
            communicator=communicator,
            is_communicator_device=is_communicator_device,
        )

        measuring_device_output_model.additional_properties = d
        return measuring_device_output_model

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
