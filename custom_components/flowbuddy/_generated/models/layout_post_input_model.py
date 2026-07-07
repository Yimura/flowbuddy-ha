from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.layout_post_input_model_other_properties_type_0 import (
        LayoutPostInputModelOtherPropertiesType0,
    )


T = TypeVar("T", bound="LayoutPostInputModel")


@_attrs_define
class LayoutPostInputModel:
    """
    Attributes:
        meter (None | str | Unset):
        orientation (int | None | Unset):
        tilt (int | None | Unset):
        wattpeak (float | None | Unset):
        expected_production (float | None | Unset):
        cspi_enabled (bool | None | Unset):
        string_number (None | str | Unset):
        number_of_panels (int | None | Unset):
        wattpeak_per_panel (float | None | Unset):
        panel_brand (None | str | Unset):
        panel_type (None | str | Unset):
        panel_classification (None | str | Unset):
        panel_serial_numbers (None | str | Unset):
        panel_cell_area (None | str | Unset):
        max_inverter_power (None | str | Unset):
        inverter_type (None | str | Unset):
        inverter_brand (None | str | Unset):
        inverter_serial_numbers (None | str | Unset):
        inverter_classification (None | str | Unset):
        panel_location (None | str | Unset):
        other_properties (LayoutPostInputModelOtherPropertiesType0 | None | Unset):
    """

    meter: None | str | Unset = UNSET
    orientation: int | None | Unset = UNSET
    tilt: int | None | Unset = UNSET
    wattpeak: float | None | Unset = UNSET
    expected_production: float | None | Unset = UNSET
    cspi_enabled: bool | None | Unset = UNSET
    string_number: None | str | Unset = UNSET
    number_of_panels: int | None | Unset = UNSET
    wattpeak_per_panel: float | None | Unset = UNSET
    panel_brand: None | str | Unset = UNSET
    panel_type: None | str | Unset = UNSET
    panel_classification: None | str | Unset = UNSET
    panel_serial_numbers: None | str | Unset = UNSET
    panel_cell_area: None | str | Unset = UNSET
    max_inverter_power: None | str | Unset = UNSET
    inverter_type: None | str | Unset = UNSET
    inverter_brand: None | str | Unset = UNSET
    inverter_serial_numbers: None | str | Unset = UNSET
    inverter_classification: None | str | Unset = UNSET
    panel_location: None | str | Unset = UNSET
    other_properties: LayoutPostInputModelOtherPropertiesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.layout_post_input_model_other_properties_type_0 import (
            LayoutPostInputModelOtherPropertiesType0,
        )

        meter: None | str | Unset
        if isinstance(self.meter, Unset):
            meter = UNSET
        else:
            meter = self.meter

        orientation: int | None | Unset
        if isinstance(self.orientation, Unset):
            orientation = UNSET
        else:
            orientation = self.orientation

        tilt: int | None | Unset
        if isinstance(self.tilt, Unset):
            tilt = UNSET
        else:
            tilt = self.tilt

        wattpeak: float | None | Unset
        if isinstance(self.wattpeak, Unset):
            wattpeak = UNSET
        else:
            wattpeak = self.wattpeak

        expected_production: float | None | Unset
        if isinstance(self.expected_production, Unset):
            expected_production = UNSET
        else:
            expected_production = self.expected_production

        cspi_enabled: bool | None | Unset
        if isinstance(self.cspi_enabled, Unset):
            cspi_enabled = UNSET
        else:
            cspi_enabled = self.cspi_enabled

        string_number: None | str | Unset
        if isinstance(self.string_number, Unset):
            string_number = UNSET
        else:
            string_number = self.string_number

        number_of_panels: int | None | Unset
        if isinstance(self.number_of_panels, Unset):
            number_of_panels = UNSET
        else:
            number_of_panels = self.number_of_panels

        wattpeak_per_panel: float | None | Unset
        if isinstance(self.wattpeak_per_panel, Unset):
            wattpeak_per_panel = UNSET
        else:
            wattpeak_per_panel = self.wattpeak_per_panel

        panel_brand: None | str | Unset
        if isinstance(self.panel_brand, Unset):
            panel_brand = UNSET
        else:
            panel_brand = self.panel_brand

        panel_type: None | str | Unset
        if isinstance(self.panel_type, Unset):
            panel_type = UNSET
        else:
            panel_type = self.panel_type

        panel_classification: None | str | Unset
        if isinstance(self.panel_classification, Unset):
            panel_classification = UNSET
        else:
            panel_classification = self.panel_classification

        panel_serial_numbers: None | str | Unset
        if isinstance(self.panel_serial_numbers, Unset):
            panel_serial_numbers = UNSET
        else:
            panel_serial_numbers = self.panel_serial_numbers

        panel_cell_area: None | str | Unset
        if isinstance(self.panel_cell_area, Unset):
            panel_cell_area = UNSET
        else:
            panel_cell_area = self.panel_cell_area

        max_inverter_power: None | str | Unset
        if isinstance(self.max_inverter_power, Unset):
            max_inverter_power = UNSET
        else:
            max_inverter_power = self.max_inverter_power

        inverter_type: None | str | Unset
        if isinstance(self.inverter_type, Unset):
            inverter_type = UNSET
        else:
            inverter_type = self.inverter_type

        inverter_brand: None | str | Unset
        if isinstance(self.inverter_brand, Unset):
            inverter_brand = UNSET
        else:
            inverter_brand = self.inverter_brand

        inverter_serial_numbers: None | str | Unset
        if isinstance(self.inverter_serial_numbers, Unset):
            inverter_serial_numbers = UNSET
        else:
            inverter_serial_numbers = self.inverter_serial_numbers

        inverter_classification: None | str | Unset
        if isinstance(self.inverter_classification, Unset):
            inverter_classification = UNSET
        else:
            inverter_classification = self.inverter_classification

        panel_location: None | str | Unset
        if isinstance(self.panel_location, Unset):
            panel_location = UNSET
        else:
            panel_location = self.panel_location

        other_properties: dict[str, Any] | None | Unset
        if isinstance(self.other_properties, Unset):
            other_properties = UNSET
        elif isinstance(self.other_properties, LayoutPostInputModelOtherPropertiesType0):
            other_properties = self.other_properties.to_dict()
        else:
            other_properties = self.other_properties

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
        from ..models.layout_post_input_model_other_properties_type_0 import (
            LayoutPostInputModelOtherPropertiesType0,
        )

        d = dict(src_dict)

        def _parse_meter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meter = _parse_meter(d.pop("meter", UNSET))

        def _parse_orientation(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        orientation = _parse_orientation(d.pop("orientation", UNSET))

        def _parse_tilt(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tilt = _parse_tilt(d.pop("tilt", UNSET))

        def _parse_wattpeak(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wattpeak = _parse_wattpeak(d.pop("wattpeak", UNSET))

        def _parse_expected_production(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        expected_production = _parse_expected_production(d.pop("expectedProduction", UNSET))

        def _parse_cspi_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        cspi_enabled = _parse_cspi_enabled(d.pop("cspiEnabled", UNSET))

        def _parse_string_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        string_number = _parse_string_number(d.pop("stringNumber", UNSET))

        def _parse_number_of_panels(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_panels = _parse_number_of_panels(d.pop("numberOfPanels", UNSET))

        def _parse_wattpeak_per_panel(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wattpeak_per_panel = _parse_wattpeak_per_panel(d.pop("wattpeakPerPanel", UNSET))

        def _parse_panel_brand(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        panel_brand = _parse_panel_brand(d.pop("panelBrand", UNSET))

        def _parse_panel_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        panel_type = _parse_panel_type(d.pop("panelType", UNSET))

        def _parse_panel_classification(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        panel_classification = _parse_panel_classification(d.pop("panelClassification", UNSET))

        def _parse_panel_serial_numbers(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        panel_serial_numbers = _parse_panel_serial_numbers(d.pop("panelSerialNumbers", UNSET))

        def _parse_panel_cell_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        panel_cell_area = _parse_panel_cell_area(d.pop("panelCellArea", UNSET))

        def _parse_max_inverter_power(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_inverter_power = _parse_max_inverter_power(d.pop("maxInverterPower", UNSET))

        def _parse_inverter_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inverter_type = _parse_inverter_type(d.pop("inverterType", UNSET))

        def _parse_inverter_brand(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inverter_brand = _parse_inverter_brand(d.pop("inverterBrand", UNSET))

        def _parse_inverter_serial_numbers(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inverter_serial_numbers = _parse_inverter_serial_numbers(
            d.pop("inverterSerialNumbers", UNSET)
        )

        def _parse_inverter_classification(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inverter_classification = _parse_inverter_classification(
            d.pop("inverterClassification", UNSET)
        )

        def _parse_panel_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        panel_location = _parse_panel_location(d.pop("panelLocation", UNSET))

        def _parse_other_properties(
            data: object,
        ) -> LayoutPostInputModelOtherPropertiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_properties_type_0 = LayoutPostInputModelOtherPropertiesType0.from_dict(data)

                return other_properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LayoutPostInputModelOtherPropertiesType0 | None | Unset, data)

        other_properties = _parse_other_properties(d.pop("otherProperties", UNSET))

        layout_post_input_model = cls(
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

        layout_post_input_model.additional_properties = d
        return layout_post_input_model

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
