from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.group_addresses_response import GroupAddressesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    group_id: int,
    address_ids: list[int] | Unset = UNSET,
    latitude: float | Unset = UNSET,
    longitude: float | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["groupId"] = group_id

    json_address_ids: list[int] | Unset = UNSET
    if not isinstance(address_ids, Unset):
        json_address_ids = address_ids

    params["addressIds"] = json_address_ids

    params["latitude"] = latitude

    params["longitude"] = longitude

    params["offset"] = offset

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/group/addresses",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GroupAddressesResponse | None:
    if response.status_code == 200:
        response_200 = GroupAddressesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | GroupAddressesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group_id: int,
    address_ids: list[int] | Unset = UNSET,
    latitude: float | Unset = UNSET,
    longitude: float | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = UNSET,
) -> Response[ErrorResponse | GroupAddressesResponse]:
    """The addresses of a community

     A page of a community's addresses (`groups.getAddresses`), as VK wrote
    them (with their timetables); any community's, not only one the page
    manages. With `latitude` and `longitude` VK sorts them by distance. One
    VK call, within 8 s (2.4.0).

    Args:
        group_id (int):  Example: -210132800.
        address_ids (list[int] | Unset):
        latitude (float | Unset):
        longitude (float | Unset):
        offset (int | Unset):  Default: 0.
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GroupAddressesResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        address_ids=address_ids,
        latitude=latitude,
        longitude=longitude,
        offset=offset,
        count=count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group_id: int,
    address_ids: list[int] | Unset = UNSET,
    latitude: float | Unset = UNSET,
    longitude: float | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = UNSET,
) -> ErrorResponse | GroupAddressesResponse | None:
    """The addresses of a community

     A page of a community's addresses (`groups.getAddresses`), as VK wrote
    them (with their timetables); any community's, not only one the page
    manages. With `latitude` and `longitude` VK sorts them by distance. One
    VK call, within 8 s (2.4.0).

    Args:
        group_id (int):  Example: -210132800.
        address_ids (list[int] | Unset):
        latitude (float | Unset):
        longitude (float | Unset):
        offset (int | Unset):  Default: 0.
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GroupAddressesResponse
    """

    return sync_detailed(
        client=client,
        group_id=group_id,
        address_ids=address_ids,
        latitude=latitude,
        longitude=longitude,
        offset=offset,
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group_id: int,
    address_ids: list[int] | Unset = UNSET,
    latitude: float | Unset = UNSET,
    longitude: float | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = UNSET,
) -> Response[ErrorResponse | GroupAddressesResponse]:
    """The addresses of a community

     A page of a community's addresses (`groups.getAddresses`), as VK wrote
    them (with their timetables); any community's, not only one the page
    manages. With `latitude` and `longitude` VK sorts them by distance. One
    VK call, within 8 s (2.4.0).

    Args:
        group_id (int):  Example: -210132800.
        address_ids (list[int] | Unset):
        latitude (float | Unset):
        longitude (float | Unset):
        offset (int | Unset):  Default: 0.
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GroupAddressesResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        address_ids=address_ids,
        latitude=latitude,
        longitude=longitude,
        offset=offset,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group_id: int,
    address_ids: list[int] | Unset = UNSET,
    latitude: float | Unset = UNSET,
    longitude: float | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = UNSET,
) -> ErrorResponse | GroupAddressesResponse | None:
    """The addresses of a community

     A page of a community's addresses (`groups.getAddresses`), as VK wrote
    them (with their timetables); any community's, not only one the page
    manages. With `latitude` and `longitude` VK sorts them by distance. One
    VK call, within 8 s (2.4.0).

    Args:
        group_id (int):  Example: -210132800.
        address_ids (list[int] | Unset):
        latitude (float | Unset):
        longitude (float | Unset):
        offset (int | Unset):  Default: 0.
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GroupAddressesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            group_id=group_id,
            address_ids=address_ids,
            latitude=latitude,
            longitude=longitude,
            offset=offset,
            count=count,
        )
    ).parsed
