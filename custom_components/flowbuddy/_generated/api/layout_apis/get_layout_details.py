from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.layout_output_model import LayoutOutputModel
from ...models.rest_error_response import RestErrorResponse
from typing import cast


def _get_kwargs(
    layout_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/layouts/{layout_id}".format(
            layout_id=quote(str(layout_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LayoutOutputModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = LayoutOutputModel.from_dict(response.json())

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
) -> Response[LayoutOutputModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    layout_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[LayoutOutputModel | RestErrorResponse]:
    """Retrieve a single Layout

    Args:
        layout_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LayoutOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        layout_id=layout_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    layout_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> LayoutOutputModel | RestErrorResponse | None:
    """Retrieve a single Layout

    Args:
        layout_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LayoutOutputModel | RestErrorResponse
    """

    return sync_detailed(
        layout_id=layout_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    layout_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[LayoutOutputModel | RestErrorResponse]:
    """Retrieve a single Layout

    Args:
        layout_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LayoutOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        layout_id=layout_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    layout_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> LayoutOutputModel | RestErrorResponse | None:
    """Retrieve a single Layout

    Args:
        layout_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LayoutOutputModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            layout_id=layout_id,
            client=client,
        )
    ).parsed
