"""Button platform — alarm acknowledge + connection test."""
from __future__ import annotations

from typing import Any

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .api import installation_id as _iid
from .entity import FlowBuddyEntity, installation_device_info


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


def _communicator_field(communicator: Any, key: str) -> Any:
	"""Best-effort accessor for a communicator field.

	``CommunicatorOutputModel`` (see ``_generated/models/communicator_output_model.py``)
	only types a subset of the raw API payload: ``resource_uri``, ``logical_device_name``,
	``external_id``, etc. Fields the live API emits but the generated model does not
	declare — ``id`` — are absent from the attrs class entirely and are left in
	``additional_properties`` by ``from_dict``. Try the typed attribute first (in case
	a future codegen run adds it), then fall back to the raw dict.
	"""
	value = getattr(communicator, key, None)
	if value is not None:
		return value
	return communicator.additional_properties.get(key)


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
        alarm_id = _alarm_field(alarm, "id")
        super().__init__(
            coordinator,
            unique_id=f"{_iid(installation) or 'unknown'}:alarm:{alarm_id}:ack",
        )
        self._api = api
        self._alarm_id = alarm_id
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
        communicator_id = _communicator_field(communicator, "id")
        super().__init__(
            coordinator,
            unique_id=f"{_iid(installation) or 'unknown'}:communicator:{communicator_id}:connection_test",
        )
        self._api = api
        self._communicator_id = communicator_id
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
