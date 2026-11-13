from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.photo_comments_response import PhotoCommentsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    photo: str | Unset = UNSET,
    album: str | Unset = UNSET,
    owner_id: int | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = UNSET,
    likes: bool | Unset = False,
    sort: str | Unset = UNSET,
    start_comment_id: int | Unset = UNSET,
    extended: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["photo"] = photo

    params["album"] = album

    params["ownerId"] = owner_id

    params["offset"] = offset

    params["count"] = count

    params["likes"] = likes

    params["sort"] = sort

    params["startCommentId"] = start_comment_id

    params["extended"] = extended

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/album/comments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PhotoCommentsResponse | None:
    if response.status_code == 200:
        response_200 = PhotoCommentsResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | PhotoCommentsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    photo: str | Unset = UNSET,
    album: str | Unset = UNSET,
    owner_id: int | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = UNSET,
    likes: bool | Unset = False,
    sort: str | Unset = UNSET,
    start_comment_id: int | Unset = UNSET,
    extended: bool | Unset = False,
) -> Response[ErrorResponse | PhotoCommentsResponse]:
    r"""The comments of a photo, of an album, or of an owner's photos

     Exactly one of `photo` (`photos.getComments`), `album` and `ownerId`
    (`photos.getAllComments`, each comment with its `photo`). A comment belongs
    to the photo's owner: its id is counted per owner, so a comment is
    `ownerId` and `commentId`. A deleted photo is VK's 15 \"photo not found\":
    `attachment_rejected`. One VK call, within 8 s (2.3.0).

    Args:
        photo (str | Unset):  Example: photo-210132800_457239475.
        album (str | Unset):  Example: -210132800_312370605.
        owner_id (int | Unset):  Example: -210132800.
        offset (int | Unset):  Default: 0.
        count (int | Unset):
        likes (bool | Unset):  Default: False.
        sort (str | Unset):  Example: asc.
        start_comment_id (int | Unset):
        extended (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PhotoCommentsResponse]
    """

    kwargs = _get_kwargs(
        photo=photo,
        album=album,
        owner_id=owner_id,
        offset=offset,
        count=count,
        likes=likes,
        sort=sort,
        start_comment_id=start_comment_id,
        extended=extended,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    photo: str | Unset = UNSET,
    album: str | Unset = UNSET,
    owner_id: int | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = UNSET,
    likes: bool | Unset = False,
    sort: str | Unset = UNSET,
    start_comment_id: int | Unset = UNSET,
    extended: bool | Unset = False,
) -> ErrorResponse | PhotoCommentsResponse | None:
    r"""The comments of a photo, of an album, or of an owner's photos

     Exactly one of `photo` (`photos.getComments`), `album` and `ownerId`
    (`photos.getAllComments`, each comment with its `photo`). A comment belongs
    to the photo's owner: its id is counted per owner, so a comment is
    `ownerId` and `commentId`. A deleted photo is VK's 15 \"photo not found\":
    `attachment_rejected`. One VK call, within 8 s (2.3.0).

    Args:
        photo (str | Unset):  Example: photo-210132800_457239475.
        album (str | Unset):  Example: -210132800_312370605.
        owner_id (int | Unset):  Example: -210132800.
        offset (int | Unset):  Default: 0.
        count (int | Unset):
        likes (bool | Unset):  Default: False.
        sort (str | Unset):  Example: asc.
        start_comment_id (int | Unset):
        extended (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PhotoCommentsResponse
    """

    return sync_detailed(
        client=client,
        photo=photo,
        album=album,
        owner_id=owner_id,
        offset=offset,
        count=count,
        likes=likes,
        sort=sort,
        start_comment_id=start_comment_id,
        extended=extended,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    photo: str | Unset = UNSET,
    album: str | Unset = UNSET,
    owner_id: int | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = UNSET,
    likes: bool | Unset = False,
    sort: str | Unset = UNSET,
    start_comment_id: int | Unset = UNSET,
    extended: bool | Unset = False,
) -> Response[ErrorResponse | PhotoCommentsResponse]:
    r"""The comments of a photo, of an album, or of an owner's photos

     Exactly one of `photo` (`photos.getComments`), `album` and `ownerId`
    (`photos.getAllComments`, each comment with its `photo`). A comment belongs
    to the photo's owner: its id is counted per owner, so a comment is
    `ownerId` and `commentId`. A deleted photo is VK's 15 \"photo not found\":
    `attachment_rejected`. One VK call, within 8 s (2.3.0).

    Args:
        photo (str | Unset):  Example: photo-210132800_457239475.
        album (str | Unset):  Example: -210132800_312370605.
        owner_id (int | Unset):  Example: -210132800.
        offset (int | Unset):  Default: 0.
        count (int | Unset):
        likes (bool | Unset):  Default: False.
        sort (str | Unset):  Example: asc.
        start_comment_id (int | Unset):
        extended (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PhotoCommentsResponse]
    """

    kwargs = _get_kwargs(
        photo=photo,
        album=album,
        owner_id=owner_id,
        offset=offset,
        count=count,
        likes=likes,
        sort=sort,
        start_comment_id=start_comment_id,
        extended=extended,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    photo: str | Unset = UNSET,
    album: str | Unset = UNSET,
    owner_id: int | Unset = UNSET,
    offset: int | Unset = 0,
    count: int | Unset = UNSET,
    likes: bool | Unset = False,
    sort: str | Unset = UNSET,
    start_comment_id: int | Unset = UNSET,
    extended: bool | Unset = False,
) -> ErrorResponse | PhotoCommentsResponse | None:
    r"""The comments of a photo, of an album, or of an owner's photos

     Exactly one of `photo` (`photos.getComments`), `album` and `ownerId`
    (`photos.getAllComments`, each comment with its `photo`). A comment belongs
    to the photo's owner: its id is counted per owner, so a comment is
    `ownerId` and `commentId`. A deleted photo is VK's 15 \"photo not found\":
    `attachment_rejected`. One VK call, within 8 s (2.3.0).

    Args:
        photo (str | Unset):  Example: photo-210132800_457239475.
        album (str | Unset):  Example: -210132800_312370605.
        owner_id (int | Unset):  Example: -210132800.
        offset (int | Unset):  Default: 0.
        count (int | Unset):
        likes (bool | Unset):  Default: False.
        sort (str | Unset):  Example: asc.
        start_comment_id (int | Unset):
        extended (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PhotoCommentsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            photo=photo,
            album=album,
            owner_id=owner_id,
            offset=offset,
            count=count,
            likes=likes,
            sort=sort,
            start_comment_id=start_comment_id,
            extended=extended,
        )
    ).parsed
