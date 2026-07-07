from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_error_response import RestErrorResponse
from ...models.send_ct_ratio_output_model import SendCtRatioOutputModel
from typing import cast


def _get_kwargs(
    send_ct_ratio_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sendctratios/{send_ct_ratio_id}".format(
            send_ct_ratio_id=quote(str(send_ct_ratio_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestErrorResponse | SendCtRatioOutputModel | None:
    if response.status_code == 200:
        response_200 = SendCtRatioOutputModel.from_dict(response.json())

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
) -> Response[RestErrorResponse | SendCtRatioOutputModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    send_ct_ratio_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestErrorResponse | SendCtRatioOutputModel]:
    """Retrieve a single SendCtRatio

    Args:
        send_ct_ratio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrorResponse | SendCtRatioOutputModel]
    """

    kwargs = _get_kwargs(
        send_ct_ratio_id=send_ct_ratio_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    send_ct_ratio_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestErrorResponse | SendCtRatioOutputModel | None:
    """Retrieve a single SendCtRatio

    Args:
        send_ct_ratio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrorResponse | SendCtRatioOutputModel
    """

    return sync_detailed(
        send_ct_ratio_id=send_ct_ratio_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    send_ct_ratio_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestErrorResponse | SendCtRatioOutputModel]:
    """Retrieve a single SendCtRatio

    Args:
        send_ct_ratio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrorResponse | SendCtRatioOutputModel]
    """

    kwargs = _get_kwargs(
        send_ct_ratio_id=send_ct_ratio_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    send_ct_ratio_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestErrorResponse | SendCtRatioOutputModel | None:
    """Retrieve a single SendCtRatio

    Args:
        send_ct_ratio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrorResponse | SendCtRatioOutputModel
    """

    return (
        await asyncio_detailed(
            send_ct_ratio_id=send_ct_ratio_id,
            client=client,
        )
    ).parsed
