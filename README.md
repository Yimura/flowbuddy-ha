# flowbuddy-ha

Home Assistant custom integration for [FlowBuddy](https://flowbuddy.earth.be)
(SIMPL by Cast4All / IZEN) — the energy-monitoring platform used by IZEN's
Belgian residential/commercial solar + battery installations.

**Status:** v0.1.0. Read-only, resident-scope: sensors + Energy dashboard.
Control entities exist but will 403 for most resident accounts (see
"What doesn't work yet" below).

## What works in v0.1.0

- Sensors for every measurement FlowBuddy exposes for your installation:
  battery state of charge, grid import/export power, PV power, and their
  cumulative energy counters (in Wh, converted to kWh where the vendor
  reports kWh-incremental units).
- Cumulative energy sensors are `total_increasing` kWh sensors, so they
  plug directly into HA's **Energy dashboard** (Solar / Grid / Battery
  cards) with no extra configuration.
- An installation-level device tree: each meter is its own HA device,
  linked via `via_device` to the parent installation device.
- Open-alarm `binary_sensor`s (subject to the 403 caveat below).

## What doesn't work yet

- **Battery / inverter / HVAC control** (`number.*` setpoints, `climate.*`,
  the `set_battery_charge_power` / `limit_inverter` services): these call
  installer-scope endpoints. A plain resident login gets HTTP 403. If you
  have installer credentials they should work, but this hasn't been
  validated against a live installer tenant.
- **Alarm binary_sensors / `ack_alarm`**: same story — alarm endpoints are
  403 for resident credentials in the tenant this was built against.
- **`flowbuddy.enable_realtime` service**: untested against a live tenant.
  FlowBuddy's "API Accounts" feature (which issues `client_credentials`
  service-account creds) isn't available on resident-tier accounts, so
  this was never exercised end-to-end. It may also 403.

None of the above breaks setup — the integration degrades gracefully
(entities requiring installer scope just won't do anything useful yet)
rather than failing to load.

## Prerequisites

- A FlowBuddy account at [flowbuddy.earth.be](https://flowbuddy.earth.be)
  with your email + password.
- **Do not use `client_credentials` auth mode** unless you know you have
  an "API Account" — that UI is not exposed to resident-tier accounts.
  Use `password` mode with your normal login instead.

## Install via HACS

1. HACS → the "⋮" menu (top right) → **Custom repositories**.
2. Add `https://github.com/Yimura/flowbuddy-ha`, category **Integration**.
3. Find "FlowBuddy" in HACS → **Install**.
4. Restart Home Assistant.

## Configure

1. Settings → Devices & Services → **Add Integration** → search
   "FlowBuddy".
2. Pick the **password** auth mode.
3. Enter your FlowBuddy email + password. Leave `client_id` at its
   default (`go_flowbuddy`) — that's the SPA's own public client ID, not
   something you need to look up.
4. Pick your installation from the list. If your account only has one,
   it's pre-selected.

The integration polls on a schedule appropriate for FlowBuddy's rate
limits; see the design spec (linked below) for the polling model if
you're curious.

## Development

Open this repository in VS Code with the "Dev Containers" extension; the
`.devcontainer/` folder builds a Python 3.13 environment with all tooling
pinned.

- `make regen`      — regenerate `custom_components/flowbuddy/_generated/`
                      from the pinned OpenAPI spec
- `make test`       — run the full test suite with coverage
- `make lint`       — ruff check + format
- `make typecheck`  — mypy strict on `custom_components/flowbuddy/`
- `make ci`         — lint + typecheck + test (what CI runs)

## Known limitations / open questions

v0.1.0 is intentionally minimal: resident-scope read-only sensors plus
Energy dashboard integration. Tracked follow-ups (installer API access,
adaptive backoff, reauth edge cases, code cleanup) live in the
[repo issue tracker](https://github.com/Yimura/flowbuddy-ha/issues).

## License

MIT — see [LICENSE](LICENSE).
