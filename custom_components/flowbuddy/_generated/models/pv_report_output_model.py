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
    from ..models.installation_reference_model import InstallationReferenceModel
    from ..models.notifier_template_reference_model import NotifierTemplateReferenceModel


T = TypeVar("T", bound="PvReportOutputModel")


@_attrs_define
class PvReportOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        create_report (None | str | Unset):
        last_report_sent_date (datetime.datetime | None | Unset):
        external_id (None | str | Unset):
        installation (InstallationReferenceModel | None | Unset):
        template (None | NotifierTemplateReferenceModel | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    create_report: None | str | Unset = UNSET
    last_report_sent_date: datetime.datetime | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    installation: InstallationReferenceModel | None | Unset = UNSET
    template: None | NotifierTemplateReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_reference_model import InstallationReferenceModel
        from ..models.notifier_template_reference_model import NotifierTemplateReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        create_report: None | str | Unset
        if isinstance(self.create_report, Unset):
            create_report = UNSET
        else:
            create_report = self.create_report

        last_report_sent_date: None | str | Unset
        if isinstance(self.last_report_sent_date, Unset):
            last_report_sent_date = UNSET
        elif isinstance(self.last_report_sent_date, datetime.datetime):
            last_report_sent_date = self.last_report_sent_date.isoformat()
        else:
            last_report_sent_date = self.last_report_sent_date

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        installation: dict[str, Any] | None | Unset
        if isinstance(self.installation, Unset):
            installation = UNSET
        elif isinstance(self.installation, InstallationReferenceModel):
            installation = self.installation.to_dict()
        else:
            installation = self.installation

        template: dict[str, Any] | None | Unset
        if isinstance(self.template, Unset):
            template = UNSET
        elif isinstance(self.template, NotifierTemplateReferenceModel):
            template = self.template.to_dict()
        else:
            template = self.template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if create_report is not UNSET:
            field_dict["createReport"] = create_report
        if last_report_sent_date is not UNSET:
            field_dict["lastReportSentDate"] = last_report_sent_date
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if installation is not UNSET:
            field_dict["installation"] = installation
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.installation_reference_model import InstallationReferenceModel
        from ..models.notifier_template_reference_model import NotifierTemplateReferenceModel

        d = dict(src_dict)

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

        def _parse_create_report(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        create_report = _parse_create_report(d.pop("createReport", UNSET))

        def _parse_last_report_sent_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_report_sent_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_report_sent_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_report_sent_date = _parse_last_report_sent_date(d.pop("lastReportSentDate", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_installation(data: object) -> InstallationReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                installation_type_1 = InstallationReferenceModel.from_dict(data)

                return installation_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InstallationReferenceModel | None | Unset, data)

        installation = _parse_installation(d.pop("installation", UNSET))

        def _parse_template(data: object) -> None | NotifierTemplateReferenceModel | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                template_type_1 = NotifierTemplateReferenceModel.from_dict(data)

                return template_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NotifierTemplateReferenceModel | Unset, data)

        template = _parse_template(d.pop("template", UNSET))

        pv_report_output_model = cls(
            resource_uri=resource_uri,
            create_report=create_report,
            last_report_sent_date=last_report_sent_date,
            external_id=external_id,
            installation=installation,
            template=template,
        )

        pv_report_output_model.additional_properties = d
        return pv_report_output_model

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
