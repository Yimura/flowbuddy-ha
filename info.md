# FlowBuddy for Home Assistant

Native integration for the FlowBuddy energy monitoring platform (SIMPL by
Cast4All / IZEN — flowbuddy.earth.be).

## What you get

- Sensors for live PV production, grid import/export, battery, HVAC.
- Automatic wiring into HA's Energy dashboard.
- Alarm binary_sensors + acknowledgement.
- Battery setChargePower, inverter limitProduction, HVAC setpoint control.
- Opt-in bounded live-mode boost via `flowbuddy.enable_realtime` service.

## Prerequisites

- A FlowBuddy account with API credentials, or an installer/admin login.
