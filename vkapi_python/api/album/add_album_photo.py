from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_photo_body import AlbumPhotoBody
from ...models.album_photo_response import AlbumPhotoResponse
from ...models.album_photo_upload import AlbumPhotoUpload
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AlbumPhotoBody | AlbumPhotoUpload | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/album/photo",
    }

    if isinstance(body, AlbumPhotoBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, AlbumPhotoUpload):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlbumPhotoResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AlbumPhotoResponse.from_dict(response.json())

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

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

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
) -> Response[AlbumPhotoResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AlbumPhotoBody | AlbumPhotoUpload | Unset = UNSET,
) -> Response[AlbumPhotoResponse | ErrorResponse]:
    """Put one photo with its caption into an album

     One photo into an album of the page or of a community it manages, with a
    caption of at most 2048 characters (VK cuts a longer one without a word).
    A new image (`url`, `data` or a multipart file, made as on
    `POST /media/photo`) is uploaded: `photos.getUploadServer` (its address
    kept per album for 30 minutes), the file posted, `photos.save`; a failed
    upload is made again as on `POST /media/photo`, up to 5 uploads, but a
    save that may have reached VK is not repeated: VK saves one upload twice
    into two photos, so a repeated call after `upload_failed` may put the
    photo in the album twice. A photo VK has (`photo`) is copied into one of
    the page's own albums (`photos.copy`, `photos.move`, `photos.edit`; the
    copy loses the original's caption, which is why the caption is set
    anew). A community's album takes no copy: the photo's largest copy of at
    most 2560 px is found with `photos.getById` (the method whose quota paused pages in
    November 2026), fetched and uploaded anew; give its address as `url`
    instead (`POST /wall/photos` gives it). VK's 15 here refuses the album or
    the photo and pauses nothing. About 45 s, up to 5 s more for
    `photos.getById`; each VK call of the photo has 12 s, a captcha's
    solving of up to 10 s included (the slider VK offers after `BOT`).
    The page's uploads into albums and its photos for messages spend the
    same of VK's flood control: VK's 9 on one stops both for hours.

    Args:
        body (AlbumPhotoBody): The album, a caption, and exactly one of `url`, `data` and `photo`.
        body (AlbumPhotoUpload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumPhotoResponse | ErrorResponse]
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
    body: AlbumPhotoBody | AlbumPhotoUpload | Unset = UNSET,
) -> AlbumPhotoResponse | ErrorResponse | None:
    """Put one photo with its caption into an album

     One photo into an album of the page or of a community it manages, with a
    caption of at most 2048 characters (VK cuts a longer one without a word).
    A new image (`url`, `data` or a multipart file, made as on
    `POST /media/photo`) is uploaded: `photos.getUploadServer` (its address
    kept per album for 30 minutes), the file posted, `photos.save`; a failed
    upload is made again as on `POST /media/photo`, up to 5 uploads, but a
    save that may have reached VK is not repeated: VK saves one upload twice
    into two photos, so a repeated call after `upload_failed` may put the
    photo in the album twice. A photo VK has (`photo`) is copied into one of
    the page's own albums (`photos.copy`, `photos.move`, `photos.edit`; the
    copy loses the original's caption, which is why the caption is set
    anew). A community's album takes no copy: the photo's largest copy of at
    most 2560 px is found with `photos.getById` (the method whose quota paused pages in
    November 2026), fetched and uploaded anew; give its address as `url`
    instead (`POST /wall/photos` gives it). VK's 15 here refuses the album or
    the photo and pauses nothing. About 45 s, up to 5 s more for
    `photos.getById`; each VK call of the photo has 12 s, a captcha's
    solving of up to 10 s included (the slider VK offers after `BOT`).
    The page's uploads into albums and its photos for messages spend the
    same of VK's flood control: VK's 9 on one stops both for hours.

    Args:
        body (AlbumPhotoBody): The album, a caption, and exactly one of `url`, `data` and `photo`.
        body (AlbumPhotoUpload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumPhotoResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AlbumPhotoBody | AlbumPhotoUpload | Unset = UNSET,
) -> Response[AlbumPhotoResponse | ErrorResponse]:
    """Put one photo with its caption into an album

     One photo into an album of the page or of a community it manages, with a
    caption of at most 2048 characters (VK cuts a longer one without a word).
    A new image (`url`, `data` or a multipart file, made as on
    `POST /media/photo`) is uploaded: `photos.getUploadServer` (its address
    kept per album for 30 minutes), the file posted, `photos.save`; a failed
    upload is made again as on `POST /media/photo`, up to 5 uploads, but a
    save that may have reached VK is not repeated: VK saves one upload twice
    into two photos, so a repeated call after `upload_failed` may put the
    photo in the album twice. A photo VK has (`photo`) is copied into one of
    the page's own albums (`photos.copy`, `photos.move`, `photos.edit`; the
    copy loses the original's caption, which is why the caption is set
    anew). A community's album takes no copy: the photo's largest copy of at
    most 2560 px is found with `photos.getById` (the method whose quota paused pages in
    November 2026), fetched and uploaded anew; give its address as `url`
    instead (`POST /wall/photos` gives it). VK's 15 here refuses the album or
    the photo and pauses nothing. About 45 s, up to 5 s more for
    `photos.getById`; each VK call of the photo has 12 s, a captcha's
    solving of up to 10 s included (the slider VK offers after `BOT`).
    The page's uploads into albums and its photos for messages spend the
    same of VK's flood control: VK's 9 on one stops both for hours.

    Args:
        body (AlbumPhotoBody): The album, a caption, and exactly one of `url`, `data` and `photo`.
        body (AlbumPhotoUpload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumPhotoResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AlbumPhotoBody | AlbumPhotoUpload | Unset = UNSET,
) -> AlbumPhotoResponse | ErrorResponse | None:
    """Put one photo with its caption into an album

     One photo into an album of the page or of a community it manages, with a
    caption of at most 2048 characters (VK cuts a longer one without a word).
    A new image (`url`, `data` or a multipart file, made as on
    `POST /media/photo`) is uploaded: `photos.getUploadServer` (its address
    kept per album for 30 minutes), the file posted, `photos.save`; a failed
    upload is made again as on `POST /media/photo`, up to 5 uploads, but a
    save that may have reached VK is not repeated: VK saves one upload twice
    into two photos, so a repeated call after `upload_failed` may put the
    photo in the album twice. A photo VK has (`photo`) is copied into one of
    the page's own albums (`photos.copy`, `photos.move`, `photos.edit`; the
    copy loses the original's caption, which is why the caption is set
    anew). A community's album takes no copy: the photo's largest copy of at
    most 2560 px is found with `photos.getById` (the method whose quota paused pages in
    November 2026), fetched and uploaded anew; give its address as `url`
    instead (`POST /wall/photos` gives it). VK's 15 here refuses the album or
    the photo and pauses nothing. About 45 s, up to 5 s more for
    `photos.getById`; each VK call of the photo has 12 s, a captcha's
    solving of up to 10 s included (the slider VK offers after `BOT`).
    The page's uploads into albums and its photos for messages spend the
    same of VK's flood control: VK's 9 on one stops both for hours.

    Args:
        body (AlbumPhotoBody): The album, a caption, and exactly one of `url`, `data` and `photo`.
        body (AlbumPhotoUpload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumPhotoResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
