# flowbuddy-ha

Home Assistant custom integration for the [FlowBuddy](https://flowbuddy.earth.be)
(SIMPL by Cast4All / IZEN) energy monitoring platform.

**Status:** pre-alpha. Not yet functional.

## Features (planned v1)

- Live and cumulative sensors for PV production, grid import/export, battery,
  and HVAC — wired into HA's Energy dashboard automatically.
- Alarm binary_sensors + acknowledgement button.
- Battery `setChargePower`, inverter `limitProduction`, and HVAC setpoint
  control via `number` and `climate` entities.
- Bounded live-mode boost via the `flowbuddy.enable_realtime` service —
  respects the vendor's polling rate limits.

## Installation

_TBD when v1 is tagged._

## Development

Open this repository in VS Code with the "Dev Containers" extension; the
`.devcontainer/` folder auto-builds a Python 3.13 environment with all
tooling installed.

- `make regen`   — regenerate `custom_components/flowbuddy/_generated/`
                   from the pinned OpenAPI spec
- `make test`    — run the full test suite with coverage
- `make lint`    — ruff check + format
- `make typecheck` — mypy strict on `custom_components/flowbuddy/`

## Design

- Spec: [`docs/superpowers/specs/2026-07-07-flowbuddy-ha-design.md`](docs/superpowers/specs/2026-07-07-flowbuddy-ha-design.md)
- Implementation plan: [`docs/superpowers/plans/2026-07-07-flowbuddy-ha-implementation.md`](docs/superpowers/plans/2026-07-07-flowbuddy-ha-implementation.md)

## License

MIT — see [LICENSE](LICENSE).
