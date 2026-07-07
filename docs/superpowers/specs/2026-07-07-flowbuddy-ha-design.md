# FlowBuddy Home Assistant Integration — Design Spec

- Author: andreas.maerten@crimson7.io
- Date: 2026-07-07
- Status: Approved (brainstorming), pending implementation-plan handoff
- Target platform: Home Assistant 2025.x+, Python 3.13
- Distribution: HACS custom repository (public GitHub, MIT license)

## 1. Problem

FlowBuddy (`https://flowbuddy.earth.be`) is IZEN's white-label of the Cast4All **SIMPL** energy monitoring platform, used to visualise solar production, grid usage, battery, and HVAC data for Belgian residential and commercial installations. It provides no first-party Home Assistant integration and no advertised public API.

The owner wants their FlowBuddy installation surfaced natively in Home Assistant so that:

1. Live power (PV, grid, battery, consumption) drives automations and dashboards.
2. Cumulative energy sensors feed HA's Energy dashboard directly (Solar / Grid / Battery cards, plus the community `helios` visualisation card, work with no bridging YAML).
3. Battery, inverter, and HVAC control is available from HA (services and entities), enabling adaptive scheduling from HA's ecosystem instead of only from the SIMPL app.
4. Alarms and events raised by SIMPL appear in HA and can be acknowledged from HA.

## 2. Findings — API is public, no reverse engineering required

Reconnaissance against `https://flowbuddy.earth.be` and its backend revealed a **fully documented public OpenAPI 3.0.1 specification**:

- **API base**: `https://izen.cast4all.energy/flexMon/v1`
- **OpenAPI spec** (unauthenticated fetch): `https://izen.cast4all.energy/flexMon/v1/openapi.json` — 129 endpoints, 217 schemas, HAL+JSON responses, RFC 7807 (`application/problem+json`) error bodies.
- **Auth**: Keycloak OIDC, realm `izen` at `https://auth.izen.cast4all.energy/realms/izen`.
  - Discovery: `https://auth.izen.cast4all.energy/realms/izen/.well-known/openid-configuration`.
  - Supported grants include `client_credentials`, `password`, `authorization_code`, `refresh_token`.
  - Spec advertises a security scheme `clientApiUser` (OAuth2 `client_credentials`, scopes `openid profile email`) with the description: _"OAuth2 connect with ClientApiUser credentials. Login into SIMPL to create new credentials."_
- **Tenant feature flags** exposed via `https://flowbuddy.earth.be/env-config.js` (`window._env_`) reveal which product surfaces are enabled per tenant (e.g. `PV_METER_SELECTION_ENABLED`, `CAPACITY_CHARTS_FLUVIUS_ENABLED`, `MODBUS_ACTIONS_ENABLED`). The integration must not assume all optional surfaces are enabled.
- **`helios-ha.org`** is **not the integration**; it is a Lovelace custom card that reads HA's Energy dashboard. Consequently, the correct architecture is to expose FlowBuddy measurements as HA sensors with proper `device_class` and `state_class` — Energy dashboard, Helios, and every other Energy-dashboard-aware card then work automatically.

### Key API surface used by this integration

| Group | Endpoints | Purpose |
|---|---|---|
| Installations | `GET /installations`, `GET /installations/{id}` | Tenant discovery, single-site selection |
| Meters | `GET /meters?installation={id}`, `GET /meters/{id}` | Physical measurement devices per installation |
| Measurement types | `GET /measurementtypes` | Static catalogue (unit, `isIncremental`, aggregationType) |
| Measurements | `GET /measurements?installation={id}` | Streams (meter × measurementType) — one HA sensor each |
| Live values | `GET /instantvalues?installation={id}` | Latest value per measurement (drives live sensors) |
| Aggregations | `GET /aggregationdayvalues`, `.../monthvalues`, `.../yearvalues` | Pre-bucketed totals (drives energy sensors) |
| Batteries | `GET /batteries`, `POST /batteries/{id}/setChargePower` | Battery info + charge power control |
| Inverters | `GET /inverters`, `POST /inverters/{id}/limitProduction` | PV inverter info + curtailment |
| HVAC | `GET /hvacs`, `POST /hvacs/{id}/setCoolTemperature`, `setHeatTemperature` | Heat-pump / A/C control |
| Alarms | `GET /alarms`, `POST /alarms/{id}/setToClosed`, `addComment` | Notifications + acknowledgement |
| Events | `GET /events`, `GET /eventtypes` | Audit trail |
| Communicators | `POST /communicators/{id}/requestConnectionTest`, `requestPvProductionTest` | Diagnostics from HA |

