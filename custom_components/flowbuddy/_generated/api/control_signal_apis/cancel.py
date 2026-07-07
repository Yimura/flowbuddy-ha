from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_error_response import RestErrorResponse
from typing import cast


def _get_kwargs(
    control_signal_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/controlsignals/{control_signal_id}/cancel".format(
            control_signal_id=quote(str(control_signal_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RestErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    control_signal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RestErrorResponse]:
    """Executing the command cancel

    Args:
        control_signal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        control_signal_id=control_signal_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    control_signal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RestErrorResponse | None:
    """Executing the command cancel

    Args:
        control_signal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RestErrorResponse
    """

    return sync_detailed(
        control_signal_id=control_signal_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    control_signal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RestErrorResponse]:
    """Executing the command cancel

    Args:
        control_signal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        control_signal_id=control_signal_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    control_signal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RestErrorResponse | None:
    """Executing the command cancel

    Args:
        control_signal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            control_signal_id=control_signal_id,
            client=client,
        )
    ).parsed
