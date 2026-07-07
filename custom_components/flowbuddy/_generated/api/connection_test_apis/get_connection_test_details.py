from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connection_test_output_model import ConnectionTestOutputModel
from ...models.rest_error_response import RestErrorResponse
from typing import cast


def _get_kwargs(
    connection_test_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/connectiontests/{connection_test_id}".format(
            connection_test_id=quote(str(connection_test_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConnectionTestOutputModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = ConnectionTestOutputModel.from_dict(response.json())

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
) -> Response[ConnectionTestOutputModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_test_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ConnectionTestOutputModel | RestErrorResponse]:
    """Retrieve a single ConnectionTest

    Args:
        connection_test_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionTestOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        connection_test_id=connection_test_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_test_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ConnectionTestOutputModel | RestErrorResponse | None:
    """Retrieve a single ConnectionTest

    Args:
        connection_test_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionTestOutputModel | RestErrorResponse
    """

    return sync_detailed(
        connection_test_id=connection_test_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    connection_test_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ConnectionTestOutputModel | RestErrorResponse]:
    """Retrieve a single ConnectionTest

    Args:
        connection_test_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionTestOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        connection_test_id=connection_test_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_test_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ConnectionTestOutputModel | RestErrorResponse | None:
    """Retrieve a single ConnectionTest

    Args:
        connection_test_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionTestOutputModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            connection_test_id=connection_test_id,
            client=client,
        )
    ).parsed
