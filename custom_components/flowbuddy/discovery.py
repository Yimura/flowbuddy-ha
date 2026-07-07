"""Data-driven measurement -> HA entity description mapping."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Final

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import (
    PERCENTAGE,
    UnitOfApparentPower,
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfFrequency,
    UnitOfPower,
    UnitOfReactivePower,
    UnitOfTemperature,
)

if TYPE_CHECKING:
    from collections.abc import Callable


@dataclass
class Description:
    key: str
    name: str
    device_class: SensorDeviceClass | None
    state_class: SensorStateClass
    native_unit_of_measurement: str
    value_transformer: Callable[[float], float] = field(default=lambda v: v)


# Targeted overrides for vendor mt.name values that ship as generic
# meter-register terminology while the mt.code carries the actual
# semantic. Keep this list small; each entry needs a justification.
#
#   E_gen_pv: vendor emits mt.name="Reverse Active Energy" (OBIS/IEC-62053
#     term for current flowing IN REVERSE through a CT-clamp meter). On
#     the PV sub-meter this is PV production kWh, but "reverse active
#     energy" reads to most users like grid-export from the utility
#     meter. Rename to reflect the code's own semantic.
_NAME_OVERRIDES: Final = {
    "E_gen_pv": "EMS PV energy",
}


def describe(mt: Any) -> Description:
    unit = mt.unit
    code = mt.code or ""
    incremental = bool(mt.is_incremental)
    name = _NAME_OVERRIDES.get(code, mt.name)

    # Power
    if unit == "W":
        return Description(
            mt.code,
            name,
            SensorDeviceClass.POWER,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.WATT,
        )
    if unit == "kW":
        return Description(
            mt.code,
            name,
            SensorDeviceClass.POWER,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.WATT,
            value_transformer=lambda v: v * 1000.0,
        )

    # Energy — kWh+incremental must match before Wh+incremental (both -> ENERGY,
    # different transformers).
    if unit == "kWh" and incremental:
        return Description(
            mt.code,
            name,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL_INCREASING,
            UnitOfEnergy.KILO_WATT_HOUR,
        )
    if unit == "Wh" and incremental:
        return Description(
            mt.code,
            name,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL_INCREASING,
            UnitOfEnergy.KILO_WATT_HOUR,
            value_transformer=lambda v: v / 1000.0,
        )

    # Electrical
    if unit == "V":
        return Description(
            mt.code,
            name,
            SensorDeviceClass.VOLTAGE,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricPotential.VOLT,
        )
    if unit == "A":
        return Description(
            mt.code,
            name,
            SensorDeviceClass.CURRENT,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricCurrent.AMPERE,
        )
    if unit == "Hz":
        return Description(
            mt.code,
            name,
            SensorDeviceClass.FREQUENCY,
            SensorStateClass.MEASUREMENT,
            UnitOfFrequency.HERTZ,
        )
    if unit == "VA":
        return Description(
            mt.code,
            name,
            SensorDeviceClass.APPARENT_POWER,
            SensorStateClass.MEASUREMENT,
            UnitOfApparentPower.VOLT_AMPERE,
        )
    if unit == "var":
        return Description(
            mt.code,
            name,
            SensorDeviceClass.REACTIVE_POWER,
            SensorStateClass.MEASUREMENT,
            UnitOfReactivePower.VOLT_AMPERE_REACTIVE,
        )

    # Percentage — battery SoC (by code hint) must match before generic percent.
    # The FlexMon vendor spec ships SoC with unit="Wh%" (a typo -- confirmed
    # against real tenant data 2026-07-07). Treat both spellings as SoC when
    # the code identifies it as such; ignore isIncremental=True on SoC since
    # SoC is a snapshot, not a cumulative counter.
    code_upper = code.upper()
    if unit in ("%", "Wh%") and ("SOC" in code_upper or code_upper == "SOC_BAT"):
        return Description(
            mt.code, name, SensorDeviceClass.BATTERY, SensorStateClass.MEASUREMENT, PERCENTAGE
        )
    if unit == "%":
        return Description(mt.code, name, None, SensorStateClass.MEASUREMENT, PERCENTAGE)

    # Temperature
    if unit == "°C":
        return Description(
            mt.code,
            name,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            UnitOfTemperature.CELSIUS,
        )

    # Monetary savings (vendor emits "€" as unit on the savings measurement types).
    # HA's MONETARY device_class doesn't strictly require a currency-code unit,
    # but Energy dashboard tooling handles common symbols like "€" fine.
    if unit == "€":
        return Description(
            mt.code,
            name,
            SensorDeviceClass.MONETARY,
            SensorStateClass.TOTAL_INCREASING if incremental else SensorStateClass.MEASUREMENT,
            "EUR",
        )

    # Enum-like unitless values (vendor emits "_Unitless_" for e.g.
    # EMS BAT Charge Direction: 0=idle, positive=charge, negative=discharge).
    # No HA device_class fits; ship a plain numeric sensor with no unit.
    if unit == "_Unitless_":
        return Description(mt.code, name, None, SensorStateClass.MEASUREMENT, None)  # type: ignore[arg-type]

    # Fallback — still create a sensor so unknown units don't silently drop data.
    return Description(mt.code, name, None, SensorStateClass.MEASUREMENT, unit)
