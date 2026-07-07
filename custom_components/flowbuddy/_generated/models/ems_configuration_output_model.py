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
    from ..models.communicator_reference_model import CommunicatorReferenceModel
    from ..models.energy_tariff_reference_model import EnergyTariffReferenceModel


T = TypeVar("T", bound="EmsConfigurationOutputModel")


@_attrs_define
class EmsConfigurationOutputModel:
    """
    Attributes:
        resource_uri (None | str | Unset):
        enable_inverter_control (bool | None | Unset): Enables the virtual grid meter and allows control over the
            behavior of a hybrid inverter.
        inverter_control_first_activated_on (datetime.datetime | None | Unset): The date when the inverter control was
            first activated.
        battery_capacity (float | None | Unset): The capacity, in kWh, of the installed batteries linked to the EMS.
        battery_power (float | None | Unset): The maximum (dis)charge power, in kW, of the installed batteries linked to
            the EMS.
        enable_ev_charger_control (bool | None | Unset): Enables the EMS app for EV charger control and allows you to
            adjust the charging power based on grid usage and solar production.
        ev_charger_control_first_activated_on (datetime.datetime | None | Unset): The date when the EV charger control
            was first activated.
        ev_number_of_phases (int | None | Unset): Number of phases configured in the EV charger controlled by the EMS.
        max_grid_current (float | None | Unset): Maximum rated current of the grid connection in Amperes.
        min_charge_current (float | None | Unset): Minimum charge current that should be used by the connected EV
            charger in Amperes.
        user_requested_ev_mode (None | str | Unset):
        user_requested_ev_battery_mode (int | None | Unset): Controls battery discharging when EV charging is active: 0
            - Off (battery will not be used to support EV charging), 1 - On.
        user_requested_max_charge_current (float | None | Unset): Maximum charging current (from grid or solar) that can
            be used by the connected EV charger in Amperes.
        user_requested_max_grid_current (float | None | Unset): Maximum charging current (imported from the grid) that
            can be used by the connected EV charger in Amperes.
        enable_peak_shaving (bool | None | Unset): Enables the EMS app for capacity tariff and allows you to limit the
            maximum grid power by adjusting charging powers, activating the battery, or disabling external devices.
        peak_shaving_first_activated_on (datetime.datetime | None | Unset): The date when the peak shaving feature was
            first activated.
        min_battery_charge_soc (int | None | Unset): A value ranging from 0-100 that represents the minimum battery
            charge. This variable is set by the installer to ensure battery health.
        user_requested_max_grid_power (int | None | Unset): The maximum grid power. This variable can be controlled by
            the user.
        user_requested_battery_peak_reserve_soc (int | None | Unset): A value ranging from 0-100 that represents the
            battery reserve used to cover peak electricity usage. This variable can be controlled by the user.
        enable_curtailing (bool | None | Unset):
        enable_realtime (bool | None | Unset): Enables the EMS app for real-time polling.
        realtime_first_activated_on (datetime.datetime | None | Unset): The date when the real-time polling feature was
            first activated.
        enable_dynamic_pricing (bool | None | Unset): Enables EMS apps for dynamic pricing
        dynamic_pricing_first_activated_on (datetime.datetime | None | Unset): The date when the dynamic pricing feature
            was first activated.
        user_requested_lower_price_threshold (float | None | Unset): The threshold for the lower price. This variable
            can be controlled by the user.
        user_requested_upper_price_threshold (float | None | Unset): The threshold for the upper price. This variable
            can be controlled by the user.
        last_calendar_sync_on (datetime.datetime | None | Unset):
        calendar_sync_status (None | str | Unset):
        enable_mbus_reader (bool | None | Unset): Enables the EMS app for reading mbus devices.
        enable_smart_grid_ready_control (bool | None | Unset): Enables the EMS app for smart grid ready control.
        smart_grid_ready_control_first_activated_on (datetime.datetime | None | Unset): The date when the smart grid
            ready control feature was first activated.
        user_requested_deactivate_heat_pump_on_high_prices (bool | None | Unset): Deactivates the heat pump on high
            prices. This variable can be controlled by the user.
        user_requested_activate_heat_pump_on_low_prices (bool | None | Unset): Activates the heat pump on low prices.
            This variable can be controlled by the user.
        increased_threshold (int | None | Unset): Consumption of the heat pump in Watt when it is in increased
            operation.
        forced_threshold (int | None | Unset): Consumption of the heat pump in Watt when it is in forced operation.
        status (None | str | Unset):
        external_id (None | str | Unset):
        phase_switching_disabled (bool | None | Unset):
        dynamic_pricing_tariff (EnergyTariffReferenceModel | None | Unset):
        communicator (CommunicatorReferenceModel | None | Unset):
    """

    resource_uri: None | str | Unset = UNSET
    enable_inverter_control: bool | None | Unset = UNSET
    inverter_control_first_activated_on: datetime.datetime | None | Unset = UNSET
    battery_capacity: float | None | Unset = UNSET
    battery_power: float | None | Unset = UNSET
    enable_ev_charger_control: bool | None | Unset = UNSET
    ev_charger_control_first_activated_on: datetime.datetime | None | Unset = UNSET
    ev_number_of_phases: int | None | Unset = UNSET
    max_grid_current: float | None | Unset = UNSET
    min_charge_current: float | None | Unset = UNSET
    user_requested_ev_mode: None | str | Unset = UNSET
    user_requested_ev_battery_mode: int | None | Unset = UNSET
    user_requested_max_charge_current: float | None | Unset = UNSET
    user_requested_max_grid_current: float | None | Unset = UNSET
    enable_peak_shaving: bool | None | Unset = UNSET
    peak_shaving_first_activated_on: datetime.datetime | None | Unset = UNSET
    min_battery_charge_soc: int | None | Unset = UNSET
    user_requested_max_grid_power: int | None | Unset = UNSET
    user_requested_battery_peak_reserve_soc: int | None | Unset = UNSET
    enable_curtailing: bool | None | Unset = UNSET
    enable_realtime: bool | None | Unset = UNSET
    realtime_first_activated_on: datetime.datetime | None | Unset = UNSET
    enable_dynamic_pricing: bool | None | Unset = UNSET
    dynamic_pricing_first_activated_on: datetime.datetime | None | Unset = UNSET
    user_requested_lower_price_threshold: float | None | Unset = UNSET
    user_requested_upper_price_threshold: float | None | Unset = UNSET
    last_calendar_sync_on: datetime.datetime | None | Unset = UNSET
    calendar_sync_status: None | str | Unset = UNSET
    enable_mbus_reader: bool | None | Unset = UNSET
    enable_smart_grid_ready_control: bool | None | Unset = UNSET
    smart_grid_ready_control_first_activated_on: datetime.datetime | None | Unset = UNSET
    user_requested_deactivate_heat_pump_on_high_prices: bool | None | Unset = UNSET
    user_requested_activate_heat_pump_on_low_prices: bool | None | Unset = UNSET
    increased_threshold: int | None | Unset = UNSET
    forced_threshold: int | None | Unset = UNSET
    status: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    phase_switching_disabled: bool | None | Unset = UNSET
    dynamic_pricing_tariff: EnergyTariffReferenceModel | None | Unset = UNSET
    communicator: CommunicatorReferenceModel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_reference_model import CommunicatorReferenceModel
        from ..models.energy_tariff_reference_model import EnergyTariffReferenceModel

        resource_uri: None | str | Unset
        if isinstance(self.resource_uri, Unset):
            resource_uri = UNSET
        else:
            resource_uri = self.resource_uri

        enable_inverter_control: bool | None | Unset
        if isinstance(self.enable_inverter_control, Unset):
            enable_inverter_control = UNSET
        else:
            enable_inverter_control = self.enable_inverter_control

        inverter_control_first_activated_on: None | str | Unset
        if isinstance(self.inverter_control_first_activated_on, Unset):
            inverter_control_first_activated_on = UNSET
        elif isinstance(self.inverter_control_first_activated_on, datetime.datetime):
            inverter_control_first_activated_on = (
                self.inverter_control_first_activated_on.isoformat()
            )
        else:
            inverter_control_first_activated_on = self.inverter_control_first_activated_on

        battery_capacity: float | None | Unset
        if isinstance(self.battery_capacity, Unset):
            battery_capacity = UNSET
        else:
            battery_capacity = self.battery_capacity

        battery_power: float | None | Unset
        if isinstance(self.battery_power, Unset):
            battery_power = UNSET
        else:
            battery_power = self.battery_power

        enable_ev_charger_control: bool | None | Unset
        if isinstance(self.enable_ev_charger_control, Unset):
            enable_ev_charger_control = UNSET
        else:
            enable_ev_charger_control = self.enable_ev_charger_control

        ev_charger_control_first_activated_on: None | str | Unset
        if isinstance(self.ev_charger_control_first_activated_on, Unset):
            ev_charger_control_first_activated_on = UNSET
        elif isinstance(self.ev_charger_control_first_activated_on, datetime.datetime):
            ev_charger_control_first_activated_on = (
                self.ev_charger_control_first_activated_on.isoformat()
            )
        else:
            ev_charger_control_first_activated_on = self.ev_charger_control_first_activated_on

        ev_number_of_phases: int | None | Unset
        if isinstance(self.ev_number_of_phases, Unset):
            ev_number_of_phases = UNSET
        else:
            ev_number_of_phases = self.ev_number_of_phases

        max_grid_current: float | None | Unset
        if isinstance(self.max_grid_current, Unset):
            max_grid_current = UNSET
        else:
            max_grid_current = self.max_grid_current

        min_charge_current: float | None | Unset
        if isinstance(self.min_charge_current, Unset):
            min_charge_current = UNSET
        else:
            min_charge_current = self.min_charge_current

        user_requested_ev_mode: None | str | Unset
        if isinstance(self.user_requested_ev_mode, Unset):
            user_requested_ev_mode = UNSET
        else:
            user_requested_ev_mode = self.user_requested_ev_mode

        user_requested_ev_battery_mode: int | None | Unset
        if isinstance(self.user_requested_ev_battery_mode, Unset):
            user_requested_ev_battery_mode = UNSET
        else:
            user_requested_ev_battery_mode = self.user_requested_ev_battery_mode

        user_requested_max_charge_current: float | None | Unset
        if isinstance(self.user_requested_max_charge_current, Unset):
            user_requested_max_charge_current = UNSET
        else:
            user_requested_max_charge_current = self.user_requested_max_charge_current

        user_requested_max_grid_current: float | None | Unset
        if isinstance(self.user_requested_max_grid_current, Unset):
            user_requested_max_grid_current = UNSET
        else:
            user_requested_max_grid_current = self.user_requested_max_grid_current

        enable_peak_shaving: bool | None | Unset
        if isinstance(self.enable_peak_shaving, Unset):
            enable_peak_shaving = UNSET
        else:
            enable_peak_shaving = self.enable_peak_shaving

        peak_shaving_first_activated_on: None | str | Unset
        if isinstance(self.peak_shaving_first_activated_on, Unset):
            peak_shaving_first_activated_on = UNSET
        elif isinstance(self.peak_shaving_first_activated_on, datetime.datetime):
            peak_shaving_first_activated_on = self.peak_shaving_first_activated_on.isoformat()
        else:
            peak_shaving_first_activated_on = self.peak_shaving_first_activated_on

        min_battery_charge_soc: int | None | Unset
        if isinstance(self.min_battery_charge_soc, Unset):
            min_battery_charge_soc = UNSET
        else:
            min_battery_charge_soc = self.min_battery_charge_soc

        user_requested_max_grid_power: int | None | Unset
        if isinstance(self.user_requested_max_grid_power, Unset):
            user_requested_max_grid_power = UNSET
        else:
            user_requested_max_grid_power = self.user_requested_max_grid_power

        user_requested_battery_peak_reserve_soc: int | None | Unset
        if isinstance(self.user_requested_battery_peak_reserve_soc, Unset):
            user_requested_battery_peak_reserve_soc = UNSET
        else:
            user_requested_battery_peak_reserve_soc = self.user_requested_battery_peak_reserve_soc

        enable_curtailing: bool | None | Unset
        if isinstance(self.enable_curtailing, Unset):
            enable_curtailing = UNSET
        else:
            enable_curtailing = self.enable_curtailing

        enable_realtime: bool | None | Unset
        if isinstance(self.enable_realtime, Unset):
            enable_realtime = UNSET
        else:
            enable_realtime = self.enable_realtime

        realtime_first_activated_on: None | str | Unset
        if isinstance(self.realtime_first_activated_on, Unset):
            realtime_first_activated_on = UNSET
        elif isinstance(self.realtime_first_activated_on, datetime.datetime):
            realtime_first_activated_on = self.realtime_first_activated_on.isoformat()
        else:
            realtime_first_activated_on = self.realtime_first_activated_on

        enable_dynamic_pricing: bool | None | Unset
        if isinstance(self.enable_dynamic_pricing, Unset):
            enable_dynamic_pricing = UNSET
        else:
            enable_dynamic_pricing = self.enable_dynamic_pricing

        dynamic_pricing_first_activated_on: None | str | Unset
        if isinstance(self.dynamic_pricing_first_activated_on, Unset):
            dynamic_pricing_first_activated_on = UNSET
        elif isinstance(self.dynamic_pricing_first_activated_on, datetime.datetime):
            dynamic_pricing_first_activated_on = self.dynamic_pricing_first_activated_on.isoformat()
        else:
            dynamic_pricing_first_activated_on = self.dynamic_pricing_first_activated_on

        user_requested_lower_price_threshold: float | None | Unset
        if isinstance(self.user_requested_lower_price_threshold, Unset):
            user_requested_lower_price_threshold = UNSET
        else:
            user_requested_lower_price_threshold = self.user_requested_lower_price_threshold

        user_requested_upper_price_threshold: float | None | Unset
        if isinstance(self.user_requested_upper_price_threshold, Unset):
            user_requested_upper_price_threshold = UNSET
        else:
            user_requested_upper_price_threshold = self.user_requested_upper_price_threshold

        last_calendar_sync_on: None | str | Unset
        if isinstance(self.last_calendar_sync_on, Unset):
            last_calendar_sync_on = UNSET
        elif isinstance(self.last_calendar_sync_on, datetime.datetime):
            last_calendar_sync_on = self.last_calendar_sync_on.isoformat()
        else:
            last_calendar_sync_on = self.last_calendar_sync_on

        calendar_sync_status: None | str | Unset
        if isinstance(self.calendar_sync_status, Unset):
            calendar_sync_status = UNSET
        else:
            calendar_sync_status = self.calendar_sync_status

        enable_mbus_reader: bool | None | Unset
        if isinstance(self.enable_mbus_reader, Unset):
            enable_mbus_reader = UNSET
        else:
            enable_mbus_reader = self.enable_mbus_reader

        enable_smart_grid_ready_control: bool | None | Unset
        if isinstance(self.enable_smart_grid_ready_control, Unset):
            enable_smart_grid_ready_control = UNSET
        else:
            enable_smart_grid_ready_control = self.enable_smart_grid_ready_control

        smart_grid_ready_control_first_activated_on: None | str | Unset
        if isinstance(self.smart_grid_ready_control_first_activated_on, Unset):
            smart_grid_ready_control_first_activated_on = UNSET
        elif isinstance(self.smart_grid_ready_control_first_activated_on, datetime.datetime):
            smart_grid_ready_control_first_activated_on = (
                self.smart_grid_ready_control_first_activated_on.isoformat()
            )
        else:
            smart_grid_ready_control_first_activated_on = (
                self.smart_grid_ready_control_first_activated_on
            )

        user_requested_deactivate_heat_pump_on_high_prices: bool | None | Unset
        if isinstance(self.user_requested_deactivate_heat_pump_on_high_prices, Unset):
            user_requested_deactivate_heat_pump_on_high_prices = UNSET
        else:
            user_requested_deactivate_heat_pump_on_high_prices = (
                self.user_requested_deactivate_heat_pump_on_high_prices
            )

        user_requested_activate_heat_pump_on_low_prices: bool | None | Unset
        if isinstance(self.user_requested_activate_heat_pump_on_low_prices, Unset):
            user_requested_activate_heat_pump_on_low_prices = UNSET
        else:
            user_requested_activate_heat_pump_on_low_prices = (
                self.user_requested_activate_heat_pump_on_low_prices
            )

        increased_threshold: int | None | Unset
        if isinstance(self.increased_threshold, Unset):
            increased_threshold = UNSET
        else:
            increased_threshold = self.increased_threshold

        forced_threshold: int | None | Unset
        if isinstance(self.forced_threshold, Unset):
            forced_threshold = UNSET
        else:
            forced_threshold = self.forced_threshold

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        phase_switching_disabled: bool | None | Unset
        if isinstance(self.phase_switching_disabled, Unset):
            phase_switching_disabled = UNSET
        else:
            phase_switching_disabled = self.phase_switching_disabled

        dynamic_pricing_tariff: dict[str, Any] | None | Unset
        if isinstance(self.dynamic_pricing_tariff, Unset):
            dynamic_pricing_tariff = UNSET
        elif isinstance(self.dynamic_pricing_tariff, EnergyTariffReferenceModel):
            dynamic_pricing_tariff = self.dynamic_pricing_tariff.to_dict()
        else:
            dynamic_pricing_tariff = self.dynamic_pricing_tariff

        communicator: dict[str, Any] | None | Unset
        if isinstance(self.communicator, Unset):
            communicator = UNSET
        elif isinstance(self.communicator, CommunicatorReferenceModel):
            communicator = self.communicator.to_dict()
        else:
            communicator = self.communicator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
        if enable_inverter_control is not UNSET:
            field_dict["enableInverterControl"] = enable_inverter_control
        if inverter_control_first_activated_on is not UNSET:
            field_dict["inverterControlFirstActivatedOn"] = inverter_control_first_activated_on
        if battery_capacity is not UNSET:
            field_dict["batteryCapacity"] = battery_capacity
        if battery_power is not UNSET:
            field_dict["batteryPower"] = battery_power
        if enable_ev_charger_control is not UNSET:
            field_dict["enableEvChargerControl"] = enable_ev_charger_control
        if ev_charger_control_first_activated_on is not UNSET:
            field_dict["evChargerControlFirstActivatedOn"] = ev_charger_control_first_activated_on
        if ev_number_of_phases is not UNSET:
            field_dict["evNumberOfPhases"] = ev_number_of_phases
        if max_grid_current is not UNSET:
            field_dict["maxGridCurrent"] = max_grid_current
        if min_charge_current is not UNSET:
            field_dict["minChargeCurrent"] = min_charge_current
        if user_requested_ev_mode is not UNSET:
            field_dict["userRequestedEvMode"] = user_requested_ev_mode
        if user_requested_ev_battery_mode is not UNSET:
            field_dict["userRequestedEvBatteryMode"] = user_requested_ev_battery_mode
        if user_requested_max_charge_current is not UNSET:
            field_dict["userRequestedMaxChargeCurrent"] = user_requested_max_charge_current
        if user_requested_max_grid_current is not UNSET:
            field_dict["userRequestedMaxGridCurrent"] = user_requested_max_grid_current
        if enable_peak_shaving is not UNSET:
            field_dict["enablePeakShaving"] = enable_peak_shaving
        if peak_shaving_first_activated_on is not UNSET:
            field_dict["peakShavingFirstActivatedOn"] = peak_shaving_first_activated_on
        if min_battery_charge_soc is not UNSET:
            field_dict["minBatteryChargeSoc"] = min_battery_charge_soc
        if user_requested_max_grid_power is not UNSET:
            field_dict["userRequestedMaxGridPower"] = user_requested_max_grid_power
        if user_requested_battery_peak_reserve_soc is not UNSET:
            field_dict["userRequestedBatteryPeakReserveSoc"] = (
                user_requested_battery_peak_reserve_soc
            )
        if enable_curtailing is not UNSET:
            field_dict["enableCurtailing"] = enable_curtailing
        if enable_realtime is not UNSET:
            field_dict["enableRealtime"] = enable_realtime
        if realtime_first_activated_on is not UNSET:
            field_dict["realtimeFirstActivatedOn"] = realtime_first_activated_on
        if enable_dynamic_pricing is not UNSET:
            field_dict["enableDynamicPricing"] = enable_dynamic_pricing
        if dynamic_pricing_first_activated_on is not UNSET:
            field_dict["dynamicPricingFirstActivatedOn"] = dynamic_pricing_first_activated_on
        if user_requested_lower_price_threshold is not UNSET:
            field_dict["userRequestedLowerPriceThreshold"] = user_requested_lower_price_threshold
        if user_requested_upper_price_threshold is not UNSET:
            field_dict["userRequestedUpperPriceThreshold"] = user_requested_upper_price_threshold
        if last_calendar_sync_on is not UNSET:
            field_dict["lastCalendarSyncOn"] = last_calendar_sync_on
        if calendar_sync_status is not UNSET:
            field_dict["calendarSyncStatus"] = calendar_sync_status
        if enable_mbus_reader is not UNSET:
            field_dict["enableMbusReader"] = enable_mbus_reader
        if enable_smart_grid_ready_control is not UNSET:
            field_dict["enableSmartGridReadyControl"] = enable_smart_grid_ready_control
        if smart_grid_ready_control_first_activated_on is not UNSET:
            field_dict["smartGridReadyControlFirstActivatedOn"] = (
                smart_grid_ready_control_first_activated_on
            )
        if user_requested_deactivate_heat_pump_on_high_prices is not UNSET:
            field_dict["userRequestedDeactivateHeatPumpOnHighPrices"] = (
                user_requested_deactivate_heat_pump_on_high_prices
            )
        if user_requested_activate_heat_pump_on_low_prices is not UNSET:
            field_dict["userRequestedActivateHeatPumpOnLowPrices"] = (
                user_requested_activate_heat_pump_on_low_prices
            )
        if increased_threshold is not UNSET:
            field_dict["increasedThreshold"] = increased_threshold
        if forced_threshold is not UNSET:
            field_dict["forcedThreshold"] = forced_threshold
        if status is not UNSET:
            field_dict["status"] = status
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if phase_switching_disabled is not UNSET:
            field_dict["phaseSwitchingDisabled"] = phase_switching_disabled
        if dynamic_pricing_tariff is not UNSET:
            field_dict["dynamicPricingTariff"] = dynamic_pricing_tariff
        if communicator is not UNSET:
            field_dict["communicator"] = communicator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communicator_reference_model import CommunicatorReferenceModel
        from ..models.energy_tariff_reference_model import EnergyTariffReferenceModel

        d = dict(src_dict)

        def _parse_resource_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_uri = _parse_resource_uri(d.pop("resourceUri", UNSET))

        def _parse_enable_inverter_control(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_inverter_control = _parse_enable_inverter_control(
            d.pop("enableInverterControl", UNSET)
        )

        def _parse_inverter_control_first_activated_on(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                inverter_control_first_activated_on_type_0 = datetime.datetime.fromisoformat(data)

                return inverter_control_first_activated_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        inverter_control_first_activated_on = _parse_inverter_control_first_activated_on(
            d.pop("inverterControlFirstActivatedOn", UNSET)
        )

        def _parse_battery_capacity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        battery_capacity = _parse_battery_capacity(d.pop("batteryCapacity", UNSET))

        def _parse_battery_power(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        battery_power = _parse_battery_power(d.pop("batteryPower", UNSET))

        def _parse_enable_ev_charger_control(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_ev_charger_control = _parse_enable_ev_charger_control(
            d.pop("enableEvChargerControl", UNSET)
        )

        def _parse_ev_charger_control_first_activated_on(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ev_charger_control_first_activated_on_type_0 = datetime.datetime.fromisoformat(data)

                return ev_charger_control_first_activated_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ev_charger_control_first_activated_on = _parse_ev_charger_control_first_activated_on(
            d.pop("evChargerControlFirstActivatedOn", UNSET)
        )

        def _parse_ev_number_of_phases(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ev_number_of_phases = _parse_ev_number_of_phases(d.pop("evNumberOfPhases", UNSET))

        def _parse_max_grid_current(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_grid_current = _parse_max_grid_current(d.pop("maxGridCurrent", UNSET))

        def _parse_min_charge_current(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_charge_current = _parse_min_charge_current(d.pop("minChargeCurrent", UNSET))

        def _parse_user_requested_ev_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_requested_ev_mode = _parse_user_requested_ev_mode(d.pop("userRequestedEvMode", UNSET))

        def _parse_user_requested_ev_battery_mode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_requested_ev_battery_mode = _parse_user_requested_ev_battery_mode(
            d.pop("userRequestedEvBatteryMode", UNSET)
        )

        def _parse_user_requested_max_charge_current(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        user_requested_max_charge_current = _parse_user_requested_max_charge_current(
            d.pop("userRequestedMaxChargeCurrent", UNSET)
        )

        def _parse_user_requested_max_grid_current(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        user_requested_max_grid_current = _parse_user_requested_max_grid_current(
            d.pop("userRequestedMaxGridCurrent", UNSET)
        )

        def _parse_enable_peak_shaving(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_peak_shaving = _parse_enable_peak_shaving(d.pop("enablePeakShaving", UNSET))

        def _parse_peak_shaving_first_activated_on(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                peak_shaving_first_activated_on_type_0 = datetime.datetime.fromisoformat(data)

                return peak_shaving_first_activated_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        peak_shaving_first_activated_on = _parse_peak_shaving_first_activated_on(
            d.pop("peakShavingFirstActivatedOn", UNSET)
        )

        def _parse_min_battery_charge_soc(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_battery_charge_soc = _parse_min_battery_charge_soc(d.pop("minBatteryChargeSoc", UNSET))

        def _parse_user_requested_max_grid_power(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_requested_max_grid_power = _parse_user_requested_max_grid_power(
            d.pop("userRequestedMaxGridPower", UNSET)
        )

        def _parse_user_requested_battery_peak_reserve_soc(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_requested_battery_peak_reserve_soc = _parse_user_requested_battery_peak_reserve_soc(
            d.pop("userRequestedBatteryPeakReserveSoc", UNSET)
        )

        def _parse_enable_curtailing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_curtailing = _parse_enable_curtailing(d.pop("enableCurtailing", UNSET))

        def _parse_enable_realtime(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_realtime = _parse_enable_realtime(d.pop("enableRealtime", UNSET))

        def _parse_realtime_first_activated_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                realtime_first_activated_on_type_0 = datetime.datetime.fromisoformat(data)

                return realtime_first_activated_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        realtime_first_activated_on = _parse_realtime_first_activated_on(
            d.pop("realtimeFirstActivatedOn", UNSET)
        )

        def _parse_enable_dynamic_pricing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_dynamic_pricing = _parse_enable_dynamic_pricing(d.pop("enableDynamicPricing", UNSET))

        def _parse_dynamic_pricing_first_activated_on(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dynamic_pricing_first_activated_on_type_0 = datetime.datetime.fromisoformat(data)

                return dynamic_pricing_first_activated_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        dynamic_pricing_first_activated_on = _parse_dynamic_pricing_first_activated_on(
            d.pop("dynamicPricingFirstActivatedOn", UNSET)
        )

        def _parse_user_requested_lower_price_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        user_requested_lower_price_threshold = _parse_user_requested_lower_price_threshold(
            d.pop("userRequestedLowerPriceThreshold", UNSET)
        )

        def _parse_user_requested_upper_price_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        user_requested_upper_price_threshold = _parse_user_requested_upper_price_threshold(
            d.pop("userRequestedUpperPriceThreshold", UNSET)
        )

        def _parse_last_calendar_sync_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_calendar_sync_on_type_0 = datetime.datetime.fromisoformat(data)

                return last_calendar_sync_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_calendar_sync_on = _parse_last_calendar_sync_on(d.pop("lastCalendarSyncOn", UNSET))

        def _parse_calendar_sync_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        calendar_sync_status = _parse_calendar_sync_status(d.pop("calendarSyncStatus", UNSET))

        def _parse_enable_mbus_reader(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_mbus_reader = _parse_enable_mbus_reader(d.pop("enableMbusReader", UNSET))

        def _parse_enable_smart_grid_ready_control(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_smart_grid_ready_control = _parse_enable_smart_grid_ready_control(
            d.pop("enableSmartGridReadyControl", UNSET)
        )

        def _parse_smart_grid_ready_control_first_activated_on(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                smart_grid_ready_control_first_activated_on_type_0 = (
                    datetime.datetime.fromisoformat(data)
                )

                return smart_grid_ready_control_first_activated_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        smart_grid_ready_control_first_activated_on = (
            _parse_smart_grid_ready_control_first_activated_on(
                d.pop("smartGridReadyControlFirstActivatedOn", UNSET)
            )
        )

        def _parse_user_requested_deactivate_heat_pump_on_high_prices(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        user_requested_deactivate_heat_pump_on_high_prices = (
            _parse_user_requested_deactivate_heat_pump_on_high_prices(
                d.pop("userRequestedDeactivateHeatPumpOnHighPrices", UNSET)
            )
        )

        def _parse_user_requested_activate_heat_pump_on_low_prices(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        user_requested_activate_heat_pump_on_low_prices = (
            _parse_user_requested_activate_heat_pump_on_low_prices(
                d.pop("userRequestedActivateHeatPumpOnLowPrices", UNSET)
            )
        )

        def _parse_increased_threshold(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        increased_threshold = _parse_increased_threshold(d.pop("increasedThreshold", UNSET))

        def _parse_forced_threshold(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        forced_threshold = _parse_forced_threshold(d.pop("forcedThreshold", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_phase_switching_disabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        phase_switching_disabled = _parse_phase_switching_disabled(
            d.pop("phaseSwitchingDisabled", UNSET)
        )

        def _parse_dynamic_pricing_tariff(
            data: object,
        ) -> EnergyTariffReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dynamic_pricing_tariff_type_1 = EnergyTariffReferenceModel.from_dict(data)

                return dynamic_pricing_tariff_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnergyTariffReferenceModel | None | Unset, data)

        dynamic_pricing_tariff = _parse_dynamic_pricing_tariff(d.pop("dynamicPricingTariff", UNSET))

        def _parse_communicator(data: object) -> CommunicatorReferenceModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                communicator_type_1 = CommunicatorReferenceModel.from_dict(data)

                return communicator_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CommunicatorReferenceModel | None | Unset, data)

        communicator = _parse_communicator(d.pop("communicator", UNSET))

        ems_configuration_output_model = cls(
            resource_uri=resource_uri,
            enable_inverter_control=enable_inverter_control,
            inverter_control_first_activated_on=inverter_control_first_activated_on,
            battery_capacity=battery_capacity,
            battery_power=battery_power,
            enable_ev_charger_control=enable_ev_charger_control,
            ev_charger_control_first_activated_on=ev_charger_control_first_activated_on,
            ev_number_of_phases=ev_number_of_phases,
            max_grid_current=max_grid_current,
            min_charge_current=min_charge_current,
            user_requested_ev_mode=user_requested_ev_mode,
            user_requested_ev_battery_mode=user_requested_ev_battery_mode,
            user_requested_max_charge_current=user_requested_max_charge_current,
            user_requested_max_grid_current=user_requested_max_grid_current,
            enable_peak_shaving=enable_peak_shaving,
            peak_shaving_first_activated_on=peak_shaving_first_activated_on,
            min_battery_charge_soc=min_battery_charge_soc,
            user_requested_max_grid_power=user_requested_max_grid_power,
            user_requested_battery_peak_reserve_soc=user_requested_battery_peak_reserve_soc,
            enable_curtailing=enable_curtailing,
            enable_realtime=enable_realtime,
            realtime_first_activated_on=realtime_first_activated_on,
            enable_dynamic_pricing=enable_dynamic_pricing,
            dynamic_pricing_first_activated_on=dynamic_pricing_first_activated_on,
            user_requested_lower_price_threshold=user_requested_lower_price_threshold,
            user_requested_upper_price_threshold=user_requested_upper_price_threshold,
            last_calendar_sync_on=last_calendar_sync_on,
            calendar_sync_status=calendar_sync_status,
            enable_mbus_reader=enable_mbus_reader,
            enable_smart_grid_ready_control=enable_smart_grid_ready_control,
            smart_grid_ready_control_first_activated_on=smart_grid_ready_control_first_activated_on,
            user_requested_deactivate_heat_pump_on_high_prices=user_requested_deactivate_heat_pump_on_high_prices,
            user_requested_activate_heat_pump_on_low_prices=user_requested_activate_heat_pump_on_low_prices,
            increased_threshold=increased_threshold,
            forced_threshold=forced_threshold,
            status=status,
            external_id=external_id,
            phase_switching_disabled=phase_switching_disabled,
            dynamic_pricing_tariff=dynamic_pricing_tariff,
            communicator=communicator,
        )

        ems_configuration_output_model.additional_properties = d
        return ems_configuration_output_model

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
