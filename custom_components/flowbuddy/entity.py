"""Entity base + DeviceInfo helpers."""
from __future__ import annotations

from typing import Any

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .api import installation_id as _installation_id
from .const import DOMAIN


def _first_str(*candidates: Any) -> str | None:
    """Return the first non-empty stripped string from candidates."""
    for c in candidates:
        if isinstance(c, str) and c.strip():
            return c.strip()
    return None


def installation_device_info(inst: Any) -> DeviceInfo:
    """Create DeviceInfo for an installation.

    Every field the vendor exposes for an installation can arrive as
    None (nullable spec patch). Use identifier + fallback labels to
    stay HA-compliant.
    """
    iid = _installation_id(inst) or "unknown"
    installation_type = getattr(inst, "installation_type", None)
    model = (
        _first_str(getattr(installation_type, "name", None))
        if installation_type is not None
        else None
    )
    return DeviceInfo(
        identifiers={(DOMAIN, iid)},
        name=_first_str(
            getattr(inst, "identification", None),
            getattr(inst, "customer_name", None),
        )
        or f"FlowBuddy {iid[:8]}",
        manufacturer="FlowBuddy",
        model=model or "Installation",
        configuration_url="https://flowbuddy.earth.be",
    )


def meter_device_info(meter: Any, inst: Any) -> DeviceInfo:
    """Create DeviceInfo for a meter, linked to its installation.

    Every meter field the vendor exposes can be None (spec fully
    nullable) -- serial_number, name, manufacturer, meter_type, and
    the installation's uuid alike. Use fallbacks: serial fallback
    to resource_uri last segment (always present since it's the URL
    the API returned itself), and via_device uses the same fallback
    chain as installation identification.
    """
    iid = _installation_id(inst)
    serial = _first_str(
        getattr(meter, "serial_number", None),
        (getattr(meter, "resource_uri", "") or "").rsplit("/", 1)[-1] or None,
    )
    if not serial:
        # Unusable meter -- give it a synthetic id derived from resource_uri
        # so DeviceInfo doesn't crash; downstream will still show the sensor
        # under a generic device.
        serial = f"meter-unknown-{id(meter)}"
    info = DeviceInfo(
        identifiers={(DOMAIN, serial)},
        name=_first_str(getattr(meter, "name", None)) or f"Meter {serial[:8]}",
        manufacturer=_first_str(getattr(meter, "manufacturer", None)) or "FlowBuddy",
        model=_first_str(getattr(meter, "meter_type", None)) or "Meter",
    )
    # Only wire via_device when we have a real installation id; passing
    # (DOMAIN, None) triggers HA's frame.py:348 warning and will hard-fail
    # in HA 2025.12.
    if iid:
        info["via_device"] = (DOMAIN, iid)
    return info


class FlowBuddyEntity(CoordinatorEntity[Any]):
    """Base entity for all FlowBuddy entities."""

    _attr_has_entity_name = True

    def __init__(self, coordinator, *, unique_id: str) -> None:
        """Initialize the entity."""
        super().__init__(coordinator)
        self._attr_unique_id = unique_id
