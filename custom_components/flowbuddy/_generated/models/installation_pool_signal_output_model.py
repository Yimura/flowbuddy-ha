from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.control_type_reference_model import ControlTypeReferenceModel
    from ..models.installation_pool_reference_model import InstallationPoolReferenceModel


T = TypeVar("T", bound="InstallationPoolSignalOutputModel")


@_attrs_define
class InstallationPoolSignalOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        external_id (None | str | Unset):
        value (None | str | Unset):
        installation_pool (InstallationPoolReferenceModel | None | Unset):
        control_type (ControlTypeReferenceModel | None | Unset):
        created (datetime.datetime | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    value: None | str | Unset = UNSET
    installation_pool: InstallationPoolReferenceModel | None | Unset = UNSET
    control_type: ControlTypeReferenceModel | None | Unset = UNSET
    created: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.control_type_reference_model import ControlTypeReferenceModel
        from ..models.installation_pool_reference_model import InstallationPoolReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        installation_pool: dict[str, Any] | None | Unset
        if isinstance(self.installation_pool, Unset):
            installation_pool = UNSET
        elif isinstance(self.installation_pool, InstallationPoolReferenceModel):
            installation_pool = self.installation_pool.to_dict()
        else:
            installation_pool = self.installation_pool

        control_type: dict[str, Any] | None | Unset
        if isinstance(self.control_type, Unset):
            control_type = UNSET
        elif isinstance(self.control_type, ControlTypeReferenceModel):
            control_type = self.control_type.to_dict()
        else:
            control_type = self.control_type

        created: None | str | Unset
        if isinstance(self.created, Unset):
            created = UNSET
        elif isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if value is not UNSET:
            field_dict["value"] = value
        if installation_pool is not UNSET:
            field_dict["installationPool"] = installation_pool
        if control_type is not UNSET:
            field_dict["controlType"] = control_type
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.control_type_reference_model import ControlTypeReferenceModel
        from ..models.installation_pool_reference_model import InstallationPoolReferenceModel

        d = dict(src_dict)

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_installation_pool(data: object) -> InstallationPoolReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                installation_pool_type_1 = InstallationPoolReferenceModel.from_dict(data)

                return installation_pool_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InstallationPoolReferenceModel | None | Unset, data)

        installation_pool = _parse_installation_pool(d.pop("installationPool", UNSET))

        def _parse_control_type(data: object) -> ControlTypeReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                control_type_type_1 = ControlTypeReferenceModel.from_dict(data)

                return control_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ControlTypeReferenceModel | None | Unset, data)

        control_type = _parse_control_type(d.pop("controlType", UNSET))

        def _parse_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = datetime.datetime.fromisoformat(data)

                return created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created = _parse_created(d.pop("created", UNSET))

        installation_pool_signal_output_model = cls(
            resource_uri=resource_uri,
            external_id=external_id,
            value=value,
            installation_pool=installation_pool,
            control_type=control_type,
            created=created,
        )

        installation_pool_signal_output_model.additional_properties = d
        return installation_pool_signal_output_model

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
