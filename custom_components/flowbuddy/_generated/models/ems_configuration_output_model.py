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
        resource_uri (str | Unset):
        enable_inverter_control (bool | Unset): Enables the virtual grid meter and allows control over the behavior of a
            hybrid inverter.
        inverter_control_first_activated_on (datetime.datetime | None | Unset): The date when the inverter control was
            first activated.
        battery_capacity (float | Unset): The capacity, in kWh, of the installed batteries linked to the EMS.
        battery_power (float | Unset): The maximum (dis)charge power, in kW, of the installed batteries linked to the
            EMS.
        enable_ev_charger_control (bool | Unset): Enables the EMS app for EV charger control and allows you to adjust
            the charging power based on grid usage and solar production.
        ev_charger_control_first_activated_on (datetime.datetime | None | Unset): The date when the EV charger control
            was first activated.
        ev_number_of_phases (int | Unset): Number of phases configured in the EV charger controlled by the EMS.
        max_grid_current (float | Unset): Maximum rated current of the grid connection in Amperes.
        min_charge_current (float | Unset): Minimum charge current that should be used by the connected EV charger in
            Amperes.
        user_requested_ev_mode (str | Unset):
        user_requested_ev_battery_mode (int | Unset): Controls battery discharging when EV charging is active: 0 - Off
            (battery will not be used to support EV charging), 1 - On.
        user_requested_max_charge_current (float | Unset): Maximum charging current (from grid or solar) that can be
            used by the connected EV charger in Amperes.
        user_requested_max_grid_current (float | Unset): Maximum charging current (imported from the grid) that can be
            used by the connected EV charger in Amperes.
        enable_peak_shaving (bool | Unset): Enables the EMS app for capacity tariff and allows you to limit the maximum
            grid power by adjusting charging powers, activating the battery, or disabling external devices.
        peak_shaving_first_activated_on (datetime.datetime | None | Unset): The date when the peak shaving feature was
            first activated.
        min_battery_charge_soc (int | Unset): A value ranging from 0-100 that represents the minimum battery charge.
            This variable is set by the installer to ensure battery health.
        user_requested_max_grid_power (int | Unset): The maximum grid power. This variable can be controlled by the
            user.
        user_requested_battery_peak_reserve_soc (int | Unset): A value ranging from 0-100 that represents the battery
            reserve used to cover peak electricity usage. This variable can be controlled by the user.
        enable_curtailing (bool | Unset):
        enable_realtime (bool | Unset): Enables the EMS app for real-time polling.
        realtime_first_activated_on (datetime.datetime | None | Unset): The date when the real-time polling feature was
            first activated.
        enable_dynamic_pricing (bool | Unset): Enables EMS apps for dynamic pricing
        dynamic_pricing_first_activated_on (datetime.datetime | None | Unset): The date when the dynamic pricing feature
            was first activated.
        user_requested_lower_price_threshold (float | Unset): The threshold for the lower price. This variable can be
            controlled by the user.
        user_requested_upper_price_threshold (float | Unset): The threshold for the upper price. This variable can be
            controlled by the user.
        last_calendar_sync_on (datetime.datetime | None | Unset):
        calendar_sync_status (str | Unset):
        enable_mbus_reader (bool | Unset): Enables the EMS app for reading mbus devices.
        enable_smart_grid_ready_control (bool | Unset): Enables the EMS app for smart grid ready control.
        smart_grid_ready_control_first_activated_on (datetime.datetime | None | Unset): The date when the smart grid
            ready control feature was first activated.
        user_requested_deactivate_heat_pump_on_high_prices (bool | Unset): Deactivates the heat pump on high prices.
            This variable can be controlled by the user.
        user_requested_activate_heat_pump_on_low_prices (bool | Unset): Activates the heat pump on low prices. This
            variable can be controlled by the user.
        increased_threshold (int | Unset): Consumption of the heat pump in Watt when it is in increased operation.
        forced_threshold (int | Unset): Consumption of the heat pump in Watt when it is in forced operation.
        status (str | Unset):
        external_id (str | Unset):
        phase_switching_disabled (bool | Unset):
        dynamic_pricing_tariff (EnergyTariffReferenceModel | Unset):
        communicator (CommunicatorReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    enable_inverter_control: bool | Unset = UNSET
    inverter_control_first_activated_on: datetime.datetime | None | Unset = UNSET
    battery_capacity: float | Unset = UNSET
    battery_power: float | Unset = UNSET
    enable_ev_charger_control: bool | Unset = UNSET
    ev_charger_control_first_activated_on: datetime.datetime | None | Unset = UNSET
    ev_number_of_phases: int | Unset = UNSET
    max_grid_current: float | Unset = UNSET
    min_charge_current: float | Unset = UNSET
    user_requested_ev_mode: str | Unset = UNSET
    user_requested_ev_battery_mode: int | Unset = UNSET
    user_requested_max_charge_current: float | Unset = UNSET
    user_requested_max_grid_current: float | Unset = UNSET
    enable_peak_shaving: bool | Unset = UNSET
    peak_shaving_first_activated_on: datetime.datetime | None | Unset = UNSET
    min_battery_charge_soc: int | Unset = UNSET
    user_requested_max_grid_power: int | Unset = UNSET
    user_requested_battery_peak_reserve_soc: int | Unset = UNSET
    enable_curtailing: bool | Unset = UNSET
    enable_realtime: bool | Unset = UNSET
    realtime_first_activated_on: datetime.datetime | None | Unset = UNSET
    enable_dynamic_pricing: bool | Unset = UNSET
    dynamic_pricing_first_activated_on: datetime.datetime | None | Unset = UNSET
    user_requested_lower_price_threshold: float | Unset = UNSET
    user_requested_upper_price_threshold: float | Unset = UNSET
    last_calendar_sync_on: datetime.datetime | None | Unset = UNSET
    calendar_sync_status: str | Unset = UNSET
    enable_mbus_reader: bool | Unset = UNSET
    enable_smart_grid_ready_control: bool | Unset = UNSET
    smart_grid_ready_control_first_activated_on: datetime.datetime | None | Unset = UNSET
    user_requested_deactivate_heat_pump_on_high_prices: bool | Unset = UNSET
    user_requested_activate_heat_pump_on_low_prices: bool | Unset = UNSET
    increased_threshold: int | Unset = UNSET
    forced_threshold: int | Unset = UNSET
    status: str | Unset = UNSET
    external_id: str | Unset = UNSET
    phase_switching_disabled: bool | Unset = UNSET
    dynamic_pricing_tariff: EnergyTariffReferenceModel | Unset = UNSET
    communicator: CommunicatorReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.communicator_reference_model import CommunicatorReferenceModel
        from ..models.energy_tariff_reference_model import EnergyTariffReferenceModel

        resource_uri = self.resource_uri

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

        battery_capacity = self.battery_capacity

        battery_power = self.battery_power

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

        ev_number_of_phases = self.ev_number_of_phases

        max_grid_current = self.max_grid_current

        min_charge_current = self.min_charge_current

        user_requested_ev_mode = self.user_requested_ev_mode

        user_requested_ev_battery_mode = self.user_requested_ev_battery_mode

        user_requested_max_charge_current = self.user_requested_max_charge_current

        user_requested_max_grid_current = self.user_requested_max_grid_current

        enable_peak_shaving = self.enable_peak_shaving

        peak_shaving_first_activated_on: None | str | Unset
        if isinstance(self.peak_shaving_first_activated_on, Unset):
            peak_shaving_first_activated_on = UNSET
        elif isinstance(self.peak_shaving_first_activated_on, datetime.datetime):
            peak_shaving_first_activated_on = self.peak_shaving_first_activated_on.isoformat()
        else:
            peak_shaving_first_activated_on = self.peak_shaving_first_activated_on

        min_battery_charge_soc = self.min_battery_charge_soc

        user_requested_max_grid_power = self.user_requested_max_grid_power

        user_requested_battery_peak_reserve_soc = self.user_requested_battery_peak_reserve_soc

        enable_curtailing = self.enable_curtailing

        enable_realtime = self.enable_realtime

        realtime_first_activated_on: None | str | Unset
        if isinstance(self.realtime_first_activated_on, Unset):
            realtime_first_activated_on = UNSET
        elif isinstance(self.realtime_first_activated_on, datetime.datetime):
            realtime_first_activated_on = self.realtime_first_activated_on.isoformat()
        else:
            realtime_first_activated_on = self.realtime_first_activated_on

        enable_dynamic_pricing = self.enable_dynamic_pricing

        dynamic_pricing_first_activated_on: None | str | Unset
        if isinstance(self.dynamic_pricing_first_activated_on, Unset):
            dynamic_pricing_first_activated_on = UNSET
        elif isinstance(self.dynamic_pricing_first_activated_on, datetime.datetime):
            dynamic_pricing_first_activated_on = self.dynamic_pricing_first_activated_on.isoformat()
        else:
            dynamic_pricing_first_activated_on = self.dynamic_pricing_first_activated_on

        user_requested_lower_price_threshold = self.user_requested_lower_price_threshold

        user_requested_upper_price_threshold = self.user_requested_upper_price_threshold

        last_calendar_sync_on: None | str | Unset
        if isinstance(self.last_calendar_sync_on, Unset):
            last_calendar_sync_on = UNSET
        elif isinstance(self.last_calendar_sync_on, datetime.datetime):
            last_calendar_sync_on = self.last_calendar_sync_on.isoformat()
        else:
            last_calendar_sync_on = self.last_calendar_sync_on

        calendar_sync_status = self.calendar_sync_status

        enable_mbus_reader = self.enable_mbus_reader

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

        user_requested_deactivate_heat_pump_on_high_prices = (
            self.user_requested_deactivate_heat_pump_on_high_prices
        )

        user_requested_activate_heat_pump_on_low_prices = (
            self.user_requested_activate_heat_pump_on_low_prices
        )

        increased_threshold = self.increased_threshold

        forced_threshold = self.forced_threshold

        status = self.status

        external_id = self.external_id

        phase_switching_disabled = self.phase_switching_disabled

        dynamic_pricing_tariff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dynamic_pricing_tariff, Unset):
            dynamic_pricing_tariff = self.dynamic_pricing_tariff.to_dict()

        communicator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.communicator, Unset):
            communicator = self.communicator.to_dict()

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
        resource_uri = d.pop("resourceUri", UNSET)

        enable_inverter_control = d.pop("enableInverterControl", UNSET)

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

        battery_capacity = d.pop("batteryCapacity", UNSET)

        battery_power = d.pop("batteryPower", UNSET)

        enable_ev_charger_control = d.pop("enableEvChargerControl", UNSET)

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

        ev_number_of_phases = d.pop("evNumberOfPhases", UNSET)

        max_grid_current = d.pop("maxGridCurrent", UNSET)

        min_charge_current = d.pop("minChargeCurrent", UNSET)

        user_requested_ev_mode = d.pop("userRequestedEvMode", UNSET)

        user_requested_ev_battery_mode = d.pop("userRequestedEvBatteryMode", UNSET)

        user_requested_max_charge_current = d.pop("userRequestedMaxChargeCurrent", UNSET)

        user_requested_max_grid_current = d.pop("userRequestedMaxGridCurrent", UNSET)

        enable_peak_shaving = d.pop("enablePeakShaving", UNSET)

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

        min_battery_charge_soc = d.pop("minBatteryChargeSoc", UNSET)

        user_requested_max_grid_power = d.pop("userRequestedMaxGridPower", UNSET)

        user_requested_battery_peak_reserve_soc = d.pop("userRequestedBatteryPeakReserveSoc", UNSET)

        enable_curtailing = d.pop("enableCurtailing", UNSET)

        enable_realtime = d.pop("enableRealtime", UNSET)

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

        enable_dynamic_pricing = d.pop("enableDynamicPricing", UNSET)

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

        user_requested_lower_price_threshold = d.pop("userRequestedLowerPriceThreshold", UNSET)

        user_requested_upper_price_threshold = d.pop("userRequestedUpperPriceThreshold", UNSET)

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

        calendar_sync_status = d.pop("calendarSyncStatus", UNSET)

        enable_mbus_reader = d.pop("enableMbusReader", UNSET)

        enable_smart_grid_ready_control = d.pop("enableSmartGridReadyControl", UNSET)

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

        user_requested_deactivate_heat_pump_on_high_prices = d.pop(
            "userRequestedDeactivateHeatPumpOnHighPrices", UNSET
        )

        user_requested_activate_heat_pump_on_low_prices = d.pop(
            "userRequestedActivateHeatPumpOnLowPrices", UNSET
        )

        increased_threshold = d.pop("increasedThreshold", UNSET)

        forced_threshold = d.pop("forcedThreshold", UNSET)

        status = d.pop("status", UNSET)

        external_id = d.pop("externalId", UNSET)

        phase_switching_disabled = d.pop("phaseSwitchingDisabled", UNSET)

        _dynamic_pricing_tariff = d.pop("dynamicPricingTariff", UNSET)
        dynamic_pricing_tariff: EnergyTariffReferenceModel | Unset
        if isinstance(_dynamic_pricing_tariff, Unset):
            dynamic_pricing_tariff = UNSET
        else:
            dynamic_pricing_tariff = EnergyTariffReferenceModel.from_dict(_dynamic_pricing_tariff)

        _communicator = d.pop("communicator", UNSET)
        communicator: CommunicatorReferenceModel | Unset
        if isinstance(_communicator, Unset):
            communicator = UNSET
        else:
            communicator = CommunicatorReferenceModel.from_dict(_communicator)

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
