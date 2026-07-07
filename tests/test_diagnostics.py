"""Tests for diagnostics.py config-entry diagnostics."""

from __future__ import annotations

from datetime import timedelta
from unittest.mock import MagicMock

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.flowbuddy.const import (
    AUTH_MODE_CLIENT_CREDS,
    CONF_AUTH_MODE,
    CONF_INSTALLATION_ID,
    DOMAIN,
)
from custom_components.flowbuddy.diagnostics import async_get_config_entry_diagnostics

IID = "00000000-0000-0000-0000-000000000001"


def _entry_data() -> dict:
    return {
        CONF_AUTH_MODE: AUTH_MODE_CLIENT_CREDS,
        "client_id": "cid",
        "client_secret": "secret-key",
        CONF_INSTALLATION_ID: IID,
        "email": "user@example.com",
    }


async def test_diagnostics_redacts_secret_fields(hass):
    """Verify that secret fields in entry.data are redacted."""
    entry = MockConfigEntry(domain=DOMAIN, unique_id=IID, data=_entry_data())
    entry.add_to_hass(hass)

    # Populate hass.data with minimal entry data (no coordinators)
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {
        "api": MagicMock(),
        "installation": None,
        "instant_coord": None,
        "daily_coord": None,
        "alarms_coord": None,
    }

    diag = await async_get_config_entry_diagnostics(hass, entry)

    # Assert redacted sentinel appears for secrets
    assert "**REDACTED**" in str(diag["entry"]["data"]["client_secret"])
    assert "**REDACTED**" in str(diag["entry"]["data"]["email"])
    assert "**REDACTED**" in str(diag["entry"]["data"]["client_id"])

    # Non-secret fields should still be present
    assert diag["entry"]["title"] == entry.title
    assert diag["entry"]["unique_id"] == IID


async def test_diagnostics_reports_coordinator_status(hass):
    """Verify that coordinator status (update_interval, last_update_success, etc.) is reported."""
    entry = MockConfigEntry(
        domain=DOMAIN, unique_id=IID, data=_entry_data(), title="FlowBuddy Test"
    )
    entry.add_to_hass(hass)

    # Create mock coordinators with realistic properties
    instant_coord = MagicMock(spec=DataUpdateCoordinator)
    instant_coord.update_interval = timedelta(seconds=90)
    instant_coord.last_update_success = True
    instant_coord.last_exception = None
    instant_coord.is_boosted = MagicMock(return_value=False)
    instant_coord.is_blocked = MagicMock(return_value=False)

    daily_coord = MagicMock(spec=DataUpdateCoordinator)
    daily_coord.update_interval = timedelta(seconds=900)
    daily_coord.last_update_success = True
    daily_coord.last_exception = ValueError("test error")
    daily_coord.is_boosted = MagicMock(return_value=True)
    daily_coord.is_blocked = MagicMock(return_value=False)

    alarms_coord = MagicMock(spec=DataUpdateCoordinator)
    alarms_coord.update_interval = timedelta(seconds=300)
    alarms_coord.last_update_success = False
    alarms_coord.last_exception = None
    alarms_coord.is_boosted = MagicMock(return_value=False)
    alarms_coord.is_blocked = MagicMock(return_value=True)

    # Mock installation
    installation = MagicMock()
    installation.uuid = IID
    installation.identification = "test-id"
    installation.city = "Amsterdam"
    installation.country = "NL"

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {
        "api": MagicMock(),
        "installation": installation,
        "instant_coord": instant_coord,
        "daily_coord": daily_coord,
        "alarms_coord": alarms_coord,
    }

    diag = await async_get_config_entry_diagnostics(hass, entry)

    # Assert installation data
    assert diag["installation"]["uuid"] == IID
    assert diag["installation"]["identification"] == "test-id"
    assert diag["installation"]["city"] == "Amsterdam"
    assert diag["installation"]["country"] == "NL"

    # Assert instant coordinator status
    assert diag["coordinators"]["instant"]["present"] is True
    assert diag["coordinators"]["instant"]["update_interval_s"] == 90.0
    assert diag["coordinators"]["instant"]["last_update_success"] is True
    assert diag["coordinators"]["instant"]["last_exception"] is None
    assert diag["coordinators"]["instant"]["is_boosted"] is False
    assert diag["coordinators"]["instant"]["is_blocked"] is False

    # Assert daily coordinator status
    assert diag["coordinators"]["daily"]["present"] is True
    assert diag["coordinators"]["daily"]["update_interval_s"] == 900.0
    assert diag["coordinators"]["daily"]["last_update_success"] is True
    assert diag["coordinators"]["daily"]["last_exception"] == "test error"
    assert diag["coordinators"]["daily"]["is_boosted"] is True
    assert diag["coordinators"]["daily"]["is_blocked"] is False

    # Assert alarms coordinator status
    assert diag["coordinators"]["alarms"]["present"] is True
    assert diag["coordinators"]["alarms"]["update_interval_s"] == 300.0
    assert diag["coordinators"]["alarms"]["last_update_success"] is False
    assert diag["coordinators"]["alarms"]["last_exception"] is None
    assert diag["coordinators"]["alarms"]["is_boosted"] is False
    assert diag["coordinators"]["alarms"]["is_blocked"] is True


async def test_diagnostics_missing_entry_data(hass):
    """Verify that diagnostics gracefully handle missing entry data (before async_setup_entry)."""
    entry = MockConfigEntry(domain=DOMAIN, unique_id=IID, data=_entry_data())
    entry.add_to_hass(hass)

    # Do NOT populate hass.data -- simulate calling diagnostics before setup

    diag = await async_get_config_entry_diagnostics(hass, entry)

    # Should gracefully return diagnostics with coordinators marked absent
    assert diag["entry"]["title"] == entry.title
    assert diag["entry"]["unique_id"] == IID
    assert diag["installation"] is None
    assert diag["coordinators"]["instant"]["present"] is False
    assert diag["coordinators"]["daily"]["present"] is False
    assert diag["coordinators"]["alarms"]["present"] is False
