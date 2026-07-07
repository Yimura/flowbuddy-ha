"""Daily aggregation coordinator (15-min cadence)."""
from __future__ import annotations

import logging
from datetime import date, datetime, time as dtime, timezone

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from datetime import timedelta

from .api import FlowBuddyClient
from .const import DEFAULT_DAILY_INTERVAL_S, DOMAIN

_LOGGER = logging.getLogger(__name__)


class FlowBuddyDailyCoordinator(DataUpdateCoordinator[dict[str, float]]):
    def __init__(
        self, hass: HomeAssistant, api: FlowBuddyClient, installation_id: str
    ) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_daily_{installation_id}",
            update_interval=timedelta(seconds=DEFAULT_DAILY_INTERVAL_S),
        )
        self._api = api
        self._installation_id = installation_id

    async def _async_update_data(self) -> dict[str, float]:
        today = datetime.combine(date.today(), dtime.min, tzinfo=timezone.utc).date()
        try:
            values = await self._api.get_day_aggregations(self._installation_id, today)
        except Exception as exc:
            raise UpdateFailed(str(exc)) from exc
        return {v.measurement.resource_uri: v.value for v in values}