## 3. Non-goals for v1

- Adding a Lovelace card (upstream `helios` covers the visualisation need).
- Contributing the integration to Home Assistant core (single-vendor Belgian utility; HACS custom is the right distribution).
- Multi-tenant onboarding beyond the current user's installations (HACS users onboard themselves via config flow).
- Historical backfill of years of aggregate data on install — statistics start from install time; the HA `recorder` grows organically. Backfill deferred to v2.
- Modbus action orchestration and EMS scheduling advanced UI — the endpoints are wrapped for API access but not modelled as first-class HA entities in v1.

## 4. Architecture

### 4.1 Repository layout

```
flowbuddy-ha/                                # sibling to HA/ at /home/andre/Documents/HomeAssistant/
├── README.md                                # install + usage + screenshots
├── LICENSE                                  # MIT
├── hacs.json                                # HACS manifest
├── info.md                                  # HACS install screen
├── pyproject.toml                           # dev deps (ruff, pytest, mypy, openapi-python-client)
├── Makefile                                 # `make regen` -> re-run codegen from pinned spec
├── openapi/
│   ├── flexmon-v1.json                      # vendored OpenAPI spec, pinned by version+sha256
│   └── flexmon-v1.sha256                    # integrity guard; CI fails if spec drifts
├── .github/workflows/
│   ├── validate.yml                         # hassfest + HACS validation on PR
│   ├── tests.yml                            # pytest + coverage
│   └── regen-check.yml                      # runs `make regen` -> fails if generated diff
├── custom_components/flowbuddy/
│   ├── __init__.py                          # async_setup_entry, coordinator wiring
│   ├── manifest.json                        # domain, version, iot_class=cloud_polling
│   ├── const.py                             # DOMAIN, defaults, Keycloak URL constants
│   ├── config_flow.py                       # UI flow: auth mode → creds → installation
│   ├── _generated/                          # openapi-python-client output (VENDORED, DO NOT EDIT)
│   │   ├── __init__.py                      # regen header: spec version + generator version
│   │   ├── client.py                        # AuthenticatedClient / Client (httpx-based)
│   │   ├── models/                          # attrs models per schema (217 files)
│   │   ├── api/                             # one module per tag (e.g. api/installation_apis/)
│   │   ├── types.py
│   │   └── errors.py
│   ├── auth.py                              # KeycloakTokenProvider + httpx.Auth adapter
│   ├── api.py                               # FlowBuddyClient — thin facade over _generated
│   ├── coordinator.py                       # FlowBuddyLiveCoordinator + DailyCoordinator + AlarmsCoordinator
│   ├── discovery.py                         # measurementtypes+meters → EntityDescription list
│   ├── entity.py                            # FlowBuddyEntity base (device wiring, via_device)
│   ├── sensor.py                            # dynamic sensors from discovery
│   ├── binary_sensor.py                     # alarms
│   ├── number.py                            # battery setChargePower, inverter limitProduction
│   ├── climate.py                           # HVAC (setCool/HeatTemperature)
│   ├── button.py                            # alarm ack, requestConnectionTest
│   ├── services.yaml                        # ack_alarm, set_charge_power, limit_inverter, ...
│   ├── strings.json                         # base translations
│   ├── translations/{en,nl,fr}.json         # match SIMPL languages
│   └── diagnostics.py                       # redacted config + last-seen data dump
└── tests/
    ├── conftest.py                          # respx (httpx mock) fixtures + sample JSON
    ├── fixtures/                            # captured API responses (redacted)
    ├── test_config_flow.py
    ├── test_auth.py                         # token refresh, 401 retry, single-flight lock
    ├── test_api_facade.py                   # api.py wraps generated calls correctly
    ├── test_coordinator.py                  # partial failure + adaptive backoff
    ├── test_discovery.py                    # every unit/isIncremental combo
    └── test_sensor.py
```

