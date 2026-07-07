from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.control_type_by_meter_output_list_model import ControlTypeByMeterOutputListModel
from ...models.rest_error_response import RestErrorResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    meter: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["meter"] = meter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/controltypes/byMeter",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ControlTypeByMeterOutputListModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = ControlTypeByMeterOutputListModel.from_dict(response.json())

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
) -> Response[ControlTypeByMeterOutputListModel | RestErrorResponse]:
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
) -> Response[ControlTypeByMeterOutputListModel | RestErrorResponse]:
    """Retrieve ControlTypes for a meter

    Args:
        meter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ControlTypeByMeterOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        meter=meter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    meter: str | Unset = UNSET,
) -> ControlTypeByMeterOutputListModel | RestErrorResponse | None:
    """Retrieve ControlTypes for a meter

    Args:
        meter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ControlTypeByMeterOutputListModel | RestErrorResponse
    """

    return sync_detailed(
        client=client,
        meter=meter,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    meter: str | Unset = UNSET,
) -> Response[ControlTypeByMeterOutputListModel | RestErrorResponse]:
    """Retrieve ControlTypes for a meter

    Args:
        meter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ControlTypeByMeterOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        meter=meter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    meter: str | Unset = UNSET,
) -> ControlTypeByMeterOutputListModel | RestErrorResponse | None:
    """Retrieve ControlTypes for a meter

    Args:
        meter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ControlTypeByMeterOutputListModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            meter=meter,
        )
    ).parsed
