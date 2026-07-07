from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.measuring_device_output_model import MeasuringDeviceOutputModel
from ...models.rest_error_response import RestErrorResponse
from typing import cast


def _get_kwargs(
    measuring_device_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/measuringdevices/{measuring_device_id}".format(
            measuring_device_id=quote(str(measuring_device_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MeasuringDeviceOutputModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = MeasuringDeviceOutputModel.from_dict(response.json())

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
) -> Response[MeasuringDeviceOutputModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    measuring_device_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[MeasuringDeviceOutputModel | RestErrorResponse]:
    """Retrieve a single MeasuringDevice

    Args:
        measuring_device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MeasuringDeviceOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        measuring_device_id=measuring_device_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    measuring_device_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> MeasuringDeviceOutputModel | RestErrorResponse | None:
    """Retrieve a single MeasuringDevice

    Args:
        measuring_device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MeasuringDeviceOutputModel | RestErrorResponse
    """

    return sync_detailed(
        measuring_device_id=measuring_device_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    measuring_device_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[MeasuringDeviceOutputModel | RestErrorResponse]:
    """Retrieve a single MeasuringDevice

    Args:
        measuring_device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MeasuringDeviceOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        measuring_device_id=measuring_device_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    measuring_device_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> MeasuringDeviceOutputModel | RestErrorResponse | None:
    """Retrieve a single MeasuringDevice

    Args:
        measuring_device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MeasuringDeviceOutputModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            measuring_device_id=measuring_device_id,
            client=client,
        )
    ).parsed
