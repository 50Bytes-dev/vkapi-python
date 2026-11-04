from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_list_response import ChatListResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = 0,
    count: int | Unset = 20,
    filter_: str | Unset = UNSET,
    start_message_id: int | Unset = UNSET,
    q: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["count"] = count

    params["filter"] = filter_

    params["startMessageId"] = start_message_id

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chat/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChatListResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = ChatListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

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
) -> Response[ChatListResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    count: int | Unset = 20,
    filter_: str | Unset = UNSET,
    start_message_id: int | Unset = UNSET,
    q: str | Unset = UNSET,
) -> Response[ChatListResponse | ErrorResponse]:
    """List or search the page's conversations

     The page's conversations as VK gives them, newest first: people,
    communities and group chats, each with the `chatId` a send takes. Without
    `q` it is a page of `messages.getConversations`; with `q`, VK's search by
    title or name (at most 255 found). One VK call, within 8 s. No message
    text is returned.

    Args:
        offset (int | Unset):  Default: 0.
        count (int | Unset):  Default: 20.
        filter_ (str | Unset):  Example: chats.
        start_message_id (int | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatListResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        offset=offset,
        count=count,
        filter_=filter_,
        start_message_id=start_message_id,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    count: int | Unset = 20,
    filter_: str | Unset = UNSET,
    start_message_id: int | Unset = UNSET,
    q: str | Unset = UNSET,
) -> ChatListResponse | ErrorResponse | None:
    """List or search the page's conversations

     The page's conversations as VK gives them, newest first: people,
    communities and group chats, each with the `chatId` a send takes. Without
    `q` it is a page of `messages.getConversations`; with `q`, VK's search by
    title or name (at most 255 found). One VK call, within 8 s. No message
    text is returned.

    Args:
        offset (int | Unset):  Default: 0.
        count (int | Unset):  Default: 20.
        filter_ (str | Unset):  Example: chats.
        start_message_id (int | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatListResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        offset=offset,
        count=count,
        filter_=filter_,
        start_message_id=start_message_id,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    count: int | Unset = 20,
    filter_: str | Unset = UNSET,
    start_message_id: int | Unset = UNSET,
    q: str | Unset = UNSET,
) -> Response[ChatListResponse | ErrorResponse]:
    """List or search the page's conversations

     The page's conversations as VK gives them, newest first: people,
    communities and group chats, each with the `chatId` a send takes. Without
    `q` it is a page of `messages.getConversations`; with `q`, VK's search by
    title or name (at most 255 found). One VK call, within 8 s. No message
    text is returned.

    Args:
        offset (int | Unset):  Default: 0.
        count (int | Unset):  Default: 20.
        filter_ (str | Unset):  Example: chats.
        start_message_id (int | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatListResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        offset=offset,
        count=count,
        filter_=filter_,
        start_message_id=start_message_id,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    count: int | Unset = 20,
    filter_: str | Unset = UNSET,
    start_message_id: int | Unset = UNSET,
    q: str | Unset = UNSET,
) -> ChatListResponse | ErrorResponse | None:
    """List or search the page's conversations

     The page's conversations as VK gives them, newest first: people,
    communities and group chats, each with the `chatId` a send takes. Without
    `q` it is a page of `messages.getConversations`; with `q`, VK's search by
    title or name (at most 255 found). One VK call, within 8 s. No message
    text is returned.

    Args:
        offset (int | Unset):  Default: 0.
        count (int | Unset):  Default: 20.
        filter_ (str | Unset):  Example: chats.
        start_message_id (int | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatListResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            count=count,
            filter_=filter_,
            start_message_id=start_message_id,
            q=q,
        )
    ).parsed
