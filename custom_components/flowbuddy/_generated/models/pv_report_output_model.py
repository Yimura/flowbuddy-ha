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
        resource_uri (str | Unset):
        create_report (str | Unset):
        last_report_sent_date (datetime.datetime | Unset):
        external_id (str | Unset):
        installation (InstallationReferenceModel | Unset):
        template (NotifierTemplateReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    create_report: str | Unset = UNSET
    last_report_sent_date: datetime.datetime | Unset = UNSET
    external_id: str | Unset = UNSET
    installation: InstallationReferenceModel | Unset = UNSET
    template: NotifierTemplateReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_reference_model import InstallationReferenceModel
        from ..models.notifier_template_reference_model import NotifierTemplateReferenceModel

        resource_uri = self.resource_uri

        create_report = self.create_report

        last_report_sent_date: str | Unset = UNSET
        if not isinstance(self.last_report_sent_date, Unset):
            last_report_sent_date = self.last_report_sent_date.isoformat()

        external_id = self.external_id

        installation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.installation, Unset):
            installation = self.installation.to_dict()

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

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
        resource_uri = d.pop("resourceUri", UNSET)

        create_report = d.pop("createReport", UNSET)

        _last_report_sent_date = d.pop("lastReportSentDate", UNSET)
        last_report_sent_date: datetime.datetime | Unset
        if isinstance(_last_report_sent_date, Unset):
            last_report_sent_date = UNSET
        else:
            last_report_sent_date = datetime.datetime.fromisoformat(_last_report_sent_date)

        external_id = d.pop("externalId", UNSET)

        _installation = d.pop("installation", UNSET)
        installation: InstallationReferenceModel | Unset
        if isinstance(_installation, Unset):
            installation = UNSET
        else:
            installation = InstallationReferenceModel.from_dict(_installation)

        _template = d.pop("template", UNSET)
        template: NotifierTemplateReferenceModel | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = NotifierTemplateReferenceModel.from_dict(_template)

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
