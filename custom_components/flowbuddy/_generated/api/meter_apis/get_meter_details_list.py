from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_response_meter_output_list_model import (
    PaginatedResponseMeterOutputListModel,
)
from ...models.rest_error_response import RestErrorResponse
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    *,
    name: str | Unset = UNSET,
    installation: str | Unset = UNSET,
    serial_number: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    from_first_registered_on: datetime.datetime | Unset = UNSET,
    to_first_registered_on: datetime.datetime | Unset = UNSET,
    from_registered_on: datetime.datetime | Unset = UNSET,
    to_registered_on: datetime.datetime | Unset = UNSET,
    last_polling_result: str | Unset = UNSET,
    from_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    to_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params["installation"] = installation

    params["serialNumber"] = serial_number

    params["type"] = type_

    params["status"] = status

    json_from_first_registered_on: str | Unset = UNSET
    if not isinstance(from_first_registered_on, Unset):
        json_from_first_registered_on = from_first_registered_on.isoformat()
    params["fromFirstRegisteredOn"] = json_from_first_registered_on

    json_to_first_registered_on: str | Unset = UNSET
    if not isinstance(to_first_registered_on, Unset):
        json_to_first_registered_on = to_first_registered_on.isoformat()
    params["toFirstRegisteredOn"] = json_to_first_registered_on

    json_from_registered_on: str | Unset = UNSET
    if not isinstance(from_registered_on, Unset):
        json_from_registered_on = from_registered_on.isoformat()
    params["fromRegisteredOn"] = json_from_registered_on

    json_to_registered_on: str | Unset = UNSET
    if not isinstance(to_registered_on, Unset):
        json_to_registered_on = to_registered_on.isoformat()
    params["toRegisteredOn"] = json_to_registered_on

    params["lastPollingResult"] = last_polling_result

    json_from_last_successful_polling_on: str | Unset = UNSET
    if not isinstance(from_last_successful_polling_on, Unset):
        json_from_last_successful_polling_on = from_last_successful_polling_on.isoformat()
    params["fromLastSuccessfulPollingOn"] = json_from_last_successful_polling_on

    json_to_last_successful_polling_on: str | Unset = UNSET
    if not isinstance(to_last_successful_polling_on, Unset):
        json_to_last_successful_polling_on = to_last_successful_polling_on.isoformat()
    params["toLastSuccessfulPollingOn"] = json_to_last_successful_polling_on

    params["page"] = page

    params["pagesize"] = pagesize

    params["sortby"] = sortby

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/meters",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponseMeterOutputListModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseMeterOutputListModel.from_dict(response.json())

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
) -> Response[PaginatedResponseMeterOutputListModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    installation: str | Unset = UNSET,
    serial_number: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    from_first_registered_on: datetime.datetime | Unset = UNSET,
    to_first_registered_on: datetime.datetime | Unset = UNSET,
    from_registered_on: datetime.datetime | Unset = UNSET,
    to_registered_on: datetime.datetime | Unset = UNSET,
    last_polling_result: str | Unset = UNSET,
    from_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    to_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseMeterOutputListModel | RestErrorResponse]:
    """Retrieve all Meter objects

    Args:
        name (str | Unset):
        installation (str | Unset):
        serial_number (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        from_first_registered_on (datetime.datetime | Unset):
        to_first_registered_on (datetime.datetime | Unset):
        from_registered_on (datetime.datetime | Unset):
        to_registered_on (datetime.datetime | Unset):
        last_polling_result (str | Unset):
        from_last_successful_polling_on (datetime.datetime | Unset):
        to_last_successful_polling_on (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseMeterOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        name=name,
        installation=installation,
        serial_number=serial_number,
        type_=type_,
        status=status,
        from_first_registered_on=from_first_registered_on,
        to_first_registered_on=to_first_registered_on,
        from_registered_on=from_registered_on,
        to_registered_on=to_registered_on,
        last_polling_result=last_polling_result,
        from_last_successful_polling_on=from_last_successful_polling_on,
        to_last_successful_polling_on=to_last_successful_polling_on,
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
    name: str | Unset = UNSET,
    installation: str | Unset = UNSET,
    serial_number: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    from_first_registered_on: datetime.datetime | Unset = UNSET,
    to_first_registered_on: datetime.datetime | Unset = UNSET,
    from_registered_on: datetime.datetime | Unset = UNSET,
    to_registered_on: datetime.datetime | Unset = UNSET,
    last_polling_result: str | Unset = UNSET,
    from_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    to_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseMeterOutputListModel | RestErrorResponse | None:
    """Retrieve all Meter objects

    Args:
        name (str | Unset):
        installation (str | Unset):
        serial_number (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        from_first_registered_on (datetime.datetime | Unset):
        to_first_registered_on (datetime.datetime | Unset):
        from_registered_on (datetime.datetime | Unset):
        to_registered_on (datetime.datetime | Unset):
        last_polling_result (str | Unset):
        from_last_successful_polling_on (datetime.datetime | Unset):
        to_last_successful_polling_on (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseMeterOutputListModel | RestErrorResponse
    """

    return sync_detailed(
        client=client,
        name=name,
        installation=installation,
        serial_number=serial_number,
        type_=type_,
        status=status,
        from_first_registered_on=from_first_registered_on,
        to_first_registered_on=to_first_registered_on,
        from_registered_on=from_registered_on,
        to_registered_on=to_registered_on,
        last_polling_result=last_polling_result,
        from_last_successful_polling_on=from_last_successful_polling_on,
        to_last_successful_polling_on=to_last_successful_polling_on,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    installation: str | Unset = UNSET,
    serial_number: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    from_first_registered_on: datetime.datetime | Unset = UNSET,
    to_first_registered_on: datetime.datetime | Unset = UNSET,
    from_registered_on: datetime.datetime | Unset = UNSET,
    to_registered_on: datetime.datetime | Unset = UNSET,
    last_polling_result: str | Unset = UNSET,
    from_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    to_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseMeterOutputListModel | RestErrorResponse]:
    """Retrieve all Meter objects

    Args:
        name (str | Unset):
        installation (str | Unset):
        serial_number (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        from_first_registered_on (datetime.datetime | Unset):
        to_first_registered_on (datetime.datetime | Unset):
        from_registered_on (datetime.datetime | Unset):
        to_registered_on (datetime.datetime | Unset):
        last_polling_result (str | Unset):
        from_last_successful_polling_on (datetime.datetime | Unset):
        to_last_successful_polling_on (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseMeterOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        name=name,
        installation=installation,
        serial_number=serial_number,
        type_=type_,
        status=status,
        from_first_registered_on=from_first_registered_on,
        to_first_registered_on=to_first_registered_on,
        from_registered_on=from_registered_on,
        to_registered_on=to_registered_on,
        last_polling_result=last_polling_result,
        from_last_successful_polling_on=from_last_successful_polling_on,
        to_last_successful_polling_on=to_last_successful_polling_on,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    installation: str | Unset = UNSET,
    serial_number: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    from_first_registered_on: datetime.datetime | Unset = UNSET,
    to_first_registered_on: datetime.datetime | Unset = UNSET,
    from_registered_on: datetime.datetime | Unset = UNSET,
    to_registered_on: datetime.datetime | Unset = UNSET,
    last_polling_result: str | Unset = UNSET,
    from_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    to_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseMeterOutputListModel | RestErrorResponse | None:
    """Retrieve all Meter objects

    Args:
        name (str | Unset):
        installation (str | Unset):
        serial_number (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        from_first_registered_on (datetime.datetime | Unset):
        to_first_registered_on (datetime.datetime | Unset):
        from_registered_on (datetime.datetime | Unset):
        to_registered_on (datetime.datetime | Unset):
        last_polling_result (str | Unset):
        from_last_successful_polling_on (datetime.datetime | Unset):
        to_last_successful_polling_on (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseMeterOutputListModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            installation=installation,
            serial_number=serial_number,
            type_=type_,
            status=status,
            from_first_registered_on=from_first_registered_on,
            to_first_registered_on=to_first_registered_on,
            from_registered_on=from_registered_on,
            to_registered_on=to_registered_on,
            last_polling_result=last_polling_result,
            from_last_successful_polling_on=from_last_successful_polling_on,
            to_last_successful_polling_on=to_last_successful_polling_on,
            page=page,
            pagesize=pagesize,
            sortby=sortby,
        )
    ).parsed
