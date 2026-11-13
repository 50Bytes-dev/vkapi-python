from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_photos_response import AlbumPhotosResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    album: str | Unset = UNSET,
    owner_id: int | Unset = UNSET,
    photos: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = UNSET,
    rev: bool | Unset = False,
    extended: bool | Unset = False,
    no_system: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["album"] = album

    params["ownerId"] = owner_id

    json_photos: list[str] | Unset = UNSET
    if not isinstance(photos, Unset):
        json_photos = photos

    params["photos"] = json_photos

    params["offset"] = offset

    params["count"] = count

    params["rev"] = rev

    params["extended"] = extended

    params["noSystem"] = no_system

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/album/photos",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlbumPhotosResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AlbumPhotosResponse.from_dict(response.json())

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
) -> Response[AlbumPhotosResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    album: str | Unset = UNSET,
    owner_id: int | Unset = UNSET,
    photos: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = UNSET,
    rev: bool | Unset = False,
    extended: bool | Unset = False,
    no_system: bool | Unset = False,
) -> Response[AlbumPhotosResponse | ErrorResponse]:
    """The photos of an album, of an owner, or by id

     Exactly one of `album` (its photos, `photos.get`; `total` is the
    album's), `ownerId` (every photo of the owner, `photos.getAll`; VK leaves
    out the saved photos) and `photos` (those photos, `photos.getById`; the
    ones VK does not give are in `missing`, and VK's refusal of all of them
    is `200` with all in `missing`). Another user's or community's open album
    reads too. `photos` asks `photos.getById`, the method whose quota paused
    pages in November 2026. One VK call, within 8 s (2.3.0).

    Args:
        album (str | Unset):  Example: -210132800_312370605.
        owner_id (int | Unset):  Example: -210132800.
        photos (list[str] | Unset):  Example: ['photo-210132800_457239475'].
        offset (int | Unset):  Default: 0.
        count (int | Unset):
        rev (bool | Unset):  Default: False.
        extended (bool | Unset):  Default: False.
        no_system (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumPhotosResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        album=album,
        owner_id=owner_id,
        photos=photos,
        offset=offset,
        count=count,
        rev=rev,
        extended=extended,
        no_system=no_system,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    album: str | Unset = UNSET,
    owner_id: int | Unset = UNSET,
    photos: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = UNSET,
    rev: bool | Unset = False,
    extended: bool | Unset = False,
    no_system: bool | Unset = False,
) -> AlbumPhotosResponse | ErrorResponse | None:
    """The photos of an album, of an owner, or by id

     Exactly one of `album` (its photos, `photos.get`; `total` is the
    album's), `ownerId` (every photo of the owner, `photos.getAll`; VK leaves
    out the saved photos) and `photos` (those photos, `photos.getById`; the
    ones VK does not give are in `missing`, and VK's refusal of all of them
    is `200` with all in `missing`). Another user's or community's open album
    reads too. `photos` asks `photos.getById`, the method whose quota paused
    pages in November 2026. One VK call, within 8 s (2.3.0).

    Args:
        album (str | Unset):  Example: -210132800_312370605.
        owner_id (int | Unset):  Example: -210132800.
        photos (list[str] | Unset):  Example: ['photo-210132800_457239475'].
        offset (int | Unset):  Default: 0.
        count (int | Unset):
        rev (bool | Unset):  Default: False.
        extended (bool | Unset):  Default: False.
        no_system (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumPhotosResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        album=album,
        owner_id=owner_id,
        photos=photos,
        offset=offset,
        count=count,
        rev=rev,
        extended=extended,
        no_system=no_system,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    album: str | Unset = UNSET,
    owner_id: int | Unset = UNSET,
    photos: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = UNSET,
    rev: bool | Unset = False,
    extended: bool | Unset = False,
    no_system: bool | Unset = False,
) -> Response[AlbumPhotosResponse | ErrorResponse]:
    """The photos of an album, of an owner, or by id

     Exactly one of `album` (its photos, `photos.get`; `total` is the
    album's), `ownerId` (every photo of the owner, `photos.getAll`; VK leaves
    out the saved photos) and `photos` (those photos, `photos.getById`; the
    ones VK does not give are in `missing`, and VK's refusal of all of them
    is `200` with all in `missing`). Another user's or community's open album
    reads too. `photos` asks `photos.getById`, the method whose quota paused
    pages in November 2026. One VK call, within 8 s (2.3.0).

    Args:
        album (str | Unset):  Example: -210132800_312370605.
        owner_id (int | Unset):  Example: -210132800.
        photos (list[str] | Unset):  Example: ['photo-210132800_457239475'].
        offset (int | Unset):  Default: 0.
        count (int | Unset):
        rev (bool | Unset):  Default: False.
        extended (bool | Unset):  Default: False.
        no_system (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumPhotosResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        album=album,
        owner_id=owner_id,
        photos=photos,
        offset=offset,
        count=count,
        rev=rev,
        extended=extended,
        no_system=no_system,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    album: str | Unset = UNSET,
    owner_id: int | Unset = UNSET,
    photos: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = UNSET,
    rev: bool | Unset = False,
    extended: bool | Unset = False,
    no_system: bool | Unset = False,
) -> AlbumPhotosResponse | ErrorResponse | None:
    """The photos of an album, of an owner, or by id

     Exactly one of `album` (its photos, `photos.get`; `total` is the
    album's), `ownerId` (every photo of the owner, `photos.getAll`; VK leaves
    out the saved photos) and `photos` (those photos, `photos.getById`; the
    ones VK does not give are in `missing`, and VK's refusal of all of them
    is `200` with all in `missing`). Another user's or community's open album
    reads too. `photos` asks `photos.getById`, the method whose quota paused
    pages in November 2026. One VK call, within 8 s (2.3.0).

    Args:
        album (str | Unset):  Example: -210132800_312370605.
        owner_id (int | Unset):  Example: -210132800.
        photos (list[str] | Unset):  Example: ['photo-210132800_457239475'].
        offset (int | Unset):  Default: 0.
        count (int | Unset):
        rev (bool | Unset):  Default: False.
        extended (bool | Unset):  Default: False.
        no_system (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumPhotosResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            album=album,
            owner_id=owner_id,
            photos=photos,
            offset=offset,
            count=count,
            rev=rev,
            extended=extended,
            no_system=no_system,
        )
    ).parsed
