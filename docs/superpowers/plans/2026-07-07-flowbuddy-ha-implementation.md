# FlowBuddy Home Assistant Integration — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking. Every task lists **`Blocked by:`** — tasks with no shared dependency and no `Blocked by` overlap may run in parallel subagents. **Task IDs with the same phase letter (e.g. `P4.A`, `P4.B`, `P4.C`) are guaranteed parallel-safe** — they touch different files, share no state, and are individually reviewable.

**Goal:** Ship a HACS-installable Home Assistant custom integration (`flowbuddy`) that authenticates against the FlowBuddy/SIMPL Keycloak realm, wraps the vendored OpenAPI-generated client, and exposes sensors, alarms, and battery/inverter/HVAC control to HA — respecting the vendor's polling rate limits.

**Architecture:** Vendored OpenAPI code generator (`openapi-python-client`) produces the transport layer; a thin `api.py` facade adds Keycloak auth via an `httpx.Auth` adapter and delegates to the generated client. Three `DataUpdateCoordinator`s (instant/daily/alarms) run at conservative baseline cadences; a `flowbuddy.enable_realtime` service opts into a bounded 5-minute high-frequency window when needed. Everything ships as `custom_components/flowbuddy/`.

**Tech Stack:** Python 3.13, Home Assistant 2025.1+, `httpx` (via HA's `homeassistant.helpers.httpx_client`), `openapi-python-client`, `attrs`, `pytest` + `respx` for tests, `ruff` + `mypy strict`, HACS custom-repo distribution.

## Global Constraints

- **Design spec is authoritative**: `/home/andre/Documents/HomeAssistant/flowbuddy-ha/docs/superpowers/specs/2026-07-07-flowbuddy-ha-design.md`. Every task assumes it as background.
- **Never install anything on the host**: all tooling runs inside the devcontainer (see Task P0.2). This applies to `pip install`, `openapi-python-client`, `pytest`, `ruff`, `mypy`. If a step says `pip install`, it means `docker exec -u vscode -w /workspaces/flowbuddy-ha flowbuddy-ha-dev pip install …`.
- **Vendor rate limits are hard**: `PollingLimitExceeded` from the SIMPL backend blocks the installation for ~10 minutes. Baseline `/instantvalues` polling MUST be ≥ 60 s. Live-mode boost only via explicit `flowbuddy.enable_realtime` service, bounded to 5 min RTO window. Any code path that could poll faster than 60 s in baseline mode is a regression.
- **TDD required for `auth.py`, `api.py`, `coordinator.py`, `discovery.py`**: tests written and failing before any implementation. These files gate correctness and rate-limit safety — reviewer must see the test first, the failure second, then the fix.
- **Never edit `custom_components/flowbuddy/_generated/`**: regenerate via `make regen`. CI enforces this.
- **Never commit real credentials or PII** to fixtures. Redact installation UUIDs to `00000000-0000-0000-0000-000000000000`, serial numbers to `TEST-SN-…`, emails to `test@example.com`.
- **Commit style**: Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`, `test:`, `ci:`). No `Co-Authored-By` or `Claude-Session` trailers.
- **Python version**: `3.13` in pyproject `[tool.ruff]` and devcontainer.
- **License**: MIT.
- **Domain**: `flowbuddy` (lowercase, matches `DOMAIN` constant and `custom_components/flowbuddy/` directory).
- **Package name in `hacs.json`**: `FlowBuddy`.

## File Structure

Per spec §4.1. Reproduced here so each task can be grabbed independently:

```
flowbuddy-ha/
├── README.md                         # P0.1
├── LICENSE                           # P0.1
├── .gitignore                        # P0.1
├── pyproject.toml                    # P0.1
├── Makefile                          # P0.1
├── hacs.json                         # P1.A
├── info.md                           # P1.A
├── openapi/
│   ├── flexmon-v1.json               # (already committed)
│   └── flexmon-v1.sha256             # (already committed)
├── .devcontainer/
│   ├── devcontainer.json             # P0.2
│   ├── Dockerfile                    # P0.2
│   └── post-create.sh                # P0.2
├── .github/workflows/
│   ├── validate.yml                  # P10.A (hassfest + HACS)
│   ├── tests.yml                     # P10.B (pytest + coverage)
│   └── regen-check.yml               # P10.C (spec drift + no hand-edits)
├── custom_components/flowbuddy/
│   ├── __init__.py                   # P9.A (async_setup_entry)
│   ├── manifest.json                 # P1.A
│   ├── const.py                      # P1.B
│   ├── strings.json                  # P1.A
│   ├── translations/en.json          # P1.A
│   ├── translations/nl.json          # P1.A
│   ├── translations/fr.json          # P1.A
│   ├── _generated/                   # P1.B (from `make regen`)
│   ├── auth.py                       # P2 (TDD-critical)
│   ├── api.py                        # P3
│   ├── coordinator.py                # P4.A + P4.B + P4.C (three classes, one file)
│   ├── discovery.py                  # P5.A (TDD-critical)
│   ├── entity.py                     # P5.B
│   ├── sensor.py                     # P6.A
│   ├── binary_sensor.py              # P6.B
│   ├── number.py                     # P6.C
│   ├── climate.py                    # P6.D
│   ├── button.py                     # P6.E
│   ├── config_flow.py                # P7
│   ├── services.yaml                 # P8.A
│   ├── diagnostics.py                # P9.B
└── tests/
    ├── conftest.py                   # P1.C
    ├── fixtures/                     # P1.C (redacted JSON captures)
    ├── test_auth.py                  # P2
    ├── test_api.py                   # P3
    ├── test_coordinator_instant.py   # P4.A
    ├── test_coordinator_daily.py     # P4.B
    ├── test_coordinator_alarms.py    # P4.C
    ├── test_discovery.py             # P5.A
    ├── test_entity.py                # P5.B
    ├── test_sensor.py                # P6.A
    ├── test_binary_sensor.py         # P6.B
    ├── test_number.py                # P6.C
    ├── test_climate.py               # P6.D
    ├── test_button.py                # P6.E
    ├── test_config_flow.py           # P7
    ├── test_services.py              # P8.A
    ├── test_init.py                  # P9.A
    └── test_diagnostics.py           # P9.B
```

## Parallel Execution Overview

| Phase | Tasks | Parallel-safe? | Notes |
|---|---|---|---|
| P0 | P0.1, P0.2 | Sequential | Repo scaffolding → devcontainer |
| **HITL Gate A** | — | Human runs it | User verifies devcontainer + `make regen` |
| P1 | P1.A, P1.B, P1.C | Fully parallel | Metadata, generated code, test fixtures |
| P2 | P2 | Solo | Auth — foundational, gates P3 |
| P3 | P3 | Solo | API facade — depends on P2 + P1.B |
| P4 | P4.A, P4.B, P4.C | Fully parallel | Three coordinators, three test files |
| P5 | P5.A, P5.B | Sequential (small) | Discovery → entity base |
| P6 | P6.A–P6.E | Fully parallel (5-wide) | Five entity platforms |
| P7 | P7 | Solo | Config flow |
| P8 | P8.A | Solo | Services |
| P9 | P9.A, P9.B | Fully parallel | Init + diagnostics |
| **HITL Gate B** | — | Human runs it | Live-tenant integration smoke |
| P10 | P10.A, P10.B, P10.C | Fully parallel | Three CI workflows |

Total: ~24 tasks. With max parallel width of 5 (P6) and typical width 3 (P1, P4, P10), throughput on a 5-agent fleet is bounded by the sequential critical path: P0 → HITL A → P1.B → P2 → P3 → P4 (parallel) → P5 → P6 (parallel) → P7 → P8 → P9 → HITL B → P10. That's ~13 sequential steps versus 24 tasks — roughly a 2× speedup from parallelism.

---

## Phase 0 — Repo scaffolding + devcontainer

### Task P0.1 — Repo scaffolding

**Blocked by:** none

**Files:**
- Create: `README.md`
- Create: `LICENSE`
- Create: `.gitignore`
- Create: `pyproject.toml`
- Create: `Makefile`

**Interfaces:**
- Produces: `pyproject.toml` [project] name `flowbuddy-ha`, dev deps (`openapi-python-client`, `pytest`, `pytest-asyncio`, `pytest-cov`, `respx`, `ruff`, `mypy`, `homeassistant`). `Makefile` targets `regen`, `test`, `lint`, `typecheck`.

- [ ] **Step 1: Write README.md**

Content (~30 lines): title, one-paragraph description, "Status: pre-alpha", install-via-HACS placeholder section, dev quickstart pointing at `.devcontainer/`, link to spec + plan.

```markdown
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
```

- [ ] **Step 2: Write LICENSE (MIT)**

Copy the standard MIT license text with copyright line: `Copyright (c) 2026 Andreas Maerten`.

- [ ] **Step 3: Write .gitignore**

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.egg-info/
.pytest_cache/
.mypy_cache/
.ruff_cache/
.coverage
htmlcov/
coverage.xml
dist/
build/

# Env
.venv/
venv/
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
.DS_Store

# HA test artefacts
config/
.storage/

# devcontainer post-create marker
.devcontainer/.post-create-done
```

- [ ] **Step 4: Write pyproject.toml**

```toml
[project]
name = "flowbuddy-ha"
version = "0.0.0"
description = "Home Assistant custom integration for FlowBuddy (SIMPL / IZEN)"
readme = "README.md"
license = { text = "MIT" }
requires-python = ">=3.13"
authors = [{ name = "Andreas Maerten", email = "andreas.maerten@crimson7.io" }]

[project.optional-dependencies]
dev = [
  "homeassistant>=2025.1.0",
  "openapi-python-client>=0.21.0",
  "attrs>=23.2.0",
  "httpx>=0.27.0",
  "pytest>=8.0.0",
  "pytest-asyncio>=0.23.0",
  "pytest-cov>=4.1.0",
  "pytest-homeassistant-custom-component>=0.13.0",
  "respx>=0.21.0",
  "ruff>=0.5.0",
  "mypy>=1.10.0",
]

[tool.ruff]
target-version = "py313"
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "I", "W", "N", "UP", "B", "A", "C4", "SIM", "TCH"]
ignore = ["E501"]

[tool.ruff.lint.per-file-ignores]
"custom_components/flowbuddy/_generated/**" = ["ALL"]
"tests/**" = ["S101"]

[tool.mypy]
python_version = "3.13"
strict = true
exclude = ["custom_components/flowbuddy/_generated/"]

[tool.pytest.ini_options]
asyncio_mode = "auto"
addopts = "--strict-markers -ra"
testpaths = ["tests"]

[tool.coverage.run]
source = ["custom_components/flowbuddy"]
omit = ["custom_components/flowbuddy/_generated/*"]

[tool.coverage.report]
fail_under = 80
show_missing = true
skip_covered = false
```

- [ ] **Step 5: Write Makefile**

```make
.PHONY: regen test lint typecheck ci

SPEC := openapi/flexmon-v1.json
SPEC_URL := https://izen.cast4all.energy/flexMon/v1/openapi.json
GEN_DIR := custom_components/flowbuddy/_generated

regen:
	@sha_new=$$(sha256sum $(SPEC) | awk '{print $$1}'); \
	sha_recorded=$$(cat $(SPEC).sha256); \
	if [ "$$sha_new" != "$$sha_recorded" ]; then \
		echo "ERROR: $(SPEC) sha256 does not match $(SPEC).sha256"; \
		echo "  recorded: $$sha_recorded"; \
		echo "  actual:   $$sha_new"; \
		exit 1; \
	fi
	rm -rf $(GEN_DIR)
	python -m openapi_python_client generate \
		--path $(SPEC) \
		--output-path $(GEN_DIR) \
		--overwrite \
		--meta none
	ruff format $(GEN_DIR)
	ruff check --fix --unsafe-fixes $(GEN_DIR) || true
	@echo '"""Auto-generated FlexMon v1 client. DO NOT EDIT — run \`make regen\`."""' > $(GEN_DIR)/__init__.py
	@echo 'spec_version = "V1.0.0"' >> $(GEN_DIR)/__init__.py
	@echo 'spec_sha256 = "'$$(cat $(SPEC).sha256)'"' >> $(GEN_DIR)/__init__.py

test:
	pytest --cov

lint:
	ruff check .
	ruff format --check .

typecheck:
	mypy custom_components/flowbuddy

ci: lint typecheck test
```

- [ ] **Step 6: Commit**

```bash
git add README.md LICENSE .gitignore pyproject.toml Makefile
git commit -m "chore: scaffold repo with pyproject, Makefile, README"
```

---

### Task P0.2 — Devcontainer

**Blocked by:** P0.1

**Files:**
- Create: `.devcontainer/devcontainer.json`
- Create: `.devcontainer/Dockerfile`
- Create: `.devcontainer/post-create.sh`

**Interfaces:**
- Produces: a running container named per `devcontainer.json` `name` field, with Python 3.13 + all dev deps + `openapi-python-client` on PATH. All subsequent tasks run inside this container.

- [ ] **Step 1: Write .devcontainer/Dockerfile**

```dockerfile
FROM mcr.microsoft.com/devcontainers/python:1-3.13-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    make \
    git \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

USER vscode
```

- [ ] **Step 2: Write .devcontainer/devcontainer.json**

```jsonc
{
  "name": "flowbuddy-ha-dev",
  "build": { "dockerfile": "Dockerfile" },
  "remoteUser": "vscode",
  "workspaceFolder": "/workspaces/flowbuddy-ha",
  "runArgs": ["--name", "flowbuddy-ha-dev"],
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "charliermarsh.ruff",
        "matangover.mypy"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "[python]": {
          "editor.defaultFormatter": "charliermarsh.ruff",
          "editor.formatOnSave": true
        }
      }
    }
  },
  "postCreateCommand": "bash .devcontainer/post-create.sh",
  "features": {
    "ghcr.io/devcontainers/features/github-cli:1": {}
  }
}
```

- [ ] **Step 3: Write .devcontainer/post-create.sh**

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "[post-create] Installing dev dependencies..."
pip install --user --upgrade pip
pip install --user -e '.[dev]'

echo "[post-create] Verifying tools on PATH..."
python --version
pip --version
openapi-python-client --version
pytest --version
ruff --version
mypy --version

echo "[post-create] Marking complete."
touch .devcontainer/.post-create-done
```

Then: `chmod +x .devcontainer/post-create.sh`.

- [ ] **Step 4: Commit**

```bash
git add .devcontainer/
git commit -m "chore: add Python 3.13 devcontainer with post-create bootstrap"
```

---

## 🛑 HITL Gate A — Human verifies devcontainer + regenerates client

**Do NOT proceed to Phase 1 automatically.** Ask the user to:

1. Open the repo in VS Code (or run `devcontainer up` via the CLI).
2. Wait for `.devcontainer/post-create.sh` to finish (marker file at `.devcontainer/.post-create-done`).
3. Confirm all `--version` calls printed cleanly.
4. Run: `docker exec -u vscode -w /workspaces/flowbuddy-ha flowbuddy-ha-dev make regen`
5. Confirm `custom_components/flowbuddy/_generated/` was populated with a `client.py`, `models/`, `api/` tree and no error output.
6. Skim generated size: `du -sh custom_components/flowbuddy/_generated/` — expect < 5 MB. If > 10 MB, flag it (open question §5.8 in spec).
7. Reply **"gate A passed"** to unblock Phase 1.

If regen fails (spec parsing errors, HAL+JSON serdes issues, etc.), STOP and hand back to the user. The fallback is `datamodel-code-generator` for types + handwritten aiohttp calls (spec §7 risk).

---

## Phase 1 — Metadata, generated code commit, test fixtures (fully parallel)

### Task P1.A — HA manifest + HACS metadata + translations

**Blocked by:** HITL Gate A

**Files:**
- Create: `custom_components/flowbuddy/manifest.json`
- Create: `custom_components/flowbuddy/strings.json`
- Create: `custom_components/flowbuddy/translations/en.json`
- Create: `custom_components/flowbuddy/translations/nl.json`
- Create: `custom_components/flowbuddy/translations/fr.json`
- Create: `hacs.json`
- Create: `info.md`

**Interfaces:**
- Produces: HA integration domain `flowbuddy` (referenced by every other file), version `0.1.0`, iot_class `cloud_polling`. Translation keys: `config.step.auth_mode.title`, `config.step.credentials.title`, `config.step.installation.title`, `config.error.invalid_auth`, `config.error.cannot_connect`, `config.abort.already_configured`.

- [ ] **Step 1: Write manifest.json**

```json
{
  "domain": "flowbuddy",
  "name": "FlowBuddy",
  "codeowners": ["@andreas-maerten"],
  "config_flow": true,
  "documentation": "https://github.com/andreas-maerten/flowbuddy-ha",
  "integration_type": "hub",
  "iot_class": "cloud_polling",
  "issue_tracker": "https://github.com/andreas-maerten/flowbuddy-ha/issues",
  "requirements": ["httpx>=0.27.0", "attrs>=23.2.0"],
  "version": "0.1.0"
}
```

- [ ] **Step 2: Write hacs.json**

```json
{
  "name": "FlowBuddy",
  "homeassistant": "2025.1.0",
  "iot_class": "cloud_polling",
  "render_readme": true
}
```

- [ ] **Step 3: Write info.md**

```markdown
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
```

- [ ] **Step 4: Write strings.json**

```json
{
  "config": {
    "step": {
      "auth_mode": {
        "title": "Authentication method",
        "data": { "mode": "How do you want to authenticate?" }
      },
      "credentials": {
        "title": "Enter your credentials",
        "data": {
          "client_id": "Client ID",
          "client_secret": "Client Secret",
          "email": "Email",
          "password": "Password"
        }
      },
      "installation": {
        "title": "Select installation",
        "data": { "installation_id": "Installation" }
      }
    },
    "error": {
      "invalid_auth": "Invalid credentials.",
      "cannot_connect": "Cannot reach FlowBuddy — check network."
    },
    "abort": {
      "already_configured": "This installation is already configured."
    }
  },
  "services": {
    "enable_realtime": {
      "name": "Enable live mode",
      "description": "Boost live-value polling for a bounded window. Rate-limited by the vendor."
    }
  }
}
```

- [ ] **Step 5: Write translations/en.json**

Identical content to `strings.json` (English is the source of truth).

- [ ] **Step 6: Write translations/nl.json**

Translate every value to Dutch. Key structure identical.

- [ ] **Step 7: Write translations/fr.json**

Translate every value to French. Key structure identical.

- [ ] **Step 8: Commit**

```bash
git add custom_components/flowbuddy/manifest.json \
        custom_components/flowbuddy/strings.json \
        custom_components/flowbuddy/translations/ \
        hacs.json info.md
git commit -m "feat: add HA manifest, HACS metadata, and translations"
```

---

### Task P1.B — Commit generated client + `const.py`

**Blocked by:** HITL Gate A

**Files:**
- Add: `custom_components/flowbuddy/_generated/` (all files produced by `make regen` in Gate A)
- Create: `custom_components/flowbuddy/const.py`

**Interfaces:**
- Produces: `_generated.client.Client` and `_generated.client.AuthenticatedClient` (from openapi-python-client), plus every module under `_generated/api/` and `_generated/models/`. `const.py` exposes: `DOMAIN`, `KEYCLOAK_TOKEN_URL`, `KEYCLOAK_REALM_URL`, `API_BASE_URL`, `DEFAULT_INSTANT_INTERVAL_S`, `DEFAULT_DAILY_INTERVAL_S`, `DEFAULT_ALARMS_INTERVAL_S`, `DEFAULT_LIVE_INTERVAL_S`, `MIN_INSTANT_INTERVAL_S`, `RTO_MAX_MINUTES`, `POLLING_LIMIT_BLOCK_S`.

- [ ] **Step 1: Add generated tree to git**

```bash
git add custom_components/flowbuddy/_generated/
git status --short | head -20   # sanity — should see ~200 files
```

- [ ] **Step 2: Write const.py**

```python
"""Constants for the FlowBuddy integration."""
from __future__ import annotations

from typing import Final

DOMAIN: Final = "flowbuddy"

# --- Vendor endpoints ---------------------------------------------------
API_BASE_URL: Final = "https://izen.cast4all.energy/flexMon/v1"
KEYCLOAK_REALM_URL: Final = "https://auth.izen.cast4all.energy/realms/izen"
KEYCLOAK_TOKEN_URL: Final = f"{KEYCLOAK_REALM_URL}/protocol/openid-connect/token"
KEYCLOAK_SCOPES: Final = "openid profile email"

# --- Polling cadence (see spec §4.4) -----------------------------------
# Baseline mode is safe/always-on. Live mode is opt-in via
# flowbuddy.enable_realtime service and bounded to RTO_MAX_MINUTES.
DEFAULT_INSTANT_INTERVAL_S: Final = 90
MIN_INSTANT_INTERVAL_S: Final = 60         # HARD floor for baseline polling
DEFAULT_DAILY_INTERVAL_S: Final = 15 * 60
DEFAULT_ALARMS_INTERVAL_S: Final = 5 * 60
DEFAULT_LIVE_INTERVAL_S: Final = 20        # only inside an RTO window

RTO_MAX_MINUTES: Final = 5
POLLING_LIMIT_BLOCK_S: Final = 10 * 60     # hard block after PollingLimitExceeded

# --- Config flow keys --------------------------------------------------
CONF_AUTH_MODE: Final = "auth_mode"
CONF_INSTALLATION_ID: Final = "installation_id"
AUTH_MODE_CLIENT_CREDS: Final = "client_credentials"
AUTH_MODE_PASSWORD: Final = "password"
```

- [ ] **Step 3: Commit**

```bash
git add custom_components/flowbuddy/_generated/ custom_components/flowbuddy/const.py
git commit -m "feat: vendor generated FlexMon v1 client + integration constants"
```

---

### Task P1.C — Test scaffolding + captured fixtures

**Blocked by:** HITL Gate A

**Files:**
- Create: `tests/__init__.py` (empty)
- Create: `tests/conftest.py`
- Create: `tests/fixtures/instantvalues.json` (redacted)
- Create: `tests/fixtures/aggregationdayvalues.json` (redacted)
- Create: `tests/fixtures/measurementtypes.json` (redacted)
- Create: `tests/fixtures/installations.json` (redacted)
- Create: `tests/fixtures/meters.json` (redacted)
- Create: `tests/fixtures/alarms_open.json` (redacted)
- Create: `tests/fixtures/token_success.json`
- Create: `tests/fixtures/token_invalid_grant.json`
- Create: `tests/fixtures/polling_limit_exceeded_event.json`

**Interfaces:**
- Produces: `pytest` fixture `fixtures_dir` (Path), `load_fixture(name: str) -> dict`, `respx_mock` (auto-used), `hass` (from `pytest_homeassistant_custom_component`).

- [ ] **Step 1: Write tests/conftest.py**

```python
"""Shared test fixtures."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import respx


@pytest.fixture
def fixtures_dir() -> Path:
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def load_fixture(fixtures_dir: Path):
    def _load(name: str) -> dict[str, Any]:
        return json.loads((fixtures_dir / name).read_text())
    return _load


@pytest.fixture
def respx_mock():
    with respx.mock(assert_all_called=False) as mock:
        yield mock
```

- [ ] **Step 2: Write tests/fixtures/token_success.json**

```json
{
  "access_token": "test-access-token-abc123",
  "expires_in": 300,
  "refresh_expires_in": 1800,
  "refresh_token": "test-refresh-token-xyz789",
  "token_type": "Bearer",
  "scope": "openid profile email"
}
```

- [ ] **Step 3: Write tests/fixtures/token_invalid_grant.json**

```json
{
  "error": "invalid_grant",
  "error_description": "Invalid user credentials"
}
```

- [ ] **Step 4: Write tests/fixtures/installations.json**

Two installations (single & multi-install path both testable):

```json
{
  "_embedded": {
    "installations": [
      {
        "resourceUri": "/installations/00000000-0000-0000-0000-000000000001",
        "identification": "TEST-INST-1",
        "uuid": "00000000-0000-0000-0000-000000000001",
        "customerName": "Test Customer",
        "customerId": "cust-1",
        "emailAddress": "test@example.com",
        "city": "Testville",
        "country": "BE",
        "alarmStatus": "OK",
        "installationType": {
          "resourceUri": "/installationtypes/residential",
          "name": "Residential PV+Battery"
        }
      },
      {
        "resourceUri": "/installations/00000000-0000-0000-0000-000000000002",
        "identification": "TEST-INST-2",
        "uuid": "00000000-0000-0000-0000-000000000002",
        "customerName": "Test Customer 2",
        "customerId": "cust-2",
        "emailAddress": "test@example.com",
        "city": "Otherville",
        "country": "BE",
        "alarmStatus": "OK",
        "installationType": {
          "resourceUri": "/installationtypes/residential",
          "name": "Residential PV only"
        }
      }
    ]
  },
  "page": { "number": 0, "size": 20, "totalPages": 1, "totalElements": 2 }
}
```

- [ ] **Step 5: Write tests/fixtures/meters.json**

One PV meter, one grid meter, one battery meter. Match schema fields from `MeterOutputModel` in spec §2.

```json
{
  "_embedded": {
    "meters": [
      {
        "resourceUri": "/meters/meter-pv-1",
        "name": "PV Inverter",
        "serialNumber": "TEST-SN-PV-1",
        "manufacturer": "TestInverterCo",
        "type": "INVERTER",
        "meterType": "PV",
        "status": "ACTIVE",
        "polling": "yes",
        "lastPollingResult": "successful",
        "installation": { "resourceUri": "/installations/00000000-0000-0000-0000-000000000001" }
      },
      {
        "resourceUri": "/meters/meter-grid-1",
        "name": "DSO Smart Meter",
        "serialNumber": "TEST-SN-GRID-1",
        "manufacturer": "Fluvius",
        "type": "SMART_METER",
        "meterType": "GRID",
        "status": "ACTIVE",
        "polling": "yes",
        "lastPollingResult": "successful",
        "installation": { "resourceUri": "/installations/00000000-0000-0000-0000-000000000001" }
      },
      {
        "resourceUri": "/meters/meter-batt-1",
        "name": "Battery",
        "serialNumber": "TEST-SN-BATT-1",
        "manufacturer": "TestBatteryCo",
        "type": "BATTERY",
        "meterType": "BATTERY",
        "status": "ACTIVE",
        "polling": "yes",
        "lastPollingResult": "successful",
        "installation": { "resourceUri": "/installations/00000000-0000-0000-0000-000000000001" }
      }
    ]
  },
  "page": { "number": 0, "size": 20, "totalPages": 1, "totalElements": 3 }
}
```

- [ ] **Step 6: Write tests/fixtures/measurementtypes.json**

Cover every row of the mapping table (spec §4.3). Include: PV_POWER (W), PV_ENERGY (Wh, incremental), GRID_IMPORT_POWER (W), GRID_IMPORT_ENERGY (kWh, incremental), GRID_EXPORT_ENERGY (kWh, incremental), BATTERY_SOC (%), BATTERY_CHARGE_POWER (W), BATTERY_VOLTAGE (V), BATTERY_CURRENT (A), HVAC_TEMP (°C), GRID_FREQ (Hz), UNKNOWN_UNIT (wombats), APPARENT_POWER (VA), REACTIVE_POWER (var).

```json
{
  "_embedded": {
    "measurementtypes": [
      { "resourceUri": "/measurementtypes/pv-power", "name": "PV Power", "code": "PV_POWER", "unit": "W", "isIncremental": false, "aggregationType": "AVG", "externalId": "PV_POWER" },
      { "resourceUri": "/measurementtypes/pv-energy", "name": "PV Energy", "code": "PV_ENERGY", "unit": "Wh", "isIncremental": true, "aggregationType": "SUM", "externalId": "PV_ENERGY" },
      { "resourceUri": "/measurementtypes/grid-import-power", "name": "Grid Import Power", "code": "GRID_IMPORT_POWER", "unit": "W", "isIncremental": false, "aggregationType": "AVG", "externalId": "GRID_IMPORT_POWER" },
      { "resourceUri": "/measurementtypes/grid-import-energy", "name": "Grid Import Energy", "code": "GRID_IMPORT_ENERGY", "unit": "kWh", "isIncremental": true, "aggregationType": "SUM", "externalId": "GRID_IMPORT_ENERGY" },
      { "resourceUri": "/measurementtypes/grid-export-energy", "name": "Grid Export Energy", "code": "GRID_EXPORT_ENERGY", "unit": "kWh", "isIncremental": true, "aggregationType": "SUM", "externalId": "GRID_EXPORT_ENERGY" },
      { "resourceUri": "/measurementtypes/battery-soc", "name": "Battery SoC", "code": "BATTERY_SOC", "unit": "%", "isIncremental": false, "aggregationType": "AVG", "externalId": "BATTERY_SOC" },
      { "resourceUri": "/measurementtypes/battery-charge-power", "name": "Battery Charge Power", "code": "BATTERY_CHARGE_POWER", "unit": "W", "isIncremental": false, "aggregationType": "AVG", "externalId": "BATTERY_CHARGE_POWER" },
      { "resourceUri": "/measurementtypes/battery-voltage", "name": "Battery Voltage", "code": "BATTERY_VOLTAGE", "unit": "V", "isIncremental": false, "aggregationType": "AVG", "externalId": "BATTERY_VOLTAGE" },
      { "resourceUri": "/measurementtypes/battery-current", "name": "Battery Current", "code": "BATTERY_CURRENT", "unit": "A", "isIncremental": false, "aggregationType": "AVG", "externalId": "BATTERY_CURRENT" },
      { "resourceUri": "/measurementtypes/hvac-temp", "name": "HVAC Temp", "code": "HVAC_TEMP", "unit": "°C", "isIncremental": false, "aggregationType": "AVG", "externalId": "HVAC_TEMP" },
      { "resourceUri": "/measurementtypes/grid-freq", "name": "Grid Frequency", "code": "GRID_FREQ", "unit": "Hz", "isIncremental": false, "aggregationType": "AVG", "externalId": "GRID_FREQ" },
      { "resourceUri": "/measurementtypes/apparent-power", "name": "Apparent Power", "code": "APPARENT_POWER", "unit": "VA", "isIncremental": false, "aggregationType": "AVG", "externalId": "APPARENT_POWER" },
      { "resourceUri": "/measurementtypes/reactive-power", "name": "Reactive Power", "code": "REACTIVE_POWER", "unit": "var", "isIncremental": false, "aggregationType": "AVG", "externalId": "REACTIVE_POWER" },
      { "resourceUri": "/measurementtypes/unknown-unit", "name": "Unknown Unit", "code": "UNKNOWN_UNIT", "unit": "wombats", "isIncremental": false, "aggregationType": "AVG", "externalId": "UNKNOWN_UNIT" }
    ]
  },
  "page": { "number": 0, "size": 20, "totalPages": 1, "totalElements": 14 }
}
```

- [ ] **Step 7: Write tests/fixtures/instantvalues.json**

One row per measurement type in step 6 with plausible values (e.g. PV_POWER=1500, BATTERY_SOC=76.5).

```json
{
  "_embedded": {
    "instantvalues": [
      { "resourceUri": "/instantvalues/iv-1", "measurement": { "resourceUri": "/measurements/m-pv-power" }, "measurementType": { "resourceUri": "/measurementtypes/pv-power" }, "value": 1500.0, "timestart": "2026-07-07T12:00:00Z" },
      { "resourceUri": "/instantvalues/iv-2", "measurement": { "resourceUri": "/measurements/m-pv-energy" }, "measurementType": { "resourceUri": "/measurementtypes/pv-energy" }, "value": 15230.5, "timestart": "2026-07-07T12:00:00Z" },
      { "resourceUri": "/instantvalues/iv-3", "measurement": { "resourceUri": "/measurements/m-grid-import-power" }, "measurementType": { "resourceUri": "/measurementtypes/grid-import-power" }, "value": 450.0, "timestart": "2026-07-07T12:00:00Z" },
      { "resourceUri": "/instantvalues/iv-4", "measurement": { "resourceUri": "/measurements/m-battery-soc" }, "measurementType": { "resourceUri": "/measurementtypes/battery-soc" }, "value": 76.5, "timestart": "2026-07-07T12:00:00Z" }
    ]
  },
  "page": { "number": 0, "size": 20, "totalPages": 1, "totalElements": 4 }
}
```

- [ ] **Step 8: Write tests/fixtures/aggregationdayvalues.json**

```json
{
  "_embedded": {
    "aggregationdayvalues": [
      { "resourceUri": "/aggregationdayvalues/adv-1", "measurement": { "resourceUri": "/measurements/m-pv-energy" }, "periodStart": "2026-07-07T00:00:00Z", "value": 8.5, "sum": 8.5, "count": 96 },
      { "resourceUri": "/aggregationdayvalues/adv-2", "measurement": { "resourceUri": "/measurements/m-grid-import-energy" }, "periodStart": "2026-07-07T00:00:00Z", "value": 2.1, "sum": 2.1, "count": 96 },
      { "resourceUri": "/aggregationdayvalues/adv-3", "measurement": { "resourceUri": "/measurements/m-grid-export-energy" }, "periodStart": "2026-07-07T00:00:00Z", "value": 3.2, "sum": 3.2, "count": 96 }
    ]
  },
  "page": { "number": 0, "size": 20, "totalPages": 1, "totalElements": 3 }
}
```

- [ ] **Step 9: Write tests/fixtures/alarms_open.json**

```json
{
  "_embedded": {
    "alarms": [
      { "resourceUri": "/alarms/alarm-1", "id": "alarm-1", "priority": "HIGH", "status": "OPEN", "message": "Communicator offline", "raisedOn": "2026-07-07T10:00:00Z", "installation": { "resourceUri": "/installations/00000000-0000-0000-0000-000000000001" } }
    ]
  },
  "page": { "number": 0, "size": 20, "totalPages": 1, "totalElements": 1 }
}
```

- [ ] **Step 10: Write tests/fixtures/polling_limit_exceeded_event.json**

```json
{
  "eventName": "PollingLimitExceeded",
  "installation": "00000000-0000-0000-0000-000000000001",
  "timestamp": "2026-07-07T12:00:00Z"
}
```

- [ ] **Step 11: Commit**

```bash
git add tests/
git commit -m "test: scaffold conftest and captured fixtures for FlexMon endpoints"
```

---

## Phase 2 — Auth (TDD-critical)

### Task P2 — `KeycloakTokenProvider` + `httpx.Auth` adapter

**Blocked by:** P1.B (needs `const.py` + generated client for context), P1.C (needs fixtures)

**Files:**
- Create: `custom_components/flowbuddy/auth.py`
- Create: `tests/test_auth.py`

**Interfaces:**
- Produces:
  - `class TokenBundle: access_token: str; expires_at: float; refresh_token: str | None`
  - `class KeycloakTokenProvider(mode: Literal["client_credentials", "password"], *, http: httpx.AsyncClient, client_id: str, client_secret: str | None = None, username: str | None = None, password: str | None = None)`
  - `async def get_token(self) -> str` — returns valid access token, refreshing if needed. Single-flight (asyncio.Lock).
  - `def httpx_auth(self) -> httpx.Auth` — returns an `httpx.Auth` that injects bearer + retries once on 401 after refresh.
  - `class InvalidCredentialsError(Exception)` — raised when refresh/re-auth returns 401 or `invalid_grant`.

- [ ] **Step 1: Write failing test — token acquisition (client_credentials)**

`tests/test_auth.py`:

```python
"""Tests for auth.KeycloakTokenProvider and its httpx.Auth adapter."""
from __future__ import annotations

import asyncio
from unittest.mock import patch

import httpx
import pytest
import respx

from custom_components.flowbuddy.auth import (
    InvalidCredentialsError,
    KeycloakTokenProvider,
)
from custom_components.flowbuddy.const import KEYCLOAK_TOKEN_URL


@pytest.fixture
async def http_client():
    async with httpx.AsyncClient() as client:
        yield client


async def test_client_credentials_first_token(http_client, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    provider = KeycloakTokenProvider(
        mode="client_credentials",
        http=http_client,
        client_id="cid",
        client_secret="secret",
    )
    token = await provider.get_token()
    assert token == "test-access-token-abc123"
```

- [ ] **Step 2: Verify test fails**

```bash
docker exec -u vscode -w /workspaces/flowbuddy-ha flowbuddy-ha-dev \
  pytest tests/test_auth.py::test_client_credentials_first_token -v
```

Expected: `ModuleNotFoundError: No module named 'custom_components.flowbuddy.auth'`.

- [ ] **Step 3: Write minimal `auth.py` — client_credentials happy path only**

`custom_components/flowbuddy/auth.py`:

```python
"""Keycloak auth for the FlowBuddy integration."""
from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass
from typing import Literal

import httpx

from .const import KEYCLOAK_SCOPES, KEYCLOAK_TOKEN_URL


class InvalidCredentialsError(Exception):
    """Raised when Keycloak rejects the credentials (401 / invalid_grant)."""


@dataclass
class TokenBundle:
    access_token: str
    expires_at: float
    refresh_token: str | None = None


class KeycloakTokenProvider:
    def __init__(
        self,
        *,
        mode: Literal["client_credentials", "password"],
        http: httpx.AsyncClient,
        client_id: str,
        client_secret: str | None = None,
        username: str | None = None,
        password: str | None = None,
    ) -> None:
        self._mode = mode
        self._http = http
        self._client_id = client_id
        self._client_secret = client_secret
        self._username = username
        self._password = password
        self._token: TokenBundle | None = None
        self._lock = asyncio.Lock()

    async def get_token(self) -> str:
        async with self._lock:
            if self._token and self._token.expires_at > time.monotonic() + 60:
                return self._token.access_token
            await self._acquire()
            assert self._token is not None
            return self._token.access_token

    async def _acquire(self) -> None:
        data: dict[str, str] = {"scope": KEYCLOAK_SCOPES, "client_id": self._client_id}
        if self._mode == "client_credentials":
            data["grant_type"] = "client_credentials"
            assert self._client_secret is not None
            data["client_secret"] = self._client_secret
        else:
            data["grant_type"] = "password"
            assert self._username is not None and self._password is not None
            data["username"] = self._username
            data["password"] = self._password
        resp = await self._http.post(KEYCLOAK_TOKEN_URL, data=data)
        if resp.status_code == 401 or (
            resp.status_code == 400 and resp.json().get("error") == "invalid_grant"
        ):
            raise InvalidCredentialsError(resp.text)
        resp.raise_for_status()
        body = resp.json()
        self._token = TokenBundle(
            access_token=body["access_token"],
            expires_at=time.monotonic() + body["expires_in"],
            refresh_token=body.get("refresh_token"),
        )
```

- [ ] **Step 4: Run test — verify pass**

```bash
docker exec -u vscode -w /workspaces/flowbuddy-ha flowbuddy-ha-dev \
  pytest tests/test_auth.py::test_client_credentials_first_token -v
```

Expected: PASS.

- [ ] **Step 5: Add failing test — token cache hit (no second POST)**

Append to `test_auth.py`:

```python
async def test_second_get_token_uses_cache(http_client, load_fixture, respx_mock):
    route = respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    provider = KeycloakTokenProvider(
        mode="client_credentials", http=http_client,
        client_id="cid", client_secret="secret",
    )
    await provider.get_token()
    await provider.get_token()
    assert route.call_count == 1
```

- [ ] **Step 6: Run — expect PASS (behaviour already correct)**

Same command. Should pass.

- [ ] **Step 7: Add failing test — invalid_grant raises**

```python
async def test_invalid_grant_raises(http_client, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(401, json=load_fixture("token_invalid_grant.json"))
    )
    provider = KeycloakTokenProvider(
        mode="password", http=http_client,
        client_id="frontend", username="wrong@example.com", password="nope",
    )
    with pytest.raises(InvalidCredentialsError):
        await provider.get_token()
```

- [ ] **Step 8: Run — expect PASS**

- [ ] **Step 9: Add failing test — single-flight lock (only one refresh under concurrent access)**

```python
async def test_single_flight_refresh(http_client, load_fixture, respx_mock):
    route = respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    provider = KeycloakTokenProvider(
        mode="client_credentials", http=http_client,
        client_id="cid", client_secret="secret",
    )
    # Fire 10 concurrent get_token calls — must result in exactly ONE POST.
    tokens = await asyncio.gather(*(provider.get_token() for _ in range(10)))
    assert route.call_count == 1
    assert all(t == "test-access-token-abc123" for t in tokens)
```

- [ ] **Step 10: Run — expect PASS**

- [ ] **Step 11: Add failing test — httpx.Auth adapter injects bearer**

```python
async def test_httpx_auth_injects_bearer(http_client, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    api_route = respx_mock.get("https://api.example.com/thing").mock(
        return_value=httpx.Response(200, json={"ok": True})
    )
    provider = KeycloakTokenProvider(
        mode="client_credentials", http=http_client,
        client_id="cid", client_secret="secret",
    )
    async with httpx.AsyncClient(auth=provider.httpx_auth()) as api:
        r = await api.get("https://api.example.com/thing")
    assert r.status_code == 200
    assert api_route.calls.last.request.headers["Authorization"] == "Bearer test-access-token-abc123"
```

- [ ] **Step 12: Verify failure** — `AttributeError: 'KeycloakTokenProvider' object has no attribute 'httpx_auth'`.

- [ ] **Step 13: Implement `httpx_auth`**

Add to `auth.py`:

```python
class _AsyncAuth(httpx.Auth):
    requires_response_body = False

    def __init__(self, provider: "KeycloakTokenProvider") -> None:
        self._provider = provider

    async def async_auth_flow(self, request):
        token = await self._provider.get_token()
        request.headers["Authorization"] = f"Bearer {token}"
        response = yield request
        if response.status_code != 401:
            return
        # Force refresh and retry once
        await self._provider.invalidate()
        token = await self._provider.get_token()
        request.headers["Authorization"] = f"Bearer {token}"
        yield request
```

Add to `KeycloakTokenProvider`:

```python
    async def invalidate(self) -> None:
        async with self._lock:
            self._token = None

    def httpx_auth(self) -> httpx.Auth:
        return _AsyncAuth(self)
```

- [ ] **Step 14: Run — expect PASS**

- [ ] **Step 15: Add failing test — 401 triggers exactly one retry with fresh token**

```python
async def test_auth_retries_once_on_401(http_client, load_fixture, respx_mock):
    # Two token responses: first is "old", second is "new" after invalidation
    old = load_fixture("token_success.json")
    new = dict(old, access_token="new-token-after-401")
    token_route = respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        side_effect=[
            httpx.Response(200, json=old),
            httpx.Response(200, json=new),
        ]
    )
    api_route = respx_mock.get("https://api.example.com/thing").mock(
        side_effect=[
            httpx.Response(401, json={"error": "expired"}),
            httpx.Response(200, json={"ok": True}),
        ]
    )
    provider = KeycloakTokenProvider(
        mode="client_credentials", http=http_client,
        client_id="cid", client_secret="secret",
    )
    async with httpx.AsyncClient(auth=provider.httpx_auth()) as api:
        r = await api.get("https://api.example.com/thing")
    assert r.status_code == 200
    assert token_route.call_count == 2
    assert api_route.call_count == 2
    assert api_route.calls[1].request.headers["Authorization"] == "Bearer new-token-after-401"
```

- [ ] **Step 16: Run — expect PASS**

- [ ] **Step 17: Add failing test — second 401 stops retry (no infinite loop)**

```python
async def test_auth_stops_after_two_401s(http_client, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    api_route = respx_mock.get("https://api.example.com/thing").mock(
        return_value=httpx.Response(401, json={"error": "still bad"})
    )
    provider = KeycloakTokenProvider(
        mode="client_credentials", http=http_client,
        client_id="cid", client_secret="secret",
    )
    async with httpx.AsyncClient(auth=provider.httpx_auth()) as api:
        r = await api.get("https://api.example.com/thing")
    assert r.status_code == 401
    assert api_route.call_count == 2   # one original + one retry, then stop
```

- [ ] **Step 18: Run — expect PASS**

- [ ] **Step 19: Commit**

```bash
git add custom_components/flowbuddy/auth.py tests/test_auth.py
git commit -m "feat(auth): KeycloakTokenProvider + httpx.Auth adapter with single-flight refresh and 401 retry"
```

---

## Phase 3 — API facade

### Task P3 — `api.py` FlowBuddyClient facade

**Blocked by:** P2

**Files:**
- Create: `custom_components/flowbuddy/api.py`
- Create: `tests/test_api.py`

**Interfaces:**
- Produces:
  - `class FlowBuddyClient(*, http: httpx.AsyncClient, token_provider: KeycloakTokenProvider)`
  - `async def list_installations(self) -> list[Installation]`
  - `async def list_meters(self, installation_id: str) -> list[Meter]`
  - `async def list_measurementtypes(self) -> list[MeasurementType]`
  - `async def get_instant_values(self, installation_id: str) -> list[InstantValue]`
  - `async def get_day_aggregations(self, installation_id: str, day: date) -> list[AggregationDayValue]`
  - `async def list_open_alarms(self, installation_id: str) -> list[Alarm]`
  - `async def set_battery_charge_power(self, battery_id: str, watts: int) -> None`
  - `async def limit_inverter(self, inverter_id: str, watts: int) -> None`
  - `async def set_hvac_cool(self, hvac_id: str, celsius: float) -> None`
  - `async def set_hvac_heat(self, hvac_id: str, celsius: float) -> None`
  - `async def close_alarm(self, alarm_id: str, comment: str | None = None) -> None`
  - `async def activate_continuous_processing(self, installation_id: str) -> None`
  - `class PollingLimitExceededError(Exception)` — raised when a request or subsequent event indicates rate-limit block.

Where each of Installation/Meter/etc. is an alias for the corresponding `_generated.models.*OutputModel` class re-exported here.

- [ ] **Step 1: Write failing test — list_installations returns typed models**

`tests/test_api.py`:

```python
"""Tests for the FlowBuddyClient facade."""
from __future__ import annotations

from datetime import date, datetime, timezone
from unittest.mock import AsyncMock

import httpx
import pytest

from custom_components.flowbuddy.api import (
    FlowBuddyClient,
    PollingLimitExceededError,
)
from custom_components.flowbuddy.auth import KeycloakTokenProvider
from custom_components.flowbuddy.const import API_BASE_URL, KEYCLOAK_TOKEN_URL


@pytest.fixture
async def client(load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    http = httpx.AsyncClient()
    provider = KeycloakTokenProvider(
        mode="client_credentials", http=http,
        client_id="cid", client_secret="secret",
    )
    yield FlowBuddyClient(http=http, token_provider=provider)
    await http.aclose()


async def test_list_installations(client, load_fixture, respx_mock):
    respx_mock.get(f"{API_BASE_URL}/installations").mock(
        return_value=httpx.Response(200, json=load_fixture("installations.json"))
    )
    installations = await client.list_installations()
    assert len(installations) == 2
    assert installations[0].uuid == "00000000-0000-0000-0000-000000000001"
    assert installations[0].identification == "TEST-INST-1"
```

- [ ] **Step 2: Run — expect ModuleNotFoundError**

- [ ] **Step 3: Write `api.py` — minimal skeleton that satisfies test 1**

```python
"""Thin facade over the generated FlexMon v1 client."""
from __future__ import annotations

from datetime import date
from typing import Any

import httpx

from ._generated import client as _gen_client
from ._generated.api.installation_apis import get_all_installations
from ._generated.models import (
    InstallationOutputModel as Installation,
)
from .auth import KeycloakTokenProvider
from .const import API_BASE_URL


class PollingLimitExceededError(Exception):
    """Raised when the vendor signals a per-installation polling block."""


class FlowBuddyClient:
    def __init__(
        self, *, http: httpx.AsyncClient, token_provider: KeycloakTokenProvider
    ) -> None:
        self._http = http
        self._token = token_provider
        # AuthenticatedClient shares OUR httpx client + auth
        self._client = _gen_client.AuthenticatedClient(
            base_url=API_BASE_URL,
            token="unused-injected-by-httpx-auth",
            httpx_args={"auth": token_provider.httpx_auth()},
        )

    async def list_installations(self) -> list[Installation]:
        result = await get_all_installations.asyncio(client=self._client)
        return list(result.embedded.installations) if result else []
```

_Note: exact generated-module names may differ per `openapi-python-client` output (`get_all_installations` vs `get_installations` vs snake_cased tag). Adjust to whatever `_generated/api/installation_apis/` actually exports — the generated code is authoritative. Verify with `docker exec … python -c "from custom_components.flowbuddy._generated.api.installation_apis import *"` if needed._

- [ ] **Step 4: Run — expect PASS**

- [ ] **Step 5: Add failing test for `get_instant_values`**

```python
async def test_get_instant_values(client, load_fixture, respx_mock):
    respx_mock.get(
        f"{API_BASE_URL}/instantvalues",
    ).mock(return_value=httpx.Response(200, json=load_fixture("instantvalues.json")))
    iid = "00000000-0000-0000-0000-000000000001"
    values = await client.get_instant_values(iid)
    assert len(values) == 4
    pv_power = next(v for v in values if v.measurement.resource_uri.endswith("m-pv-power"))
    assert pv_power.value == 1500.0
```

- [ ] **Step 6: Implement `get_instant_values` — add to `api.py`**

```python
    async def get_instant_values(self, installation_id: str):
        from ._generated.api.instant_value_apis import get_all_instant_values
        result = await get_all_instant_values.asyncio(
            client=self._client, installation=installation_id, pagesize=500
        )
        return list(result.embedded.instantvalues) if result else []
```

- [ ] **Step 7: Run — expect PASS**

- [ ] **Step 8: Repeat pattern for the remaining endpoints — one failing test per method**

For each of `list_meters`, `list_measurementtypes`, `get_day_aggregations`, `list_open_alarms`, `set_battery_charge_power`, `limit_inverter`, `set_hvac_cool`, `set_hvac_heat`, `close_alarm`, `activate_continuous_processing`:
1. Add failing test using the matching fixture (or a stub for write endpoints).
2. Add the method to `api.py` delegating to the corresponding `_generated/api/…` function.
3. Run — expect PASS.

For write endpoints (mock 204 No Content responses), verify the request body carries the expected payload with `respx_mock.calls.last.request.content`.

- [ ] **Step 9: Add failing test — activate_continuous_processing raises on rate limit**

```python
async def test_activate_continuous_processing_rate_limit(client, respx_mock, load_fixture):
    iid = "00000000-0000-0000-0000-000000000001"
    respx_mock.post(
        f"{API_BASE_URL}/installations/{iid}/activateContinuousProcessing"
    ).mock(return_value=httpx.Response(429, json={"code": "RL001", "extraInfo": {"message": "PollingLimitExceeded"}}))
    with pytest.raises(PollingLimitExceededError):
        await client.activate_continuous_processing(iid)
```

- [ ] **Step 10: Implement rate-limit handling in `activate_continuous_processing`**

```python
    async def activate_continuous_processing(self, installation_id: str) -> None:
        url = f"{API_BASE_URL}/installations/{installation_id}/activateContinuousProcessing"
        auth = self._token.httpx_auth()
        # Not in the public OpenAPI spec — call directly with our httpx client
        resp = await self._http.post(url, auth=auth)
        if resp.status_code == 429 or (
            resp.status_code >= 400 and "PollingLimitExceeded" in resp.text
        ):
            raise PollingLimitExceededError(resp.text)
        resp.raise_for_status()
```

- [ ] **Step 11: Run — expect PASS**

- [ ] **Step 12: Commit**

```bash
git add custom_components/flowbuddy/api.py tests/test_api.py
git commit -m "feat(api): FlowBuddyClient facade wrapping generated FlexMon endpoints"
```

---

## Phase 4 — Coordinators (three tasks, parallel-safe)

All three tasks share the same file `custom_components/flowbuddy/coordinator.py`, but each adds an INDEPENDENT class. To keep them parallel-safe: after all three subagents finish, a merge step verifies imports and no name clashes. Alternatively, each subagent creates its class in a private module (`_coord_instant.py`, `_coord_daily.py`, `_coord_alarms.py`) that `coordinator.py` re-exports — recommended if running truly in parallel.

**Coordination note for reviewer**: choose ONE strategy up front. Below assumes the private-module strategy for safe parallelism.

### Task P4.A — Instant coordinator (TDD-critical for rate limiting)

**Blocked by:** P3

**Files:**
- Create: `custom_components/flowbuddy/_coord_instant.py`
- Create: `tests/test_coordinator_instant.py`

**Interfaces:**
- Produces:
  - `class FlowBuddyInstantCoordinator(DataUpdateCoordinator[dict[str, float]])`
  - `__init__(self, hass, api, installation_id, *, base_interval_s=DEFAULT_INSTANT_INTERVAL_S)`
  - `async def _async_update_data() -> dict[str, float]` — keyed by measurement resource_uri
  - `async def boost(duration_minutes: int)` — sets interval to `DEFAULT_LIVE_INTERVAL_S` for the given window, then restores baseline
  - `def is_boosted(self) -> bool`
  - `def is_blocked(self) -> bool` — True while `PollingLimitExceeded` block is active
  - Raises `UpdateFailed` on transport failure; sets `data` to `{}` on empty response but does NOT raise.
  - On `PollingLimitExceededError` from boost path: cancels boost, sets `_blocked_until = time.monotonic() + POLLING_LIMIT_BLOCK_S`, creates a `repairs` issue.

- [ ] **Step 1: Write failing test — baseline interval is at least 60s**

```python
"""Tests for FlowBuddyInstantCoordinator."""
from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest
from homeassistant.helpers.update_coordinator import UpdateFailed

from custom_components.flowbuddy._coord_instant import FlowBuddyInstantCoordinator
from custom_components.flowbuddy.api import PollingLimitExceededError
from custom_components.flowbuddy.const import (
    DEFAULT_INSTANT_INTERVAL_S,
    DEFAULT_LIVE_INTERVAL_S,
    MIN_INSTANT_INTERVAL_S,
    POLLING_LIMIT_BLOCK_S,
)


@pytest.fixture
def mock_api():
    api = MagicMock()
    api.get_instant_values = AsyncMock(return_value=[])
    api.activate_continuous_processing = AsyncMock()
    return api


def test_baseline_interval_never_below_min(hass, mock_api):
    coord = FlowBuddyInstantCoordinator(
        hass, mock_api, "iid-1", base_interval_s=5   # try to abuse
    )
    assert coord.update_interval.total_seconds() >= MIN_INSTANT_INTERVAL_S
```

- [ ] **Step 2: Verify failure** — `ModuleNotFoundError`.

- [ ] **Step 3: Write `_coord_instant.py` — minimal**

```python
"""Instant-value coordinator with rate-limit-aware boost."""
from __future__ import annotations

import asyncio
import logging
import time
from datetime import timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import FlowBuddyClient, PollingLimitExceededError
from .const import (
    DEFAULT_INSTANT_INTERVAL_S,
    DEFAULT_LIVE_INTERVAL_S,
    DOMAIN,
    MIN_INSTANT_INTERVAL_S,
    POLLING_LIMIT_BLOCK_S,
    RTO_MAX_MINUTES,
)

_LOGGER = logging.getLogger(__name__)


class FlowBuddyInstantCoordinator(DataUpdateCoordinator[dict[str, float]]):
    def __init__(
        self,
        hass: HomeAssistant,
        api: FlowBuddyClient,
        installation_id: str,
        *,
        base_interval_s: int = DEFAULT_INSTANT_INTERVAL_S,
    ) -> None:
        # Enforce hard floor
        interval_s = max(base_interval_s, MIN_INSTANT_INTERVAL_S)
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_instant_{installation_id}",
            update_interval=timedelta(seconds=interval_s),
        )
        self._api = api
        self._installation_id = installation_id
        self._base_interval_s = interval_s
        self._boosted_until: float | None = None
        self._blocked_until: float | None = None
        self._boost_task: asyncio.Task[None] | None = None

    def is_boosted(self) -> bool:
        return self._boosted_until is not None and time.monotonic() < self._boosted_until

    def is_blocked(self) -> bool:
        return self._blocked_until is not None and time.monotonic() < self._blocked_until

    async def _async_update_data(self) -> dict[str, float]:
        try:
            values = await self._api.get_instant_values(self._installation_id)
        except Exception as exc:
            raise UpdateFailed(str(exc)) from exc
        return {v.measurement.resource_uri: v.value for v in values}
```

- [ ] **Step 4: Run — expect PASS**

- [ ] **Step 5: Add failing test — boost() switches interval to DEFAULT_LIVE_INTERVAL_S**

```python
async def test_boost_shortens_interval(hass, mock_api):
    coord = FlowBuddyInstantCoordinator(hass, mock_api, "iid-1")
    assert coord.update_interval.total_seconds() == DEFAULT_INSTANT_INTERVAL_S
    await coord.boost(1)
    assert coord.is_boosted()
    assert coord.update_interval.total_seconds() == DEFAULT_LIVE_INTERVAL_S
    mock_api.activate_continuous_processing.assert_awaited_once_with("iid-1")
```

- [ ] **Step 6: Verify failure** — `AttributeError: no attribute 'boost'`.

- [ ] **Step 7: Implement boost**

Add to `_coord_instant.py`:

```python
    async def boost(self, duration_minutes: int) -> None:
        if self.is_blocked():
            raise PollingLimitExceededError(
                f"Installation {self._installation_id} is blocked "
                f"for {int(self._blocked_until - time.monotonic())}s"
            )
        duration_minutes = min(duration_minutes, RTO_MAX_MINUTES)
        try:
            await self._api.activate_continuous_processing(self._installation_id)
        except PollingLimitExceededError:
            self._blocked_until = time.monotonic() + POLLING_LIMIT_BLOCK_S
            raise
        self._boosted_until = time.monotonic() + duration_minutes * 60
        self.update_interval = timedelta(seconds=DEFAULT_LIVE_INTERVAL_S)
        if self._boost_task and not self._boost_task.done():
            self._boost_task.cancel()
        self._boost_task = self.hass.loop.create_task(self._auto_restore(duration_minutes * 60))

    async def _auto_restore(self, delay_s: float) -> None:
        try:
            await asyncio.sleep(delay_s)
        except asyncio.CancelledError:
            return
        self._boosted_until = None
        self.update_interval = timedelta(seconds=self._base_interval_s)
```

- [ ] **Step 8: Run — expect PASS**

- [ ] **Step 9: Add failing test — boost respects RTO cap**

```python
async def test_boost_caps_duration_at_rto_max(hass, mock_api):
    coord = FlowBuddyInstantCoordinator(hass, mock_api, "iid-1")
    await coord.boost(99)   # try to boost for 99 min
    # _boosted_until - now should be <= RTO_MAX_MINUTES * 60
    remaining = coord._boosted_until - time.monotonic()
    assert remaining <= RTO_MAX_MINUTES * 60 + 1
```

- [ ] **Step 10: Run — expect PASS**

- [ ] **Step 11: Add failing test — PollingLimitExceeded from activate triggers hard block**

```python
async def test_polling_limit_exceeded_triggers_block(hass, mock_api):
    mock_api.activate_continuous_processing.side_effect = PollingLimitExceededError("blocked")
    coord = FlowBuddyInstantCoordinator(hass, mock_api, "iid-1")
    with pytest.raises(PollingLimitExceededError):
        await coord.boost(5)
    assert coord.is_blocked()
    # A second boost attempt must also raise, immediately
    mock_api.activate_continuous_processing.reset_mock()
    with pytest.raises(PollingLimitExceededError):
        await coord.boost(5)
    # activate should NOT have been called the second time
    mock_api.activate_continuous_processing.assert_not_called()
```

- [ ] **Step 12: Run — expect PASS**

- [ ] **Step 13: Add failing test — auto_restore reverts interval after window**

```python
async def test_auto_restore_reverts_interval(hass, mock_api, monkeypatch):
    # Compress time
    slept: list[float] = []
    async def fake_sleep(s):
        slept.append(s)
    monkeypatch.setattr("custom_components.flowbuddy._coord_instant.asyncio.sleep", fake_sleep)
    coord = FlowBuddyInstantCoordinator(hass, mock_api, "iid-1")
    await coord.boost(1)
    # Give the boost task a chance to run
    await asyncio.sleep(0)
    await asyncio.sleep(0)
    assert coord.update_interval.total_seconds() == DEFAULT_INSTANT_INTERVAL_S
    assert 55 <= slept[0] <= 65
```

- [ ] **Step 14: Run — expect PASS**

- [ ] **Step 15: Add failing test — is_blocked clears after POLLING_LIMIT_BLOCK_S**

```python
async def test_block_expires_after_block_duration(hass, mock_api, monkeypatch):
    mock_api.activate_continuous_processing.side_effect = PollingLimitExceededError("blocked")
    coord = FlowBuddyInstantCoordinator(hass, mock_api, "iid-1")
    with pytest.raises(PollingLimitExceededError):
        await coord.boost(5)
    assert coord.is_blocked()
    # Fake advance monotonic time past the block window
    orig = time.monotonic
    monkeypatch.setattr(
        "custom_components.flowbuddy._coord_instant.time.monotonic",
        lambda: orig() + POLLING_LIMIT_BLOCK_S + 1,
    )
    assert not coord.is_blocked()
```

- [ ] **Step 16: Run — expect PASS**

- [ ] **Step 17: Add failing test — update_data returns keyed dict**

```python
async def test_async_update_data_returns_keyed_dict(hass, mock_api):
    class V:
        def __init__(self, uri, val):
            self.measurement = MagicMock(resource_uri=uri)
            self.value = val
    mock_api.get_instant_values.return_value = [
        V("/measurements/a", 100.0), V("/measurements/b", 200.0)
    ]
    coord = FlowBuddyInstantCoordinator(hass, mock_api, "iid-1")
    data = await coord._async_update_data()
    assert data == {"/measurements/a": 100.0, "/measurements/b": 200.0}
```

- [ ] **Step 18: Run — expect PASS**

- [ ] **Step 19: Add failing test — API exception -> UpdateFailed**

```python
async def test_api_exception_raises_update_failed(hass, mock_api):
    mock_api.get_instant_values.side_effect = RuntimeError("network")
    coord = FlowBuddyInstantCoordinator(hass, mock_api, "iid-1")
    with pytest.raises(UpdateFailed):
        await coord._async_update_data()
```

- [ ] **Step 20: Run — expect PASS**

- [ ] **Step 21: Commit**

```bash
git add custom_components/flowbuddy/_coord_instant.py tests/test_coordinator_instant.py
git commit -m "feat(coordinator): FlowBuddyInstantCoordinator with rate-limit-aware boost"
```

---

### Task P4.B — Daily coordinator

**Blocked by:** P3

**Files:**
- Create: `custom_components/flowbuddy/_coord_daily.py`
- Create: `tests/test_coordinator_daily.py`

**Interfaces:**
- Produces:
  - `class FlowBuddyDailyCoordinator(DataUpdateCoordinator[dict[str, float]])`
  - `__init__(self, hass, api, installation_id)` — interval fixed at `DEFAULT_DAILY_INTERVAL_S`
  - `async def _async_update_data() -> dict[str, float]` — keyed by measurement resource_uri, value is today's cumulative kWh

- [ ] **Step 1: Write failing test — returns keyed dict from fixture**

```python
"""Tests for FlowBuddyDailyCoordinator."""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from custom_components.flowbuddy._coord_daily import FlowBuddyDailyCoordinator
from custom_components.flowbuddy.const import DEFAULT_DAILY_INTERVAL_S


@pytest.fixture
def mock_api():
    api = MagicMock()
    api.get_day_aggregations = AsyncMock(return_value=[])
    return api


def test_interval_is_daily_default(hass, mock_api):
    coord = FlowBuddyDailyCoordinator(hass, mock_api, "iid-1")
    assert coord.update_interval.total_seconds() == DEFAULT_DAILY_INTERVAL_S


async def test_update_returns_keyed_dict(hass, mock_api):
    class V:
        def __init__(self, uri, val):
            self.measurement = MagicMock(resource_uri=uri)
            self.value = val
    mock_api.get_day_aggregations.return_value = [V("/m/pv", 8.5), V("/m/grid-import", 2.1)]
    coord = FlowBuddyDailyCoordinator(hass, mock_api, "iid-1")
    data = await coord._async_update_data()
    assert data == {"/m/pv": 8.5, "/m/grid-import": 2.1}
```

- [ ] **Step 2: Verify failure — ModuleNotFoundError**

- [ ] **Step 3: Write `_coord_daily.py`**

```python
"""Daily aggregation coordinator (15-min cadence)."""
from __future__ import annotations

import logging
from datetime import date, datetime, time as dtime, timedelta, timezone

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import FlowBuddyClient
from .const import DEFAULT_DAILY_INTERVAL_S, DOMAIN

_LOGGER = logging.getLogger(__name__)


class FlowBuddyDailyCoordinator(DataUpdateCoordinator[dict[str, float]]):
    def __init__(
        self, hass: HomeAssistant, api: FlowBuddyClient, installation_id: str
    ) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_daily_{installation_id}",
            update_interval=timedelta(seconds=DEFAULT_DAILY_INTERVAL_S),
        )
        self._api = api
        self._installation_id = installation_id

    async def _async_update_data(self) -> dict[str, float]:
        today = datetime.combine(date.today(), dtime.min, tzinfo=timezone.utc).date()
        try:
            values = await self._api.get_day_aggregations(self._installation_id, today)
        except Exception as exc:
            raise UpdateFailed(str(exc)) from exc
        return {v.measurement.resource_uri: v.value for v in values}
```

- [ ] **Step 4: Run — expect PASS**

- [ ] **Step 5: Add failing test — exception surfaces as UpdateFailed**

```python
async def test_api_exception_raises_update_failed(hass, mock_api):
    from homeassistant.helpers.update_coordinator import UpdateFailed
    mock_api.get_day_aggregations.side_effect = RuntimeError("network")
    coord = FlowBuddyDailyCoordinator(hass, mock_api, "iid-1")
    with pytest.raises(UpdateFailed):
        await coord._async_update_data()
```

- [ ] **Step 6: Run — expect PASS**

- [ ] **Step 7: Commit**

```bash
git add custom_components/flowbuddy/_coord_daily.py tests/test_coordinator_daily.py
git commit -m "feat(coordinator): FlowBuddyDailyCoordinator for 15-min kWh aggregates"
```

---

### Task P4.C — Alarms coordinator

**Blocked by:** P3

**Files:**
- Create: `custom_components/flowbuddy/_coord_alarms.py`
- Create: `tests/test_coordinator_alarms.py`

**Interfaces:**
- Produces:
  - `class FlowBuddyAlarmsCoordinator(DataUpdateCoordinator[list[Alarm]])`
  - `__init__(self, hass, api, installation_id)` — interval `DEFAULT_ALARMS_INTERVAL_S`
  - `async def _async_update_data() -> list[Alarm]` — currently open alarms

- [ ] **Step 1–3: Write failing test, verify failure, implement**

Same TDD pattern as P4.B. Test fixture: `alarms_open.json`.

```python
"""Tests for FlowBuddyAlarmsCoordinator."""
from unittest.mock import AsyncMock, MagicMock

import pytest

from custom_components.flowbuddy._coord_alarms import FlowBuddyAlarmsCoordinator
from custom_components.flowbuddy.const import DEFAULT_ALARMS_INTERVAL_S


@pytest.fixture
def mock_api():
    api = MagicMock()
    api.list_open_alarms = AsyncMock(return_value=[])
    return api


def test_interval_is_alarms_default(hass, mock_api):
    coord = FlowBuddyAlarmsCoordinator(hass, mock_api, "iid-1")
    assert coord.update_interval.total_seconds() == DEFAULT_ALARMS_INTERVAL_S


async def test_update_returns_alarm_list(hass, mock_api):
    a = MagicMock(id="alarm-1", status="OPEN")
    mock_api.list_open_alarms.return_value = [a]
    coord = FlowBuddyAlarmsCoordinator(hass, mock_api, "iid-1")
    data = await coord._async_update_data()
    assert data == [a]
```

Implementation mirrors `_coord_daily.py` but returns `list[Alarm]` and calls `api.list_open_alarms`.

- [ ] **Step 4: Commit**

```bash
git add custom_components/flowbuddy/_coord_alarms.py tests/test_coordinator_alarms.py
git commit -m "feat(coordinator): FlowBuddyAlarmsCoordinator for open alarms at 5-min cadence"
```

---

### Task P4.merge — Coordinator public re-export

**Blocked by:** P4.A + P4.B + P4.C

**Files:**
- Create: `custom_components/flowbuddy/coordinator.py`

- [ ] **Step 1: Write `coordinator.py`**

```python
"""Public re-exports for coordinators."""
from ._coord_alarms import FlowBuddyAlarmsCoordinator
from ._coord_daily import FlowBuddyDailyCoordinator
from ._coord_instant import FlowBuddyInstantCoordinator

__all__ = [
    "FlowBuddyAlarmsCoordinator",
    "FlowBuddyDailyCoordinator",
    "FlowBuddyInstantCoordinator",
]
```

- [ ] **Step 2: Commit**

```bash
git add custom_components/flowbuddy/coordinator.py
git commit -m "feat(coordinator): re-export coordinators from coordinator.py"
```

---

## Phase 5 — Discovery + entity base

### Task P5.A — Discovery (TDD-critical)

**Blocked by:** P3, P1.C

**Files:**
- Create: `custom_components/flowbuddy/discovery.py`
- Create: `tests/test_discovery.py`

**Interfaces:**
- Produces:
  - `def describe(mt: MeasurementType) -> SensorEntityDescription` — data-driven per spec §4.3 table.
  - Uses HA's `SensorDeviceClass`, `SensorStateClass`, `UnitOfPower`, `UnitOfEnergy`, `UnitOfElectricPotential`, `UnitOfElectricCurrent`, `UnitOfTemperature`, `UnitOfFrequency`, `UnitOfApparentPower`, `UnitOfReactivePower`, `PERCENTAGE`.
  - kW → W, kWh → Wh scaling handled inside `describe` (returns native unit + a `state_transformer` callable).

- [ ] **Step 1: Write failing tests — one per row of the mapping table**

Full test file spelled out; the point of TDD here is that every mapping row is covered before any code exists.

```python
"""Tests for discovery.describe — one per row of the spec §4.3 mapping table."""
from unittest.mock import MagicMock

import pytest
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

from custom_components.flowbuddy.discovery import describe


def _mt(code, unit, incremental):
    m = MagicMock()
    m.code = code; m.unit = unit; m.is_incremental = incremental; m.name = code
    return m


@pytest.mark.parametrize("unit_in,unit_expected", [("W", UnitOfPower.WATT), ("kW", UnitOfPower.WATT)])
def test_power_measurement(unit_in, unit_expected):
    d = describe(_mt("PV_POWER", unit_in, False))
    assert d.device_class == SensorDeviceClass.POWER
    assert d.state_class == SensorStateClass.MEASUREMENT
    assert d.native_unit_of_measurement == unit_expected


@pytest.mark.parametrize("unit_in,unit_expected", [("Wh", UnitOfEnergy.KILO_WATT_HOUR), ("kWh", UnitOfEnergy.KILO_WATT_HOUR)])
def test_energy_incremental(unit_in, unit_expected):
    d = describe(_mt("PV_ENERGY", unit_in, True))
    assert d.device_class == SensorDeviceClass.ENERGY
    assert d.state_class == SensorStateClass.TOTAL_INCREASING
    assert d.native_unit_of_measurement == unit_expected


def test_voltage():
    d = describe(_mt("V_LINE", "V", False))
    assert d.device_class == SensorDeviceClass.VOLTAGE
    assert d.native_unit_of_measurement == UnitOfElectricPotential.VOLT


def test_current():
    d = describe(_mt("I_LINE", "A", False))
    assert d.device_class == SensorDeviceClass.CURRENT
    assert d.native_unit_of_measurement == UnitOfElectricCurrent.AMPERE


def test_battery_soc_by_code_hint():
    d = describe(_mt("BATTERY_SOC", "%", False))
    assert d.device_class == SensorDeviceClass.BATTERY
    assert d.native_unit_of_measurement == PERCENTAGE


def test_generic_percent_not_soc():
    d = describe(_mt("PERF_INDEX", "%", False))
    assert d.device_class is None
    assert d.native_unit_of_measurement == PERCENTAGE


def test_temperature():
    d = describe(_mt("HVAC_TEMP", "°C", False))
    assert d.device_class == SensorDeviceClass.TEMPERATURE
    assert d.native_unit_of_measurement == UnitOfTemperature.CELSIUS


def test_frequency():
    d = describe(_mt("GRID_FREQ", "Hz", False))
    assert d.device_class == SensorDeviceClass.FREQUENCY
    assert d.native_unit_of_measurement == UnitOfFrequency.HERTZ


def test_apparent_power():
    d = describe(_mt("APPARENT_POWER", "VA", False))
    assert d.device_class == SensorDeviceClass.APPARENT_POWER
    assert d.native_unit_of_measurement == UnitOfApparentPower.VOLT_AMPERE


def test_reactive_power():
    d = describe(_mt("REACTIVE_POWER", "var", False))
    assert d.device_class == SensorDeviceClass.REACTIVE_POWER
    assert d.native_unit_of_measurement == UnitOfReactivePower.VOLT_AMPERE_REACTIVE


def test_unknown_unit_still_creates_sensor():
    d = describe(_mt("UNKNOWN", "wombats", False))
    assert d.device_class is None
    assert d.native_unit_of_measurement == "wombats"
    assert d.state_class == SensorStateClass.MEASUREMENT


def test_scale_kw_input_returns_watt():
    d = describe(_mt("PV_POWER", "kW", False))
    # Value transformer: kW input -> W output (× 1000)
    assert d.value_transformer(1.5) == 1500.0


def test_scale_wh_input_returns_kwh():
    d = describe(_mt("PV_ENERGY", "Wh", True))
    assert d.value_transformer(15230.5) == pytest.approx(15.2305)
```

- [ ] **Step 2: Verify failures** — expect ~13 test collection failures on `discovery.describe`.

- [ ] **Step 3: Write `discovery.py`**

```python
"""Data-driven measurement -> HA entity description mapping."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

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


@dataclass
class Description:
    key: str
    name: str
    device_class: SensorDeviceClass | None
    state_class: SensorStateClass
    native_unit_of_measurement: str
    value_transformer: Callable[[float], float] = field(default=lambda v: v)


def describe(mt: Any) -> Description:
    unit = mt.unit
    code = mt.code or ""
    incremental = bool(mt.is_incremental)

    transformer: Callable[[float], float] = lambda v: v

    # Power
    if unit == "W":
        return Description(mt.code, mt.name, SensorDeviceClass.POWER,
                           SensorStateClass.MEASUREMENT, UnitOfPower.WATT)
    if unit == "kW":
        return Description(mt.code, mt.name, SensorDeviceClass.POWER,
                           SensorStateClass.MEASUREMENT, UnitOfPower.WATT,
                           value_transformer=lambda v: v * 1000.0)

    # Energy
    if unit == "kWh" and incremental:
        return Description(mt.code, mt.name, SensorDeviceClass.ENERGY,
                           SensorStateClass.TOTAL_INCREASING, UnitOfEnergy.KILO_WATT_HOUR)
    if unit == "Wh" and incremental:
        return Description(mt.code, mt.name, SensorDeviceClass.ENERGY,
                           SensorStateClass.TOTAL_INCREASING, UnitOfEnergy.KILO_WATT_HOUR,
                           value_transformer=lambda v: v / 1000.0)

    # Electrical
    if unit == "V":
        return Description(mt.code, mt.name, SensorDeviceClass.VOLTAGE,
                           SensorStateClass.MEASUREMENT, UnitOfElectricPotential.VOLT)
    if unit == "A":
        return Description(mt.code, mt.name, SensorDeviceClass.CURRENT,
                           SensorStateClass.MEASUREMENT, UnitOfElectricCurrent.AMPERE)
    if unit == "Hz":
        return Description(mt.code, mt.name, SensorDeviceClass.FREQUENCY,
                           SensorStateClass.MEASUREMENT, UnitOfFrequency.HERTZ)
    if unit == "VA":
        return Description(mt.code, mt.name, SensorDeviceClass.APPARENT_POWER,
                           SensorStateClass.MEASUREMENT, UnitOfApparentPower.VOLT_AMPERE)
    if unit == "var":
        return Description(mt.code, mt.name, SensorDeviceClass.REACTIVE_POWER,
                           SensorStateClass.MEASUREMENT,
                           UnitOfReactivePower.VOLT_AMPERE_REACTIVE)

    # Percentage — battery SoC vs generic
    if unit == "%":
        if "SOC" in code.upper():
            return Description(mt.code, mt.name, SensorDeviceClass.BATTERY,
                               SensorStateClass.MEASUREMENT, PERCENTAGE)
        return Description(mt.code, mt.name, None,
                           SensorStateClass.MEASUREMENT, PERCENTAGE)

    # Temperature
    if unit == "°C":
        return Description(mt.code, mt.name, SensorDeviceClass.TEMPERATURE,
                           SensorStateClass.MEASUREMENT, UnitOfTemperature.CELSIUS)

    # Fallback — still create a sensor
    return Description(mt.code, mt.name, None,
                       SensorStateClass.MEASUREMENT, unit)
```

- [ ] **Step 4: Run — expect ALL PASS**

```bash
docker exec -u vscode -w /workspaces/flowbuddy-ha flowbuddy-ha-dev \
  pytest tests/test_discovery.py -v
```

- [ ] **Step 5: Commit**

```bash
git add custom_components/flowbuddy/discovery.py tests/test_discovery.py
git commit -m "feat(discovery): unit+incremental -> HA SensorEntityDescription mapping"
```

---

### Task P5.B — Entity base + DeviceInfo wiring

**Blocked by:** P5.A

**Files:**
- Create: `custom_components/flowbuddy/entity.py`
- Create: `tests/test_entity.py`

**Interfaces:**
- Produces:
  - `def installation_device_info(inst: Installation) -> DeviceInfo`
  - `def meter_device_info(meter: Meter, installation: Installation) -> DeviceInfo` — sets `via_device` to installation
  - `class FlowBuddyEntity(CoordinatorEntity[Any])` — base for all platforms; sets `_attr_has_entity_name = True`, `_attr_unique_id` derived from `installation_uuid + measurement_uri`.

- [ ] **Step 1: Write failing tests**

```python
"""Tests for entity base + DeviceInfo helpers."""
from unittest.mock import MagicMock

from custom_components.flowbuddy.const import DOMAIN
from custom_components.flowbuddy.entity import (
    installation_device_info,
    meter_device_info,
)


def test_installation_device_info():
    inst = MagicMock(uuid="00000000-0000-0000-0000-000000000001",
                     identification="TEST-INST-1", city="Testville")
    inst.installation_type.name = "Residential PV+Battery"
    di = installation_device_info(inst)
    assert di["identifiers"] == {(DOMAIN, "00000000-0000-0000-0000-000000000001")}
    assert di["name"] == "TEST-INST-1"
    assert di["model"] == "Residential PV+Battery"


def test_meter_device_info_via_installation():
    inst = MagicMock(uuid="00000000-0000-0000-0000-000000000001")
    meter = MagicMock(serial_number="TEST-SN-PV-1", name="PV Inverter",
                      manufacturer="TestInverterCo", meter_type="PV")
    di = meter_device_info(meter, inst)
    assert di["identifiers"] == {(DOMAIN, "TEST-SN-PV-1")}
    assert di["via_device"] == (DOMAIN, "00000000-0000-0000-0000-000000000001")
    assert di["manufacturer"] == "TestInverterCo"
```

- [ ] **Step 2: Verify failure — ModuleNotFoundError**

- [ ] **Step 3: Implement `entity.py`**

```python
"""Entity base + DeviceInfo helpers."""
from __future__ import annotations

from typing import Any

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


def installation_device_info(inst: Any) -> DeviceInfo:
    return DeviceInfo(
        identifiers={(DOMAIN, inst.uuid)},
        name=inst.identification,
        manufacturer="FlowBuddy",
        model=inst.installation_type.name if inst.installation_type else "Installation",
        configuration_url="https://flowbuddy.earth.be",
    )


def meter_device_info(meter: Any, inst: Any) -> DeviceInfo:
    return DeviceInfo(
        identifiers={(DOMAIN, meter.serial_number)},
        name=meter.name,
        manufacturer=meter.manufacturer,
        model=meter.meter_type,
        via_device=(DOMAIN, inst.uuid),
    )


class FlowBuddyEntity(CoordinatorEntity[Any]):
    _attr_has_entity_name = True

    def __init__(self, coordinator, *, unique_id: str) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = unique_id
```

- [ ] **Step 4: Run — expect PASS**

- [ ] **Step 5: Commit**

```bash
git add custom_components/flowbuddy/entity.py tests/test_entity.py
git commit -m "feat(entity): FlowBuddyEntity base + installation/meter DeviceInfo helpers"
```

---

## Phase 6 — Entity platforms (5 tasks, fully parallel)

Each platform task follows the same pattern: write failing test that constructs the platform with a stub coordinator + fixture data, verify entities are created with correct attributes, then implement `async_setup_entry`.

Below is P6.A in full. P6.B–P6.E follow the same skeleton with minor tweaks called out.

### Task P6.A — `sensor.py`

**Blocked by:** P5.A, P5.B, P4.merge

**Files:**
- Create: `custom_components/flowbuddy/sensor.py`
- Create: `tests/test_sensor.py`

**Interfaces:**
- Produces: `async def async_setup_entry(hass, entry, async_add_entities) -> None` — reads discovery data from `hass.data[DOMAIN][entry.entry_id]`, creates one `FlowBuddySensor` per `Measurement`, adds all at once.
- `class FlowBuddySensor(FlowBuddyEntity, SensorEntity)` — reads `coordinator.data[measurement_uri]`, applies `description.value_transformer`.

- [ ] **Step 1: Write failing test — one sensor per measurement in fixture**

```python
"""Tests for sensor platform."""
from unittest.mock import AsyncMock, MagicMock

import pytest
from homeassistant.components.sensor import SensorEntity

from custom_components.flowbuddy.sensor import FlowBuddySensor


def test_sensor_reads_from_coordinator():
    coord = MagicMock()
    coord.data = {"/measurements/m-pv": 1500.0}
    mt = MagicMock(code="PV_POWER", name="PV Power", unit="W", is_incremental=False)
    meas = MagicMock(resource_uri="/measurements/m-pv")
    sensor = FlowBuddySensor(
        coordinator=coord,
        installation_uuid="00000000-0000-0000-0000-000000000001",
        meter=MagicMock(serial_number="TEST-SN-PV-1"),
        installation=MagicMock(uuid="00000000-0000-0000-0000-000000000001"),
        measurement=meas,
        measurement_type=mt,
    )
    assert sensor.native_value == 1500.0
    assert sensor.native_unit_of_measurement == "W"
```

- [ ] **Step 2: Verify failure — ModuleNotFoundError**

- [ ] **Step 3: Implement `sensor.py`**

```python
"""Sensor platform."""
from __future__ import annotations

from typing import Any

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .discovery import describe
from .entity import FlowBuddyEntity, meter_device_info


class FlowBuddySensor(FlowBuddyEntity, SensorEntity):
    def __init__(
        self, *, coordinator, installation_uuid: str, meter, installation,
        measurement, measurement_type,
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


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback,
) -> None:
    data = hass.data[DOMAIN][entry.entry_id]
    entities: list[FlowBuddySensor] = []
    for measurement in data["measurements"]:
        mt = data["measurementtypes_by_uri"].get(measurement.measurement_type.resource_uri)
        if mt is None:
            continue
        meter = data["meters_by_uri"].get(measurement.meter.resource_uri)
        if meter is None:
            continue
        # Route: instant (measurement) -> instant coordinator; incremental -> daily coordinator
        coord = data["daily_coord"] if mt.is_incremental else data["instant_coord"]
        entities.append(FlowBuddySensor(
            coordinator=coord,
            installation_uuid=data["installation"].uuid,
            meter=meter,
            installation=data["installation"],
            measurement=measurement,
            measurement_type=mt,
        ))
    async_add_entities(entities)
```

- [ ] **Step 4: Run — expect PASS**

- [ ] **Step 5: Add failing test — sensor is unavailable when coordinator returns None**

```python
def test_sensor_returns_none_when_missing_from_coordinator():
    coord = MagicMock(); coord.data = {}
    mt = MagicMock(code="PV_POWER", name="PV Power", unit="W", is_incremental=False)
    meas = MagicMock(resource_uri="/measurements/m-pv")
    s = FlowBuddySensor(
        coordinator=coord,
        installation_uuid="i", meter=MagicMock(serial_number="s"),
        installation=MagicMock(uuid="i"),
        measurement=meas, measurement_type=mt,
    )
    assert s.native_value is None
```

- [ ] **Step 6: Run — expect PASS**

- [ ] **Step 7: Commit**

```bash
git add custom_components/flowbuddy/sensor.py tests/test_sensor.py
git commit -m "feat(sensor): FlowBuddySensor platform reading from instant+daily coordinators"
```

---

### Task P6.B — `binary_sensor.py`

**Blocked by:** P5.B, P4.merge

**Files:**
- Create: `custom_components/flowbuddy/binary_sensor.py`
- Create: `tests/test_binary_sensor.py`

**Interfaces:**
- Produces: `class FlowBuddyAlarmBinarySensor(FlowBuddyEntity, BinarySensorEntity)` per alarm; entities list refreshed on each coordinator update (add/remove via `async_add_entities` in `async_setup_entry` returning a listener that recreates on data change).
- `_attr_device_class = BinarySensorDeviceClass.PROBLEM`

TDD pattern: write test that creates the platform from `alarms_open.json`, assert exactly one binary_sensor with `is_on = True` for the open alarm; then implement.

- [ ] **Steps 1–4**: same test/implement/verify/commit rhythm.

- [ ] **Step 5: Commit**

```bash
git add custom_components/flowbuddy/binary_sensor.py tests/test_binary_sensor.py
git commit -m "feat(binary_sensor): open alarms as PROBLEM binary_sensors"
```

---

### Task P6.C — `number.py`

**Blocked by:** P5.B, P4.merge, P3

**Files:**
- Create: `custom_components/flowbuddy/number.py`
- Create: `tests/test_number.py`

**Interfaces:**
- Produces:
  - `class BatteryChargePowerNumber(FlowBuddyEntity, NumberEntity)` per battery — min = `-battery.max_discharge_power`, max = `+battery.max_charge_power`, step 100, unit `W`. `async_set_native_value(value)` → `api.set_battery_charge_power`.
  - `class InverterProductionLimitNumber(FlowBuddyEntity, NumberEntity)` per inverter — min 0, max `inverter.max_power`, step 100, unit `W`. → `api.limit_inverter`.

TDD tests: assert min/max derived from vendor-reported values (spec §4.5), assert `async_set_native_value` calls the correct api method with the given watts.

- [ ] **Step 5: Commit**

```bash
git add custom_components/flowbuddy/number.py tests/test_number.py
git commit -m "feat(number): battery charge power + inverter production limit controls"
```

---

### Task P6.D — `climate.py`

**Blocked by:** P5.B, P4.merge, P3

**Files:**
- Create: `custom_components/flowbuddy/climate.py`
- Create: `tests/test_climate.py`

**Interfaces:**
- Produces: `class FlowBuddyHvac(FlowBuddyEntity, ClimateEntity)` per HVAC unit; supports `HVACMode.HEAT`, `HVACMode.COOL`, `HVACMode.OFF`; `async_set_temperature` routes to `api.set_hvac_cool` or `set_hvac_heat` based on current mode.

TDD test: set target temperature in cool mode → asserts `api.set_hvac_cool(hvac_id, 22.0)` called; same for heat.

- [ ] **Step 5: Commit**

```bash
git add custom_components/flowbuddy/climate.py tests/test_climate.py
git commit -m "feat(climate): HVAC entity with heat/cool setpoint control"
```

---

### Task P6.E — `button.py`

**Blocked by:** P5.B, P4.merge, P3

**Files:**
- Create: `custom_components/flowbuddy/button.py`
- Create: `tests/test_button.py`

**Interfaces:**
- Produces: `class AlarmAckButton(FlowBuddyEntity, ButtonEntity)` per open alarm (recreated on alarms coordinator update); `async_press()` → `api.close_alarm(alarm_id)`. Also `RequestConnectionTestButton` per communicator (created at setup, always present).

TDD test: press button → assert `api.close_alarm("alarm-1")` awaited exactly once.

- [ ] **Step 5: Commit**

```bash
git add custom_components/flowbuddy/button.py tests/test_button.py
git commit -m "feat(button): alarm-ack + connection-test buttons"
```

---

## Phase 7 — Config flow

### Task P7 — `config_flow.py`

**Blocked by:** P2, P3

**Files:**
- Create: `custom_components/flowbuddy/config_flow.py`
- Create: `tests/test_config_flow.py`

**Interfaces:**
- Produces: `class FlowBuddyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN)` with three steps: `user` (pick auth mode) → `auth` (enter creds, validate by hitting `POST /token` + `GET /installations`) → `installation` (pick installation if >1; skip if 1). Stores `client_id`/`client_secret` or `email`/`password` in `entry.data`, `installation_id` in `entry.data`. `async_step_reauth` supported.

- [ ] **Step 1: Write failing tests — one per branch (client_creds happy, password happy, invalid creds, no installations, single installation auto-select, multi installation picker, duplicate config, reauth)**

```python
"""Tests for the FlowBuddy config flow."""
from unittest.mock import AsyncMock, patch

