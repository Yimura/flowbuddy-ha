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
        resource_uri (None | str | Unset):
        serial_number (None | str | Unset):
        status (None | str | Unset):
        external_id (None | str | Unset):
        communicator (CommunicatorReferenceModel | None | Unset):
        is_communicator_device (bool | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    serial_number: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    communicator: CommunicatorReferenceModel | None | Unset = UNSET
    is_communicator_device: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_reference_model import CommunicatorReferenceModel

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

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        communicator: dict[str, Any] | None | Unset
        if isinstance(self.communicator, Unset):
            communicator = UNSET
        elif isinstance(self.communicator, CommunicatorReferenceModel):
            communicator = self.communicator.to_dict()
        else:
            communicator = self.communicator

        is_communicator_device: bool | None | Unset
        if isinstance(self.is_communicator_device, Unset):
            is_communicator_device = UNSET
        else:
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

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_communicator(data: object) -> CommunicatorReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                communicator_type_1 = CommunicatorReferenceModel.from_dict(data)

                return communicator_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CommunicatorReferenceModel | None | Unset, data)

        communicator = _parse_communicator(d.pop("communicator", UNSET))

        def _parse_is_communicator_device(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_communicator_device = _parse_is_communicator_device(d.pop("isCommunicatorDevice", UNSET))

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
