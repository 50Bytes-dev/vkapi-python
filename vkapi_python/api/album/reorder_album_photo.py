from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_photo_ref_response import AlbumPhotoRefResponse
from ...models.album_photo_reorder_body import AlbumPhotoReorderBody
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AlbumPhotoReorderBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/album/photo/reorder",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlbumPhotoRefResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AlbumPhotoRefResponse.from_dict(response.json())

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
) -> Response[AlbumPhotoRefResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AlbumPhotoReorderBody,
) -> Response[AlbumPhotoRefResponse | ErrorResponse]:
    """Move a photo among its album's photos

     Puts the photo right before (`before`) or right after (`after`) another
    photo of its album (`photos.reorderPhotos`; a community's too). With a
    photo of another album VK answers 1 and moves nothing (checked live): `200`
    does not tell that apart. One VK call, within 8 s (2.3.0).

    Args:
        body (AlbumPhotoReorderBody): The photo and exactly one of `before` and `after`, a photo
            of the same album.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumPhotoRefResponse | ErrorResponse]
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
    body: AlbumPhotoReorderBody,
) -> AlbumPhotoRefResponse | ErrorResponse | None:
    """Move a photo among its album's photos

     Puts the photo right before (`before`) or right after (`after`) another
    photo of its album (`photos.reorderPhotos`; a community's too). With a
    photo of another album VK answers 1 and moves nothing (checked live): `200`
    does not tell that apart. One VK call, within 8 s (2.3.0).

    Args:
        body (AlbumPhotoReorderBody): The photo and exactly one of `before` and `after`, a photo
            of the same album.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumPhotoRefResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AlbumPhotoReorderBody,
) -> Response[AlbumPhotoRefResponse | ErrorResponse]:
    """Move a photo among its album's photos

     Puts the photo right before (`before`) or right after (`after`) another
    photo of its album (`photos.reorderPhotos`; a community's too). With a
    photo of another album VK answers 1 and moves nothing (checked live): `200`
    does not tell that apart. One VK call, within 8 s (2.3.0).

    Args:
        body (AlbumPhotoReorderBody): The photo and exactly one of `before` and `after`, a photo
            of the same album.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumPhotoRefResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AlbumPhotoReorderBody,
) -> AlbumPhotoRefResponse | ErrorResponse | None:
    """Move a photo among its album's photos

     Puts the photo right before (`before`) or right after (`after`) another
    photo of its album (`photos.reorderPhotos`; a community's too). With a
    photo of another album VK answers 1 and moves nothing (checked live): `200`
    does not tell that apart. One VK call, within 8 s (2.3.0).

    Args:
        body (AlbumPhotoReorderBody): The photo and exactly one of `before` and `after`, a photo
            of the same album.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumPhotoRefResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
