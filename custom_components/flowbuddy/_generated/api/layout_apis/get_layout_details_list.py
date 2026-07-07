from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_response_layout_output_list_model import (
    PaginatedResponseLayoutOutputListModel,
)
from ...models.rest_error_response import RestErrorResponse
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    *,
    meter: str | Unset = UNSET,
    cspi_enabled: bool | Unset = UNSET,
    from_last_changed_on: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["meter"] = meter

    params["cspiEnabled"] = cspi_enabled

    json_from_last_changed_on: str | Unset = UNSET
    if not isinstance(from_last_changed_on, Unset):
        json_from_last_changed_on = from_last_changed_on.isoformat()
    params["fromLastChangedOn"] = json_from_last_changed_on

    params["page"] = page

    params["pagesize"] = pagesize

    params["sortby"] = sortby

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/layouts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponseLayoutOutputListModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseLayoutOutputListModel.from_dict(response.json())

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
) -> Response[PaginatedResponseLayoutOutputListModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    meter: str | Unset = UNSET,
    cspi_enabled: bool | Unset = UNSET,
    from_last_changed_on: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseLayoutOutputListModel | RestErrorResponse]:
    """Retrieve all Layout objects

    Args:
        meter (str | Unset):
        cspi_enabled (bool | Unset):
        from_last_changed_on (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseLayoutOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        meter=meter,
        cspi_enabled=cspi_enabled,
        from_last_changed_on=from_last_changed_on,
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
    meter: str | Unset = UNSET,
    cspi_enabled: bool | Unset = UNSET,
    from_last_changed_on: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseLayoutOutputListModel | RestErrorResponse | None:
    """Retrieve all Layout objects

    Args:
        meter (str | Unset):
        cspi_enabled (bool | Unset):
        from_last_changed_on (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseLayoutOutputListModel | RestErrorResponse
    """

    return sync_detailed(
        client=client,
        meter=meter,
        cspi_enabled=cspi_enabled,
        from_last_changed_on=from_last_changed_on,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    meter: str | Unset = UNSET,
    cspi_enabled: bool | Unset = UNSET,
    from_last_changed_on: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseLayoutOutputListModel | RestErrorResponse]:
    """Retrieve all Layout objects

    Args:
        meter (str | Unset):
        cspi_enabled (bool | Unset):
        from_last_changed_on (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseLayoutOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        meter=meter,
        cspi_enabled=cspi_enabled,
        from_last_changed_on=from_last_changed_on,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    meter: str | Unset = UNSET,
    cspi_enabled: bool | Unset = UNSET,
    from_last_changed_on: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseLayoutOutputListModel | RestErrorResponse | None:
    """Retrieve all Layout objects

    Args:
        meter (str | Unset):
        cspi_enabled (bool | Unset):
        from_last_changed_on (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseLayoutOutputListModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            meter=meter,
            cspi_enabled=cspi_enabled,
            from_last_changed_on=from_last_changed_on,
            page=page,
            pagesize=pagesize,
            sortby=sortby,
        )
    ).parsed
