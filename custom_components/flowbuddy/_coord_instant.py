"""Instant-value coordinator with rate-limit-aware boost."""

from __future__ import annotations

import asyncio
import logging
import time
from datetime import timedelta
from typing import TYPE_CHECKING, Any

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


def _extract_value_and_uri(item: Any) -> tuple[str | None, float | None]:
    """Return (measurement_resource_uri, value) from a realtime-value row.

    ``get_instant_values`` now returns raw dict rows from
    ``/realtimevalues`` (spec §5 Q10 — resident-scope endpoint). Support
    both raw-dict and (legacy) InstantValueOutputModel attribute access
    so tests + future codegen changes don't force a rewrite.
    """
    if isinstance(item, dict):
        measurement = item.get("measurement") or {}
        if not isinstance(measurement, dict):
            return None, None
        uri = measurement.get("resourceUri") or measurement.get("resource_uri")
        raw_val = item.get("value")
        if isinstance(uri, str) and raw_val is not None:
            try:
                return uri, float(raw_val)
            except (TypeError, ValueError):
                return None, None
        return None, None

    try:
        uri = item.measurement.resource_uri
        val = item.value
        if isinstance(uri, str) and val is not None:
            return uri, float(val)
    except AttributeError:
        pass

    additional = getattr(item, "additional_properties", None) or {}
    measurement = additional.get("measurement")
    if not isinstance(measurement, dict):
        return None, None
    uri = measurement.get("resourceUri") or measurement.get("resource_uri")
    raw_val = additional.get("value")
    if not isinstance(uri, str) or raw_val is None:
        return None, None
    return uri, float(raw_val)


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
        """Return {measurement.resource_uri: value} from /measurements.

        Live probe (2026-07-07) showed each Measurement object carries
        ``lastPolledValue`` + ``lastPolledRealtimeValue`` directly, so a
        plain refresh of /measurements gives every current sensor value
        without needing /realtimevalues (which is only populated after
        activateContinuousProcessing and returns empty otherwise). Prefer
        ``lastPolledRealtimeValue`` when a realtime session is active,
        fall back to ``lastPolledValue`` otherwise.
        """
        try:
            measurements = await self._api.list_measurements(self._installation_id)
        except Exception as exc:
            raise UpdateFailed(str(exc)) from exc
        result: dict[str, float] = {}
        for m in measurements:
            uri = getattr(m, "resource_uri", None)
            if not isinstance(uri, str):
                continue
            # Prefer realtime value when present, fall back to polled value.
            val = getattr(m, "last_polled_realtime_value", None)
            if val is None:
                val = getattr(m, "last_polled_value", None)
            if val is None:
                # Dict-style fallback for under-typed generated shapes.
                add = getattr(m, "additional_properties", None) or {}
                val = add.get("lastPolledRealtimeValue") or add.get("lastPolledValue")
            if val is None:
                continue
            try:
                result[uri] = float(val)
            except (TypeError, ValueError):
                continue
        return result

    async def boost(self, duration_minutes: int) -> None:
        async with self._boost_lock:
            if self.is_blocked():
                # is_blocked() returning True guarantees _blocked_until is set
                # (see is_blocked's own None check); no await happened since
                # that check, so this can't have changed underneath us.
                assert self._blocked_until is not None
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
            self._boost_task = self.hass.loop.create_task(self._auto_restore(duration_minutes * 60))

    async def _auto_restore(self, delay_s: float) -> None:
        try:
            await asyncio.sleep(delay_s)
        except asyncio.CancelledError:
            return
        self._boosted_until = None
        self.update_interval = timedelta(seconds=self._base_interval_s)
