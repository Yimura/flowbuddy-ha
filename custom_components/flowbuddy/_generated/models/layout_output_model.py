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
    from ..models.meter_reference_model import MeterReferenceModel


T = TypeVar("T", bound="LayoutOutputModel")


@_attrs_define
class LayoutOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        orientation (int | None | Unset): Orientation of the installed solar panels, 0 is North, 90 is East, 180 is
            South, and 270 is West.
        tilt (int | None | Unset): Tilt of the installed solar panels, 0 is horizontal, and 90 is vertical.
        wattpeak (float | None | Unset): Maximum power of installad solar panels. Expressed in Wp.
        expected_production (float | None | Unset): Expected energy production in one year for this specific
            installation. Can also be used to register the guaranteed production.
        cspi_enabled (bool | None | Unset): Enable this to activate the CSPI algorithm. Orientation, tilt, wattpeak and
            location/zip should be filled in before your installation can be analyzed.
        string_number (None | str | Unset):
        number_of_panels (int | None | Unset):
        wattpeak_per_panel (float | None | Unset):
        panel_brand (None | str | Unset):
        panel_type (None | str | Unset):
        panel_classification (None | str | Unset): Type of silicon solar cell that is used.
        panel_serial_numbers (None | str | Unset):
        panel_cell_area (None | str | Unset):
        max_inverter_power (None | str | Unset):
        inverter_type (None | str | Unset):
        inverter_brand (None | str | Unset):
        inverter_serial_numbers (None | str | Unset):
        inverter_classification (None | str | Unset): Type of inverter that is used. e.g. micro-inverter, string-
            inverter
        panel_location (None | str | Unset):
        external_id (None | str | Unset):
        last_changed_on (datetime.datetime | None | Unset):
        meter (MeterReferenceModel | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
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
    external_id: None | str | Unset = UNSET
    last_changed_on: datetime.datetime | None | Unset = UNSET
    meter: MeterReferenceModel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meter_reference_model import MeterReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

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

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        last_changed_on: None | str | Unset
        if isinstance(self.last_changed_on, Unset):
            last_changed_on = UNSET
        elif isinstance(self.last_changed_on, datetime.datetime):
            last_changed_on = self.last_changed_on.isoformat()
        else:
            last_changed_on = self.last_changed_on

        meter: dict[str, Any] | None | Unset
        if isinstance(self.meter, Unset):
            meter = UNSET
        elif isinstance(self.meter, MeterReferenceModel):
            meter = self.meter.to_dict()
        else:
            meter = self.meter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
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
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if last_changed_on is not UNSET:
            field_dict["lastChangedOn"] = last_changed_on
        if meter is not UNSET:
            field_dict["meter"] = meter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meter_reference_model import MeterReferenceModel

        d = dict(src_dict)

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

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

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_last_changed_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_changed_on_type_0 = datetime.datetime.fromisoformat(data)

                return last_changed_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_changed_on = _parse_last_changed_on(d.pop("lastChangedOn", UNSET))

        def _parse_meter(data: object) -> MeterReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meter_type_1 = MeterReferenceModel.from_dict(data)

                return meter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MeterReferenceModel | None | Unset, data)

        meter = _parse_meter(d.pop("meter", UNSET))

        layout_output_model = cls(
            resource_uri=resource_uri,
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
            external_id=external_id,
            last_changed_on=last_changed_on,
            meter=meter,
        )

        layout_output_model.additional_properties = d
        return layout_output_model

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
