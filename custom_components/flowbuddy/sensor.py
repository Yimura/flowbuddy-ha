"""Sensor platform."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .discovery import describe
from .api import installation_id as _iid
from .entity import FlowBuddyEntity, meter_device_info


class FlowBuddySensor(FlowBuddyEntity, SensorEntity):
    """A single measurement, sourced from either the instant or daily coordinator."""

    def __init__(
        self, *, coordinator, installation_uuid: str, meter, installation,
        measurement, measurement_type,
    ) -> None:
        desc = describe(measurement_type)
        super().__init__(
            coordinator,
            unique_id=f"{installation_uuid}:{measurement.resource_uri}",
        )
        self._measurement_uri = measurement.resource_uri
        self._desc = desc
        self._attr_name = desc.name
        self._attr_native_unit_of_measurement = desc.native_unit_of_measurement
        self._attr_device_class = desc.device_class
        self._attr_state_class = desc.state_class
        self._attr_device_info = meter_device_info(meter, installation)

    @property
    def native_value(self) -> float | None:
        raw = self.coordinator.data.get(self._measurement_uri)
        return self._desc.value_transformer(raw) if raw is not None else None


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FlowBuddy sensors from the discovery data cached in hass.data."""
    data = hass.data[DOMAIN][entry.entry_id]
    entities: list[FlowBuddySensor] = []
    for measurement in data["measurements"]:
        mt = data["measurementtypes_by_uri"].get(measurement.measurement_type.resource_uri)
        if mt is None:
            continue
        meter = data["meters_by_uri"].get(measurement.meter.resource_uri)
        if meter is None:
            continue
        # All measurements route to instant_coord: Measurement.lastPolledValue
        # already carries both live power AND cumulative energy counters in
        # the same payload. The daily coordinator's separate
        # /aggregationdayvalues filter matches zero rows because real
        # responses ship periodStart=null (spec vs runtime mismatch),
        # so it's not useful as a data source right now.
        coord = data["instant_coord"]
        entities.append(FlowBuddySensor(
            coordinator=coord,
            installation_uuid=(_iid(data["installation"]) or "unknown"),
            meter=meter,
            installation=data["installation"],
            measurement=measurement,
            measurement_type=mt,
        ))
    async_add_entities(entities)
