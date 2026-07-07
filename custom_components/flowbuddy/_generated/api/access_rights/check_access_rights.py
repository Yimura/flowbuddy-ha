from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_response_access_right_output_list_model import (
    PaginatedResponseAccessRightOutputListModel,
)
from ...models.rest_error_response import RestErrorResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    filter_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/security/accessrights",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponseAccessRightOutputListModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseAccessRightOutputListModel.from_dict(response.json())

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
) -> Response[PaginatedResponseAccessRightOutputListModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
) -> Response[PaginatedResponseAccessRightOutputListModel | RestErrorResponse]:
    """Check if the user or session has the supplied access rights

    Args:
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseAccessRightOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
) -> PaginatedResponseAccessRightOutputListModel | RestErrorResponse | None:
    """Check if the user or session has the supplied access rights

    Args:
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseAccessRightOutputListModel | RestErrorResponse
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
) -> Response[PaginatedResponseAccessRightOutputListModel | RestErrorResponse]:
    """Check if the user or session has the supplied access rights

    Args:
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseAccessRightOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
) -> PaginatedResponseAccessRightOutputListModel | RestErrorResponse | None:
    """Check if the user or session has the supplied access rights

    Args:
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseAccessRightOutputListModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
        )
    ).parsed
