from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_response_measuring_device_output_list_model import (
    PaginatedResponseMeasuringDeviceOutputListModel,
)
from ...models.rest_error_response import RestErrorResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    is_communicator_device: str | Unset = UNSET,
    communicator: str | Unset = UNSET,
    communicator_any_of: str | Unset = UNSET,
    serial_number: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["isCommunicatorDevice"] = is_communicator_device

    params["communicator"] = communicator

    params["communicatorAnyOf"] = communicator_any_of

    params["serialNumber"] = serial_number

    params["page"] = page

    params["pagesize"] = pagesize

    params["sortby"] = sortby

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/measuringdevices",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponseMeasuringDeviceOutputListModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseMeasuringDeviceOutputListModel.from_dict(response.json())

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
) -> Response[PaginatedResponseMeasuringDeviceOutputListModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    is_communicator_device: str | Unset = UNSET,
    communicator: str | Unset = UNSET,
    communicator_any_of: str | Unset = UNSET,
    serial_number: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseMeasuringDeviceOutputListModel | RestErrorResponse]:
    """Retrieve all MeasuringDevice objects

    Args:
        is_communicator_device (str | Unset):
        communicator (str | Unset):
        communicator_any_of (str | Unset):
        serial_number (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseMeasuringDeviceOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        is_communicator_device=is_communicator_device,
        communicator=communicator,
        communicator_any_of=communicator_any_of,
        serial_number=serial_number,
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
    is_communicator_device: str | Unset = UNSET,
    communicator: str | Unset = UNSET,
    communicator_any_of: str | Unset = UNSET,
    serial_number: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseMeasuringDeviceOutputListModel | RestErrorResponse | None:
    """Retrieve all MeasuringDevice objects

    Args:
        is_communicator_device (str | Unset):
        communicator (str | Unset):
        communicator_any_of (str | Unset):
        serial_number (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseMeasuringDeviceOutputListModel | RestErrorResponse
    """

    return sync_detailed(
        client=client,
        is_communicator_device=is_communicator_device,
        communicator=communicator,
        communicator_any_of=communicator_any_of,
        serial_number=serial_number,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    is_communicator_device: str | Unset = UNSET,
    communicator: str | Unset = UNSET,
    communicator_any_of: str | Unset = UNSET,
    serial_number: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseMeasuringDeviceOutputListModel | RestErrorResponse]:
    """Retrieve all MeasuringDevice objects

    Args:
        is_communicator_device (str | Unset):
        communicator (str | Unset):
        communicator_any_of (str | Unset):
        serial_number (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseMeasuringDeviceOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        is_communicator_device=is_communicator_device,
        communicator=communicator,
        communicator_any_of=communicator_any_of,
        serial_number=serial_number,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    is_communicator_device: str | Unset = UNSET,
    communicator: str | Unset = UNSET,
    communicator_any_of: str | Unset = UNSET,
    serial_number: str | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseMeasuringDeviceOutputListModel | RestErrorResponse | None:
    """Retrieve all MeasuringDevice objects

    Args:
        is_communicator_device (str | Unset):
        communicator (str | Unset):
        communicator_any_of (str | Unset):
        serial_number (str | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseMeasuringDeviceOutputListModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            is_communicator_device=is_communicator_device,
            communicator=communicator,
            communicator_any_of=communicator_any_of,
            serial_number=serial_number,
            page=page,
            pagesize=pagesize,
            sortby=sortby,
        )
    ).parsed
