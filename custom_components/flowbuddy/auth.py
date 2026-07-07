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

    async def invalidate(self) -> None:
        async with self._lock:
            self._token = None

    def httpx_auth(self) -> httpx.Auth:
        return _AsyncAuth(self)


class _AsyncAuth(httpx.Auth):
    requires_response_body = False

    def __init__(self, provider: KeycloakTokenProvider) -> None:
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
