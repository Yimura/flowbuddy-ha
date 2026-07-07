"""Entity base + DeviceInfo helpers."""
from __future__ import annotations

from typing import Any

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


def installation_device_info(inst: Any) -> DeviceInfo:
    """Create DeviceInfo for an installation."""
    return DeviceInfo(
        identifiers={(DOMAIN, inst.uuid)},
        name=inst.identification,
        manufacturer="FlowBuddy",
        model=inst.installation_type.name if inst.installation_type else "Installation",
        configuration_url="https://flowbuddy.earth.be",
    )


def meter_device_info(meter: Any, inst: Any) -> DeviceInfo:
    """Create DeviceInfo for a meter, linked to its installation."""
    return DeviceInfo(
        identifiers={(DOMAIN, meter.serial_number)},
        name=meter.name,
        manufacturer=meter.manufacturer,
        model=meter.meter_type,
        via_device=(DOMAIN, inst.uuid),
    )


class FlowBuddyEntity(CoordinatorEntity[Any]):
    """Base entity for all FlowBuddy entities."""

    _attr_has_entity_name = True

    def __init__(self, coordinator, *, unique_id: str) -> None:
        """Initialize the entity."""
        super().__init__(coordinator)
        self._attr_unique_id = unique_id
