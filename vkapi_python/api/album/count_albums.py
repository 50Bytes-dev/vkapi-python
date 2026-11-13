from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_count_response import AlbumCountResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    owner_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ownerId"] = owner_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/album/count",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlbumCountResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AlbumCountResponse.from_dict(response.json())

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

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

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
) -> Response[AlbumCountResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    owner_id: int | Unset = UNSET,
) -> Response[AlbumCountResponse | ErrorResponse]:
    """How many albums the page, a community or a user has

     How many albums an owner has (`photos.getAlbumsCount`): the total
    `GET /album/list` does not give. VK counts no system album (the test page
    had 8, and 10 with `system`). 15, 200, 203 or 114 from VK is
    `album_refused` and pauses nothing. One VK call, within 8 s (2.3.0).

    Args:
        owner_id (int | Unset):  Example: -210132800.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumCountResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        owner_id=owner_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    owner_id: int | Unset = UNSET,
) -> AlbumCountResponse | ErrorResponse | None:
    """How many albums the page, a community or a user has

     How many albums an owner has (`photos.getAlbumsCount`): the total
    `GET /album/list` does not give. VK counts no system album (the test page
    had 8, and 10 with `system`). 15, 200, 203 or 114 from VK is
    `album_refused` and pauses nothing. One VK call, within 8 s (2.3.0).

    Args:
        owner_id (int | Unset):  Example: -210132800.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumCountResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        owner_id=owner_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    owner_id: int | Unset = UNSET,
) -> Response[AlbumCountResponse | ErrorResponse]:
    """How many albums the page, a community or a user has

     How many albums an owner has (`photos.getAlbumsCount`): the total
    `GET /album/list` does not give. VK counts no system album (the test page
    had 8, and 10 with `system`). 15, 200, 203 or 114 from VK is
    `album_refused` and pauses nothing. One VK call, within 8 s (2.3.0).

    Args:
        owner_id (int | Unset):  Example: -210132800.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumCountResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        owner_id=owner_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    owner_id: int | Unset = UNSET,
) -> AlbumCountResponse | ErrorResponse | None:
    """How many albums the page, a community or a user has

     How many albums an owner has (`photos.getAlbumsCount`): the total
    `GET /album/list` does not give. VK counts no system album (the test page
    had 8, and 10 with `system`). 15, 200, 203 or 114 from VK is
    `album_refused` and pauses nothing. One VK call, within 8 s (2.3.0).

    Args:
        owner_id (int | Unset):  Example: -210132800.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumCountResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            owner_id=owner_id,
        )
    ).parsed
