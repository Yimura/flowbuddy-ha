from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.communicator_verification_output_model import CommunicatorVerificationOutputModel
from ...models.rest_error_response import RestErrorResponse
from typing import cast


def _get_kwargs(
    communicator_verification_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/communicatorverifications/{communicator_verification_id}".format(
            communicator_verification_id=quote(str(communicator_verification_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommunicatorVerificationOutputModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = CommunicatorVerificationOutputModel.from_dict(response.json())

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
) -> Response[CommunicatorVerificationOutputModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    communicator_verification_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CommunicatorVerificationOutputModel | RestErrorResponse]:
    """Retrieve a single CommunicatorVerification

    Args:
        communicator_verification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommunicatorVerificationOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        communicator_verification_id=communicator_verification_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    communicator_verification_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> CommunicatorVerificationOutputModel | RestErrorResponse | None:
    """Retrieve a single CommunicatorVerification

    Args:
        communicator_verification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommunicatorVerificationOutputModel | RestErrorResponse
    """

    return sync_detailed(
        communicator_verification_id=communicator_verification_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    communicator_verification_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CommunicatorVerificationOutputModel | RestErrorResponse]:
    """Retrieve a single CommunicatorVerification

    Args:
        communicator_verification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommunicatorVerificationOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        communicator_verification_id=communicator_verification_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    communicator_verification_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> CommunicatorVerificationOutputModel | RestErrorResponse | None:
    """Retrieve a single CommunicatorVerification

    Args:
        communicator_verification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommunicatorVerificationOutputModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            communicator_verification_id=communicator_verification_id,
            client=client,
        )
    ).parsed
