from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.notifier_template_output_model import NotifierTemplateOutputModel


T = TypeVar("T", bound="NotifierTemplateOutputListModel")


@_attrs_define
class NotifierTemplateOutputListModel:
    """
    Attributes:
        notifier_templates (list[NotifierTemplateOutputModel] | Unset):
    """

    notifier_templates: list[NotifierTemplateOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.notifier_template_output_model import NotifierTemplateOutputModel

        notifier_templates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notifier_templates, Unset):
            notifier_templates = []
            for notifier_templates_item_data in self.notifier_templates:
                notifier_templates_item = notifier_templates_item_data.to_dict()
                notifier_templates.append(notifier_templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notifier_templates is not UNSET:
            field_dict["notifierTemplates"] = notifier_templates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notifier_template_output_model import NotifierTemplateOutputModel

        d = dict(src_dict)
        _notifier_templates = d.pop("notifierTemplates", UNSET)
        notifier_templates: list[NotifierTemplateOutputModel] | Unset = UNSET
        if _notifier_templates is not UNSET:
            notifier_templates = []
            for notifier_templates_item_data in _notifier_templates:
                notifier_templates_item = NotifierTemplateOutputModel.from_dict(
                    notifier_templates_item_data
                )

                notifier_templates.append(notifier_templates_item)

        notifier_template_output_list_model = cls(
            notifier_templates=notifier_templates,
        )

        notifier_template_output_list_model.additional_properties = d
        return notifier_template_output_list_model

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
