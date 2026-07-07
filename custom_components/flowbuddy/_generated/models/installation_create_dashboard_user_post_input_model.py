from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.installation_create_dashboard_user_post_input_model_other_properties_type_0 import (
        InstallationCreateDashboardUserPostInputModelOtherPropertiesType0,
    )


T = TypeVar("T", bound="InstallationCreateDashboardUserPostInputModel")


@_attrs_define
class InstallationCreateDashboardUserPostInputModel:
    """
    Attributes:
        notifier_template (None | str | Unset): link to mail template that will be used
        other_properties (InstallationCreateDashboardUserPostInputModelOtherPropertiesType0 | None | Unset):
    """

    notifier_template: None | str | Unset = UNSET
    other_properties: (
        InstallationCreateDashboardUserPostInputModelOtherPropertiesType0 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_create_dashboard_user_post_input_model_other_properties_type_0 import (
            InstallationCreateDashboardUserPostInputModelOtherPropertiesType0,
        )

        notifier_template: None | str | Unset
        if isinstance(self.notifier_template, Unset):
            notifier_template = UNSET
        else:
            notifier_template = self.notifier_template

        other_properties: dict[str, Any] | None | Unset
        if isinstance(self.other_properties, Unset):
            other_properties = UNSET
        elif isinstance(
            self.other_properties, InstallationCreateDashboardUserPostInputModelOtherPropertiesType0
        ):
            other_properties = self.other_properties.to_dict()
        else:
            other_properties = self.other_properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notifier_template is not UNSET:
            field_dict["notifierTemplate"] = notifier_template
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.installation_create_dashboard_user_post_input_model_other_properties_type_0 import (
            InstallationCreateDashboardUserPostInputModelOtherPropertiesType0,
        )

        d = dict(src_dict)

        def _parse_notifier_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notifier_template = _parse_notifier_template(d.pop("notifierTemplate", UNSET))

        def _parse_other_properties(
            data: object,
        ) -> InstallationCreateDashboardUserPostInputModelOtherPropertiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_properties_type_0 = (
                    InstallationCreateDashboardUserPostInputModelOtherPropertiesType0.from_dict(
                        data
                    )
                )

                return other_properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InstallationCreateDashboardUserPostInputModelOtherPropertiesType0 | None | Unset,
                data,
            )

        other_properties = _parse_other_properties(d.pop("otherProperties", UNSET))

        installation_create_dashboard_user_post_input_model = cls(
            notifier_template=notifier_template,
            other_properties=other_properties,
        )

        installation_create_dashboard_user_post_input_model.additional_properties = d
        return installation_create_dashboard_user_post_input_model

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
