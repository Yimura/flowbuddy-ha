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
