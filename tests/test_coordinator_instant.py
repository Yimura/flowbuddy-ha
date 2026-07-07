"""Tests for FlowBuddyInstantCoordinator."""
from __future__ import annotations

import asyncio
import time
from unittest.mock import AsyncMock, MagicMock

import pytest
from homeassistant.helpers.update_coordinator import UpdateFailed

from custom_components.flowbuddy._coord_instant import FlowBuddyInstantCoordinator
from custom_components.flowbuddy.api import PollingLimitExceededError
from custom_components.flowbuddy.const import (
    DEFAULT_INSTANT_INTERVAL_S,
    DEFAULT_LIVE_INTERVAL_S,
    MIN_INSTANT_INTERVAL_S,
    POLLING_LIMIT_BLOCK_S,
    RTO_MAX_MINUTES,
)


@pytest.fixture
def mock_api():
    api = MagicMock()
    api.get_instant_values = AsyncMock(return_value=[])
    api.list_measurements = AsyncMock(return_value=[])
    api.activate_continuous_processing = AsyncMock()
    return api


def test_baseline_interval_never_below_min(hass, mock_api):
    coord = FlowBuddyInstantCoordinator(
        hass, mock_api, "iid-1", base_interval_s=5   # try to abuse
    )
    assert coord.update_interval.total_seconds() >= MIN_INSTANT_INTERVAL_S


async def test_boost_shortens_interval(hass, mock_api):
    coord = FlowBuddyInstantCoordinator(hass, mock_api, "iid-1")
    assert coord.update_interval.total_seconds() == DEFAULT_INSTANT_INTERVAL_S
    await coord.boost(1)
    assert coord.is_boosted()
    assert coord.update_interval.total_seconds() == DEFAULT_LIVE_INTERVAL_S
    mock_api.activate_continuous_processing.assert_awaited_once_with("iid-1")


async def test_boost_caps_duration_at_rto_max(hass, mock_api):
    coord = FlowBuddyInstantCoordinator(hass, mock_api, "iid-1")
    await coord.boost(99)   # try to boost for 99 min
    # _boosted_until - now should be <= RTO_MAX_MINUTES * 60
    remaining = coord._boosted_until - time.monotonic()
    assert remaining <= RTO_MAX_MINUTES * 60 + 1


async def test_polling_limit_exceeded_triggers_block(hass, mock_api):
    mock_api.activate_continuous_processing.side_effect = PollingLimitExceededError("blocked")
    coord = FlowBuddyInstantCoordinator(hass, mock_api, "iid-1")
    with pytest.raises(PollingLimitExceededError):
        await coord.boost(5)
    assert coord.is_blocked()
    # A second boost attempt must also raise, immediately
    mock_api.activate_continuous_processing.reset_mock()
    with pytest.raises(PollingLimitExceededError):
        await coord.boost(5)
    # activate should NOT have been called the second time
    mock_api.activate_continuous_processing.assert_not_called()


async def test_auto_restore_reverts_interval(hass, mock_api, monkeypatch):
    # Compress time
    slept: list[float] = []
    # Capture the *real* sleep before patching. The monkeypatch target below
    # is "custom_components.flowbuddy._coord_instant.asyncio.sleep" -- but
    # `_coord_instant`'s `asyncio` name is bound to the actual asyncio
    # module object (not a private copy), so this patches asyncio.sleep
    # *globally* for the duration of the test. If we used the (now-patched)
    # `asyncio.sleep(0)` below to yield control to the loop, we would
    # actually be calling `fake_sleep`, which never suspends -- it would
    # never hand control back to the event loop, and the already-scheduled
    # auto-restore task would never get a chance to run. Use the captured
    # real implementation so these really do yield.
    real_sleep = asyncio.sleep

    async def fake_sleep(s):
        slept.append(s)

    monkeypatch.setattr("custom_components.flowbuddy._coord_instant.asyncio.sleep", fake_sleep)
    coord = FlowBuddyInstantCoordinator(hass, mock_api, "iid-1")
    await coord.boost(1)
    # Give the boost task a chance to run
    await real_sleep(0)
    await real_sleep(0)
    assert coord.update_interval.total_seconds() == DEFAULT_INSTANT_INTERVAL_S
    assert 55 <= slept[0] <= 65


