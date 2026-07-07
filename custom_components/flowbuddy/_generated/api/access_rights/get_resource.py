from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.access_right_output_model import AccessRightOutputModel
from ...models.rest_error_response import RestErrorResponse
from typing import cast


def _get_kwargs(
    access_right: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/security/accessrights/{access_right}".format(
            access_right=quote(str(access_right), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccessRightOutputModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = AccessRightOutputModel.from_dict(response.json())

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
) -> Response[AccessRightOutputModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    access_right: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AccessRightOutputModel | RestErrorResponse]:
    """Check if the user or session has an access right

    Args:
        access_right (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccessRightOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        access_right=access_right,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    access_right: str,
    *,
    client: AuthenticatedClient | Client,
) -> AccessRightOutputModel | RestErrorResponse | None:
    """Check if the user or session has an access right

    Args:
        access_right (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccessRightOutputModel | RestErrorResponse
    """

    return sync_detailed(
        access_right=access_right,
        client=client,
    ).parsed


async def asyncio_detailed(
    access_right: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AccessRightOutputModel | RestErrorResponse]:
    """Check if the user or session has an access right

    Args:
        access_right (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccessRightOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        access_right=access_right,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    access_right: str,
    *,
    client: AuthenticatedClient | Client,
) -> AccessRightOutputModel | RestErrorResponse | None:
    """Check if the user or session has an access right

    Args:
        access_right (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccessRightOutputModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            access_right=access_right,
            client=client,
        )
    ).parsed