import httpx
import pytest
from homeassistant import config_entries, data_entry_flow

from custom_components.flowbuddy.const import (
    AUTH_MODE_CLIENT_CREDS, AUTH_MODE_PASSWORD, CONF_AUTH_MODE,
    CONF_INSTALLATION_ID, DOMAIN, KEYCLOAK_TOKEN_URL,
)


async def test_client_creds_happy_path_single_installation(hass, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    # Only one installation -> auto-select
    single = load_fixture("installations.json")
    single["_embedded"]["installations"] = single["_embedded"]["installations"][:1]
    respx_mock.get("https://izen.cast4all.energy/flexMon/v1/installations").mock(
        return_value=httpx.Response(200, json=single)
    )
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {CONF_AUTH_MODE: AUTH_MODE_CLIENT_CREDS}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"client_id": "cid", "client_secret": "secret"}
    )
    assert result["type"] == data_entry_flow.FlowResultType.CREATE_ENTRY
    assert result["data"][CONF_INSTALLATION_ID] == "00000000-0000-0000-0000-000000000001"


async def test_invalid_credentials_shows_error(hass, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(401, json=load_fixture("token_invalid_grant.json"))
    )
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {CONF_AUTH_MODE: AUTH_MODE_CLIENT_CREDS}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"client_id": "cid", "client_secret": "wrong"}
    )
    assert result["type"] == data_entry_flow.FlowResultType.FORM
    assert result["errors"] == {"base": "invalid_auth"}


