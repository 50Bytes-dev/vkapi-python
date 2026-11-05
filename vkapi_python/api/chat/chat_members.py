from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_members_response import ChatMembersResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    chat_id: int,
    offset: int | Unset = 0,
    count: int | Unset = 200,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["chatId"] = chat_id

    params["offset"] = offset

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chat/members",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChatMembersResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = ChatMembersResponse.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

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
) -> Response[ChatMembersResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    chat_id: int,
    offset: int | Unset = 0,
    count: int | Unset = 200,
) -> Response[ChatMembersResponse | ErrorResponse]:
    """A group chat's members, page by page

     The members of a group chat or channel of the page
    (`messages.getConversationMembers`): `count` from `offset` on, with
    `total` and `nextOffset`. When VK gives the whole list whatever
    `offset` and `count` (as it did for a small chat), the gateway cuts
    the page itself. One VK call. Within 8 s.

    Args:
        chat_id (int):  Example: 2000000001.
        offset (int | Unset):  Default: 0.
        count (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatMembersResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
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
    chat_id: int,
    offset: int | Unset = 0,
    count: int | Unset = 200,
) -> ChatMembersResponse | ErrorResponse | None:
    """A group chat's members, page by page

     The members of a group chat or channel of the page
    (`messages.getConversationMembers`): `count` from `offset` on, with
    `total` and `nextOffset`. When VK gives the whole list whatever
    `offset` and `count` (as it did for a small chat), the gateway cuts
    the page itself. One VK call. Within 8 s.

    Args:
        chat_id (int):  Example: 2000000001.
        offset (int | Unset):  Default: 0.
        count (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatMembersResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        chat_id=chat_id,
        offset=offset,
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    chat_id: int,
    offset: int | Unset = 0,
    count: int | Unset = 200,
) -> Response[ChatMembersResponse | ErrorResponse]:
    """A group chat's members, page by page

     The members of a group chat or channel of the page
    (`messages.getConversationMembers`): `count` from `offset` on, with
    `total` and `nextOffset`. When VK gives the whole list whatever
    `offset` and `count` (as it did for a small chat), the gateway cuts
    the page itself. One VK call. Within 8 s.

    Args:
        chat_id (int):  Example: 2000000001.
        offset (int | Unset):  Default: 0.
        count (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatMembersResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        offset=offset,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    chat_id: int,
    offset: int | Unset = 0,
    count: int | Unset = 200,
) -> ChatMembersResponse | ErrorResponse | None:
    """A group chat's members, page by page

     The members of a group chat or channel of the page
    (`messages.getConversationMembers`): `count` from `offset` on, with
    `total` and `nextOffset`. When VK gives the whole list whatever
    `offset` and `count` (as it did for a small chat), the gateway cuts
    the page itself. One VK call. Within 8 s.

    Args:
        chat_id (int):  Example: 2000000001.
        offset (int | Unset):  Default: 0.
        count (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatMembersResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            chat_id=chat_id,
            offset=offset,
            count=count,
        )
    ).parsed
