from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ems_configuration_output_model import EmsConfigurationOutputModel
from ...models.rest_error_response import RestErrorResponse
from typing import cast


def _get_kwargs(
    ems_configuration_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/emsconfigurations/{ems_configuration_id}".format(
            ems_configuration_id=quote(str(ems_configuration_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmsConfigurationOutputModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = EmsConfigurationOutputModel.from_dict(response.json())

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
) -> Response[EmsConfigurationOutputModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ems_configuration_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[EmsConfigurationOutputModel | RestErrorResponse]:
    """Retrieve a single EmsConfiguration

    Args:
        ems_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmsConfigurationOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        ems_configuration_id=ems_configuration_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ems_configuration_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> EmsConfigurationOutputModel | RestErrorResponse | None:
    """Retrieve a single EmsConfiguration

    Args:
        ems_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmsConfigurationOutputModel | RestErrorResponse
    """

    return sync_detailed(
        ems_configuration_id=ems_configuration_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    ems_configuration_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[EmsConfigurationOutputModel | RestErrorResponse]:
    """Retrieve a single EmsConfiguration

    Args:
        ems_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmsConfigurationOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        ems_configuration_id=ems_configuration_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ems_configuration_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> EmsConfigurationOutputModel | RestErrorResponse | None:
    """Retrieve a single EmsConfiguration

    Args:
        ems_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmsConfigurationOutputModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            ems_configuration_id=ems_configuration_id,
            client=client,
        )
    ).parsed