### 4.1.1 Code generation

The upstream OpenAPI 3.0.1 spec is the source of truth for models, request/response shapes, and endpoint URLs. All of that code is **generated, never handwritten**.

- **Generator**: [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client) (async, typed, `attrs`-based models, `httpx` transport). Chosen over `openapi-generator` (JVM-based, less idiomatic Python) and `datamodel-code-generator` (models only, no client).
- **Vendored output**: generated code is committed to `custom_components/flowbuddy/_generated/`. Vendoring (vs generating at install time) matters because:
  1. HACS installs the component as-is — no build step available at the user's HA host.
  2. Users' HA runtime cannot depend on `openapi-python-client` (dev-only tool).
  3. `hassfest` validates only what's committed.
- **Spec pinning**: `openapi/flexmon-v1.json` is committed alongside a `flexmon-v1.sha256`. The `regen-check.yml` workflow re-downloads the spec from the vendor URL, compares the hash, and if it drifts opens a "spec updated upstream" issue rather than silently regenerating. This prevents an upstream breaking change from being auto-merged.
- **Regen command**: `make regen` runs, in order:
  1. `python -m openapi_python_client generate --path openapi/flexmon-v1.json --output-path custom_components/flowbuddy/_generated --overwrite --meta none`
  2. `ruff format` + `ruff check --fix` on the generated tree (removes generator noise, applies project style).
  3. `python -m scripts.check_generated_header` — asserts `_generated/__init__.py` records `spec_version` + `generator_version` for provenance.
- **CI enforcement**: `regen-check.yml` runs `make regen` on every PR and fails if the working tree has any diff — guarantees generated code always matches the pinned spec. Prevents drift where someone hand-edits `_generated/` and the next regen would silently overwrite it.
- **What stays hand-written**:
  - `auth.py` — Keycloak token acquisition + refresh + single-flight lock. Generated client's default auth is trivial bearer; ours needs OIDC lifecycle management.
  - `api.py` — thin facade that (a) constructs the generated `AuthenticatedClient` with the HA-provided `httpx.AsyncClient` and our auth adapter, and (b) exposes convenience methods (`list_installations()`, `instant_values(installation_id)`, `set_charge_power(battery_id, watts)`) that delegate to the generated per-endpoint functions. This isolates the rest of the integration from generator API-shape churn.
  - `coordinator.py`, `discovery.py`, entity platforms, config flow — pure integration logic, uses generated *types* but not generator-specific transport primitives.

### 4.2 Authentication

Two auth modes are supported via config flow. Both use the same token endpoint:
`POST https://auth.izen.cast4all.energy/realms/izen/protocol/openid-connect/token`.

**Primary — `client_credentials`** (recommended, cleanest):

- User creates an "API account" in the SIMPL web UI (Settings → API Accounts, per the `/apiaccounts` endpoint hint).
- Config flow prompts for `Client ID` (UUID) and `Client Secret`.
- Token request: `grant_type=client_credentials&client_id=…&client_secret=…&scope=openid profile email`.

**Fallback — `password`** (Resource Owner Password Grant, for tenants where the API-account UI is admin-only or unavailable):

- Config flow prompts for `Email`, `Password`, and optional `Client ID` (defaulting to the public Keycloak web client `go_flowbuddy`, discovered via `GET https://flowbuddy.earth.be/keycloak.json` at 2026-07-07 Gate B — `{"realm":"izen","resource":"go_flowbuddy","public-client":true}`).
- Token request: `grant_type=password&username=…&password=…&client_id=…&scope=openid profile email`.
- Refresh via `grant_type=refresh_token` — the password grant returns a refresh token; client_credentials does not, so the credentials flow simply re-authenticates on expiry.