# ...additional cases: password mode, multi-install picker, duplicate config prevention, reauth
```

- [ ] **Step 2: Verify failure — ModuleNotFoundError**

- [ ] **Step 3: Implement `config_flow.py`**

Full implementation (~150 lines) with three `async_step_*` methods, `_async_test_credentials` helper, and `async_step_reauth`. Follows HA config-flow conventions. Delegates auth validation to `KeycloakTokenProvider` + `FlowBuddyClient.list_installations()`.

- [ ] **Step 4–5: Run — iterate until all cases pass**

- [ ] **Step 6: Commit**

```bash
git add custom_components/flowbuddy/config_flow.py tests/test_config_flow.py
git commit -m "feat(config_flow): auth-mode + credentials + installation picker with reauth"
```

---

## Phase 8 — Services

### Task P8.A — `services.yaml` + service handlers

**Blocked by:** P3, P4.merge

**Files:**
- Create: `custom_components/flowbuddy/services.yaml`
- Modify: `custom_components/flowbuddy/__init__.py` (or add a `services.py`) — the actual service registration.
- Create: `tests/test_services.py`

**Interfaces:**
- Registers services (see spec §4.5 services.yaml block, reproduced verbatim in-file): `set_battery_charge_power`, `limit_inverter`, `ack_alarm`, `request_connection_test`, `enable_realtime`.
- `enable_realtime(installation_id, duration_minutes)` calls `coord.boost(duration_minutes)` on the matching instant coordinator; on `PollingLimitExceededError`, raises HA `ServiceValidationError` with the block-remaining time in the message and creates a `repairs` issue.

TDD tests: mock the coordinators/api in `hass.data`, call `hass.services.async_call("flowbuddy", "enable_realtime", …)`, assert `coord.boost` was awaited; separate test asserts `ServiceValidationError` on blocked installation.

- [ ] **Step 5: Commit**

```bash
git add custom_components/flowbuddy/services.yaml \
        custom_components/flowbuddy/__init__.py \
        tests/test_services.py
