from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.api_meter_type_reference_model import ApiMeterTypeReferenceModel


T = TypeVar("T", bound="ApiAccountOutputModel")


@_attrs_define
class ApiAccountOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        name (str | Unset):
        external_id (str | Unset):
        api_meter_type (ApiMeterTypeReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    name: str | Unset = UNSET
    external_id: str | Unset = UNSET
    api_meter_type: ApiMeterTypeReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_meter_type_reference_model import ApiMeterTypeReferenceModel

        resource_uri = self.resource_uri

        name = self.name

        external_id = self.external_id

        api_meter_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.api_meter_type, Unset):
            api_meter_type = self.api_meter_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if name is not UNSET:
            field_dict["name"] = name
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if api_meter_type is not UNSET:
            field_dict["apiMeterType"] = api_meter_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_meter_type_reference_model import ApiMeterTypeReferenceModel

        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

        name = d.pop("name", UNSET)

        external_id = d.pop("externalId", UNSET)

        _api_meter_type = d.pop("apiMeterType", UNSET)
        api_meter_type: ApiMeterTypeReferenceModel | Unset
        if isinstance(_api_meter_type, Unset):
            api_meter_type = UNSET
        else:
            api_meter_type = ApiMeterTypeReferenceModel.from_dict(_api_meter_type)

        api_account_output_model = cls(
            resource_uri=resource_uri,
            name=name,
            external_id=external_id,
            api_meter_type=api_meter_type,
        )

        api_account_output_model.additional_properties = d
        return api_account_output_model

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
