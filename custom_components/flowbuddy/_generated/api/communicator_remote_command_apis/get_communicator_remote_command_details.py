from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.communicator_remote_command_output_model import CommunicatorRemoteCommandOutputModel
from ...models.rest_error_response import RestErrorResponse
from typing import cast


def _get_kwargs(
    communicator_remote_command_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/communicatorremotecommands/{communicator_remote_command_id}".format(
            communicator_remote_command_id=quote(str(communicator_remote_command_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommunicatorRemoteCommandOutputModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = CommunicatorRemoteCommandOutputModel.from_dict(response.json())

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
) -> Response[CommunicatorRemoteCommandOutputModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    communicator_remote_command_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CommunicatorRemoteCommandOutputModel | RestErrorResponse]:
    """Retrieve a single CommunicatorRemoteCommand

    Args:
        communicator_remote_command_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommunicatorRemoteCommandOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        communicator_remote_command_id=communicator_remote_command_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    communicator_remote_command_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> CommunicatorRemoteCommandOutputModel | RestErrorResponse | None:
    """Retrieve a single CommunicatorRemoteCommand

    Args:
        communicator_remote_command_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommunicatorRemoteCommandOutputModel | RestErrorResponse
    """

    return sync_detailed(
        communicator_remote_command_id=communicator_remote_command_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    communicator_remote_command_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CommunicatorRemoteCommandOutputModel | RestErrorResponse]:
    """Retrieve a single CommunicatorRemoteCommand

    Args:
        communicator_remote_command_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommunicatorRemoteCommandOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        communicator_remote_command_id=communicator_remote_command_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    communicator_remote_command_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> CommunicatorRemoteCommandOutputModel | RestErrorResponse | None:
    """Retrieve a single CommunicatorRemoteCommand

    Args:
        communicator_remote_command_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommunicatorRemoteCommandOutputModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            communicator_remote_command_id=communicator_remote_command_id,
            client=client,
        )
    ).parsed