**Token lifecycle** — implemented in `auth.py` as `KeycloakTokenProvider`:

- Access token + `expires_at` held in the provider instance.
- On every request (or ahead of it, when refresh timer fires) if `expires_at < now + 60s`, refresh (or re-auth for `client_credentials`) inside an `asyncio.Lock` so concurrent requests don't stampede.
- On `401` from a downstream request, invalidate the token, retry once with a fresh token, then raise `ConfigEntryAuthFailed` (HA triggers the re-auth flow automatically).

**HTTP transport + auth adapter**:

- Uses HA's shared httpx client via `homeassistant.helpers.httpx_client.get_async_client(hass)` — first-class HA helper that inherits proxy config, cert store, and lifecycle management. No separate connection pool.
- `KeycloakTokenProvider` exposes `httpx_auth() -> httpx.Auth`. That adapter implements httpx's `auth_flow` generator: yields a request with the current bearer, if response is `401` refreshes and yields the request again (single retry). Plugs directly into the generated `AuthenticatedClient` via its `token=` / `auth=` hook.
- Token refresh **does not** go through the generated client — it hits `POST .../protocol/openid-connect/token` directly with `httpx.AsyncClient` (Keycloak isn't in the FlexMon OpenAPI spec).

**Secret storage**: HA's `ConfigEntry.data` (encrypted at rest by the storage layer). Never logged. `diagnostics.py` uses `async_redact_data` on `client_secret`, `password`, `refresh_token`, `access_token`.

### 4.3 Discovery — measurements → entities

At `async_setup_entry`:

1. `GET /installations` → auto-select if one, else installation picker was completed during config flow.
2. `GET /meters?installation={id}` → list of meters.
3. `GET /measurementtypes` (paginated, all pages) → keyed by `code`.
4. `GET /measurements?installation={id}` → one HA sensor entity per stream.

Data-driven mapping (in `discovery.py`, no per-code branches):

| `MeasurementType.unit` \ `isIncremental` | HA `device_class` | HA `state_class` | Notes |
|---|---|---|---|
| `W`, `kW` — false | `power` | `measurement` | Auto-scale kW→W native |
| `Wh`, `kWh` — true | `energy` | `total_increasing` | Auto-scale Wh→kWh native |
| `V` — false | `voltage` | `measurement` | |
| `A` — false | `current` | `measurement` | |
| `%` and `code` contains `SOC` — false | `battery` | `measurement` | |
| `%` otherwise — false | (unset) | `measurement` | |
| `°C` — false | `temperature` | `measurement` | |
| `Hz` — false | `frequency` | `measurement` | |
| `VA` — false | `apparent_power` | `measurement` | |
| `var` — false | `reactive_power` | `measurement` | |
| unknown | (unset) | `measurement` | Sensor still created — better than silent drop |

Device grouping:

- One HA `DeviceInfo` per `Installation` (identifiers = `(DOMAIN, installation.uuid)`, model = `installationType.name`, area = derived from `city`).
- One child `DeviceInfo` per `Meter` (identifiers = `(DOMAIN, meter.serialNumber)`, `via_device` = the installation).
- One grandchild `DeviceInfo` per `Battery` / `Inverter` / `HVAC`, `via_device` = its parent meter.

### 4.4 Polling — vendor model informs cadence

Reconnaissance of the FlowBuddy SPA revealed that live data is not a passive stream. The vendor architecture is:

1. **Meters push measurements at their own natural cadence** (typically 60–900 s depending on device — DSO smart meters push slowly, inverter/battery communicators faster). `/instantvalues` returns the last-received value; polling the API faster than the meter pushes yields no new data.
2. **Aggregations are cached upstream** (`/aggregationdayvalues`, `.../monthvalues`, `.../yearvalues`) and are always cheap to fetch — no rate limit observed.
3. **"True real-time" (sub-minute) requires activation**: the SPA calls `POST /installations/{id}/activateContinuousProcessing` (an endpoint that returns 401 unauth but is not in the public OpenAPI spec — it lives in an internal `realtimeorchestration` module) to boost meter push frequency for a bounded window. The activation opens a **5-minute Real-Time Overview (RTO) session** (`RTO_DURATION * 60_000 ms`), after which the meter reverts to its baseline cadence.
4. **Activation is rate-limited per installation**: the SPA handles a `PollingLimitExceeded` server event by writing the installation to `sessionStorage.go_block_rto` and refusing further activation attempts for that installation until the block clears. States observed: `StartRealtime`, `MeterStarting`, `CommunicatorStarted`, `PollingRequested`, `PollingLimitExceeded`, `Stopped`, `ForceStopped`.

**Design consequence**: this integration MUST NOT continuously poll `/instantvalues` at sub-minute intervals — the vendor will block us. Two modes instead:

#### Baseline mode (always-on, safe)

Runs unattended in the background. All defaults below are user-configurable via the Options flow.

| Coordinator | Endpoint | Default interval | Purpose |
|---|---|---|---|
| `FlowBuddyInstantCoordinator` | `GET /instantvalues?installation={id}&pagesize=500` | **90 s** (min 60 s, max 300 s) | Drives live-ish `measurement`-class sensors (power, voltage, current, SoC, temperature). Frequency matches typical meter push cadence — no gain from polling faster. |
| `FlowBuddyDailyCoordinator` | `GET /aggregationdayvalues?installation={id}&fromPeriodStart={today_local_midnight_iso8601}&pagesize=500` | **15 min** | Drives `total_increasing` kWh sensors (Energy dashboard). Aggregations are cached upstream; safe cadence. |
| `FlowBuddyAlarmsCoordinator` | `GET /alarms?installation={id}` (filter open status, verify exact param at implementation) | **5 min** | Feeds `binary_sensor` alarms + per-alarm `button` for ack. |

#### Live mode (opt-in, session-bounded, rate-aware)

Exposed as an HA service, not a background poll:

- **`flowbuddy.enable_realtime(installation_id, duration_minutes=5)`** → calls `POST /installations/{id}/activateContinuousProcessing` (via the internal `realtimeorchestration` module) then temporarily drops `FlowBuddyInstantCoordinator.update_interval` to **20 s** for the duration of the RTO window. Restores baseline interval on window expiry.
- **Guard against rate limits**: subscribe to installation event stream (`GET /events?installation={id}` polled every 30 s during a live session, or use the same event that the SPA reads). On `PollingLimitExceeded`, immediately restore baseline interval, mark installation as `rto_blocked_until = now + 10 min`, log an HA `repairs` entry ("FlowBuddy blocked live polling — vendor rate limit"), and refuse further `enable_realtime` calls until the timer clears.
- **Auto-stop**: after `duration_minutes`, revert interval and stop consuming realtime API budget. Vendor deactivates on its side automatically at the 5-min RTO window end regardless.
- **Typical use**: automation opens live view when dashboard is loaded, or when a specific load pattern needs sub-minute reaction. Not the default.

#### Common behaviour (both modes)

- Partial failure per measurement does not fail the coordinator — a missing value becomes an `unknown` state for that sensor only. `UpdateFailed` is only raised on transport, auth, or full response failure.
- **Adaptive backoff**: on `429` or repeated `5xx`, double the affected coordinator's `update_interval` up to 10 min; halve on next success. After 3 consecutive failures, create an HA `repairs` issue.
- **`PollingLimitExceeded` treated as harder than 429**: 10-min hard block on that installation before any further live-mode activation; baseline coordinators continue at their (already conservative) intervals.

### 4.5 Control (write path)

- **`number.flowbuddy_battery_<serial>_charge_power`** — `POST /batteries/{id}/setChargePower`.
  - Range: `-maxDischargePower … +maxChargePower` (from `BatteryOutputModel`).
  - Step: 100 W. Unit: W.
- **`number.flowbuddy_inverter_<serial>_production_limit`** — `POST /inverters/{id}/limitProduction`.
  - Range: `0 … maxPower`. Step: 100 W. Unit: W.
- **`climate.flowbuddy_hvac_<id>`** — `POST /hvacs/{id}/setCoolTemperature` and `setHeatTemperature`.
  - HVAC modes: `heat`, `cool`, `off` (SIMPL data model at implementation to confirm mode enum).
  - Current temperature sourced from the linked meter's live temperature measurement.
- **`button.flowbuddy_alarm_<id>_ack`** per open alarm — `POST /alarms/{id}/setToClosed`.

Registered services in `services.yaml` (for automations):

```yaml
set_battery_charge_power:
  fields:
    entity_id: { selector: { entity: { domain: number, integration: flowbuddy } } }
    watts: { selector: { number: { min: -20000, max: 20000, step: 100 } } }

limit_inverter:
  fields:
    entity_id: { selector: { entity: { domain: number, integration: flowbuddy } } }
    watts: { selector: { number: { min: 0, max: 20000, step: 100 } } }

ack_alarm:
  fields:
    alarm_id: { selector: { text: {} } }
    comment:  { selector: { text: {} } }

request_connection_test:
  fields:
    communicator_id: { selector: { text: {} } }

enable_realtime:
  # Boost the instant-values coordinator to ~20s for a bounded window by
  # calling POST /installations/{id}/activateContinuousProcessing.
  # Rate-limited by the vendor -- see §4.4 "Live mode".
  fields:
    installation_id: { selector: { text: {} } }
    duration_minutes: { selector: { number: { min: 1, max: 5, step: 1 } }, default: 5 }
```

**Post-write refresh**: after any successful write, schedule `coordinator.async_request_refresh()` after 5 s so state reflects the change (SIMPL propagation is not immediate).

### 4.6 Error handling

| Condition | Behaviour |
|---|---|
| `401 Unauthorized` | Invalidate token → retry once → on second 401 raise `ConfigEntryAuthFailed` (HA re-auth flow) |
| `403 Forbidden` (tenant lacks feature) | Log at INFO once per entity class, skip creating entities of that class |
| `404 Not Found` on write | Remove entity from HA registry on next coordinator reload |
| `429 Too Many Requests` | Adaptive backoff (double interval, cap 5 min) |
| `5xx` / timeout | `UpdateFailed`; adaptive backoff after 3 in a row; create `repairs` issue after 5 |
| RFC 7807 body present | Surface `code` + `identifier` + `extraInfo.message` in log line (single line, no dump) |

### 4.7 HA Energy Dashboard integration

No custom work. The `total_increasing` kWh sensors produced by the mapping table are auto-eligible in **Settings → Dashboards → Energy**:

- **Solar production**: sensor(s) whose measurement code identifies PV production (identified at first setup from `MeasurementType.code` — likely `PV_PRODUCTION_ENERGY` or similar).
- **Grid consumption**: separate `GRID_IMPORT_ENERGY` and `GRID_EXPORT_ENERGY` sensors.
- **Battery**: separate `BATTERY_CHARGE_ENERGY` and `BATTERY_DISCHARGE_ENERGY` sensors if a battery is present.

Once the user picks these in the Energy setup UI, the Energy Distribution card, Helios card, and any other Energy-dashboard-consuming Lovelace card work end-to-end with zero YAML.

### 4.8 Testing

- Unit tests use `respx` (httpx transport mock) with captured JSON fixtures (redacted before commit — installation UUIDs replaced with `00000000-0000-0000-0000-000000000000`, serial numbers replaced with `TEST-SN-…`, email/personal-name fields replaced).
- Generated code under `_generated/` is not directly unit-tested (generator is authoritative); tests exercise `api.py`, `auth.py`, `coordinator.py`, `discovery.py`, and entity platforms.
- Coverage floor: 85% for `api.py`, `auth.py`, `coordinator.py`, `discovery.py`; 70% for entity platforms. `_generated/` excluded from coverage.
- **`test_config_flow.py`**: both auth modes; wrong creds; installation picker (0, 1, N installations); duplicate config prevention.
- **`test_auth.py`**: token refresh; 401 → retry → success; 401 → retry → 401 → `ConfigEntryAuthFailed`; concurrent requests during refresh (single-flight lock); httpx.Auth adapter contract.
- **`test_api_facade.py`**: `api.py` invokes the correct generated endpoint function with correct params; response typing round-trips via generated `attrs` models.
- **`test_coordinator.py`**: normal update; per-measurement missing value; full failure; `429` backoff; `5xx` backoff; recovery halves interval.
- **`test_discovery.py`**: every row of the mapping table; unknown unit still creates sensor; SOC vs generic `%`; kW↔W unit scaling.
- **`test_sensor.py`**: state updates from coordinator; unavailable when coordinator failed; correct `device_class` + `state_class` per fixture.
- CI: `hassfest` (`home-assistant/actions/hassfest@master`) + `hacs/action@main` + `regen-check.yml` on every PR; pytest + coverage on Python 3.13; ruff + mypy strict (with `_generated/` excluded from mypy strict but included in ruff format check).

Manual E2E on the owner's live HA:

1. Install via HACS "custom repository" pointing at the local checkout (`file:///home/andre/Documents/HomeAssistant/flowbuddy-ha`) OR the pushed GitHub repo.
2. Complete config flow with real credentials against `flowbuddy.earth.be`.
3. Verify entities appear grouped by installation → meters → devices.
4. Verify Energy dashboard picks up the kWh sensors.
5. Verify a battery `setChargePower` call round-trips (state reflects change within ~1 min).

### 4.9 Distribution

- Public GitHub repo `flowbuddy-ha` under the owner's account, MIT-licensed.
- `hacs.json`: `{"name": "FlowBuddy", "homeassistant": "2025.1.0", "iot_class": "cloud_polling"}`.
- `info.md`: install screen with feature summary + prerequisites.
- Release process: SemVer tag → GitHub Actions builds the release zip → HACS discovers via tag.
- Not targeting HA core in v1 (single-vendor Belgian utility, high review bar); HACS custom is the intended terminal state.

## 5. Open questions to resolve during implementation

These do not block the design but must be answered before v1 ships. They are called out here so the writing-plans skill can slot investigation tasks in early:

1. **Live-tenant API-account availability** — does the owner's SIMPL account expose the API accounts UI? Confirms the primary auth path is usable. Fallback (`password`) works either way.
2. **Public web-client `client_id` for the password grant fallback** — pin the exact value at implementation by grepping the SPA bundle (`/assets/index-*.js`) once with an authenticated fetch.
3. **Actual `MeasurementType.code` values** in this tenant — the mapping table above is unit-driven so it will work regardless, but the Energy dashboard onboarding docs (README) will name specific codes only after the first run.
4. **Rate limits — vendor model confirmed via SPA recon**. Baseline cadence: 90 s instant / 15 min daily / 5 min alarms (defaults in §4.4). The vendor rejects sub-minute continuous polling with `PollingLimitExceeded`; the SPA blocks the offending installation client-side when it sees this event. Live mode via `activateContinuousProcessing` is 5-min-bounded and per-installation rate-limited. Confirm at implementation: (a) whether `client_credentials` tokens have the scope to call `activateContinuousProcessing`, (b) the exact event name/shape observed on `PollingLimitExceeded` so we can detect it programmatically, (c) whether alarms endpoint accepts a `status=open` filter or requires client-side filtering, (d) actual meter push cadence observed by watching `MeasurementValue.createdOn` deltas over a 10-min window on the live tenant (this sets the practical floor for `FlowBuddyInstantCoordinator.update_interval`).
5. **HVAC mode enum** — verify the `hvac` schema's mode field name and allowed values against a live response before finalising the `climate` entity's `hvac_modes`.
6. **`instantvalues` vs `measurementvalues`** — confirm `/instantvalues` returns latest-per-measurement (assumed from name); if not, fall back to `/measurementvalues?sortby=-timestart&pagesize=1` per measurement (worse — N requests per poll).
7. **`installation` filter on `/instantvalues`** — the spec parameters list didn't include `installation` for `/instantvalues` (unlike `/measurementvalues`). Confirm with a live call; if unsupported, filter client-side or iterate per meter.
8. **Codegen output review** — first `make regen` output will land ~200 model files + ~40 API modules under `_generated/`. Sanity-check bundle size (target < 2 MB) and that `openapi-python-client` handles the spec's `application/hal+json` responses (HAL-specific unmarshalling may need a small custom decoder in `api.py`). If HAL breaks generator, fall back to `application/problem+json` variant (spec offers both content types on same responses).
9. **HA shared httpx client integration** (deferred from P3 review 2026-07-07) — spec §4.2 mandates `homeassistant.helpers.httpx_client.get_async_client(hass)` for shared connection pool + proxy/cert inheritance, but `openapi-python-client`'s generated `AuthenticatedClient` creates its own private `httpx.AsyncClient` internally. `set_async_httpx_client()` exists to inject a shared instance, but binding the FlowBuddy Keycloak bearer via `client.auth=` on a truly shared HA client would leak the token into unrelated integrations' requests through that same client. Decision needed at P9.A implementation: (a) accept the deviation from §4.2 and document; (b) inject shared client + move Keycloak auth from client-level to per-request override; (c) bypass generated HTTP layer entirely. Interim: P3 ships with the generated client's private pool; `activate_continuous_processing` bypass path already uses the (currently unshared) `self._http`.

## 6. Success criteria

The integration is considered successful when:

1. A HACS user can install FlowBuddy from a custom repository, complete the config flow with either auth mode, and see their live power sensors update within 30 s.
2. Their kWh energy sensors are eligible in HA's Energy dashboard configuration and populate the Solar / Grid / Battery cards without any YAML.
3. Calling the `flowbuddy.set_battery_charge_power` service changes the battery's charge power on the SIMPL side (verifiable in the FlowBuddy web UI).
4. Opening an alarm on the SIMPL side surfaces as a `binary_sensor` in HA within 5 minutes; acknowledging it from HA closes it upstream.
5. `hassfest` and `hacs/action` pass in CI on every PR.
6. Test coverage meets the thresholds in §4.8.

## 7. Risks

- **Vendor cooperation**: no formal API contract; endpoint semantics or auth can change without notice. Mitigation: adaptive backoff, `ConfigEntryAuthFailed` on unrecoverable auth, clear diagnostics for issue reports.
- **Vendor rate limits are enforced**: continuous sub-minute polling triggers `PollingLimitExceeded` and the vendor blocks the installation (SPA does this client-side; server likely does too). Mitigation: conservative 90 s baseline, live mode is opt-in + session-bounded + auto-stopped, `PollingLimitExceeded` handled as a 10-min hard block with HA `repairs` visibility, no "aggressive polling" option in Options flow (would be a footgun).
- **`password` grant may be disabled** on the Keycloak client used by the SPA. Mitigation: `client_credentials` is documented and preferred; password is the fallback only.
- **Feature-flag heterogeneity**: `env-config.js` shows many features can be tenant-disabled. Mitigation: skip-on-403 and skip-on-empty-response behaviour, no hard-coded per-feature assumptions.
- **HVAC / battery control mis-operation** could damage equipment or cause discomfort. Mitigation: `number` entities constrained by the vendor-reported ranges (`maxPower`, `maxChargePower`), no default automation shipped, README warns to test before wiring into automations.
- **Vendored generated code bloat**: `_generated/` may add hundreds of files (~217 model files, ~40 tag-grouped API modules). Mitigation: `make regen` post-processes with `ruff format` + `ruff check --fix`; a pre-commit gate rejects PRs where `_generated/` was hand-edited (checked via `regen-check.yml`). Component still loads fine in HA — Python import cost is a one-time hit at HA start.
- **Generator abandonment / spec incompatibility**: `openapi-python-client` may struggle with FlexMon's HAL+JSON responses, or drop maintenance. Mitigation: `api.py` facade isolates the rest of the code from generator specifics; swapping to `datamodel-code-generator` (types only) + handwritten aiohttp calls is a bounded change that touches only `api.py` and `_generated/`.
