from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.control_type_output_model import ControlTypeOutputModel
from ...models.rest_error_response import RestErrorResponse
from typing import cast


def _get_kwargs(
    control_type_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/controltypes/{control_type_id}".format(
            control_type_id=quote(str(control_type_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ControlTypeOutputModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = ControlTypeOutputModel.from_dict(response.json())

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
) -> Response[ControlTypeOutputModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    control_type_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ControlTypeOutputModel | RestErrorResponse]:
    """Retrieve a single ControlType

    Args:
        control_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ControlTypeOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        control_type_id=control_type_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    control_type_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ControlTypeOutputModel | RestErrorResponse | None:
    """Retrieve a single ControlType

    Args:
        control_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ControlTypeOutputModel | RestErrorResponse
    """

    return sync_detailed(
        control_type_id=control_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    control_type_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ControlTypeOutputModel | RestErrorResponse]:
    """Retrieve a single ControlType

    Args:
        control_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ControlTypeOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        control_type_id=control_type_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    control_type_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ControlTypeOutputModel | RestErrorResponse | None:
    """Retrieve a single ControlType

    Args:
        control_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ControlTypeOutputModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            control_type_id=control_type_id,
            client=client,
        )
    ).parsed
