# FlowBuddy for Home Assistant

Native integration for the FlowBuddy energy-monitoring platform (SIMPL by
Cast4All / IZEN — flowbuddy.earth.be).

**v0.1.0 — resident-scope, read-only.** Sensors + Energy dashboard work
today; battery/inverter/HVAC control and alarms are installer-scope and
will 403 for most resident accounts (tracked as follow-up).

## What you get in v0.1.0

- Sensors for battery SoC, grid import/export power, PV power, and their
  cumulative energy counters — `total_increasing` kWh sensors wired
  straight into HA's Energy dashboard, no extra setup.
- An installation → meter device tree.

## Not yet working for resident accounts

- Battery/inverter (`number`) and HVAC (`climate`) control + their
  services — installer-scope, 403 for residents.
- Alarm binary_sensors + `ack_alarm` — same 403 story.
- `flowbuddy.enable_realtime` — untested (API Accounts aren't available
  on resident-tier logins).

## Prerequisites

- A FlowBuddy account (flowbuddy.earth.be) — your normal email + password.
- Use auth mode **password**, not `client_credentials` — the latter needs
  an "API Account" that resident-tier accounts don't have.

## Setup

Settings → Devices & Services → Add Integration → "FlowBuddy" → pick
**password** mode → email + password (leave `client_id` at its default,
`go_flowbuddy`) → pick your installation.
