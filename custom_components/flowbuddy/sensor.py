"""Sensor platform."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import UnitOfEnergy
from homeassistant.helpers.restore_state import RestoreEntity
from homeassistant.util.dt import utcnow

from .api import installation_id as _iid
from .const import DEFAULT_INSTANT_INTERVAL_S, DOMAIN
from .discovery import describe
from .entity import FlowBuddyEntity, meter_device_info

if TYPE_CHECKING:
    import datetime as dt
    from collections.abc import Iterable

    from homeassistant.config_entries import ConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback
    from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


class FlowBuddySensor(FlowBuddyEntity, SensorEntity):
    """A single measurement, sourced from either the instant or daily coordinator."""

    def __init__(
        self,
        *,
        coordinator: DataUpdateCoordinator[Any],
        installation_uuid: str,
        meter: Any,
        installation: Any,
        measurement: Any,
        measurement_type: Any,
    ) -> None:
        desc = describe(measurement_type)
        super().__init__(
            coordinator,
            unique_id=f"{installation_uuid}:{measurement.resource_uri}",
        )
        self._measurement_uri = measurement.resource_uri
        self._desc = desc
        self._attr_name = desc.name
        self._attr_native_unit_of_measurement = desc.native_unit_of_measurement
        self._attr_device_class = desc.device_class
        self._attr_state_class = desc.state_class
        self._attr_device_info = meter_device_info(meter, installation)

    @property
    def native_value(self) -> float | None:
        raw = self.coordinator.data.get(self._measurement_uri)
        return self._desc.value_transformer(raw) if raw is not None else None


class FlowBuddyIntegratedEnergySensor(FlowBuddyEntity, RestoreEntity, SensorEntity):
    """Derives a total_increasing kWh sensor from a power (W) source.

    Motivation: the FlexMon EMS box exposes EMS_PV_POWER (W) but no
    cumulative kWh peer measurement. The HA Energy dashboard's Solar
    card requires a total_increasing kWh sensor, and the P1 meter
    cannot fill this gap because it never sees self-consumed PV.

    Uses trapezoidal integration between successive coordinator ticks
    with a gap guard: if the elapsed time since the last tick exceeds
    ``max_gap_s`` (default 6x poll interval), the tick moves the
    baseline forward without accumulating -- prevents overnight
    outages, HA restarts, and coordinator backoff from injecting
    fictional kWh into the statistics.
    """

    _attr_device_class = SensorDeviceClass.ENERGY
    _attr_state_class = SensorStateClass.TOTAL_INCREASING
    _attr_native_unit_of_measurement = UnitOfEnergy.KILO_WATT_HOUR
    _attr_suggested_display_precision = 3

    def __init__(
        self,
        *,
        coordinator: DataUpdateCoordinator[Any],
        installation_uuid: str,
        meter: Any,
        installation: Any,
        source_measurement: Any,
        source_name: str,
        max_gap_s: float,
    ) -> None:
        super().__init__(
            coordinator,
            unique_id=f"{installation_uuid}:{source_measurement.resource_uri}:integrated_energy",
        )
        self._source_uri = source_measurement.resource_uri
        self._max_gap_s = max_gap_s
        self._total: float = 0.0
        self._last_watts: float | None = None
        self._last_ts: dt.datetime | None = None
        self._attr_name = f"{source_name} energy"
        self._attr_device_info = meter_device_info(meter, installation)

    @staticmethod
    def _now() -> dt.datetime:
        """Indirection so tests can freeze the clock."""
        return utcnow()

    @property
    def native_value(self) -> float:
        return self._total

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        last_state = await self.async_get_last_state()
        if last_state is not None and last_state.state not in (
            None,
            "",
            "unknown",
            "unavailable",
        ):
            try:
                self._total = float(last_state.state)
            except (TypeError, ValueError):
                self._total = 0.0
        # Force one skipped tick after restart: leave _last_ts=None so the
        # first coordinator update doesn't accumulate against a stale
        # last-known-state timestamp (which is not preserved anyway).

    def _accumulate_from_coordinator(self) -> None:
        """Consume one coordinator tick and update the running total.

        Separated from ``_handle_coordinator_update`` so unit tests can
        drive the integration math without needing a live ``hass``
        object attached to the entity (CoordinatorEntity's default
        _handle_coordinator_update calls async_write_ha_state which
        crashes without hass wired up).
        """
        raw = self.coordinator.data.get(self._source_uri)
        if raw is None:
            return
        watts = float(raw)
        now = self._now()
        if self._last_ts is not None and self._last_watts is not None:
            dt_s = (now - self._last_ts).total_seconds()
            if 0 < dt_s <= self._max_gap_s:
                avg_w = (self._last_watts + watts) / 2.0
                # W · s -> kWh: divide by 3.6e6.
                self._total += avg_w * dt_s / 3_600_000.0
        self._last_watts = watts
        self._last_ts = now

    def _handle_coordinator_update(self) -> None:
        self._accumulate_from_coordinator()
        super()._handle_coordinator_update()


def _is_pv_power(mt: Any) -> bool:
    """True if the measurement type describes PV power (W or kW).

    Permissive: matches on unit in ("W", "kW") plus the substring "pv" in
    either the vendor ``code`` or ``name``, case-insensitive. Prior art at
    ``discovery.py::describe`` normalizes both to ``UnitOfPower.WATT`` via
    a value_transformer, so both are legitimate raw-unit shapes coming out
    of the vendor spec -- pinning "W" only silently missed kW-emitting
    tenants.
    """
    if mt is None or getattr(mt, "unit", None) not in ("W", "kW"):
        return False
    label = f"{(getattr(mt, 'code', '') or '')} {(getattr(mt, 'name', '') or '')}".lower()
    return "pv" in label


def _is_pv_energy(mt: Any) -> bool:
    """True if the measurement type describes cumulative PV energy (Wh/kWh, incremental)."""
    if (
        mt is None
        or getattr(mt, "unit", None) not in ("Wh", "kWh")
        or not bool(getattr(mt, "is_incremental", False))
    ):
        return False
    label = f"{(getattr(mt, 'code', '') or '')} {(getattr(mt, 'name', '') or '')}".lower()
    return "pv" in label


def _needs_pv_integrator(
    measurements: list[Any], measurementtypes_by_uri: dict[str, Any]
) -> Iterable[tuple[Any, Any]]:
    """Yield ``(measurement, measurement_type)`` for each PV power measurement
    that lacks a cumulative PV energy peer on the same meter."""
    for m in measurements:
        if getattr(m, "measurement_type", None) is None or getattr(m, "meter", None) is None:
            continue
        mt = measurementtypes_by_uri.get(m.measurement_type.resource_uri)
        if not _is_pv_power(mt):
            continue
        meter_uri = m.meter.resource_uri
        peer_has_energy = any(
            getattr(peer, "measurement_type", None) is not None
            and getattr(peer, "meter", None) is not None
            and peer.meter.resource_uri == meter_uri
            and _is_pv_energy(measurementtypes_by_uri.get(peer.measurement_type.resource_uri))
            for peer in measurements
        )
        if not peer_has_energy:
            yield m, mt


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FlowBuddy sensors from the discovery data cached in hass.data."""
    data = hass.data[DOMAIN][entry.entry_id]
    entities: list[SensorEntity] = []
    for measurement in data["measurements"]:
        # Spec (openapi/flexmon-v1.json) marks every $ref property nullable,
        # and the live tenant does return null for these links on some rows
        # -- guard both before dereferencing .resource_uri, or one bad
        # measurement would raise AttributeError and fail platform setup
        # for every sensor, not just the affected one.
        if measurement.measurement_type is None:
            _LOGGER.debug(
                "Skipping measurement %s with no measurement_type link",
                measurement.resource_uri,
            )
            continue
        mt = data["measurementtypes_by_uri"].get(measurement.measurement_type.resource_uri)
        if mt is None:
            continue
        if measurement.meter is None:
            _LOGGER.debug("Skipping measurement %s with no meter link", measurement.resource_uri)
            continue
        meter = data["meters_by_uri"].get(measurement.meter.resource_uri)
        if meter is None:
            continue
        # All measurements route to instant_coord: Measurement.lastPolledValue
        # already carries both live power AND cumulative energy counters in
        # the same payload. The daily coordinator's separate
        # /aggregationdayvalues filter matches zero rows because real
        # responses ship periodStart=null (spec vs runtime mismatch),
        # so it's not useful as a data source right now.
        coord = data["instant_coord"]
        entities.append(
            FlowBuddySensor(
                coordinator=coord,
                installation_uuid=(_iid(data["installation"]) or "unknown"),
                meter=meter,
                installation=data["installation"],
                measurement=measurement,
                measurement_type=mt,
            )
        )

    # Derive a total_increasing kWh sensor from any PV power measurement
    # that has no cumulative PV energy peer on the same meter. Unlocks the
    # HA Energy dashboard Solar card + Helios lovelace card without asking
    # the user to configure a Riemann-sum helper.
    coord = data["instant_coord"]
    update_interval = getattr(coord, "update_interval", None)
    poll_interval_s = (
        update_interval.total_seconds()
        if update_interval is not None
        else DEFAULT_INSTANT_INTERVAL_S
    )
    max_gap_s = 6.0 * poll_interval_s
    for src_meas, src_mt in _needs_pv_integrator(
        data["measurements"], data["measurementtypes_by_uri"]
    ):
        meter = data["meters_by_uri"].get(src_meas.meter.resource_uri)
        if meter is None:
            continue
        entities.append(
            FlowBuddyIntegratedEnergySensor(
                coordinator=coord,
                installation_uuid=(_iid(data["installation"]) or "unknown"),
                meter=meter,
                installation=data["installation"],
                source_measurement=src_meas,
                source_name=(src_mt.name or "PV power"),
                max_gap_s=max_gap_s,
            )
        )

    async_add_entities(entities)
