"""Tests for button entities."""

from __future__ import annotations

from unittest.mock import AsyncMock

import pytest

from custom_components.flowbuddy.button import (
    AlarmAckButton,
    RequestConnectionTestButton,
)


@pytest.fixture
def mock_alarm():
    """Mock an alarm object."""
    alarm = AsyncMock()
    alarm.id = "alarm-1"
    alarm.priority = "HIGH"
    alarm.status = "OPEN"
    return alarm


@pytest.fixture
def mock_installation():
    """Mock an installation object."""
    inst = AsyncMock()
    inst.uuid = "00000000-0000-0000-0000-000000000001"
    inst.identification = "TEST-INST-1"
    return inst


@pytest.fixture
def mock_communicator():
    """Mock a communicator object."""
    comm = AsyncMock()
    comm.id = "comm-1"
    comm.identification = "Communicator 1"
    return comm


@pytest.fixture
def mock_coordinator():
    """Mock a coordinator."""
    coord = AsyncMock()
    coord.data = []
    return coord


@pytest.fixture
def mock_api():
    """Mock the API client."""
    api = AsyncMock()
    return api


async def test_alarm_ack_button_unique_id(load_fixture):
    """Test AlarmAckButton has correct unique_id."""
    from custom_components.flowbuddy._generated.models.alarm_output_model import (
        AlarmOutputModel,
    )
    from unittest.mock import MagicMock

    raw = load_fixture("alarms_open.json")
    alarm = AlarmOutputModel.from_dict(raw["_embedded"]["alarms"][0])
    installation = MagicMock(uuid="00000000-0000-0000-0000-000000000001")
    coordinator = MagicMock()
    coordinator.data = [alarm]
    button = AlarmAckButton(
        coordinator=coordinator,
        api=AsyncMock(),
        alarm=alarm,
        installation=installation,
    )
    assert button.unique_id == "00000000-0000-0000-0000-000000000001:alarm:alarm-1:ack"


async def test_alarm_ack_button_calls_close_alarm(load_fixture):
    """Test AlarmAckButton.async_press calls api.close_alarm."""
    from custom_components.flowbuddy._generated.models.alarm_output_model import (
        AlarmOutputModel,
    )
    from unittest.mock import MagicMock

    raw = load_fixture("alarms_open.json")
    alarm = AlarmOutputModel.from_dict(raw["_embedded"]["alarms"][0])
    installation = MagicMock(uuid="00000000-0000-0000-0000-000000000001")
    coordinator = MagicMock()
    coordinator.data = [alarm]
    api = AsyncMock()
    button = AlarmAckButton(
        coordinator=coordinator,
        api=api,
        alarm=alarm,
        installation=installation,
    )
    await button.async_press()
    api.close_alarm.assert_awaited_once_with("alarm-1")


async def test_request_connection_test_button_unique_id(mock_communicator, mock_installation, mock_coordinator):
    """Test RequestConnectionTestButton has correct unique_id."""
    button = RequestConnectionTestButton(
        coordinator=mock_coordinator,
        api=AsyncMock(),
        communicator=mock_communicator,
        installation=mock_installation,
    )
    assert button.unique_id == f"{mock_installation.uuid}:communicator:{mock_communicator.id}:connection_test"


async def test_request_connection_test_button_calls_api(mock_communicator, mock_installation, mock_coordinator, mock_api):
    """Test RequestConnectionTestButton.async_press calls api.request_connection_test."""
    button = RequestConnectionTestButton(
        coordinator=mock_coordinator,
        api=mock_api,
        communicator=mock_communicator,
        installation=mock_installation,
    )
    await button.async_press()
    mock_api.request_connection_test.assert_awaited_once_with(mock_communicator.id)
