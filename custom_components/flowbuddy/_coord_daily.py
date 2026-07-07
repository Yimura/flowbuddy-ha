"""Daily aggregation coordinator (15-min cadence)."""

from __future__ import annotations

import logging
from datetime import UTC, date, datetime, timedelta
from datetime import time as dtime
from typing import TYPE_CHECKING

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from ._generated.types import Unset
from .const import DEFAULT_DAILY_INTERVAL_S, DOMAIN

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant

    from .api import FlowBuddyClient

_LOGGER = logging.getLogger(__name__)


class FlowBuddyDailyCoordinator(DataUpdateCoordinator[dict[str, float]]):
    def __init__(self, hass: HomeAssistant, api: FlowBuddyClient, installation_id: str) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_daily_{installation_id}",
            update_interval=timedelta(seconds=DEFAULT_DAILY_INTERVAL_S),
        )
        self._api = api
        self._installation_id = installation_id

    async def _async_update_data(self) -> dict[str, float]:
        today = datetime.combine(date.today(), dtime.min, tzinfo=UTC).date()
        try:
            values = await self._api.get_day_aggregations(self._installation_id, today)
        except Exception as exc:
            raise UpdateFailed(str(exc)) from exc
        result: dict[str, float] = {}
        for v in values:
            measurement = v.measurement
            if measurement is None or isinstance(measurement, Unset):
                continue
            uri = measurement.resource_uri
            val = v.value
            if not isinstance(uri, str) or val is None or isinstance(val, Unset):
                continue
            result[uri] = val
        return result
