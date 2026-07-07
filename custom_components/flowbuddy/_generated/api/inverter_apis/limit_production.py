from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.inverter_limit_production_post_input_model import (
    InverterLimitProductionPostInputModel,
)
from ...models.rest_error_response import RestErrorResponse
from typing import cast


def _get_kwargs(
    inverter_id: str,
    *,
    body: InverterLimitProductionPostInputModel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/inverters/{inverter_id}/limitProduction".format(
            inverter_id=quote(str(inverter_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RestErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    inverter_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InverterLimitProductionPostInputModel,
) -> Response[Any | RestErrorResponse]:
    """Executing the command limitProduction

    Args:
        inverter_id (str):
        body (InverterLimitProductionPostInputModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        inverter_id=inverter_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    inverter_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InverterLimitProductionPostInputModel,
) -> Any | RestErrorResponse | None:
    """Executing the command limitProduction

    Args:
        inverter_id (str):
        body (InverterLimitProductionPostInputModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RestErrorResponse
    """

    return sync_detailed(
        inverter_id=inverter_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    inverter_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InverterLimitProductionPostInputModel,
) -> Response[Any | RestErrorResponse]:
    """Executing the command limitProduction

    Args:
        inverter_id (str):
        body (InverterLimitProductionPostInputModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        inverter_id=inverter_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    inverter_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InverterLimitProductionPostInputModel,
) -> Any | RestErrorResponse | None:
    """Executing the command limitProduction

    Args:
        inverter_id (str):
        body (InverterLimitProductionPostInputModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            inverter_id=inverter_id,
            client=client,
            body=body,
        )
    ).parsed
