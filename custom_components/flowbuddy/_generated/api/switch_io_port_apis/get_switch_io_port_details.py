from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_error_response import RestErrorResponse
from ...models.switch_io_port_output_model import SwitchIoPortOutputModel
from typing import cast


def _get_kwargs(
    switch_io_port_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/switchioports/{switch_io_port_id}".format(
            switch_io_port_id=quote(str(switch_io_port_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestErrorResponse | SwitchIoPortOutputModel | None:
    if response.status_code == 200:
        response_200 = SwitchIoPortOutputModel.from_dict(response.json())

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
) -> Response[RestErrorResponse | SwitchIoPortOutputModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    switch_io_port_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestErrorResponse | SwitchIoPortOutputModel]:
    """Retrieve a single SwitchIoPort

    Args:
        switch_io_port_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrorResponse | SwitchIoPortOutputModel]
    """

    kwargs = _get_kwargs(
        switch_io_port_id=switch_io_port_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    switch_io_port_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestErrorResponse | SwitchIoPortOutputModel | None:
    """Retrieve a single SwitchIoPort

    Args:
        switch_io_port_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrorResponse | SwitchIoPortOutputModel
    """

    return sync_detailed(
        switch_io_port_id=switch_io_port_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    switch_io_port_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestErrorResponse | SwitchIoPortOutputModel]:
    """Retrieve a single SwitchIoPort

    Args:
        switch_io_port_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrorResponse | SwitchIoPortOutputModel]
    """

    kwargs = _get_kwargs(
        switch_io_port_id=switch_io_port_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    switch_io_port_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestErrorResponse | SwitchIoPortOutputModel | None:
    """Retrieve a single SwitchIoPort

    Args:
        switch_io_port_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrorResponse | SwitchIoPortOutputModel
    """

    return (
        await asyncio_detailed(
            switch_io_port_id=switch_io_port_id,
            client=client,
        )
    ).parsed
