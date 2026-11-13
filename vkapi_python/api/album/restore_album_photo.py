from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_photo_ref_body import AlbumPhotoRefBody
from ...models.album_photo_restore_response import AlbumPhotoRestoreResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AlbumPhotoRefBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/album/photo/restore",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlbumPhotoRestoreResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AlbumPhotoRestoreResponse.from_dict(response.json())

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
) -> Response[AlbumPhotoRestoreResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AlbumPhotoRefBody,
) -> Response[AlbumPhotoRestoreResponse | ErrorResponse]:
    """Restore a deleted photo

     Restores one deleted photo (`photos.restore` takes one a call): it comes
    back into its album with its caption, as the album's last photo. VK answers
    1 whatever it did, so the gateway then asks VK for the photo
    (`photos.getById`): one VK does not give answers `422`
    `attachment_rejected` (deleted with its album, deleted too long ago, or
    never there). How long a deleted photo can be restored VK does not say (a
    minute later it could). When only that read fails, the answer is `success`
    with `checked` false and without `photo`. Each VK call has 12 s, a captcha's solving of up to 10 s
    included, within 25 s, as on `POST /album/photo`. (2.3.0)

    Args:
        body (AlbumPhotoRefBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumPhotoRestoreResponse | ErrorResponse]
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
    body: AlbumPhotoRefBody,
) -> AlbumPhotoRestoreResponse | ErrorResponse | None:
    """Restore a deleted photo

     Restores one deleted photo (`photos.restore` takes one a call): it comes
    back into its album with its caption, as the album's last photo. VK answers
    1 whatever it did, so the gateway then asks VK for the photo
    (`photos.getById`): one VK does not give answers `422`
    `attachment_rejected` (deleted with its album, deleted too long ago, or
    never there). How long a deleted photo can be restored VK does not say (a
    minute later it could). When only that read fails, the answer is `success`
    with `checked` false and without `photo`. Each VK call has 12 s, a captcha's solving of up to 10 s
    included, within 25 s, as on `POST /album/photo`. (2.3.0)

    Args:
        body (AlbumPhotoRefBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumPhotoRestoreResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AlbumPhotoRefBody,
) -> Response[AlbumPhotoRestoreResponse | ErrorResponse]:
    """Restore a deleted photo

     Restores one deleted photo (`photos.restore` takes one a call): it comes
    back into its album with its caption, as the album's last photo. VK answers
    1 whatever it did, so the gateway then asks VK for the photo
    (`photos.getById`): one VK does not give answers `422`
    `attachment_rejected` (deleted with its album, deleted too long ago, or
    never there). How long a deleted photo can be restored VK does not say (a
    minute later it could). When only that read fails, the answer is `success`
    with `checked` false and without `photo`. Each VK call has 12 s, a captcha's solving of up to 10 s
    included, within 25 s, as on `POST /album/photo`. (2.3.0)

    Args:
        body (AlbumPhotoRefBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumPhotoRestoreResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AlbumPhotoRefBody,
) -> AlbumPhotoRestoreResponse | ErrorResponse | None:
    """Restore a deleted photo

     Restores one deleted photo (`photos.restore` takes one a call): it comes
    back into its album with its caption, as the album's last photo. VK answers
    1 whatever it did, so the gateway then asks VK for the photo
    (`photos.getById`): one VK does not give answers `422`
    `attachment_rejected` (deleted with its album, deleted too long ago, or
    never there). How long a deleted photo can be restored VK does not say (a
    minute later it could). When only that read fails, the answer is `success`
    with `checked` false and without `photo`. Each VK call has 12 s, a captcha's solving of up to 10 s
    included, within 25 s, as on `POST /album/photo`. (2.3.0)

    Args:
        body (AlbumPhotoRefBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumPhotoRestoreResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
