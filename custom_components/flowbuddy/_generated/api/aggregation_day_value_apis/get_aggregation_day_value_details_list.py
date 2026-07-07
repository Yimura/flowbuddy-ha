from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_response_aggregation_day_value_output_list_model import (
    PaginatedResponseAggregationDayValueOutputListModel,
)
from ...models.rest_error_response import RestErrorResponse
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    *,
    measurement: str | Unset = UNSET,
    from_timestart: datetime.datetime | Unset = UNSET,
    to_timestart: datetime.datetime | Unset = UNSET,
    from_period_start: datetime.datetime | Unset = UNSET,
    to_period_start: datetime.datetime | Unset = UNSET,
    installation: str | Unset = UNSET,
    measurement_type: str | Unset = UNSET,
    meter: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["measurement"] = measurement

    json_from_timestart: str | Unset = UNSET
    if not isinstance(from_timestart, Unset):
        json_from_timestart = from_timestart.isoformat()
    params["fromTimestart"] = json_from_timestart

    json_to_timestart: str | Unset = UNSET
    if not isinstance(to_timestart, Unset):
        json_to_timestart = to_timestart.isoformat()
    params["toTimestart"] = json_to_timestart

    json_from_period_start: str | Unset = UNSET
    if not isinstance(from_period_start, Unset):
        json_from_period_start = from_period_start.isoformat()
    params["fromPeriodStart"] = json_from_period_start

    json_to_period_start: str | Unset = UNSET
    if not isinstance(to_period_start, Unset):
        json_to_period_start = to_period_start.isoformat()
    params["toPeriodStart"] = json_to_period_start

    params["installation"] = installation

    params["measurementType"] = measurement_type

    params["meter"] = meter

    params["page"] = page

    params["pagesize"] = pagesize

    params["sortby"] = sortby

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/aggregationdayvalues",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponseAggregationDayValueOutputListModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseAggregationDayValueOutputListModel.from_dict(
            response.json()
        )

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
) -> Response[PaginatedResponseAggregationDayValueOutputListModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    measurement: str | Unset = UNSET,
    from_timestart: datetime.datetime | Unset = UNSET,
    to_timestart: datetime.datetime | Unset = UNSET,
    from_period_start: datetime.datetime | Unset = UNSET,
    to_period_start: datetime.datetime | Unset = UNSET,
    installation: str | Unset = UNSET,
    measurement_type: str | Unset = UNSET,
    meter: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseAggregationDayValueOutputListModel | RestErrorResponse]:
    """Retrieve all AggregationDayValue objects

    Args:
        measurement (str | Unset):
        from_timestart (datetime.datetime | Unset):
        to_timestart (datetime.datetime | Unset):
        from_period_start (datetime.datetime | Unset):
        to_period_start (datetime.datetime | Unset):
        installation (str | Unset):
        measurement_type (str | Unset):
        meter (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseAggregationDayValueOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        measurement=measurement,
        from_timestart=from_timestart,
        to_timestart=to_timestart,
        from_period_start=from_period_start,
        to_period_start=to_period_start,
        installation=installation,
        measurement_type=measurement_type,
        meter=meter,
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
    measurement: str | Unset = UNSET,
    from_timestart: datetime.datetime | Unset = UNSET,
    to_timestart: datetime.datetime | Unset = UNSET,
    from_period_start: datetime.datetime | Unset = UNSET,
    to_period_start: datetime.datetime | Unset = UNSET,
    installation: str | Unset = UNSET,
    measurement_type: str | Unset = UNSET,
    meter: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseAggregationDayValueOutputListModel | RestErrorResponse | None:
    """Retrieve all AggregationDayValue objects

    Args:
        measurement (str | Unset):
        from_timestart (datetime.datetime | Unset):
        to_timestart (datetime.datetime | Unset):
        from_period_start (datetime.datetime | Unset):
        to_period_start (datetime.datetime | Unset):
        installation (str | Unset):
        measurement_type (str | Unset):
        meter (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseAggregationDayValueOutputListModel | RestErrorResponse
    """

    return sync_detailed(
        client=client,
        measurement=measurement,
        from_timestart=from_timestart,
        to_timestart=to_timestart,
        from_period_start=from_period_start,
        to_period_start=to_period_start,
        installation=installation,
        measurement_type=measurement_type,
        meter=meter,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    measurement: str | Unset = UNSET,
    from_timestart: datetime.datetime | Unset = UNSET,
    to_timestart: datetime.datetime | Unset = UNSET,
    from_period_start: datetime.datetime | Unset = UNSET,
    to_period_start: datetime.datetime | Unset = UNSET,
    installation: str | Unset = UNSET,
    measurement_type: str | Unset = UNSET,
    meter: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseAggregationDayValueOutputListModel | RestErrorResponse]:
    """Retrieve all AggregationDayValue objects

    Args:
        measurement (str | Unset):
        from_timestart (datetime.datetime | Unset):
        to_timestart (datetime.datetime | Unset):
        from_period_start (datetime.datetime | Unset):
        to_period_start (datetime.datetime | Unset):
        installation (str | Unset):
        measurement_type (str | Unset):
        meter (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseAggregationDayValueOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        measurement=measurement,
        from_timestart=from_timestart,
        to_timestart=to_timestart,
        from_period_start=from_period_start,
        to_period_start=to_period_start,
        installation=installation,
        measurement_type=measurement_type,
        meter=meter,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    measurement: str | Unset = UNSET,
    from_timestart: datetime.datetime | Unset = UNSET,
    to_timestart: datetime.datetime | Unset = UNSET,
    from_period_start: datetime.datetime | Unset = UNSET,
    to_period_start: datetime.datetime | Unset = UNSET,
    installation: str | Unset = UNSET,
    measurement_type: str | Unset = UNSET,
    meter: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseAggregationDayValueOutputListModel | RestErrorResponse | None:
    """Retrieve all AggregationDayValue objects

    Args:
        measurement (str | Unset):
        from_timestart (datetime.datetime | Unset):
        to_timestart (datetime.datetime | Unset):
        from_period_start (datetime.datetime | Unset):
        to_period_start (datetime.datetime | Unset):
        installation (str | Unset):
        measurement_type (str | Unset):
        meter (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseAggregationDayValueOutputListModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            measurement=measurement,
            from_timestart=from_timestart,
            to_timestart=to_timestart,
            from_period_start=from_period_start,
            to_period_start=to_period_start,
            installation=installation,
            measurement_type=measurement_type,
            meter=meter,
            page=page,
            pagesize=pagesize,
            sortby=sortby,
        )
    ).parsed
