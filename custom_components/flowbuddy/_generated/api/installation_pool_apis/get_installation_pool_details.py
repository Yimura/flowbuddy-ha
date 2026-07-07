from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.installation_pool_output_model import InstallationPoolOutputModel
from ...models.rest_error_response import RestErrorResponse
from typing import cast


def _get_kwargs(
    installation_pool_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/installationpools/{installation_pool_id}".format(
            installation_pool_id=quote(str(installation_pool_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InstallationPoolOutputModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = InstallationPoolOutputModel.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RestErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RestErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = RestErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = RestErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InstallationPoolOutputModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    installation_pool_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[InstallationPoolOutputModel | RestErrorResponse]:
    """Retrieve a single InstallationPool

    Args:
        installation_pool_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstallationPoolOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        installation_pool_id=installation_pool_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    installation_pool_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> InstallationPoolOutputModel | RestErrorResponse | None:
    """Retrieve a single InstallationPool

    Args:
        installation_pool_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstallationPoolOutputModel | RestErrorResponse
    """

    return sync_detailed(
        installation_pool_id=installation_pool_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    installation_pool_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[InstallationPoolOutputModel | RestErrorResponse]:
    """Retrieve a single InstallationPool

    Args:
        installation_pool_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstallationPoolOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        installation_pool_id=installation_pool_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    installation_pool_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> InstallationPoolOutputModel | RestErrorResponse | None:
    """Retrieve a single InstallationPool

    Args:
        installation_pool_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstallationPoolOutputModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            installation_pool_id=installation_pool_id,
            client=client,
        )
    ).parsed
