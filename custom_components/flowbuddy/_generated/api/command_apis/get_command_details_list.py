from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_response_command_output_list_model import (
    PaginatedResponseCommandOutputListModel,
)
from ...models.rest_error_response import RestErrorResponse
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    *,
    installation: str | Unset = UNSET,
    meter: str | Unset = UNSET,
    measurement: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    entered_on: datetime.datetime | Unset = UNSET,
    performed_on: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["installation"] = installation

    params["meter"] = meter

    params["measurement"] = measurement

    params["type"] = type_

    params["status"] = status

    json_entered_on: str | Unset = UNSET
    if not isinstance(entered_on, Unset):
        json_entered_on = entered_on.isoformat()
    params["enteredOn"] = json_entered_on

    json_performed_on: str | Unset = UNSET
    if not isinstance(performed_on, Unset):
        json_performed_on = performed_on.isoformat()
    params["performedOn"] = json_performed_on

    params["page"] = page

    params["pagesize"] = pagesize

    params["sortby"] = sortby

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/commands",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponseCommandOutputListModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseCommandOutputListModel.from_dict(response.json())

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
) -> Response[PaginatedResponseCommandOutputListModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    installation: str | Unset = UNSET,
    meter: str | Unset = UNSET,
    measurement: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    entered_on: datetime.datetime | Unset = UNSET,
    performed_on: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseCommandOutputListModel | RestErrorResponse]:
    """Retrieve all Command objects

    Args:
        installation (str | Unset):
        meter (str | Unset):
        measurement (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        entered_on (datetime.datetime | Unset):
        performed_on (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseCommandOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        installation=installation,
        meter=meter,
        measurement=measurement,
        type_=type_,
        status=status,
        entered_on=entered_on,
        performed_on=performed_on,
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
    installation: str | Unset = UNSET,
    meter: str | Unset = UNSET,
    measurement: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    entered_on: datetime.datetime | Unset = UNSET,
    performed_on: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseCommandOutputListModel | RestErrorResponse | None:
    """Retrieve all Command objects

    Args:
        installation (str | Unset):
        meter (str | Unset):
        measurement (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        entered_on (datetime.datetime | Unset):
        performed_on (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseCommandOutputListModel | RestErrorResponse
    """

    return sync_detailed(
        client=client,
        installation=installation,
        meter=meter,
        measurement=measurement,
        type_=type_,
        status=status,
        entered_on=entered_on,
        performed_on=performed_on,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    installation: str | Unset = UNSET,
    meter: str | Unset = UNSET,
    measurement: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    entered_on: datetime.datetime | Unset = UNSET,
    performed_on: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseCommandOutputListModel | RestErrorResponse]:
    """Retrieve all Command objects

    Args:
        installation (str | Unset):
        meter (str | Unset):
        measurement (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        entered_on (datetime.datetime | Unset):
        performed_on (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseCommandOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        installation=installation,
        meter=meter,
        measurement=measurement,
        type_=type_,
        status=status,
        entered_on=entered_on,
        performed_on=performed_on,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    installation: str | Unset = UNSET,
    meter: str | Unset = UNSET,
    measurement: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    entered_on: datetime.datetime | Unset = UNSET,
    performed_on: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseCommandOutputListModel | RestErrorResponse | None:
    """Retrieve all Command objects

    Args:
        installation (str | Unset):
        meter (str | Unset):
        measurement (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        entered_on (datetime.datetime | Unset):
        performed_on (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseCommandOutputListModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            installation=installation,
            meter=meter,
            measurement=measurement,
            type_=type_,
            status=status,
            entered_on=entered_on,
            performed_on=performed_on,
            page=page,
            pagesize=pagesize,
            sortby=sortby,
        )
    ).parsed
