from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.group_list_response import GroupListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: int | Unset = UNSET,
    filter_: list[str] | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = 1000,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["userId"] = user_id

    json_filter_: list[str] | Unset = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_

    params["filter"] = json_filter_

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params["offset"] = offset

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/group/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GroupListResponse | None:
    if response.status_code == 200:
        response_200 = GroupListResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | GroupListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_id: int | Unset = UNSET,
    filter_: list[str] | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = 1000,
) -> Response[ErrorResponse | GroupListResponse]:
    """The communities of the page or of another user

     The communities of a user (`groups.get`, extended), the page's when
    `userId` is left out, each with the gateway's fields and VK's object as
    VK wrote it (`vk`). VK unites the filters it is given (a community of
    any of them), and gives nothing for a filter it does not know: the
    gateway refuses one before VK. The role filters (`admin`, `editor`,
    `moder`, `advertiser`) are the page's own: with another user's
    `userId` they answer `400` before VK. VK's `total` counts the banned
    communities it leaves out of the page, so `nextOffset` is `offset` +
    `count` asked, not + what came. 15, 203, 260, 125, 30 or 18 from VK is
    `group_refused` and pauses nothing. One VK call, within 8 s, plus 50 ms
    for each of `count` when `fields` is given (2.4.0).

    Args:
        user_id (int | Unset):  Example: 1127016903.
        filter_ (list[str] | Unset):  Example: ['admin'].
        fields (list[str] | Unset):  Example: ['members_count', 'description'].
        offset (int | Unset):  Default: 0.
        count (int | Unset):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GroupListResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        filter_=filter_,
        fields=fields,
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
    user_id: int | Unset = UNSET,
    filter_: list[str] | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = 1000,
) -> ErrorResponse | GroupListResponse | None:
    """The communities of the page or of another user

     The communities of a user (`groups.get`, extended), the page's when
    `userId` is left out, each with the gateway's fields and VK's object as
    VK wrote it (`vk`). VK unites the filters it is given (a community of
    any of them), and gives nothing for a filter it does not know: the
    gateway refuses one before VK. The role filters (`admin`, `editor`,
    `moder`, `advertiser`) are the page's own: with another user's
    `userId` they answer `400` before VK. VK's `total` counts the banned
    communities it leaves out of the page, so `nextOffset` is `offset` +
    `count` asked, not + what came. 15, 203, 260, 125, 30 or 18 from VK is
    `group_refused` and pauses nothing. One VK call, within 8 s, plus 50 ms
    for each of `count` when `fields` is given (2.4.0).

    Args:
        user_id (int | Unset):  Example: 1127016903.
        filter_ (list[str] | Unset):  Example: ['admin'].
        fields (list[str] | Unset):  Example: ['members_count', 'description'].
        offset (int | Unset):  Default: 0.
        count (int | Unset):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GroupListResponse
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        filter_=filter_,
        fields=fields,
        offset=offset,
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: int | Unset = UNSET,
    filter_: list[str] | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = 1000,
) -> Response[ErrorResponse | GroupListResponse]:
    """The communities of the page or of another user

     The communities of a user (`groups.get`, extended), the page's when
    `userId` is left out, each with the gateway's fields and VK's object as
    VK wrote it (`vk`). VK unites the filters it is given (a community of
    any of them), and gives nothing for a filter it does not know: the
    gateway refuses one before VK. The role filters (`admin`, `editor`,
    `moder`, `advertiser`) are the page's own: with another user's
    `userId` they answer `400` before VK. VK's `total` counts the banned
    communities it leaves out of the page, so `nextOffset` is `offset` +
    `count` asked, not + what came. 15, 203, 260, 125, 30 or 18 from VK is
    `group_refused` and pauses nothing. One VK call, within 8 s, plus 50 ms
    for each of `count` when `fields` is given (2.4.0).

    Args:
        user_id (int | Unset):  Example: 1127016903.
        filter_ (list[str] | Unset):  Example: ['admin'].
        fields (list[str] | Unset):  Example: ['members_count', 'description'].
        offset (int | Unset):  Default: 0.
        count (int | Unset):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GroupListResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        filter_=filter_,
        fields=fields,
        offset=offset,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: int | Unset = UNSET,
    filter_: list[str] | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = 1000,
) -> ErrorResponse | GroupListResponse | None:
    """The communities of the page or of another user

     The communities of a user (`groups.get`, extended), the page's when
    `userId` is left out, each with the gateway's fields and VK's object as
    VK wrote it (`vk`). VK unites the filters it is given (a community of
    any of them), and gives nothing for a filter it does not know: the
    gateway refuses one before VK. The role filters (`admin`, `editor`,
    `moder`, `advertiser`) are the page's own: with another user's
    `userId` they answer `400` before VK. VK's `total` counts the banned
    communities it leaves out of the page, so `nextOffset` is `offset` +
    `count` asked, not + what came. 15, 203, 260, 125, 30 or 18 from VK is
    `group_refused` and pauses nothing. One VK call, within 8 s, plus 50 ms
    for each of `count` when `fields` is given (2.4.0).

    Args:
        user_id (int | Unset):  Example: 1127016903.
        filter_ (list[str] | Unset):  Example: ['admin'].
        fields (list[str] | Unset):  Example: ['members_count', 'description'].
        offset (int | Unset):  Default: 0.
        count (int | Unset):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GroupListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            filter_=filter_,
            fields=fields,
            offset=offset,
            count=count,
        )
    ).parsed
