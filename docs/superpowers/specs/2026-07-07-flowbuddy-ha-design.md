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
├── pyproject.toml                           # dev deps (ruff, pytest, mypy), Python 3.13
├── .github/workflows/
│   ├── validate.yml                         # hassfest + HACS validation on PR
│   └── tests.yml                            # pytest + coverage
├── custom_components/flowbuddy/
│   ├── __init__.py                          # async_setup_entry, coordinator wiring
│   ├── manifest.json                        # domain, version, iot_class=cloud_polling
│   ├── const.py                             # DOMAIN, defaults, Keycloak URL constants
│   ├── config_flow.py                       # UI flow: auth mode → creds → installation
│   ├── api.py                               # FlowBuddyClient (aiohttp), auth + refresh
│   ├── coordinator.py                       # FlowBuddyLiveCoordinator + DailyCoordinator
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
    ├── conftest.py                          # aioresponses fixtures + sample JSON
    ├── fixtures/                            # captured API responses (redacted)
    ├── test_config_flow.py
    ├── test_api_auth.py                     # token refresh, 401 retry, single-flight lock
    ├── test_coordinator.py                  # partial failure + adaptive backoff
    ├── test_discovery.py                    # every unit/isIncremental combo
    └── test_sensor.py
```

### 4.2 Authentication

Two auth modes are supported via config flow. Both use the same token endpoint:
`POST https://auth.izen.cast4all.energy/realms/izen/protocol/openid-connect/token`.

**Primary — `client_credentials`** (recommended, cleanest):

- User creates an "API account" in the SIMPL web UI (Settings → API Accounts, per the `/apiaccounts` endpoint hint).
- Config flow prompts for `Client ID` (UUID) and `Client Secret`.
- Token request: `grant_type=client_credentials&client_id=…&client_secret=…&scope=openid profile email`.

**Fallback — `password`** (Resource Owner Password Grant, for tenants where the API-account UI is admin-only or unavailable):

- Config flow prompts for `Email`, `Password`, and optional `Client ID` (defaulting to the public web client discovered from the SPA bundle at recon time; if absent, the default `simpl-go-frontend` or equivalent is used — to be pinned at implementation).
- Token request: `grant_type=password&username=…&password=…&client_id=…&scope=openid profile email`.
- Refresh via `grant_type=refresh_token` — the password grant returns a refresh token; client_credentials does not, so the credentials flow simply re-authenticates on expiry.

**Token lifecycle**:

- Access token cached in `FlowBuddyClient._token` with `expires_at` timestamp.
- On every request, if `expires_at < now + 60s`, refresh (or re-auth for client_credentials) inside an `asyncio.Lock` so concurrent requests don't stampede.
- On `401` from a request, invalidate the token, retry once with a fresh token, then raise `ConfigEntryAuthFailed` (HA triggers the re-auth flow automatically).

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

### 4.4 Polling

Two coordinators per installation, sharing one `FlowBuddyClient`.

**`FlowBuddyLiveCoordinator`** — default `update_interval=30s` (user-configurable 10–300s via Options flow):

- `GET /instantvalues?installation={id}&pagesize=500` — one call returns all live values.
- Returns `dict[str, float]` keyed by measurement `resourceUri`.
- Drives all `measurement`-class sensors (power, current, voltage, SoC, temperature, frequency).

**`FlowBuddyDailyCoordinator`** — `update_interval=15m`:

- `GET /aggregationdayvalues?installation={id}&fromPeriodStart={today_local_midnight_iso8601}&pagesize=500`.
- Returns `dict[str, float]` keyed by measurement `resourceUri`.
- Drives all `total_increasing` energy sensors (kWh today).

**Alarms coordinator** — `update_interval=5m`:

- `GET /alarms?installation={id}&status=open` (or equivalent per spec — verify at implementation).
- Feeds `binary_sensor` entities and creates per-alarm `button` for ack.

Partial failure per measurement does not fail the coordinator — a missing value becomes an `unknown` state for that sensor only. `UpdateFailed` is only raised on transport, auth, or complete response failure.

**Adaptive backoff**: on `429` or repeated `5xx`, double `update_interval` up to 5 minutes; halve on next success. After 3 consecutive failures, create an HA `repairs` issue.

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

- Unit tests use `aioresponses` (or `aiohttp`'s test utilities) with captured JSON fixtures (redacted before commit — installation UUIDs replaced with `00000000-0000-0000-0000-000000000000`, serial numbers replaced with `TEST-SN-…`, email/personal-name fields replaced).
- Coverage floor: 85% for `api.py`, `coordinator.py`, `discovery.py`; 70% for entity platforms.
- **`test_config_flow.py`**: both auth modes; wrong creds; installation picker (0, 1, N installations); duplicate config prevention.
- **`test_api_auth.py`**: token refresh; 401 → retry → success; 401 → retry → 401 → `ConfigEntryAuthFailed`; concurrent requests during refresh (single-flight lock).
- **`test_coordinator.py`**: normal update; per-measurement missing value; full failure; `429` backoff; `5xx` backoff; recovery halves interval.
- **`test_discovery.py`**: every row of the mapping table; unknown unit still creates sensor; SOC vs generic `%`; kW↔W unit scaling.
- **`test_sensor.py`**: state updates from coordinator; unavailable when coordinator failed; correct `device_class` + `state_class` per fixture.
- CI: `hassfest` (`home-assistant/actions/hassfest@master`) + `hacs/action@main` on every PR; pytest + coverage on Python 3.13; ruff + mypy strict.

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
4. **Rate limits** — undocumented. Start with 30 s live / 15 m daily / 5 m alarms; watch for `429` and tighten if observed.
5. **HVAC mode enum** — verify the `hvac` schema's mode field name and allowed values against a live response before finalising the `climate` entity's `hvac_modes`.
6. **`instantvalues` vs `measurementvalues`** — confirm `/instantvalues` returns latest-per-measurement (assumed from name); if not, fall back to `/measurementvalues?sortby=-timestart&pagesize=1` per measurement (worse — N requests per poll).
7. **`installation` filter on `/instantvalues`** — the spec parameters list didn't include `installation` for `/instantvalues` (unlike `/measurementvalues`). Confirm with a live call; if unsupported, filter client-side or iterate per meter.

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
- **Rate limiting is undocumented**: overzealous polling could get the tenant throttled or blocked. Mitigation: conservative defaults, adaptive backoff, opt-in "aggressive" polling in Options flow.
- **`password` grant may be disabled** on the Keycloak client used by the SPA. Mitigation: `client_credentials` is documented and preferred; password is the fallback only.
- **Feature-flag heterogeneity**: `env-config.js` shows many features can be tenant-disabled. Mitigation: skip-on-403 and skip-on-empty-response behaviour, no hard-coded per-feature assumptions.
- **HVAC / battery control mis-operation** could damage equipment or cause discomfort. Mitigation: `number` entities constrained by the vendor-reported ranges (`maxPower`, `maxChargePower`), no default automation shipped, README warns to test before wiring into automations.
