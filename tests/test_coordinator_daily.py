"""Tests for FlowBuddyDailyCoordinator."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from custom_components.flowbuddy._coord_daily import FlowBuddyDailyCoordinator
from custom_components.flowbuddy.const import DEFAULT_DAILY_INTERVAL_S


@pytest.fixture
def mock_api():
    api = MagicMock()
    api.get_day_aggregations = AsyncMock(return_value=[])
    return api


def test_interval_is_daily_default(hass, mock_api):
    coord = FlowBuddyDailyCoordinator(hass, mock_api, "iid-1")
    assert coord.update_interval.total_seconds() == DEFAULT_DAILY_INTERVAL_S


async def test_update_returns_keyed_dict(hass, mock_api):
    class V:
        def __init__(self, uri, val):
            self.measurement = MagicMock(resource_uri=uri)
            self.value = val

    mock_api.get_day_aggregations.return_value = [V("/m/pv", 8.5), V("/m/grid-import", 2.1)]
    coord = FlowBuddyDailyCoordinator(hass, mock_api, "iid-1")
    data = await coord._async_update_data()
    assert data == {"/m/pv": 8.5, "/m/grid-import": 2.1}


async def test_api_exception_raises_update_failed(hass, mock_api):
    from homeassistant.helpers.update_coordinator import UpdateFailed

    mock_api.get_day_aggregations.side_effect = RuntimeError("network")
    coord = FlowBuddyDailyCoordinator(hass, mock_api, "iid-1")
    with pytest.raises(UpdateFailed):
        await coord._async_update_data()
