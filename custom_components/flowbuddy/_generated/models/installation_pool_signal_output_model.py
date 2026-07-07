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
        resource_uri (str | Unset):
        external_id (str | Unset):
        value (str | Unset):
        installation_pool (InstallationPoolReferenceModel | Unset):
        control_type (ControlTypeReferenceModel | Unset):
        created (datetime.datetime | None | Unset):
    """

    resource_uri: str | Unset = UNSET
    external_id: str | Unset = UNSET
    value: str | Unset = UNSET
    installation_pool: InstallationPoolReferenceModel | Unset = UNSET
    control_type: ControlTypeReferenceModel | Unset = UNSET
    created: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.control_type_reference_model import ControlTypeReferenceModel
        from ..models.installation_pool_reference_model import InstallationPoolReferenceModel

        resource_uri = self.resource_uri

        external_id = self.external_id

        value = self.value

        installation_pool: dict[str, Any] | Unset = UNSET
        if not isinstance(self.installation_pool, Unset):
            installation_pool = self.installation_pool.to_dict()

        control_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.control_type, Unset):
            control_type = self.control_type.to_dict()

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
        resource_uri = d.pop("resourceUri", UNSET)

        external_id = d.pop("externalId", UNSET)

        value = d.pop("value", UNSET)

        _installation_pool = d.pop("installationPool", UNSET)
        installation_pool: InstallationPoolReferenceModel | Unset
        if isinstance(_installation_pool, Unset):
            installation_pool = UNSET
        else:
            installation_pool = InstallationPoolReferenceModel.from_dict(_installation_pool)

        _control_type = d.pop("controlType", UNSET)
        control_type: ControlTypeReferenceModel | Unset
        if isinstance(_control_type, Unset):
            control_type = UNSET
        else:
            control_type = ControlTypeReferenceModel.from_dict(_control_type)

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
