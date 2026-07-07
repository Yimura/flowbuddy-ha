"""Tests for FlowBuddyAlarmsCoordinator."""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from custom_components.flowbuddy._coord_alarms import FlowBuddyAlarmsCoordinator
from custom_components.flowbuddy.const import DEFAULT_ALARMS_INTERVAL_S


@pytest.fixture
def mock_api():
    api = MagicMock()
    api.list_open_alarms = AsyncMock(return_value=[])
    return api


def test_interval_is_alarms_default(hass, mock_api):
    coord = FlowBuddyAlarmsCoordinator(hass, mock_api, "iid-1")
    assert coord.update_interval.total_seconds() == DEFAULT_ALARMS_INTERVAL_S


async def test_update_returns_alarm_list(hass, mock_api):
    a = MagicMock(id="alarm-1", status="OPEN")
    mock_api.list_open_alarms.return_value = [a]
    coord = FlowBuddyAlarmsCoordinator(hass, mock_api, "iid-1")
    data = await coord._async_update_data()
    assert data == [a]
