"""Binary sensor platform — open alarms surfaced as PROBLEM binary sensors."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)

from .api import installation_id as _iid
from .const import DOMAIN
from .entity import FlowBuddyEntity, installation_device_info

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback
    from homeassistant.helpers.update_coordinator import DataUpdateCoordinator


def _alarm_field(alarm: Any, key: str) -> Any:
    """Best-effort accessor for an alarm field.

    ``AlarmOutputModel`` (see ``_generated/models/alarm_output_model.py``)
    only types a subset of the raw API payload: ``priority``, ``status``,
    ``resource_uri``, ``description``, etc. Fields the live API emits but
    the generated model does not declare — ``id``, ``message``,
    ``raisedOn`` — are absent from the attrs class entirely and are left
    in ``additional_properties`` by ``from_dict``. Try the typed
    attribute first (in case a future codegen run adds it), then fall
    back to the raw dict.
    """
    value = getattr(alarm, key, None)
    if value is not None:
        return value
    return alarm.additional_properties.get(key)


class FlowBuddyAlarmBinarySensor(FlowBuddyEntity, BinarySensorEntity):
    """An open alarm, surfaced as a PROBLEM binary sensor.

    Attached to the installation-level device rather than a meter: alarms
    are not necessarily meter-scoped (e.g. communicator-offline alarms).
    """

    _attr_device_class = BinarySensorDeviceClass.PROBLEM

    def __init__(
        self, *, coordinator: DataUpdateCoordinator[Any], installation: Any, alarm: Any
    ) -> None:
        alarm_id = _alarm_field(alarm, "id")
        super().__init__(
            coordinator,
            unique_id=f"{_iid(installation) or 'unknown'}:alarm:{alarm_id}",
        )
        message = _alarm_field(alarm, "message")
        self._attr_name = message or alarm_id
        self._attr_device_info = installation_device_info(installation)
        self._attr_extra_state_attributes = {
            "priority": alarm.priority,
            "message": message,
            "raisedOn": _alarm_field(alarm, "raisedOn"),
        }

    @property
    def is_on(self) -> bool:
        """The entity is only ever created for alarms that are currently open."""
        return True


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FlowBuddy alarm binary sensors from the alarms coordinator.

    v1: entities are created once, statically, from the alarms already
    fetched by the coordinator at setup time (mirrors the sensor.py
    platform's static-list approach). Dynamically adding/removing
    entities as alarms open/close on subsequent coordinator refreshes is
    deferred to a future refinement.
    """
    data = hass.data[DOMAIN][entry.entry_id]
    installation = data["installation"]
    alarms_coord = data["alarms_coord"]
    entities = [
        FlowBuddyAlarmBinarySensor(
            coordinator=alarms_coord,
            installation=installation,
            alarm=alarm,
        )
        for alarm in alarms_coord.data
    ]
    async_add_entities(entities)
