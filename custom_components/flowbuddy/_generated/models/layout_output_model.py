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
        resource_uri (str | Unset):
        orientation (int | Unset): Orientation of the installed solar panels, 0 is North, 90 is East, 180 is South, and
            270 is West.
        tilt (int | Unset): Tilt of the installed solar panels, 0 is horizontal, and 90 is vertical.
        wattpeak (float | Unset): Maximum power of installad solar panels. Expressed in Wp.
        expected_production (float | Unset): Expected energy production in one year for this specific installation. Can
            also be used to register the guaranteed production.
        cspi_enabled (bool | Unset): Enable this to activate the CSPI algorithm. Orientation, tilt, wattpeak and
            location/zip should be filled in before your installation can be analyzed.
        string_number (str | Unset):
        number_of_panels (int | Unset):
        wattpeak_per_panel (float | Unset):
        panel_brand (str | Unset):
        panel_type (str | Unset):
        panel_classification (str | Unset): Type of silicon solar cell that is used.
        panel_serial_numbers (str | Unset):
        panel_cell_area (str | Unset):
        max_inverter_power (str | Unset):
        inverter_type (str | Unset):
        inverter_brand (str | Unset):
        inverter_serial_numbers (str | Unset):
        inverter_classification (str | Unset): Type of inverter that is used. e.g. micro-inverter, string-inverter
        panel_location (str | Unset):
        external_id (str | Unset):
        last_changed_on (datetime.datetime | None | Unset):
        meter (MeterReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
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
    external_id: str | Unset = UNSET
    last_changed_on: datetime.datetime | None | Unset = UNSET
    meter: MeterReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meter_reference_model import MeterReferenceModel

        resource_uri = self.resource_uri

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

        external_id = self.external_id

        last_changed_on: None | str | Unset
        if isinstance(self.last_changed_on, Unset):
            last_changed_on = UNSET
        elif isinstance(self.last_changed_on, datetime.datetime):
            last_changed_on = self.last_changed_on.isoformat()
        else:
            last_changed_on = self.last_changed_on

        meter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meter, Unset):
            meter = self.meter.to_dict()

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
        resource_uri = d.pop("resourceUri", UNSET)

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

        external_id = d.pop("externalId", UNSET)

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

        _meter = d.pop("meter", UNSET)
        meter: MeterReferenceModel | Unset
        if isinstance(_meter, Unset):
            meter = UNSET
        else:
            meter = MeterReferenceModel.from_dict(_meter)

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