async def test_block_expires_after_block_duration(hass, mock_api, monkeypatch):
    mock_api.activate_continuous_processing.side_effect = PollingLimitExceededError("blocked")
    coord = FlowBuddyInstantCoordinator(hass, mock_api, "iid-1")
    with pytest.raises(PollingLimitExceededError):
        await coord.boost(5)
    assert coord.is_blocked()
    # Fake advance monotonic time past the block window
    orig = time.monotonic
    monkeypatch.setattr(
        "custom_components.flowbuddy._coord_instant.time.monotonic",
        lambda: orig() + POLLING_LIMIT_BLOCK_S + 1,
    )
    assert not coord.is_blocked()


async def test_async_update_data_reads_last_polled_from_measurements(hass, mock_api):
    """_async_update_data now reads Measurement.lastPolledValue directly.

    Live probe (spec §5 Q10 follow-up 2026-07-07): /realtimevalues is
    empty unless activateContinuousProcessing was called, but every
    Measurement object carries its own lastPolledValue +
    lastPolledRealtimeValue. Pull those instead.
    """
    m_pv = MagicMock()
    m_pv.resource_uri = "https://api/measurements/pv-power"
    m_pv.last_polled_realtime_value = None
    m_pv.last_polled_value = 1500.0
    m_grid = MagicMock()
    m_grid.resource_uri = "https://api/measurements/grid-power"
    m_grid.last_polled_realtime_value = 250.0  # realtime overrides polled
    m_grid.last_polled_value = 200.0
    mock_api.list_measurements.return_value = [m_pv, m_grid]

    coord = FlowBuddyInstantCoordinator(hass, mock_api, "iid-1")
    data = await coord._async_update_data()

    assert data == {
        "https://api/measurements/pv-power": 1500.0,
        "https://api/measurements/grid-power": 250.0,  # realtime wins
    }
    mock_api.list_measurements.assert_awaited_with("iid-1")


async def test_api_exception_raises_update_failed(hass, mock_api):
    mock_api.list_measurements.side_effect = RuntimeError("network")
    coord = FlowBuddyInstantCoordinator(hass, mock_api, "iid-1")
    with pytest.raises(UpdateFailed):
        await coord._async_update_data()


async def test_concurrent_boost_calls_serialize_api_calls(hass, mock_api):
    """Concurrent boost() calls must not race the vendor endpoint.

    Without an internal lock, several boost() calls fired within the same
    event-loop tick (e.g. a double-tap on a UI control, or two automations
    both requesting live mode) would each independently pass the
    is_blocked() check and call activate_continuous_processing
    concurrently -- multiplying the request rate against a rate-limited
    per-installation vendor endpoint at the worst possible moment. This
    must be serialized so at most one call is ever in flight.

    Uses a real asyncio.Event barrier (not AsyncMock(return_value=...)) so
    the mock genuinely suspends -- otherwise everything resolves
    synchronously and the race can't be observed.
    """
    proceed = asyncio.Event()
    in_flight = 0
    max_in_flight = 0

    async def barrier(installation_id):
        nonlocal in_flight, max_in_flight
        in_flight += 1
        max_in_flight = max(max_in_flight, in_flight)
        await proceed.wait()
        in_flight -= 1

    mock_api.activate_continuous_processing.side_effect = barrier
    coord = FlowBuddyInstantCoordinator(hass, mock_api, "iid-1")
    tasks = [asyncio.create_task(coord.boost(1)) for _ in range(5)]
    for _ in range(20):
        await asyncio.sleep(0)
    proceed.set()
    await asyncio.gather(*tasks, return_exceptions=True)
    assert max_in_flight == 1, f"boost() allowed {max_in_flight} concurrent vendor calls"
