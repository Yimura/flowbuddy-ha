from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.command_output_model import CommandOutputModel
from ...models.rest_error_response import RestErrorResponse
from typing import cast


def _get_kwargs(
    command_external_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/commands/{command_external_id}".format(
            command_external_id=quote(str(command_external_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommandOutputModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = CommandOutputModel.from_dict(response.json())

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
) -> Response[CommandOutputModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    command_external_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CommandOutputModel | RestErrorResponse]:
    """Retrieve a single Command

    Args:
        command_external_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommandOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        command_external_id=command_external_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    command_external_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> CommandOutputModel | RestErrorResponse | None:
    """Retrieve a single Command

    Args:
        command_external_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommandOutputModel | RestErrorResponse
    """

    return sync_detailed(
        command_external_id=command_external_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    command_external_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CommandOutputModel | RestErrorResponse]:
    """Retrieve a single Command

    Args:
        command_external_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommandOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        command_external_id=command_external_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    command_external_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> CommandOutputModel | RestErrorResponse | None:
    """Retrieve a single Command

    Args:
        command_external_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommandOutputModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            command_external_id=command_external_id,
            client=client,
        )
    ).parsed
