from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_ref_response import AlbumRefResponse
from ...models.album_reorder_body import AlbumReorderBody
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AlbumReorderBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/album/reorder",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlbumRefResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AlbumRefResponse.from_dict(response.json())

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
) -> Response[AlbumRefResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AlbumReorderBody,
) -> Response[AlbumRefResponse | ErrorResponse]:
    """Move an album among its owner's albums

     Puts the album right before (`before`) or right after (`after`) another
    album of the same owner, in the order of `GET /album/list`
    (`photos.reorderAlbums`; a community's too). One VK call, within 8 s
    (2.3.0).

    Args:
        body (AlbumReorderBody): The album and exactly one of `before` and `after`, an album of
            the same owner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumRefResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: AlbumReorderBody,
) -> AlbumRefResponse | ErrorResponse | None:
    """Move an album among its owner's albums

     Puts the album right before (`before`) or right after (`after`) another
    album of the same owner, in the order of `GET /album/list`
    (`photos.reorderAlbums`; a community's too). One VK call, within 8 s
    (2.3.0).

    Args:
        body (AlbumReorderBody): The album and exactly one of `before` and `after`, an album of
            the same owner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumRefResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AlbumReorderBody,
) -> Response[AlbumRefResponse | ErrorResponse]:
    """Move an album among its owner's albums

     Puts the album right before (`before`) or right after (`after`) another
    album of the same owner, in the order of `GET /album/list`
    (`photos.reorderAlbums`; a community's too). One VK call, within 8 s
    (2.3.0).

    Args:
        body (AlbumReorderBody): The album and exactly one of `before` and `after`, an album of
            the same owner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumRefResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AlbumReorderBody,
) -> AlbumRefResponse | ErrorResponse | None:
    """Move an album among its owner's albums

     Puts the album right before (`before`) or right after (`after`) another
    album of the same owner, in the order of `GET /album/list`
    (`photos.reorderAlbums`; a community's too). One VK call, within 8 s
    (2.3.0).

    Args:
        body (AlbumReorderBody): The album and exactly one of `before` and `after`, an album of
            the same owner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumRefResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
