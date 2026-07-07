"""Diagnostics dump for FlowBuddy config entries."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from homeassistant.components.diagnostics import async_redact_data

from .const import DOMAIN

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.core import HomeAssistant

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
            "discovery": {
                "meters": [_meter_summary(m) for m in data.get("meters", [])],
                "measurements": [
                    _measurement_summary(m, data.get("measurementtypes_by_uri", {}))
                    for m in data.get("measurements", [])
                ],
                "communicators": [_communicator_summary(c) for c in data.get("communicators", [])],
            },
        },
        TO_REDACT,
    )


def _meter_summary(meter: Any) -> dict[str, Any]:
    return {
        "resource_uri": getattr(meter, "resource_uri", None),
        "serial_number": getattr(meter, "serial_number", None),
        "name": getattr(meter, "name", None),
        "manufacturer": getattr(meter, "manufacturer", None),
        "meter_type": getattr(meter, "meter_type", None),
    }


def _measurement_summary(
    measurement: Any, measurementtypes_by_uri: dict[str, Any]
) -> dict[str, Any]:
    mt_ref = getattr(measurement, "measurement_type", None)
    mt = measurementtypes_by_uri.get(mt_ref.resource_uri) if mt_ref is not None else None
    return {
        "resource_uri": getattr(measurement, "resource_uri", None),
        "meter_uri": (
            getattr(measurement.meter, "resource_uri", None) if measurement.meter else None
        ),
        "measurement_type": {
            "resource_uri": getattr(mt_ref, "resource_uri", None),
            "code": getattr(mt, "code", None) if mt else None,
            "name": getattr(mt, "name", None) if mt else None,
            "unit": getattr(mt, "unit", None) if mt else None,
            "is_incremental": getattr(mt, "is_incremental", None) if mt else None,
        },
    }


def _communicator_summary(comm: Any) -> dict[str, Any]:
    comm_type = getattr(comm, "type_", None)
    return {
        "external_id": getattr(comm, "external_id", None),
        "logical_device_name": getattr(comm, "logical_device_name", None),
        "firm_ware_version": getattr(comm, "firm_ware_version", None),
        "status": getattr(comm, "status", None),
        "type": getattr(comm_type, "name", None) if comm_type else None,
    }


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