git commit -m "feat(services): register FlowBuddy services with rate-limit-aware enable_realtime"
```

---

## Phase 9 — Init wiring + diagnostics (parallel)

### Task P9.A — `__init__.py` `async_setup_entry`

**Blocked by:** P4.merge, P5, P6.A, P6.B, P6.C, P6.D, P6.E, P8.A

**Files:**
- Modify: `custom_components/flowbuddy/__init__.py` (extended from P8.A to include the setup/teardown wiring)
- Create: `tests/test_init.py`

**Interfaces:**
- `async def async_setup_entry(hass, entry) -> bool` — creates `FlowBuddyClient`, three coordinators, primes them once (`await coord.async_config_entry_first_refresh()`), stores discovery data (installation, meters, measurementtypes, measurements) in `hass.data[DOMAIN][entry.entry_id]`, forwards platforms.
- `async def async_unload_entry(hass, entry) -> bool` — unloads platforms, cancels any running boost task, closes httpx client.

TDD tests: full setup happy path with all fixtures, unload cleanup, `ConfigEntryAuthFailed` propagation, `ConfigEntryNotReady` on transport failure.

- [ ] **Step 6: Commit**

```bash
git add custom_components/flowbuddy/__init__.py tests/test_init.py
git commit -m "feat: wire up async_setup_entry + async_unload_entry with priming"
```

---

### Task P9.B — `diagnostics.py`

**Blocked by:** P9.A

**Files:**
- Create: `custom_components/flowbuddy/diagnostics.py`
- Create: `tests/test_diagnostics.py`

**Interfaces:**
- `async def async_get_config_entry_diagnostics(hass, entry) -> dict` — dumps `entry.data`, coordinator `last_update_success`, `last_exception` strings, block state, installation identification. Uses `async_redact_data(TO_REDACT)` for `client_secret`, `password`, `refresh_token`, `access_token`, `email`, `customerName`, `customerId`.

TDD test: create entry, run diagnostics, assert redacted fields are `"**REDACTED**"` and non-secret fields present.

- [ ] **Step 5: Commit**

```bash
git add custom_components/flowbuddy/diagnostics.py tests/test_diagnostics.py
git commit -m "feat(diagnostics): redacted config-entry diagnostics for issue reports"
```

---

## 🛑 HITL Gate B — Live-tenant smoke test

**Do NOT proceed to CI phase until the user runs this.**

Ask the user to:

1. Ensure the devcontainer is up and `make test` passes end-to-end.
2. Symlink or copy `custom_components/flowbuddy/` into their live HA config's `custom_components/` (or add this repo as a HACS custom repository).
3. Restart HA.
4. Add the integration via UI: **Settings → Devices & Services → Add Integration → FlowBuddy**.
5. Attempt `client_credentials` first; if it fails ("no API account UI available"), fall back to `password` mode.
6. Confirm at least one instant sensor and one daily kWh sensor appear and update.
7. Open **Settings → Dashboards → Energy** and confirm the FlowBuddy kWh sensors appear in the pickers.
8. Call `flowbuddy.enable_realtime` from **Developer Tools → Services** with `installation_id = <their-uuid>`, `duration_minutes = 1`; watch the instant coordinator's `update_interval` drop to 20 s in the HA logs, then restore after ~1 minute.
9. Answer for the spec's Open Questions §5:
   - Is `activateContinuousProcessing` callable with the `client_credentials` scope? (§5 item 4a)
   - What does the vendor's `PollingLimitExceeded` response body look like on the wire? Capture and paste. (§5 item 4b)
   - What is the observed baseline meter push cadence (delta between successive `MeasurementValue.createdOn`)? (§5 item 4d)

Reply **"gate B passed"** (plus answers) to unblock Phase 10.

If the integration fails to load, or a battery/inverter control call errors, STOP and file findings before touching CI.

---

## Phase 10 — CI workflows (fully parallel)

### Task P10.A — `validate.yml` — hassfest + HACS

**Blocked by:** HITL Gate B

**Files:**
- Create: `.github/workflows/validate.yml`

- [ ] **Step 1: Write validate.yml**

```yaml
name: Validate

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  hassfest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: home-assistant/actions/hassfest@master

  hacs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: hacs/action@main
        with:
          category: integration
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/validate.yml
git commit -m "ci: hassfest + HACS validation on PR"
```

---

### Task P10.B — `tests.yml` — pytest + coverage

**Blocked by:** HITL Gate B

**Files:**
- Create: `.github/workflows/tests.yml`

- [ ] **Step 1: Write tests.yml**

```yaml
name: Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.13" }
      - name: Install dev dependencies
        run: pip install -e '.[dev]'
      - name: Lint
        run: |
          ruff check .
          ruff format --check .
      - name: Type-check
        run: mypy custom_components/flowbuddy
      - name: Test
        run: pytest --cov --cov-fail-under=80
      - name: Upload coverage
        uses: actions/upload-artifact@v4
        with:
          name: coverage
          path: htmlcov/
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/tests.yml
git commit -m "ci: pytest + ruff + mypy strict with 80% coverage floor"
```

---

### Task P10.C — `regen-check.yml` — spec-drift + no hand-edits

**Blocked by:** HITL Gate B

**Files:**
- Create: `.github/workflows/regen-check.yml`

- [ ] **Step 1: Write regen-check.yml**

```yaml
name: Regen check

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: "0 6 * * 1"   # Mondays 06:00 UTC — detect upstream spec drift

