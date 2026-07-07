"""Tests for auth.KeycloakTokenProvider and its httpx.Auth adapter."""

from __future__ import annotations

import asyncio

import httpx
import pytest

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


async def test_second_get_token_uses_cache(http_client, load_fixture, respx_mock):
    route = respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    provider = KeycloakTokenProvider(
        mode="client_credentials",
        http=http_client,
        client_id="cid",
        client_secret="secret",
    )
    await provider.get_token()
    await provider.get_token()
    assert route.call_count == 1


async def test_invalid_grant_raises(http_client, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(401, json=load_fixture("token_invalid_grant.json"))
    )
    provider = KeycloakTokenProvider(
        mode="password",
        http=http_client,
        client_id="frontend",
        username="wrong@example.com",
        password="nope",
    )
    with pytest.raises(InvalidCredentialsError):
        await provider.get_token()


async def test_single_flight_refresh(http_client, load_fixture, respx_mock):
    route = respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    provider = KeycloakTokenProvider(
        mode="client_credentials",
        http=http_client,
        client_id="cid",
        client_secret="secret",
    )
    # Fire 10 concurrent get_token calls — must result in exactly ONE POST.
    tokens = await asyncio.gather(*(provider.get_token() for _ in range(10)))
    assert route.call_count == 1
    assert all(t == "test-access-token-abc123" for t in tokens)


async def test_httpx_auth_injects_bearer(http_client, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    api_route = respx_mock.get("https://api.example.com/thing").mock(
        return_value=httpx.Response(200, json={"ok": True})
    )
    provider = KeycloakTokenProvider(
        mode="client_credentials",
        http=http_client,
        client_id="cid",
        client_secret="secret",
    )
    async with httpx.AsyncClient(auth=provider.httpx_auth()) as api:
        r = await api.get("https://api.example.com/thing")
    assert r.status_code == 200
    assert (
        api_route.calls.last.request.headers["Authorization"] == "Bearer test-access-token-abc123"
    )


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
        mode="client_credentials",
        http=http_client,
        client_id="cid",
        client_secret="secret",
    )
    async with httpx.AsyncClient(auth=provider.httpx_auth()) as api:
        r = await api.get("https://api.example.com/thing")
    assert r.status_code == 200
    assert token_route.call_count == 2
    assert api_route.call_count == 2
    assert api_route.calls[1].request.headers["Authorization"] == "Bearer new-token-after-401"


async def test_auth_stops_after_two_401s(http_client, load_fixture, respx_mock):
    respx_mock.post(KEYCLOAK_TOKEN_URL).mock(
        return_value=httpx.Response(200, json=load_fixture("token_success.json"))
    )
    api_route = respx_mock.get("https://api.example.com/thing").mock(
        return_value=httpx.Response(401, json={"error": "still bad"})
    )
    provider = KeycloakTokenProvider(
        mode="client_credentials",
        http=http_client,
        client_id="cid",
        client_secret="secret",
    )
    async with httpx.AsyncClient(auth=provider.httpx_auth()) as api:
        r = await api.get("https://api.example.com/thing")
    assert r.status_code == 401
    assert api_route.call_count == 2  # one original + one retry, then stop
