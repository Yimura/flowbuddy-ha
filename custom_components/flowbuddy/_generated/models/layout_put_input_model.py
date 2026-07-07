from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.layout_put_input_model_other_properties import LayoutPutInputModelOtherProperties


T = TypeVar("T", bound="LayoutPutInputModel")


@_attrs_define
class LayoutPutInputModel:
    """
    Attributes:
        meter (str | Unset):
        orientation (int | Unset):
        tilt (int | Unset):
        wattpeak (float | Unset):
        expected_production (float | Unset):
        cspi_enabled (bool | Unset):
        string_number (str | Unset):
        number_of_panels (int | Unset):
        wattpeak_per_panel (float | Unset):
        panel_brand (str | Unset):
        panel_type (str | Unset):
        panel_classification (str | Unset):
        panel_serial_numbers (str | Unset):
        panel_cell_area (str | Unset):
        max_inverter_power (str | Unset):
        inverter_type (str | Unset):
        inverter_brand (str | Unset):
        inverter_serial_numbers (str | Unset):
        inverter_classification (str | Unset):
        panel_location (str | Unset):
        other_properties (LayoutPutInputModelOtherProperties | Unset):
    """

    meter: str | Unset = UNSET
    orientation: int | Unset = UNSET
    tilt: int | Unset = UNSET
    wattpeak: float | Unset = UNSET
    expected_production: float | Unset = UNSET
    cspi_enabled: bool | Unset = UNSET
    string_number: str | Unset = UNSET
    number_of_panels: int | Unset = UNSET
    wattpeak_per_panel: float | Unset = UNSET
    panel_brand: str | Unset = UNSET
    panel_type: str | Unset = UNSET
    panel_classification: str | Unset = UNSET
    panel_serial_numbers: str | Unset = UNSET
    panel_cell_area: str | Unset = UNSET
    max_inverter_power: str | Unset = UNSET
    inverter_type: str | Unset = UNSET
    inverter_brand: str | Unset = UNSET
    inverter_serial_numbers: str | Unset = UNSET
    inverter_classification: str | Unset = UNSET
    panel_location: str | Unset = UNSET
    other_properties: LayoutPutInputModelOtherProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.layout_put_input_model_other_properties import (
            LayoutPutInputModelOtherProperties,
        )

        meter = self.meter

        orientation = self.orientation

        tilt = self.tilt

        wattpeak = self.wattpeak

        expected_production = self.expected_production

        cspi_enabled = self.cspi_enabled

        string_number = self.string_number

        number_of_panels = self.number_of_panels

        wattpeak_per_panel = self.wattpeak_per_panel

        panel_brand = self.panel_brand

        panel_type = self.panel_type

        panel_classification = self.panel_classification

        panel_serial_numbers = self.panel_serial_numbers

        panel_cell_area = self.panel_cell_area

        max_inverter_power = self.max_inverter_power

        inverter_type = self.inverter_type

        inverter_brand = self.inverter_brand

        inverter_serial_numbers = self.inverter_serial_numbers

        inverter_classification = self.inverter_classification

        panel_location = self.panel_location

        other_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_properties, Unset):
            other_properties = self.other_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meter is not UNSET:
            field_dict["meter"] = meter
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if tilt is not UNSET:
            field_dict["tilt"] = tilt
        if wattpeak is not UNSET:
            field_dict["wattpeak"] = wattpeak
        if expected_production is not UNSET:
            field_dict["expectedProduction"] = expected_production
        if cspi_enabled is not UNSET:
            field_dict["cspiEnabled"] = cspi_enabled
        if string_number is not UNSET:
            field_dict["stringNumber"] = string_number
        if number_of_panels is not UNSET:
            field_dict["numberOfPanels"] = number_of_panels
        if wattpeak_per_panel is not UNSET:
            field_dict["wattpeakPerPanel"] = wattpeak_per_panel
        if panel_brand is not UNSET:
            field_dict["panelBrand"] = panel_brand
        if panel_type is not UNSET:
            field_dict["panelType"] = panel_type
        if panel_classification is not UNSET:
            field_dict["panelClassification"] = panel_classification
        if panel_serial_numbers is not UNSET:
            field_dict["panelSerialNumbers"] = panel_serial_numbers
        if panel_cell_area is not UNSET:
            field_dict["panelCellArea"] = panel_cell_area
        if max_inverter_power is not UNSET:
            field_dict["maxInverterPower"] = max_inverter_power
        if inverter_type is not UNSET:
            field_dict["inverterType"] = inverter_type
        if inverter_brand is not UNSET:
            field_dict["inverterBrand"] = inverter_brand
        if inverter_serial_numbers is not UNSET:
            field_dict["inverterSerialNumbers"] = inverter_serial_numbers
        if inverter_classification is not UNSET:
            field_dict["inverterClassification"] = inverter_classification
        if panel_location is not UNSET:
            field_dict["panelLocation"] = panel_location
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.layout_put_input_model_other_properties import (
            LayoutPutInputModelOtherProperties,
        )

        d = dict(src_dict)
        meter = d.pop("meter", UNSET)

        orientation = d.pop("orientation", UNSET)

        tilt = d.pop("tilt", UNSET)

        wattpeak = d.pop("wattpeak", UNSET)

        expected_production = d.pop("expectedProduction", UNSET)

        cspi_enabled = d.pop("cspiEnabled", UNSET)

        string_number = d.pop("stringNumber", UNSET)

        number_of_panels = d.pop("numberOfPanels", UNSET)

        wattpeak_per_panel = d.pop("wattpeakPerPanel", UNSET)

        panel_brand = d.pop("panelBrand", UNSET)

        panel_type = d.pop("panelType", UNSET)

        panel_classification = d.pop("panelClassification", UNSET)

        panel_serial_numbers = d.pop("panelSerialNumbers", UNSET)

        panel_cell_area = d.pop("panelCellArea", UNSET)

        max_inverter_power = d.pop("maxInverterPower", UNSET)

        inverter_type = d.pop("inverterType", UNSET)

        inverter_brand = d.pop("inverterBrand", UNSET)

        inverter_serial_numbers = d.pop("inverterSerialNumbers", UNSET)

        inverter_classification = d.pop("inverterClassification", UNSET)

        panel_location = d.pop("panelLocation", UNSET)

        _other_properties = d.pop("otherProperties", UNSET)
        other_properties: LayoutPutInputModelOtherProperties | Unset
        if isinstance(_other_properties, Unset):
            other_properties = UNSET
        else:
            other_properties = LayoutPutInputModelOtherProperties.from_dict(_other_properties)

        layout_put_input_model = cls(
            meter=meter,
            orientation=orientation,
            tilt=tilt,
            wattpeak=wattpeak,
            expected_production=expected_production,
            cspi_enabled=cspi_enabled,
            string_number=string_number,
            number_of_panels=number_of_panels,
            wattpeak_per_panel=wattpeak_per_panel,
            panel_brand=panel_brand,
            panel_type=panel_type,
            panel_classification=panel_classification,
            panel_serial_numbers=panel_serial_numbers,
            panel_cell_area=panel_cell_area,
            max_inverter_power=max_inverter_power,
            inverter_type=inverter_type,
            inverter_brand=inverter_brand,
            inverter_serial_numbers=inverter_serial_numbers,
            inverter_classification=inverter_classification,
            panel_location=panel_location,
            other_properties=other_properties,
        )

        layout_put_input_model.additional_properties = d
        return layout_put_input_model

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
