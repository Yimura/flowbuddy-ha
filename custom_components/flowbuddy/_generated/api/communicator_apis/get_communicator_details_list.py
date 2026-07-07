from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_response_communicator_output_list_model import (
    PaginatedResponseCommunicatorOutputListModel,
)
from ...models.rest_error_response import RestErrorResponse
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    *,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    notstatus: str | Unset = UNSET,
    logical_device_name: str | Unset = UNSET,
    from_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    to_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    last_polling_result: str | Unset = UNSET,
    last_successful_communication_on: datetime.datetime | Unset = UNSET,
    is_ems: bool | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["type"] = type_

    params["status"] = status

    params["notstatus"] = notstatus

    params["logicalDeviceName"] = logical_device_name

    json_from_last_successful_polling_on: str | Unset = UNSET
    if not isinstance(from_last_successful_polling_on, Unset):
        json_from_last_successful_polling_on = from_last_successful_polling_on.isoformat()
    params["fromLastSuccessfulPollingOn"] = json_from_last_successful_polling_on

    json_to_last_successful_polling_on: str | Unset = UNSET
    if not isinstance(to_last_successful_polling_on, Unset):
        json_to_last_successful_polling_on = to_last_successful_polling_on.isoformat()
    params["toLastSuccessfulPollingOn"] = json_to_last_successful_polling_on

    params["lastPollingResult"] = last_polling_result

    json_last_successful_communication_on: str | Unset = UNSET
    if not isinstance(last_successful_communication_on, Unset):
        json_last_successful_communication_on = last_successful_communication_on.isoformat()
    params["lastSuccessfulCommunicationOn"] = json_last_successful_communication_on

    params["isEms"] = is_ems

    params["page"] = page

    params["pagesize"] = pagesize

    params["sortby"] = sortby

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/communicators",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponseCommunicatorOutputListModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseCommunicatorOutputListModel.from_dict(response.json())

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
) -> Response[PaginatedResponseCommunicatorOutputListModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    notstatus: str | Unset = UNSET,
    logical_device_name: str | Unset = UNSET,
    from_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    to_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    last_polling_result: str | Unset = UNSET,
    last_successful_communication_on: datetime.datetime | Unset = UNSET,
    is_ems: bool | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseCommunicatorOutputListModel | RestErrorResponse]:
    """Retrieve all Communicator objects

    Args:
        type_ (str | Unset):
        status (str | Unset):
        notstatus (str | Unset):
        logical_device_name (str | Unset):
        from_last_successful_polling_on (datetime.datetime | Unset):
        to_last_successful_polling_on (datetime.datetime | Unset):
        last_polling_result (str | Unset):
        last_successful_communication_on (datetime.datetime | Unset):
        is_ems (bool | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseCommunicatorOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        status=status,
        notstatus=notstatus,
        logical_device_name=logical_device_name,
        from_last_successful_polling_on=from_last_successful_polling_on,
        to_last_successful_polling_on=to_last_successful_polling_on,
        last_polling_result=last_polling_result,
        last_successful_communication_on=last_successful_communication_on,
        is_ems=is_ems,
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
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    notstatus: str | Unset = UNSET,
    logical_device_name: str | Unset = UNSET,
    from_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    to_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    last_polling_result: str | Unset = UNSET,
    last_successful_communication_on: datetime.datetime | Unset = UNSET,
    is_ems: bool | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseCommunicatorOutputListModel | RestErrorResponse | None:
    """Retrieve all Communicator objects

    Args:
        type_ (str | Unset):
        status (str | Unset):
        notstatus (str | Unset):
        logical_device_name (str | Unset):
        from_last_successful_polling_on (datetime.datetime | Unset):
        to_last_successful_polling_on (datetime.datetime | Unset):
        last_polling_result (str | Unset):
        last_successful_communication_on (datetime.datetime | Unset):
        is_ems (bool | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseCommunicatorOutputListModel | RestErrorResponse
    """

    return sync_detailed(
        client=client,
        type_=type_,
        status=status,
        notstatus=notstatus,
        logical_device_name=logical_device_name,
        from_last_successful_polling_on=from_last_successful_polling_on,
        to_last_successful_polling_on=to_last_successful_polling_on,
        last_polling_result=last_polling_result,
        last_successful_communication_on=last_successful_communication_on,
        is_ems=is_ems,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    notstatus: str | Unset = UNSET,
    logical_device_name: str | Unset = UNSET,
    from_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    to_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    last_polling_result: str | Unset = UNSET,
    last_successful_communication_on: datetime.datetime | Unset = UNSET,
    is_ems: bool | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseCommunicatorOutputListModel | RestErrorResponse]:
    """Retrieve all Communicator objects

    Args:
        type_ (str | Unset):
        status (str | Unset):
        notstatus (str | Unset):
        logical_device_name (str | Unset):
        from_last_successful_polling_on (datetime.datetime | Unset):
        to_last_successful_polling_on (datetime.datetime | Unset):
        last_polling_result (str | Unset):
        last_successful_communication_on (datetime.datetime | Unset):
        is_ems (bool | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseCommunicatorOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        status=status,
        notstatus=notstatus,
        logical_device_name=logical_device_name,
        from_last_successful_polling_on=from_last_successful_polling_on,
        to_last_successful_polling_on=to_last_successful_polling_on,
        last_polling_result=last_polling_result,
        last_successful_communication_on=last_successful_communication_on,
        is_ems=is_ems,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    notstatus: str | Unset = UNSET,
    logical_device_name: str | Unset = UNSET,
    from_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    to_last_successful_polling_on: datetime.datetime | Unset = UNSET,
    last_polling_result: str | Unset = UNSET,
    last_successful_communication_on: datetime.datetime | Unset = UNSET,
    is_ems: bool | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseCommunicatorOutputListModel | RestErrorResponse | None:
    """Retrieve all Communicator objects

    Args:
        type_ (str | Unset):
        status (str | Unset):
        notstatus (str | Unset):
        logical_device_name (str | Unset):
        from_last_successful_polling_on (datetime.datetime | Unset):
        to_last_successful_polling_on (datetime.datetime | Unset):
        last_polling_result (str | Unset):
        last_successful_communication_on (datetime.datetime | Unset):
        is_ems (bool | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseCommunicatorOutputListModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            status=status,
            notstatus=notstatus,
            logical_device_name=logical_device_name,
            from_last_successful_polling_on=from_last_successful_polling_on,
            to_last_successful_polling_on=to_last_successful_polling_on,
            last_polling_result=last_polling_result,
            last_successful_communication_on=last_successful_communication_on,
            is_ems=is_ems,
            page=page,
            pagesize=pagesize,
            sortby=sortby,
        )
    ).parsed
