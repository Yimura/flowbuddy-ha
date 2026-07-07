"""Diagnostics dump for FlowBuddy config entries."""
from __future__ import annotations

from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

TO_REDACT = {
    "client_id",
    "client_secret",
    "password",
    "email",
    "refresh_token",
    "access_token",
    "customerName",
    "customerId",
    "customer_name",
    "customer_id",
    "emailAddress",
    "email_address",
}


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics data for a FlowBuddy config entry."""
    data = hass.data.get(DOMAIN, {}).get(entry.entry_id, {})
    installation = data.get("installation")
    instant_coord = data.get("instant_coord")
    daily_coord = data.get("daily_coord")
    alarms_coord = data.get("alarms_coord")
    return async_redact_data(
        {
            "entry": {
                "title": entry.title,
                "data": dict(entry.data),
                "unique_id": entry.unique_id,
            },
            "installation": {
                "uuid": getattr(installation, "uuid", None),
                "identification": getattr(installation, "identification", None),
                "city": getattr(installation, "city", None),
                "country": getattr(installation, "country", None),
            }
            if installation
            else None,
            "coordinators": {
                "instant": _coord_status(instant_coord),
                "daily": _coord_status(daily_coord),
                "alarms": _coord_status(alarms_coord),
            },
        },
        TO_REDACT,
    )


def _coord_status(coord: Any) -> dict[str, Any]:
    """Return coordinator status dict."""
    if coord is None:
        return {"present": False}
    return {
        "present": True,
        "update_interval_s": coord.update_interval.total_seconds()
        if coord.update_interval
        else None,
        "last_update_success": getattr(coord, "last_update_success", None),
        "last_exception": (
            str(getattr(coord, "last_exception", None))
            if getattr(coord, "last_exception", None) is not None
            else None
        ),
        "is_boosted": coord.is_boosted() if hasattr(coord, "is_boosted") else None,
        "is_blocked": coord.is_blocked() if hasattr(coord, "is_blocked") else None,
    }