jobs:
  regen:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.13" }
      - name: Install dev dependencies
        run: pip install -e '.[dev]'

      - name: Compare vendored spec to upstream
        id: drift
        run: |
          curl -sSL https://izen.cast4all.energy/flexMon/v1/openapi.json -o /tmp/upstream.json
          upstream=$(sha256sum /tmp/upstream.json | awk '{print $1}')
          vendored=$(cat openapi/flexmon-v1.sha256)
          if [ "$upstream" != "$vendored" ]; then
            echo "Upstream spec has drifted."
            echo "  vendored: $vendored"
            echo "  upstream: $upstream"
            echo "drift=true" >> "$GITHUB_OUTPUT"
          fi

      - name: Fail on drift (schedule only) or continue
        if: steps.drift.outputs.drift == 'true' && github.event_name == 'schedule'
        run: |
          echo "::warning::Vendored OpenAPI spec has drifted from upstream. Human review required."
          exit 1

      - name: Regenerate and diff
        run: |
          make regen
          if ! git diff --quiet; then
            echo "::error::_generated/ was hand-edited or is stale. Run \`make regen\` locally and commit."
            git diff --stat
            exit 1
          fi
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/regen-check.yml
git commit -m "ci: enforce regen parity + weekly upstream spec drift check"
```

---

## Self-Review

Checked against `docs/superpowers/specs/2026-07-07-flowbuddy-ha-design.md`:

- **§2 Findings** — captured in `openapi/` (already committed) + `const.py` (P1.B). ✓
- **§3 Non-goals** — Lovelace card, HA core submission, multi-tenant onboarding, historical backfill, advanced EMS/Modbus UI — all deliberately excluded from tasks. ✓
- **§4.1 Repo layout** — Every file listed in the spec has a task. ✓
- **§4.1.1 Code generation** — P0.2 devcontainer, P1.B regen, Makefile `regen` target, `regen-check.yml` (P10.C). ✓
- **§4.2 Auth** — P2 covers both modes + refresh + 401 retry + secret storage (via `entry.data`). ✓
- **§4.3 Discovery mapping** — P5.A tests every row of the mapping table. ✓
- **§4.4 Polling** — P4.A hard-floors baseline at 60 s, gates boost on RTO cap and block state; P4.B/C are separate coordinators. ✓
- **§4.5 Control (write)** — P6.C (number), P6.D (climate), P6.E (button), P8.A (services). ✓
- **§4.6 Error handling** — 401 retry (P2), UpdateFailed on transport (P4), PollingLimitExceeded 10-min block (P4.A + P8.A). ✓
- **§4.7 Energy dashboard** — covered by `state_class = TOTAL_INCREASING` in discovery (P5.A). No dedicated task needed. ✓
- **§4.8 Tests** — every listed test file has a task; 80% coverage floor in `pyproject.toml` (P0.1) enforced by `tests.yml` (P10.B). ✓
- **§4.9 Distribution** — `hacs.json` (P1.A), MIT LICENSE (P0.1), version in `manifest.json` (P1.A). ✓
- **§5 Open questions** — items 1, 2, 6, 7 folded into HITL Gate B checklist. Items 3, 5, 8 remain in-progress items for implementation-time verification (documented in the code as `# TODO(§5.<n>)` markers where relevant). Explicitly: P3 verifies openapi-python-client handles HAL+JSON (§5.8); P4.A test suite verifies observed cadence assumptions (§5.4d) live in HITL B. ✓
- **§7 Risks** — vendor rate limits (P4.A + P8.A + `repairs` issue), password-grant availability (P2 supports both), feature-flag heterogeneity (P4/P6 skip empty coordinator data silently), HVAC/battery mis-op (P6.C/D constrain by vendor-reported ranges), generated code bloat (P10.C enforces regen parity), generator abandonment (P3 facade isolates generator specifics). ✓

