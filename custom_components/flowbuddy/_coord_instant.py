"""Instant-value coordinator with rate-limit-aware boost."""
from __future__ import annotations

import asyncio
import logging
import time
from datetime import timedelta
from typing import TYPE_CHECKING

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import FlowBuddyClient, PollingLimitExceededError
from .const import (
    DEFAULT_INSTANT_INTERVAL_S,
    DEFAULT_LIVE_INTERVAL_S,
    DOMAIN,
    MIN_INSTANT_INTERVAL_S,
    POLLING_LIMIT_BLOCK_S,
    RTO_MAX_MINUTES,
)

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)


class FlowBuddyInstantCoordinator(DataUpdateCoordinator[dict[str, float]]):
    def __init__(
        self,
        hass: HomeAssistant,
        api: FlowBuddyClient,
        installation_id: str,
        *,
        base_interval_s: int = DEFAULT_INSTANT_INTERVAL_S,
    ) -> None:
        # Enforce hard floor
        interval_s = max(base_interval_s, MIN_INSTANT_INTERVAL_S)
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_instant_{installation_id}",
            update_interval=timedelta(seconds=interval_s),
        )
        self._api = api
        self._installation_id = installation_id
        self._base_interval_s = interval_s
        self._boosted_until: float | None = None
        self._blocked_until: float | None = None
        self._boost_task: asyncio.Task[None] | None = None
        # Serializes boost() so concurrent callers (e.g. a double-tap on a
        # UI control, or two automations racing to request live mode)
        # never fire overlapping activateContinuousProcessing requests at
        # the vendor -- that endpoint is rate-limited per installation.
        self._boost_lock = asyncio.Lock()

    def is_boosted(self) -> bool:
        return self._boosted_until is not None and time.monotonic() < self._boosted_until

    def is_blocked(self) -> bool:
        return self._blocked_until is not None and time.monotonic() < self._blocked_until

    async def _async_update_data(self) -> dict[str, float]:
        try:
            values = await self._api.get_instant_values(self._installation_id)
        except Exception as exc:
            raise UpdateFailed(str(exc)) from exc
        return {v.measurement.resource_uri: v.value for v in values}

    async def boost(self, duration_minutes: int) -> None:
        async with self._boost_lock:
            if self.is_blocked():
                raise PollingLimitExceededError(
                    f"Installation {self._installation_id} is blocked "
                    f"for {int(self._blocked_until - time.monotonic())}s"
                )
            duration_minutes = min(duration_minutes, RTO_MAX_MINUTES)
            try:
                await self._api.activate_continuous_processing(self._installation_id)
            except PollingLimitExceededError:
                self._blocked_until = time.monotonic() + POLLING_LIMIT_BLOCK_S
                raise
            self._boosted_until = time.monotonic() + duration_minutes * 60
            self.update_interval = timedelta(seconds=DEFAULT_LIVE_INTERVAL_S)
            if self._boost_task and not self._boost_task.done():
                self._boost_task.cancel()
            self._boost_task = self.hass.loop.create_task(
                self._auto_restore(duration_minutes * 60)
            )

    async def _auto_restore(self, delay_s: float) -> None:
        try:
            await asyncio.sleep(delay_s)
        except asyncio.CancelledError:
            return
        self._boosted_until = None
        self.update_interval = timedelta(seconds=self._base_interval_s)
