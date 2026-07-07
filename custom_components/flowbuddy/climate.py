"""Climate platform — HVAC units with independent heat/cool setpoint control."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import ClimateEntityFeature, HVACMode
from homeassistant.const import ATTR_TEMPERATURE, UnitOfTemperature
from homeassistant.exceptions import HomeAssistantError

from .api import installation_id as _iid
from .const import DOMAIN
from .entity import FlowBuddyEntity, meter_device_info

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback
    from homeassistant.helpers.update_coordinator import DataUpdateCoordinator


class FlowBuddyHvac(FlowBuddyEntity, ClimateEntity):
    """An HVAC unit, exposing independent heat/cool setpoint control.

    ``HVACOutputModel`` (see ``_generated/models/hvac_output_model.py``,
    confirmed against the vendor OpenAPI spec — not just an under-typed
    codegen gap) only types ``resource_uri``, ``external_id``, ``info``,
    ``last_set_cool_temperature`` and ``last_set_heat_temperature``.
    There is no operating-mode field at all, so the current HEAT/COOL/OFF
    state can never be read back from the API, and there is no unified
    "target temperature" — only two independent last-set setpoints.

    Consequently ``_attr_hvac_mode`` starts at ``HVACMode.OFF`` (the safe
    default per the task brief) and is only ever changed locally via
    ``async_set_hvac_mode`` — an HA-side-only "assumed mode" concept,
    the same optimistic-state pattern the setpoint entities in
    ``number.py`` use for their own last-set values. Requiring the user
    to explicitly pick HEAT or COOL from the climate card before
    ``async_set_temperature`` will act is a deliberate safety choice:
    it's safer to refuse a write when we don't know which setpoint
    should receive it than to guess.
    """

    _attr_hvac_modes = [HVACMode.HEAT, HVACMode.COOL, HVACMode.OFF]
    _attr_temperature_unit = UnitOfTemperature.CELSIUS
    _attr_supported_features = ClimateEntityFeature.TARGET_TEMPERATURE
    _attr_name = None

    def __init__(
        self,
        *,
        coordinator: DataUpdateCoordinator[Any],
        api: Any,
        hvac: Any,
        meter: Any,
        installation: Any,
    ) -> None:
        super().__init__(
            coordinator,
            unique_id=f"{_iid(installation) or 'unknown'}:hvac:{hvac.resource_uri}",
        )
        self._api = api
        self._hvac_id = hvac.external_id
        self._last_set_cool_temperature: float | None = hvac.last_set_cool_temperature
        self._last_set_heat_temperature: float | None = hvac.last_set_heat_temperature
        self._attr_hvac_mode = HVACMode.OFF
        # The vendor API exposes no live temperature reading on the HVAC
        # unit itself. Surfacing the linked meter's own "°C" measurement
        # would require cross-referencing the meter's measurement list
        # (see discovery.py / sensor.py), which isn't wired into this
        # platform in this phase — left as None rather than guessed.
        self._attr_current_temperature = None
        self._attr_device_info = meter_device_info(meter, installation)

    @property
    def target_temperature(self) -> float | None:
        """The setpoint for whichever mode is currently selected."""
        if self._attr_hvac_mode == HVACMode.COOL:
            return self._last_set_cool_temperature
        if self._attr_hvac_mode == HVACMode.HEAT:
            return self._last_set_heat_temperature
        return None

    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None:
        """Locally select HEAT/COOL/OFF (not readable back from the vendor API)."""
        self._attr_hvac_mode = hvac_mode
        if self.hass is not None:
            self.async_write_ha_state()

    async def async_set_temperature(self, **kwargs: Any) -> None:
        """Push a new setpoint to whichever mode is currently selected."""
        temp = kwargs[ATTR_TEMPERATURE]
        if self._attr_hvac_mode == HVACMode.HEAT:
            await self._api.set_hvac_heat(self._hvac_id, temp)
            self._last_set_heat_temperature = temp
        elif self._attr_hvac_mode == HVACMode.COOL:
            await self._api.set_hvac_cool(self._hvac_id, temp)
            self._last_set_cool_temperature = temp
        else:
            raise HomeAssistantError("Cannot set temperature while HVAC is off")
        if self.hass is not None:
            self.async_write_ha_state()


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FlowBuddy HVAC climate entities from the hvacs cached in hass.data."""
    data = hass.data[DOMAIN][entry.entry_id]
    installation = data["installation"]
    api = data["api"]
    coordinator = data["instant_coord"]
    meters_by_uri = data.get("meters_by_uri", {})

    entities: list[FlowBuddyHvac] = []
    for hvac in data.get("hvacs", []):
        meter = meters_by_uri.get(hvac.info.resource_uri) if hvac.info else None
        if meter is None:
            continue
        entities.append(
            FlowBuddyHvac(
                coordinator=coordinator,
                api=api,
                hvac=hvac,
                meter=meter,
                installation=installation,
            )
        )
    async_add_entities(entities)
