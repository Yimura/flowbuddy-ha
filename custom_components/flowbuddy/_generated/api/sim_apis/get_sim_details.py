from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_error_response import RestErrorResponse
from ...models.sim_output_model import SimOutputModel
from typing import cast


def _get_kwargs(
    sim_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sims/{sim_id}".format(
            sim_id=quote(str(sim_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestErrorResponse | SimOutputModel | None:
    if response.status_code == 200:
        response_200 = SimOutputModel.from_dict(response.json())

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
) -> Response[RestErrorResponse | SimOutputModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sim_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestErrorResponse | SimOutputModel]:
    """Retrieve a single Sim

    Args:
        sim_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrorResponse | SimOutputModel]
    """

    kwargs = _get_kwargs(
        sim_id=sim_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sim_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestErrorResponse | SimOutputModel | None:
    """Retrieve a single Sim

    Args:
        sim_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrorResponse | SimOutputModel
    """

    return sync_detailed(
        sim_id=sim_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sim_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestErrorResponse | SimOutputModel]:
    """Retrieve a single Sim

    Args:
        sim_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrorResponse | SimOutputModel]
    """

    kwargs = _get_kwargs(
        sim_id=sim_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sim_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestErrorResponse | SimOutputModel | None:
    """Retrieve a single Sim

    Args:
        sim_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrorResponse | SimOutputModel
    """

    return (
        await asyncio_detailed(
            sim_id=sim_id,
            client=client,
        )
    ).parsed
