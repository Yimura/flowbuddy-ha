from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_response_measurement_value_output_list_model import (
    PaginatedResponseMeasurementValueOutputListModel,
)
from ...models.rest_error_response import RestErrorResponse
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    *,
    measurement: str | Unset = UNSET,
    from_created_on: datetime.datetime | Unset = UNSET,
    to_created_on: datetime.datetime | Unset = UNSET,
    from_timestart: datetime.datetime | Unset = UNSET,
    to_timestart: datetime.datetime | Unset = UNSET,
    installation: str | Unset = UNSET,
    meter: str | Unset = UNSET,
    measurement_type: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["measurement"] = measurement

    json_from_created_on: str | Unset = UNSET
    if not isinstance(from_created_on, Unset):
        json_from_created_on = from_created_on.isoformat()
    params["fromCreatedOn"] = json_from_created_on

    json_to_created_on: str | Unset = UNSET
    if not isinstance(to_created_on, Unset):
        json_to_created_on = to_created_on.isoformat()
    params["toCreatedOn"] = json_to_created_on

    json_from_timestart: str | Unset = UNSET
    if not isinstance(from_timestart, Unset):
        json_from_timestart = from_timestart.isoformat()
    params["fromTimestart"] = json_from_timestart

    json_to_timestart: str | Unset = UNSET
    if not isinstance(to_timestart, Unset):
        json_to_timestart = to_timestart.isoformat()
    params["toTimestart"] = json_to_timestart

    params["installation"] = installation

    params["meter"] = meter

    params["measurementType"] = measurement_type

    params["page"] = page

    params["pagesize"] = pagesize

    params["sortby"] = sortby

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/measurementvalues",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponseMeasurementValueOutputListModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseMeasurementValueOutputListModel.from_dict(response.json())

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
) -> Response[PaginatedResponseMeasurementValueOutputListModel | RestErrorResponse]:
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
    from_created_on: datetime.datetime | Unset = UNSET,
    to_created_on: datetime.datetime | Unset = UNSET,
    from_timestart: datetime.datetime | Unset = UNSET,
    to_timestart: datetime.datetime | Unset = UNSET,
    installation: str | Unset = UNSET,
    meter: str | Unset = UNSET,
    measurement_type: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseMeasurementValueOutputListModel | RestErrorResponse]:
    """Retrieve all MeasurementValue objects

    Args:
        measurement (str | Unset):
        from_created_on (datetime.datetime | Unset):
        to_created_on (datetime.datetime | Unset):
        from_timestart (datetime.datetime | Unset):
        to_timestart (datetime.datetime | Unset):
        installation (str | Unset):
        meter (str | Unset):
        measurement_type (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseMeasurementValueOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        measurement=measurement,
        from_created_on=from_created_on,
        to_created_on=to_created_on,
        from_timestart=from_timestart,
        to_timestart=to_timestart,
        installation=installation,
        meter=meter,
        measurement_type=measurement_type,
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
    from_created_on: datetime.datetime | Unset = UNSET,
    to_created_on: datetime.datetime | Unset = UNSET,
    from_timestart: datetime.datetime | Unset = UNSET,
    to_timestart: datetime.datetime | Unset = UNSET,
    installation: str | Unset = UNSET,
    meter: str | Unset = UNSET,
    measurement_type: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseMeasurementValueOutputListModel | RestErrorResponse | None:
    """Retrieve all MeasurementValue objects

    Args:
        measurement (str | Unset):
        from_created_on (datetime.datetime | Unset):
        to_created_on (datetime.datetime | Unset):
        from_timestart (datetime.datetime | Unset):
        to_timestart (datetime.datetime | Unset):
        installation (str | Unset):
        meter (str | Unset):
        measurement_type (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseMeasurementValueOutputListModel | RestErrorResponse
    """

    return sync_detailed(
        client=client,
        measurement=measurement,
        from_created_on=from_created_on,
        to_created_on=to_created_on,
        from_timestart=from_timestart,
        to_timestart=to_timestart,
        installation=installation,
        meter=meter,
        measurement_type=measurement_type,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    measurement: str | Unset = UNSET,
    from_created_on: datetime.datetime | Unset = UNSET,
    to_created_on: datetime.datetime | Unset = UNSET,
    from_timestart: datetime.datetime | Unset = UNSET,
    to_timestart: datetime.datetime | Unset = UNSET,
    installation: str | Unset = UNSET,
    meter: str | Unset = UNSET,
    measurement_type: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseMeasurementValueOutputListModel | RestErrorResponse]:
    """Retrieve all MeasurementValue objects

    Args:
        measurement (str | Unset):
        from_created_on (datetime.datetime | Unset):
        to_created_on (datetime.datetime | Unset):
        from_timestart (datetime.datetime | Unset):
        to_timestart (datetime.datetime | Unset):
        installation (str | Unset):
        meter (str | Unset):
        measurement_type (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseMeasurementValueOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        measurement=measurement,
        from_created_on=from_created_on,
        to_created_on=to_created_on,
        from_timestart=from_timestart,
        to_timestart=to_timestart,
        installation=installation,
        meter=meter,
        measurement_type=measurement_type,
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
    from_created_on: datetime.datetime | Unset = UNSET,
    to_created_on: datetime.datetime | Unset = UNSET,
    from_timestart: datetime.datetime | Unset = UNSET,
    to_timestart: datetime.datetime | Unset = UNSET,
    installation: str | Unset = UNSET,
    meter: str | Unset = UNSET,
    measurement_type: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseMeasurementValueOutputListModel | RestErrorResponse | None:
    """Retrieve all MeasurementValue objects

    Args:
        measurement (str | Unset):
        from_created_on (datetime.datetime | Unset):
        to_created_on (datetime.datetime | Unset):
        from_timestart (datetime.datetime | Unset):
        to_timestart (datetime.datetime | Unset):
        installation (str | Unset):
        meter (str | Unset):
        measurement_type (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseMeasurementValueOutputListModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            measurement=measurement,
            from_created_on=from_created_on,
            to_created_on=to_created_on,
            from_timestart=from_timestart,
            to_timestart=to_timestart,
            installation=installation,
            meter=meter,
            measurement_type=measurement_type,
            page=page,
            pagesize=pagesize,
            sortby=sortby,
        )
    ).parsed
