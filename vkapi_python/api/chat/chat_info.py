from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_info_response import ChatInfoResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    chat_id: list[int],
    include: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_chat_id = chat_id

    params["chatId"] = json_chat_id

    json_include: list[str] | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chat/info",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChatInfoResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = ChatInfoResponse.from_dict(response.json())

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
) -> Response[ChatInfoResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    chat_id: list[int],
    include: list[str] | Unset = UNSET,
) -> Response[ChatInfoResponse | ErrorResponse]:
    """The conversations of given ids

     The rows of `GET /chat/list` for up to 100 `chatId`s, in the order asked
    (a repeat once), with one `messages.getConversationsById`. The ones VK
    does not give the page are listed in `missing`. `include` as in the
    list. Within 8 s, and 0.5 s more for each id with
    `include=participants`.

    Args:
        chat_id (list[int]):  Example: [2000000001, 1128917798].
        include (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatInfoResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    chat_id: list[int],
    include: list[str] | Unset = UNSET,
) -> ChatInfoResponse | ErrorResponse | None:
    """The conversations of given ids

     The rows of `GET /chat/list` for up to 100 `chatId`s, in the order asked
    (a repeat once), with one `messages.getConversationsById`. The ones VK
    does not give the page are listed in `missing`. `include` as in the
    list. Within 8 s, and 0.5 s more for each id with
    `include=participants`.

    Args:
        chat_id (list[int]):  Example: [2000000001, 1128917798].
        include (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatInfoResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        chat_id=chat_id,
        include=include,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    chat_id: list[int],
    include: list[str] | Unset = UNSET,
) -> Response[ChatInfoResponse | ErrorResponse]:
    """The conversations of given ids

     The rows of `GET /chat/list` for up to 100 `chatId`s, in the order asked
    (a repeat once), with one `messages.getConversationsById`. The ones VK
    does not give the page are listed in `missing`. `include` as in the
    list. Within 8 s, and 0.5 s more for each id with
    `include=participants`.

    Args:
        chat_id (list[int]):  Example: [2000000001, 1128917798].
        include (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatInfoResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    chat_id: list[int],
    include: list[str] | Unset = UNSET,
) -> ChatInfoResponse | ErrorResponse | None:
    """The conversations of given ids

     The rows of `GET /chat/list` for up to 100 `chatId`s, in the order asked
    (a repeat once), with one `messages.getConversationsById`. The ones VK
    does not give the page are listed in `missing`. `include` as in the
    list. Within 8 s, and 0.5 s more for each id with
    `include=participants`.

    Args:
        chat_id (list[int]):  Example: [2000000001, 1128917798].
        include (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatInfoResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            chat_id=chat_id,
            include=include,
        )
    ).parsed
