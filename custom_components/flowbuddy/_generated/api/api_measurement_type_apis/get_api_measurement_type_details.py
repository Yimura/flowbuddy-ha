from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_measurement_type_output_model import ApiMeasurementTypeOutputModel
from ...models.rest_error_response import RestErrorResponse
from typing import cast


def _get_kwargs(
    api_measurement_type_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/apimeasurementtypes/{api_measurement_type_id}".format(
            api_measurement_type_id=quote(str(api_measurement_type_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiMeasurementTypeOutputModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = ApiMeasurementTypeOutputModel.from_dict(response.json())

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
) -> Response[ApiMeasurementTypeOutputModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    api_measurement_type_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiMeasurementTypeOutputModel | RestErrorResponse]:
    """Retrieve a single ApiMeasurementType

    Args:
        api_measurement_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiMeasurementTypeOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        api_measurement_type_id=api_measurement_type_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    api_measurement_type_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ApiMeasurementTypeOutputModel | RestErrorResponse | None:
    """Retrieve a single ApiMeasurementType

    Args:
        api_measurement_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiMeasurementTypeOutputModel | RestErrorResponse
    """

    return sync_detailed(
        api_measurement_type_id=api_measurement_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    api_measurement_type_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiMeasurementTypeOutputModel | RestErrorResponse]:
    """Retrieve a single ApiMeasurementType

    Args:
        api_measurement_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiMeasurementTypeOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        api_measurement_type_id=api_measurement_type_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    api_measurement_type_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ApiMeasurementTypeOutputModel | RestErrorResponse | None:
    """Retrieve a single ApiMeasurementType

    Args:
        api_measurement_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiMeasurementTypeOutputModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            api_measurement_type_id=api_measurement_type_id,
            client=client,
        )
    ).parsed
