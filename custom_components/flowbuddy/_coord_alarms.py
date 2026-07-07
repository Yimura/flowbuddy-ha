"""Alarms coordinator (5-min cadence)."""
from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import FlowBuddyClient
from .const import DEFAULT_ALARMS_INTERVAL_S, DOMAIN

_LOGGER = logging.getLogger(__name__)


class FlowBuddyAlarmsCoordinator(DataUpdateCoordinator[list]):
    def __init__(
        self, hass: HomeAssistant, api: FlowBuddyClient, installation_id: str
    ) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_alarms_{installation_id}",
            update_interval=timedelta(seconds=DEFAULT_ALARMS_INTERVAL_S),
        )
        self._api = api
        self._installation_id = installation_id

    async def _async_update_data(self) -> list:
        try:
            values = await self._api.list_open_alarms(self._installation_id)
        except Exception as exc:
            raise UpdateFailed(str(exc)) from exc
        return list(values)
