from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_response_switch_breaker_output_list_model import (
    PaginatedResponseSwitchBreakerOutputListModel,
)
from ...models.rest_error_response import RestErrorResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    communicator: str | Unset = UNSET,
    status: str | Unset = UNSET,
    communicator_remote_command: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["communicator"] = communicator

    params["status"] = status

    params["communicatorRemoteCommand"] = communicator_remote_command

    params["page"] = page

    params["pagesize"] = pagesize

    params["sortby"] = sortby

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/switchbreakers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponseSwitchBreakerOutputListModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseSwitchBreakerOutputListModel.from_dict(response.json())

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
) -> Response[PaginatedResponseSwitchBreakerOutputListModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    communicator: str | Unset = UNSET,
    status: str | Unset = UNSET,
    communicator_remote_command: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseSwitchBreakerOutputListModel | RestErrorResponse]:
    """Retrieve all SwitchBreaker objects

    Args:
        communicator (str | Unset):
        status (str | Unset):
        communicator_remote_command (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseSwitchBreakerOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        communicator=communicator,
        status=status,
        communicator_remote_command=communicator_remote_command,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    communicator: str | Unset = UNSET,
    status: str | Unset = UNSET,
    communicator_remote_command: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseSwitchBreakerOutputListModel | RestErrorResponse | None:
    """Retrieve all SwitchBreaker objects

    Args:
        communicator (str | Unset):
        status (str | Unset):
        communicator_remote_command (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseSwitchBreakerOutputListModel | RestErrorResponse
    """

    return sync_detailed(
        client=client,
        communicator=communicator,
        status=status,
        communicator_remote_command=communicator_remote_command,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    communicator: str | Unset = UNSET,
    status: str | Unset = UNSET,
    communicator_remote_command: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseSwitchBreakerOutputListModel | RestErrorResponse]:
    """Retrieve all SwitchBreaker objects

    Args:
        communicator (str | Unset):
        status (str | Unset):
        communicator_remote_command (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseSwitchBreakerOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        communicator=communicator,
        status=status,
        communicator_remote_command=communicator_remote_command,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    communicator: str | Unset = UNSET,
    status: str | Unset = UNSET,
    communicator_remote_command: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseSwitchBreakerOutputListModel | RestErrorResponse | None:
    """Retrieve all SwitchBreaker objects

    Args:
        communicator (str | Unset):
        status (str | Unset):
        communicator_remote_command (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseSwitchBreakerOutputListModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            communicator=communicator,
            status=status,
            communicator_remote_command=communicator_remote_command,
            page=page,
            pagesize=pagesize,
            sortby=sortby,
        )
    ).parsed
