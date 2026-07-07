"""Button platform — alarm acknowledge + connection test."""
from __future__ import annotations

from typing import Any

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .entity import FlowBuddyEntity, installation_device_info


class AlarmAckButton(FlowBuddyEntity, ButtonEntity):
    """Button to acknowledge (close) an open alarm."""

    _attr_name = "Acknowledge"

    def __init__(
        self,
        *,
        coordinator: Any,
        api: Any,
        alarm: Any,
        installation: Any,
    ) -> None:
        super().__init__(
            coordinator,
            unique_id=f"{installation.uuid}:alarm:{alarm.id}:ack",
        )
        self._api = api
        self._alarm_id = alarm.id
        self._attr_device_info = installation_device_info(installation)

    async def async_press(self) -> None:
        """Acknowledge the alarm by closing it."""
        await self._api.close_alarm(self._alarm_id)


class RequestConnectionTestButton(FlowBuddyEntity, ButtonEntity):
    """Button to request a connection test for a communicator."""

    _attr_name = "Request connection test"

    def __init__(
        self,
        *,
        coordinator: Any,
        api: Any,
        communicator: Any,
        installation: Any,
    ) -> None:
        super().__init__(
            coordinator,
            unique_id=f"{installation.uuid}:communicator:{communicator.id}:connection_test",
        )
        self._api = api
        self._communicator_id = communicator.id
        self._attr_device_info = installation_device_info(installation)

    async def async_press(self) -> None:
        """Request a connection test for the communicator."""
        await self._api.request_connection_test(self._communicator_id)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FlowBuddy button entities from installation and communicators data."""
    data = hass.data[DOMAIN][entry.entry_id]
    installation = data["installation"]
    api = data["api"]
    alarms_coord = data["alarms_coord"]

    entities: list[ButtonEntity] = []

    # Add alarm ack buttons for each open alarm
    for alarm in alarms_coord.data:
        entities.append(
            AlarmAckButton(
                coordinator=alarms_coord,
                api=api,
                alarm=alarm,
                installation=installation,
            )
        )

    # Add connection test button for each communicator
    # Use instant coordinator as a stable reference (always available)
    instant_coord = data["instant_coord"]
    for communicator in data.get("communicators", []):
        entities.append(
            RequestConnectionTestButton(
                coordinator=instant_coord,
                api=api,
                communicator=communicator,
                installation=installation,
            )
        )

    async_add_entities(entities)
