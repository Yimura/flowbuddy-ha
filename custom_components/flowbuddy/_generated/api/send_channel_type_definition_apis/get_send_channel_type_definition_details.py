from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_error_response import RestErrorResponse
from ...models.send_channel_type_definition_output_model import SendChannelTypeDefinitionOutputModel
from typing import cast


def _get_kwargs(
    send_channel_type_definition_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sendchanneltypedefinitions/{send_channel_type_definition_id}".format(
            send_channel_type_definition_id=quote(str(send_channel_type_definition_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestErrorResponse | SendChannelTypeDefinitionOutputModel | None:
    if response.status_code == 200:
        response_200 = SendChannelTypeDefinitionOutputModel.from_dict(response.json())

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
) -> Response[RestErrorResponse | SendChannelTypeDefinitionOutputModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    send_channel_type_definition_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestErrorResponse | SendChannelTypeDefinitionOutputModel]:
    """Retrieve a single SendChannelTypeDefinition

    Args:
        send_channel_type_definition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrorResponse | SendChannelTypeDefinitionOutputModel]
    """

    kwargs = _get_kwargs(
        send_channel_type_definition_id=send_channel_type_definition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    send_channel_type_definition_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestErrorResponse | SendChannelTypeDefinitionOutputModel | None:
    """Retrieve a single SendChannelTypeDefinition

    Args:
        send_channel_type_definition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrorResponse | SendChannelTypeDefinitionOutputModel
    """

    return sync_detailed(
        send_channel_type_definition_id=send_channel_type_definition_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    send_channel_type_definition_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestErrorResponse | SendChannelTypeDefinitionOutputModel]:
    """Retrieve a single SendChannelTypeDefinition

    Args:
        send_channel_type_definition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrorResponse | SendChannelTypeDefinitionOutputModel]
    """

    kwargs = _get_kwargs(
        send_channel_type_definition_id=send_channel_type_definition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    send_channel_type_definition_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestErrorResponse | SendChannelTypeDefinitionOutputModel | None:
    """Retrieve a single SendChannelTypeDefinition

    Args:
        send_channel_type_definition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrorResponse | SendChannelTypeDefinitionOutputModel
    """

    return (
        await asyncio_detailed(
            send_channel_type_definition_id=send_channel_type_definition_id,
            client=client,
        )
    ).parsed
