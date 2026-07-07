"""Number platform — battery charge power + inverter production limit setpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from homeassistant.components.number import NumberEntity, NumberMode

from .api import installation_id as _iid
from .const import DOMAIN
from .entity import FlowBuddyEntity, meter_device_info

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback
    from homeassistant.helpers.update_coordinator import DataUpdateCoordinator


class BatteryChargePowerNumber(FlowBuddyEntity, NumberEntity):
    """Setpoint for a battery's charge/discharge power.

    Per spec §4.5, the vendor API exposes a single signed setpoint:
    positive values charge the battery, negative values discharge it.
    The range is therefore asymmetric and derived from the battery's
    own reported limits: min = -max_discharge_power, max = +max_charge_power.
    """

    _attr_native_step = 100
    _attr_native_unit_of_measurement = "W"
    _attr_mode = NumberMode.BOX
    _attr_name = "Charge power"

    def __init__(
        self,
        *,
        coordinator: DataUpdateCoordinator[Any],
        api: Any,
        battery: Any,
        meter: Any,
        installation: Any,
    ) -> None:
        super().__init__(
            coordinator,
            unique_id=f"{_iid(installation) or 'unknown'}:battery:{battery.resource_uri}:charge_power",
        )
        self._api = api
        self._battery_id = battery.external_id
        self._attr_native_min_value = -battery.max_discharge_power
        self._attr_native_max_value = battery.max_charge_power
        self._attr_native_value = battery.last_set_charge_power
        self._attr_device_info = meter_device_info(meter, installation)

    async def async_set_native_value(self, value: float) -> None:
        """Push a new charge/discharge setpoint to the vendor API."""
        await self._api.set_battery_charge_power(self._battery_id, int(value))
        self._attr_native_value = value
        if self.hass is not None:
            self.async_write_ha_state()


class InverterProductionLimitNumber(FlowBuddyEntity, NumberEntity):
    """Curtailment setpoint for a PV inverter's production capacity."""

    _attr_native_min_value = 0
    _attr_native_step = 100
    _attr_native_unit_of_measurement = "W"
    _attr_mode = NumberMode.BOX
    _attr_name = "Production limit"

    def __init__(
        self,
        *,
        coordinator: DataUpdateCoordinator[Any],
        api: Any,
        inverter: Any,
        meter: Any,
        installation: Any,
    ) -> None:
        super().__init__(
            coordinator,
            unique_id=f"{_iid(installation) or 'unknown'}:inverter:{inverter.resource_uri}:production_limit",
        )
        self._api = api
        self._inverter_id = inverter.external_id
        self._attr_native_max_value = inverter.max_power
        self._attr_native_value = inverter.last_set_production_capacity
        self._attr_device_info = meter_device_info(meter, installation)

    async def async_set_native_value(self, value: float) -> None:
        """Push a new production limit to the vendor API."""
        await self._api.limit_inverter(self._inverter_id, int(value))
        self._attr_native_value = value
        if self.hass is not None:
            self.async_write_ha_state()


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FlowBuddy number entities from the batteries/inverters cached in hass.data."""
    data = hass.data[DOMAIN][entry.entry_id]
    installation = data["installation"]
    api = data["api"]
    coordinator = data["instant_coord"]
    meters_by_uri = data.get("meters_by_uri", {})

    entities: list[NumberEntity] = []
    for battery in data.get("batteries", []):
        meter = meters_by_uri.get(battery.info.resource_uri) if battery.info else None
        if meter is None:
            continue
        entities.append(
            BatteryChargePowerNumber(
                coordinator=coordinator,
                api=api,
                battery=battery,
                meter=meter,
                installation=installation,
            )
        )
    for inverter in data.get("inverters", []):
        meter = meters_by_uri.get(inverter.info.resource_uri) if inverter.info else None
        if meter is None:
            continue
        entities.append(
            InverterProductionLimitNumber(
                coordinator=coordinator,
                api=api,
                inverter=inverter,
                meter=meter,
                installation=installation,
            )
        )
    async_add_entities(entities)