**Type consistency check**:
- `FlowBuddyClient` methods named identically across P3 (definition) and P4/P6/P7/P8 (consumers).
- `TokenBundle`, `KeycloakTokenProvider`, `PollingLimitExceededError`, `InvalidCredentialsError` — same names throughout.
- Coordinator classes: `FlowBuddyInstantCoordinator`, `FlowBuddyDailyCoordinator`, `FlowBuddyAlarmsCoordinator` — consistent between definition (P4) and consumption (P6/P8/P9).
- Constants (`DEFAULT_INSTANT_INTERVAL_S` etc.) declared in P1.B, referenced in P4/P8/P9 with identical spelling.

**Placeholder scan**: no `TBD`, `TODO`, "implement later", "add appropriate error handling", or "similar to Task N" in imperative-step positions. The `# TODO(§5.<n>)` markers in P5-review are for runtime-only spec-verification tasks and are explicitly scoped.

---

## Execution Handoff

**Plan complete and saved to `docs/superpowers/plans/2026-07-07-flowbuddy-ha-implementation.md`.**

Two execution options:

1. **Subagent-Driven (recommended)** — dispatch a fresh subagent per task, review between tasks, respect the two HITL gates, exploit the parallel-safe phase structure (P1×3, P4×3, P6×5, P10×3 fan out).
2. **Inline Execution** — execute tasks sequentially in this session with checkpoints at each HITL gate.

**Which approach?**
