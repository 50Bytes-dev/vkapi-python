from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_photo_delete_response import AlbumPhotoDeleteResponse
from ...models.album_photos_body import AlbumPhotosBody
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AlbumPhotosBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/album/photo/delete",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlbumPhotoDeleteResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AlbumPhotoDeleteResponse.from_dict(response.json())

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
) -> Response[AlbumPhotoDeleteResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AlbumPhotosBody,
) -> Response[AlbumPhotoDeleteResponse | ErrorResponse]:
    """Delete up to 100 photos

     Deletes up to 100 photos of the page and of the communities it manages,
    of several owners in one call (`photos.delete` with `photos`). VK answers 1
    whatever it did: also for a photo deleted already, one never there, and
    another owner's, which stays (checked live). So the gateway then asks VK
    for the photos (`photos.getById`, the method whose quota paused pages in
    November 2026): one VK still gives is `kept`, the others `deleted`. When
    only that read fails, the delete is done all the same: `checked` false and
    every photo in `unchecked`. Every page forgets the photos: a send asks VK
    for them again. **A deleted photo leaves the messages sent with it**
    (checked live), and comes back into them on a restore. `POST /album/photo/restore` brings one back;
    for how long,
    VK does not say. Each VK call has 12 s, a captcha's solving of up to 10 s included, within 25 s, as
    on `POST /album/photo`. (2.3.0)

    Args:
        body (AlbumPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumPhotoDeleteResponse | ErrorResponse]
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
    body: AlbumPhotosBody,
) -> AlbumPhotoDeleteResponse | ErrorResponse | None:
    """Delete up to 100 photos

     Deletes up to 100 photos of the page and of the communities it manages,
    of several owners in one call (`photos.delete` with `photos`). VK answers 1
    whatever it did: also for a photo deleted already, one never there, and
    another owner's, which stays (checked live). So the gateway then asks VK
    for the photos (`photos.getById`, the method whose quota paused pages in
    November 2026): one VK still gives is `kept`, the others `deleted`. When
    only that read fails, the delete is done all the same: `checked` false and
    every photo in `unchecked`. Every page forgets the photos: a send asks VK
    for them again. **A deleted photo leaves the messages sent with it**
    (checked live), and comes back into them on a restore. `POST /album/photo/restore` brings one back;
    for how long,
    VK does not say. Each VK call has 12 s, a captcha's solving of up to 10 s included, within 25 s, as
    on `POST /album/photo`. (2.3.0)

    Args:
        body (AlbumPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumPhotoDeleteResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AlbumPhotosBody,
) -> Response[AlbumPhotoDeleteResponse | ErrorResponse]:
    """Delete up to 100 photos

     Deletes up to 100 photos of the page and of the communities it manages,
    of several owners in one call (`photos.delete` with `photos`). VK answers 1
    whatever it did: also for a photo deleted already, one never there, and
    another owner's, which stays (checked live). So the gateway then asks VK
    for the photos (`photos.getById`, the method whose quota paused pages in
    November 2026): one VK still gives is `kept`, the others `deleted`. When
    only that read fails, the delete is done all the same: `checked` false and
    every photo in `unchecked`. Every page forgets the photos: a send asks VK
    for them again. **A deleted photo leaves the messages sent with it**
    (checked live), and comes back into them on a restore. `POST /album/photo/restore` brings one back;
    for how long,
    VK does not say. Each VK call has 12 s, a captcha's solving of up to 10 s included, within 25 s, as
    on `POST /album/photo`. (2.3.0)

    Args:
        body (AlbumPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumPhotoDeleteResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AlbumPhotosBody,
) -> AlbumPhotoDeleteResponse | ErrorResponse | None:
    """Delete up to 100 photos

     Deletes up to 100 photos of the page and of the communities it manages,
    of several owners in one call (`photos.delete` with `photos`). VK answers 1
    whatever it did: also for a photo deleted already, one never there, and
    another owner's, which stays (checked live). So the gateway then asks VK
    for the photos (`photos.getById`, the method whose quota paused pages in
    November 2026): one VK still gives is `kept`, the others `deleted`. When
    only that read fails, the delete is done all the same: `checked` false and
    every photo in `unchecked`. Every page forgets the photos: a send asks VK
    for them again. **A deleted photo leaves the messages sent with it**
    (checked live), and comes back into them on a restore. `POST /album/photo/restore` brings one back;
    for how long,
    VK does not say. Each VK call has 12 s, a captcha's solving of up to 10 s included, within 25 s, as
    on `POST /album/photo`. (2.3.0)

    Args:
        body (AlbumPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumPhotoDeleteResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
