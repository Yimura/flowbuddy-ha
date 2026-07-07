from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.notifier_template_output_model import NotifierTemplateOutputModel
from ...models.rest_error_response import RestErrorResponse
from typing import cast


def _get_kwargs(
    notifier_template_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/notifiertemplate/{notifier_template_id}".format(
            notifier_template_id=quote(str(notifier_template_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> NotifierTemplateOutputModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = NotifierTemplateOutputModel.from_dict(response.json())

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
) -> Response[NotifierTemplateOutputModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    notifier_template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[NotifierTemplateOutputModel | RestErrorResponse]:
    """Retrieve a single NotifierTemplate

    Args:
        notifier_template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotifierTemplateOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        notifier_template_id=notifier_template_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    notifier_template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> NotifierTemplateOutputModel | RestErrorResponse | None:
    """Retrieve a single NotifierTemplate

    Args:
        notifier_template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotifierTemplateOutputModel | RestErrorResponse
    """

    return sync_detailed(
        notifier_template_id=notifier_template_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    notifier_template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[NotifierTemplateOutputModel | RestErrorResponse]:
    """Retrieve a single NotifierTemplate

    Args:
        notifier_template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotifierTemplateOutputModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        notifier_template_id=notifier_template_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    notifier_template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> NotifierTemplateOutputModel | RestErrorResponse | None:
    """Retrieve a single NotifierTemplate

    Args:
        notifier_template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotifierTemplateOutputModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            notifier_template_id=notifier_template_id,
            client=client,
        )
    ).parsed
