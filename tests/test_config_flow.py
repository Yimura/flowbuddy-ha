"""Tests for the FlowBuddy config flow."""

from __future__ import annotations

import httpx
from homeassistant import config_entries, data_entry_flow
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.flowbuddy.const import (
    AUTH_MODE_CLIENT_CREDS,
    AUTH_MODE_PASSWORD,
    CONF_AUTH_MODE,
    CONF_INSTALLATION_ID,
    DOMAIN,
    KEYCLOAK_TOKEN_URL,
)

INSTALLATIONS_URL = "https://izen.cast4all.energy/flexMon/v1/installations"


def _single_installation(load_fixture):
    data = load_fixture("installations.json")
    data["_embedded"]["installations"] = data["_embedded"]["installations"][:1]
    return data


async def _start_user_flow(hass):
    return await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )


async def test_client_creds_happy_path_single_installation(hass, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    respx_mock.get(INSTALLATIONS_URL).mock(
        return_value=httpx.Response(200, json=_single_installation(load_fixture))
    )

    result = await _start_user_flow(hass)
    assert result["type"] == data_entry_flow.FlowResultType.FORM
    assert result["step_id"] == "user"

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"mode": AUTH_MODE_CLIENT_CREDS}
    )
    assert result["type"] == data_entry_flow.FlowResultType.FORM
    assert result["step_id"] == "credentials"

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"client_id": "cid", "client_secret": "secret"}
    )

    assert result["type"] == data_entry_flow.FlowResultType.CREATE_ENTRY
    assert result["data"][CONF_AUTH_MODE] == AUTH_MODE_CLIENT_CREDS
    assert result["data"]["client_id"] == "cid"
    assert result["data"]["client_secret"] == "secret"
    assert result["data"][CONF_INSTALLATION_ID] == "00000000-0000-0000-0000-000000000001"
    await hass.async_block_till_done()


async def test_client_creds_happy_path_multi_installation(hass, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    respx_mock.get(INSTALLATIONS_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("installations.json"))
    )

    result = await _start_user_flow(hass)
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"mode": AUTH_MODE_CLIENT_CREDS}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"client_id": "cid", "client_secret": "secret"}
    )

    assert result["type"] == data_entry_flow.FlowResultType.FORM
    assert result["step_id"] == "installation"

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {CONF_INSTALLATION_ID: "00000000-0000-0000-0000-000000000002"},
    )

    assert result["type"] == data_entry_flow.FlowResultType.CREATE_ENTRY
    assert result["data"][CONF_INSTALLATION_ID] == "00000000-0000-0000-0000-000000000002"
    await hass.async_block_till_done()


async def test_client_creds_invalid_credentials(hass, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(401, json=load_fixture("token_invalid_grant.json"))
    )

    result = await _start_user_flow(hass)
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"mode": AUTH_MODE_CLIENT_CREDS}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"client_id": "cid", "client_secret": "wrong"}
    )

    assert result["type"] == data_entry_flow.FlowResultType.FORM
    assert result["step_id"] == "credentials"
    assert result["errors"] == {"base": "invalid_auth"}


async def test_client_creds_cannot_connect(hass, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(side_effect=httpx.ConnectError("refused"))

    result = await _start_user_flow(hass)
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"mode": AUTH_MODE_CLIENT_CREDS}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"client_id": "cid", "client_secret": "secret"}
    )

    assert result["type"] == data_entry_flow.FlowResultType.FORM
    assert result["step_id"] == "credentials"
    assert result["errors"] == {"base": "cannot_connect"}


async def test_password_mode_happy_path(hass, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    respx_mock.get(INSTALLATIONS_URL).mock(
        return_value=httpx.Response(200, json=_single_installation(load_fixture))
    )

    result = await _start_user_flow(hass)
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"mode": AUTH_MODE_PASSWORD}
    )
    assert result["type"] == data_entry_flow.FlowResultType.FORM
    assert result["step_id"] == "credentials"

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {"email": "user@example.com", "password": "hunter2"},
    )

    assert result["type"] == data_entry_flow.FlowResultType.CREATE_ENTRY
    assert result["data"][CONF_AUTH_MODE] == AUTH_MODE_PASSWORD
    assert result["data"]["email"] == "user@example.com"
    assert result["data"]["password"] == "hunter2"
    # Placeholder default client_id for the password grant (spec §5.2).
    assert result["data"]["client_id"] == "simpl-go-frontend"
    await hass.async_block_till_done()


async def test_password_mode_invalid_credentials(hass, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(401, json=load_fixture("token_invalid_grant.json"))
    )

    result = await _start_user_flow(hass)
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"mode": AUTH_MODE_PASSWORD}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {"email": "user@example.com", "password": "wrong"},
    )

    assert result["type"] == data_entry_flow.FlowResultType.FORM
    assert result["step_id"] == "credentials"
    assert result["errors"] == {"base": "invalid_auth"}


async def test_zero_installations_aborts(hass, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    empty = load_fixture("installations.json")
    empty["_embedded"]["installations"] = []
    respx_mock.get(INSTALLATIONS_URL).mock(return_value=httpx.Response(200, json=empty))

    result = await _start_user_flow(hass)
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"mode": AUTH_MODE_CLIENT_CREDS}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"client_id": "cid", "client_secret": "secret"}
    )

    assert result["type"] == data_entry_flow.FlowResultType.ABORT
    assert result["reason"] == "no_installations"


async def test_duplicate_installation_aborts(hass, load_fixture, respx_mock):
    iid = "00000000-0000-0000-0000-000000000001"
    MockConfigEntry(domain=DOMAIN, unique_id=iid, data={CONF_INSTALLATION_ID: iid}).add_to_hass(
        hass
    )

    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    respx_mock.get(INSTALLATIONS_URL).mock(
        return_value=httpx.Response(200, json=_single_installation(load_fixture))
    )

    result = await _start_user_flow(hass)
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"mode": AUTH_MODE_CLIENT_CREDS}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"client_id": "cid", "client_secret": "secret"}
    )

    assert result["type"] == data_entry_flow.FlowResultType.ABORT
    assert result["reason"] == "already_configured"


async def test_reauth_flow(hass, load_fixture, respx_mock):
    iid = "00000000-0000-0000-0000-000000000001"
    entry = MockConfigEntry(
        domain=DOMAIN,
        unique_id=iid,
        data={
            CONF_AUTH_MODE: AUTH_MODE_CLIENT_CREDS,
            "client_id": "old-cid",
            "client_secret": "old-secret",
            CONF_INSTALLATION_ID: iid,
        },
    )
    entry.add_to_hass(hass)

    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    respx_mock.get(INSTALLATIONS_URL).mock(
        return_value=httpx.Response(200, json=_single_installation(load_fixture))
    )

    result = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={
            "source": config_entries.SOURCE_REAUTH,
            "entry_id": entry.entry_id,
            "unique_id": entry.unique_id,
        },
        data=entry.data,
    )

    # Reauth reuses the credentials step directly -- no need to re-pick auth mode.
    assert result["type"] == data_entry_flow.FlowResultType.FORM
    assert result["step_id"] == "credentials"

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"client_id": "new-cid", "client_secret": "new-secret"}
    )
    await hass.async_block_till_done()

    assert result["type"] == data_entry_flow.FlowResultType.ABORT
    assert result["reason"] == "reauth_successful"
    assert entry.data["client_id"] == "new-cid"
    assert entry.data["client_secret"] == "new-secret"
    assert entry.data[CONF_INSTALLATION_ID] == iid
