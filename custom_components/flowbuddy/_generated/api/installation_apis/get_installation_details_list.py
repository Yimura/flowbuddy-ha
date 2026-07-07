from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_response_installation_output_list_model import (
    PaginatedResponseInstallationOutputListModel,
)
from ...models.rest_error_response import RestErrorResponse
from ...types import UNSET, Unset
from typing import cast
import datetime


def _get_kwargs(
    *,
    alarm_status: str | Unset = UNSET,
    from_installation_date: datetime.datetime | Unset = UNSET,
    to_installation_date: datetime.datetime | Unset = UNSET,
    identification: str | Unset = UNSET,
    customer_name: str | Unset = UNSET,
    customer_id: str | Unset = UNSET,
    email_address: str | Unset = UNSET,
    street: str | Unset = UNSET,
    house_number: str | Unset = UNSET,
    zip_code: str | Unset = UNSET,
    city: str | Unset = UNSET,
    country: str | Unset = UNSET,
    resident: str | Unset = UNSET,
    project: str | Unset = UNSET,
    custom01: str | Unset = UNSET,
    custom02: str | Unset = UNSET,
    custom03: str | Unset = UNSET,
    custom04: str | Unset = UNSET,
    custom05: str | Unset = UNSET,
    full_text_search: str | Unset = UNSET,
    client_user_group: str | Unset = UNSET,
    is_resident_user_null: bool | Unset = UNSET,
    is_communicator_null: bool | Unset = UNSET,
    has_registered_meters: bool | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["alarmStatus"] = alarm_status

    json_from_installation_date: str | Unset = UNSET
    if not isinstance(from_installation_date, Unset):
        json_from_installation_date = from_installation_date.isoformat()
    params["fromInstallationDate"] = json_from_installation_date

    json_to_installation_date: str | Unset = UNSET
    if not isinstance(to_installation_date, Unset):
        json_to_installation_date = to_installation_date.isoformat()
    params["toInstallationDate"] = json_to_installation_date

    params["identification"] = identification

    params["customerName"] = customer_name

    params["customerId"] = customer_id

    params["emailAddress"] = email_address

    params["street"] = street

    params["houseNumber"] = house_number

    params["zipCode"] = zip_code

    params["city"] = city

    params["country"] = country

    params["resident"] = resident

    params["project"] = project

    params["custom01"] = custom01

    params["custom02"] = custom02

    params["custom03"] = custom03

    params["custom04"] = custom04

    params["custom05"] = custom05

    params["fullTextSearch"] = full_text_search

    params["clientUserGroup"] = client_user_group

    params["isResidentUserNull"] = is_resident_user_null

    params["isCommunicatorNull"] = is_communicator_null

    params["hasRegisteredMeters"] = has_registered_meters

    params["page"] = page

    params["pagesize"] = pagesize

    params["sortby"] = sortby

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/installations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponseInstallationOutputListModel | RestErrorResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseInstallationOutputListModel.from_dict(response.json())

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
) -> Response[PaginatedResponseInstallationOutputListModel | RestErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    alarm_status: str | Unset = UNSET,
    from_installation_date: datetime.datetime | Unset = UNSET,
    to_installation_date: datetime.datetime | Unset = UNSET,
    identification: str | Unset = UNSET,
    customer_name: str | Unset = UNSET,
    customer_id: str | Unset = UNSET,
    email_address: str | Unset = UNSET,
    street: str | Unset = UNSET,
    house_number: str | Unset = UNSET,
    zip_code: str | Unset = UNSET,
    city: str | Unset = UNSET,
    country: str | Unset = UNSET,
    resident: str | Unset = UNSET,
    project: str | Unset = UNSET,
    custom01: str | Unset = UNSET,
    custom02: str | Unset = UNSET,
    custom03: str | Unset = UNSET,
    custom04: str | Unset = UNSET,
    custom05: str | Unset = UNSET,
    full_text_search: str | Unset = UNSET,
    client_user_group: str | Unset = UNSET,
    is_resident_user_null: bool | Unset = UNSET,
    is_communicator_null: bool | Unset = UNSET,
    has_registered_meters: bool | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseInstallationOutputListModel | RestErrorResponse]:
    """Retrieve all Installation objects

    Args:
        alarm_status (str | Unset):
        from_installation_date (datetime.datetime | Unset):
        to_installation_date (datetime.datetime | Unset):
        identification (str | Unset):
        customer_name (str | Unset):
        customer_id (str | Unset):
        email_address (str | Unset):
        street (str | Unset):
        house_number (str | Unset):
        zip_code (str | Unset):
        city (str | Unset):
        country (str | Unset):
        resident (str | Unset):
        project (str | Unset):
        custom01 (str | Unset):
        custom02 (str | Unset):
        custom03 (str | Unset):
        custom04 (str | Unset):
        custom05 (str | Unset):
        full_text_search (str | Unset):
        client_user_group (str | Unset):
        is_resident_user_null (bool | Unset):
        is_communicator_null (bool | Unset):
        has_registered_meters (bool | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseInstallationOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        alarm_status=alarm_status,
        from_installation_date=from_installation_date,
        to_installation_date=to_installation_date,
        identification=identification,
        customer_name=customer_name,
        customer_id=customer_id,
        email_address=email_address,
        street=street,
        house_number=house_number,
        zip_code=zip_code,
        city=city,
        country=country,
        resident=resident,
        project=project,
        custom01=custom01,
        custom02=custom02,
        custom03=custom03,
        custom04=custom04,
        custom05=custom05,
        full_text_search=full_text_search,
        client_user_group=client_user_group,
        is_resident_user_null=is_resident_user_null,
        is_communicator_null=is_communicator_null,
        has_registered_meters=has_registered_meters,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    alarm_status: str | Unset = UNSET,
    from_installation_date: datetime.datetime | Unset = UNSET,
    to_installation_date: datetime.datetime | Unset = UNSET,
    identification: str | Unset = UNSET,
    customer_name: str | Unset = UNSET,
    customer_id: str | Unset = UNSET,
    email_address: str | Unset = UNSET,
    street: str | Unset = UNSET,
    house_number: str | Unset = UNSET,
    zip_code: str | Unset = UNSET,
    city: str | Unset = UNSET,
    country: str | Unset = UNSET,
    resident: str | Unset = UNSET,
    project: str | Unset = UNSET,
    custom01: str | Unset = UNSET,
    custom02: str | Unset = UNSET,
    custom03: str | Unset = UNSET,
    custom04: str | Unset = UNSET,
    custom05: str | Unset = UNSET,
    full_text_search: str | Unset = UNSET,
    client_user_group: str | Unset = UNSET,
    is_resident_user_null: bool | Unset = UNSET,
    is_communicator_null: bool | Unset = UNSET,
    has_registered_meters: bool | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseInstallationOutputListModel | RestErrorResponse | None:
    """Retrieve all Installation objects

    Args:
        alarm_status (str | Unset):
        from_installation_date (datetime.datetime | Unset):
        to_installation_date (datetime.datetime | Unset):
        identification (str | Unset):
        customer_name (str | Unset):
        customer_id (str | Unset):
        email_address (str | Unset):
        street (str | Unset):
        house_number (str | Unset):
        zip_code (str | Unset):
        city (str | Unset):
        country (str | Unset):
        resident (str | Unset):
        project (str | Unset):
        custom01 (str | Unset):
        custom02 (str | Unset):
        custom03 (str | Unset):
        custom04 (str | Unset):
        custom05 (str | Unset):
        full_text_search (str | Unset):
        client_user_group (str | Unset):
        is_resident_user_null (bool | Unset):
        is_communicator_null (bool | Unset):
        has_registered_meters (bool | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseInstallationOutputListModel | RestErrorResponse
    """

    return sync_detailed(
        client=client,
        alarm_status=alarm_status,
        from_installation_date=from_installation_date,
        to_installation_date=to_installation_date,
        identification=identification,
        customer_name=customer_name,
        customer_id=customer_id,
        email_address=email_address,
        street=street,
        house_number=house_number,
        zip_code=zip_code,
        city=city,
        country=country,
        resident=resident,
        project=project,
        custom01=custom01,
        custom02=custom02,
        custom03=custom03,
        custom04=custom04,
        custom05=custom05,
        full_text_search=full_text_search,
        client_user_group=client_user_group,
        is_resident_user_null=is_resident_user_null,
        is_communicator_null=is_communicator_null,
        has_registered_meters=has_registered_meters,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    alarm_status: str | Unset = UNSET,
    from_installation_date: datetime.datetime | Unset = UNSET,
    to_installation_date: datetime.datetime | Unset = UNSET,
    identification: str | Unset = UNSET,
    customer_name: str | Unset = UNSET,
    customer_id: str | Unset = UNSET,
    email_address: str | Unset = UNSET,
    street: str | Unset = UNSET,
    house_number: str | Unset = UNSET,
    zip_code: str | Unset = UNSET,
    city: str | Unset = UNSET,
    country: str | Unset = UNSET,
    resident: str | Unset = UNSET,
    project: str | Unset = UNSET,
    custom01: str | Unset = UNSET,
    custom02: str | Unset = UNSET,
    custom03: str | Unset = UNSET,
    custom04: str | Unset = UNSET,
    custom05: str | Unset = UNSET,
    full_text_search: str | Unset = UNSET,
    client_user_group: str | Unset = UNSET,
    is_resident_user_null: bool | Unset = UNSET,
    is_communicator_null: bool | Unset = UNSET,
    has_registered_meters: bool | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> Response[PaginatedResponseInstallationOutputListModel | RestErrorResponse]:
    """Retrieve all Installation objects

    Args:
        alarm_status (str | Unset):
        from_installation_date (datetime.datetime | Unset):
        to_installation_date (datetime.datetime | Unset):
        identification (str | Unset):
        customer_name (str | Unset):
        customer_id (str | Unset):
        email_address (str | Unset):
        street (str | Unset):
        house_number (str | Unset):
        zip_code (str | Unset):
        city (str | Unset):
        country (str | Unset):
        resident (str | Unset):
        project (str | Unset):
        custom01 (str | Unset):
        custom02 (str | Unset):
        custom03 (str | Unset):
        custom04 (str | Unset):
        custom05 (str | Unset):
        full_text_search (str | Unset):
        client_user_group (str | Unset):
        is_resident_user_null (bool | Unset):
        is_communicator_null (bool | Unset):
        has_registered_meters (bool | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseInstallationOutputListModel | RestErrorResponse]
    """

    kwargs = _get_kwargs(
        alarm_status=alarm_status,
        from_installation_date=from_installation_date,
        to_installation_date=to_installation_date,
        identification=identification,
        customer_name=customer_name,
        customer_id=customer_id,
        email_address=email_address,
        street=street,
        house_number=house_number,
        zip_code=zip_code,
        city=city,
        country=country,
        resident=resident,
        project=project,
        custom01=custom01,
        custom02=custom02,
        custom03=custom03,
        custom04=custom04,
        custom05=custom05,
        full_text_search=full_text_search,
        client_user_group=client_user_group,
        is_resident_user_null=is_resident_user_null,
        is_communicator_null=is_communicator_null,
        has_registered_meters=has_registered_meters,
        page=page,
        pagesize=pagesize,
        sortby=sortby,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    alarm_status: str | Unset = UNSET,
    from_installation_date: datetime.datetime | Unset = UNSET,
    to_installation_date: datetime.datetime | Unset = UNSET,
    identification: str | Unset = UNSET,
    customer_name: str | Unset = UNSET,
    customer_id: str | Unset = UNSET,
    email_address: str | Unset = UNSET,
    street: str | Unset = UNSET,
    house_number: str | Unset = UNSET,
    zip_code: str | Unset = UNSET,
    city: str | Unset = UNSET,
    country: str | Unset = UNSET,
    resident: str | Unset = UNSET,
    project: str | Unset = UNSET,
    custom01: str | Unset = UNSET,
    custom02: str | Unset = UNSET,
    custom03: str | Unset = UNSET,
    custom04: str | Unset = UNSET,
    custom05: str | Unset = UNSET,
    full_text_search: str | Unset = UNSET,
    client_user_group: str | Unset = UNSET,
    is_resident_user_null: bool | Unset = UNSET,
    is_communicator_null: bool | Unset = UNSET,
    has_registered_meters: bool | Unset = UNSET,
    page: int | Unset = 1,
    pagesize: int | Unset = 10,
    sortby: str | Unset = UNSET,
) -> PaginatedResponseInstallationOutputListModel | RestErrorResponse | None:
    """Retrieve all Installation objects

    Args:
        alarm_status (str | Unset):
        from_installation_date (datetime.datetime | Unset):
        to_installation_date (datetime.datetime | Unset):
        identification (str | Unset):
        customer_name (str | Unset):
        customer_id (str | Unset):
        email_address (str | Unset):
        street (str | Unset):
        house_number (str | Unset):
        zip_code (str | Unset):
        city (str | Unset):
        country (str | Unset):
        resident (str | Unset):
        project (str | Unset):
        custom01 (str | Unset):
        custom02 (str | Unset):
        custom03 (str | Unset):
        custom04 (str | Unset):
        custom05 (str | Unset):
        full_text_search (str | Unset):
        client_user_group (str | Unset):
        is_resident_user_null (bool | Unset):
        is_communicator_null (bool | Unset):
        has_registered_meters (bool | Unset):
        page (int | Unset):  Default: 1.
        pagesize (int | Unset):  Default: 10.
        sortby (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseInstallationOutputListModel | RestErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            alarm_status=alarm_status,
            from_installation_date=from_installation_date,
            to_installation_date=to_installation_date,
            identification=identification,
            customer_name=customer_name,
            customer_id=customer_id,
            email_address=email_address,
            street=street,
            house_number=house_number,
            zip_code=zip_code,
            city=city,
            country=country,
            resident=resident,
            project=project,
            custom01=custom01,
            custom02=custom02,
            custom03=custom03,
            custom04=custom04,
            custom05=custom05,
            full_text_search=full_text_search,
            client_user_group=client_user_group,
            is_resident_user_null=is_resident_user_null,
            is_communicator_null=is_communicator_null,
            has_registered_meters=has_registered_meters,
            page=page,
            pagesize=pagesize,
            sortby=sortby,
        )
    ).parsed
