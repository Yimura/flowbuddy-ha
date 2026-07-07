"""Config flow for the FlowBuddy integration.

Three steps: pick an auth mode, enter credentials for that mode (validated
live against Keycloak + the FlexMon /installations endpoint), then pick an
installation if the account has more than one. ``async_step_reauth`` re-uses
the credentials step so a token that has gone permanently invalid (refresh
token revoked, password rotated, ...) can be re-established without losing
the rest of the config entry.
"""

from __future__ import annotations

import logging
from typing import Any

import httpx
import voluptuous as vol
from homeassistant import config_entries

from .api import FlowBuddyClient
from .auth import InvalidCredentialsError, KeycloakTokenProvider
from .const import (
    AUTH_MODE_CLIENT_CREDS,
    AUTH_MODE_PASSWORD,
    CONF_AUTH_MODE,
    CONF_INSTALLATION_ID,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

# Placeholder client_id for the Keycloak "password" grant. In production this
# should be read from the SPA bundle (spec §5.2); until that inspection is
# automated we ship a sane default the user can override in the UI.
DEFAULT_PASSWORD_CLIENT_ID = "go_flowbuddy"


class FlowBuddyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for FlowBuddy."""

    VERSION = 1

    def __init__(self) -> None:
        self._auth_mode: str | None = None
        self._credentials: dict[str, Any] = {}
        self._installations: list[Any] = []

    # -- Step 1: auth mode -------------------------------------------------

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.ConfigFlowResult:
        """Standard SOURCE_USER entry point; delegates to the named auth_mode step."""
        return await self.async_step_auth_mode(user_input)

    async def async_step_auth_mode(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.ConfigFlowResult:
        """Show the auth-mode picker (mapped to the config.step.auth_mode translation)."""
        if user_input is not None:
            self._auth_mode = user_input["mode"]
            return await self.async_step_credentials()

        schema = vol.Schema(
            {
                vol.Required("mode", default=AUTH_MODE_CLIENT_CREDS): vol.In(
                    [AUTH_MODE_CLIENT_CREDS, AUTH_MODE_PASSWORD]
                )
            }
        )
        return self.async_show_form(step_id="auth_mode", data_schema=schema)

    # -- Step 2: credentials -------------------------------------------------

    async def async_step_credentials(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.ConfigFlowResult:
        errors: dict[str, str] = {}
        if user_input is not None:
            try:
                installations = await self._async_validate_credentials(user_input)
            except InvalidCredentialsError:
                errors["base"] = "invalid_auth"
            except httpx.HTTPError:
                errors["base"] = "cannot_connect"
            else:
                self._credentials = user_input
                self._installations = installations
                return await self.async_step_installation()

        return self.async_show_form(
            step_id="credentials",
            data_schema=self._credentials_schema(),
            errors=errors,
        )

    def _credentials_schema(self) -> vol.Schema:
        if self._auth_mode == AUTH_MODE_PASSWORD:
            return vol.Schema(
                {
                    vol.Required("email"): str,
                    vol.Required("password"): str,
                    vol.Optional("client_id", default=DEFAULT_PASSWORD_CLIENT_ID): str,
                }
            )
        return vol.Schema(
            {
                vol.Required("client_id"): str,
                vol.Required("client_secret"): str,
            }
        )

    async def _async_validate_credentials(self, user_input: dict[str, Any]) -> list[Any]:
        """Exercise POST /token + GET /installations to prove the creds work.

        Raises ``InvalidCredentialsError`` on 401/invalid_grant (mapped to the
        ``invalid_auth`` form error) and lets any other ``httpx.HTTPError``
        (connection failure, timeout, unexpected 5xx, ...) propagate for the
        caller to map to ``cannot_connect``.
        """
        http = httpx.AsyncClient()
        try:
            if self._auth_mode == AUTH_MODE_PASSWORD:
                provider = KeycloakTokenProvider(
                    mode="password",
                    http=http,
                    client_id=user_input.get("client_id") or DEFAULT_PASSWORD_CLIENT_ID,
                    username=user_input["email"],
                    password=user_input["password"],
                )
            else:
                provider = KeycloakTokenProvider(
                    mode="client_credentials",
                    http=http,
                    client_id=user_input["client_id"],
                    client_secret=user_input["client_secret"],
                )
            client = FlowBuddyClient(http=http, token_provider=provider)
            return await client.list_installations()
        finally:
            await http.aclose()

    # -- Step 3: installation picker -----------------------------------------

    async def async_step_installation(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.ConfigFlowResult:
        if not self._installations:
            return self.async_abort(reason="no_installations")

        if len(self._installations) == 1:
            return await self._async_finish(self._installations[0])

        if user_input is not None:
            installation_id = user_input[CONF_INSTALLATION_ID]
            installation = next(i for i in self._installations if i.uuid == installation_id)
            return await self._async_finish(installation)

        options = {i.uuid: i.identification for i in self._installations}
        schema = vol.Schema({vol.Required(CONF_INSTALLATION_ID): vol.In(options)})
        return self.async_show_form(step_id="installation", data_schema=schema)

    async def _async_finish(self, installation: Any) -> config_entries.ConfigFlowResult:
        await self.async_set_unique_id(installation.uuid)

        data = {
            **self._credentials,
            CONF_AUTH_MODE: self._auth_mode,
            CONF_INSTALLATION_ID: installation.uuid,
        }
        # Password mode always carries a client_id (defaulted in the schema);
        # make sure it lands in entry.data even if the user left it blank.
        if self._auth_mode == AUTH_MODE_PASSWORD:
            data.setdefault("client_id", DEFAULT_PASSWORD_CLIENT_ID)

        if self.source == config_entries.SOURCE_REAUTH:
            self._abort_if_unique_id_mismatch()
            return self.async_update_reload_and_abort(self._get_reauth_entry(), data=data)

        self._abort_if_unique_id_configured()
        return self.async_create_entry(title=installation.identification, data=data)

    # -- Reauth --------------------------------------------------------------

    async def async_step_reauth(
        self, entry_data: dict[str, Any]
    ) -> config_entries.ConfigFlowResult:
        """Handle re-authentication when a token becomes permanently invalid.

        Skips straight to the credentials step -- the auth mode is already
        known from the existing config entry -- and otherwise follows the
        same validate-then-pick-installation path as the initial setup.
        """
        self._auth_mode = entry_data.get(CONF_AUTH_MODE, AUTH_MODE_CLIENT_CREDS)
        return await self.async_step_credentials()
