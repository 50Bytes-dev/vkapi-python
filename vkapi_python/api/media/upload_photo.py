from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.photo_body import PhotoBody
from ...models.photo_response import PhotoResponse
from ...models.photo_upload import PhotoUpload
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PhotoBody | PhotoUpload | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/media/photo",
    }

    if isinstance(body, PhotoBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PhotoUpload):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PhotoResponse | None:
    if response.status_code == 200:
        response_200 = PhotoResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | PhotoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PhotoBody | PhotoUpload | Unset = UNSET,
) -> Response[ErrorResponse | PhotoResponse]:
    """Upload a photo once for every chat of the page

     Makes a VK photo of an image and answers its `attachment`, which a send
    takes in any dialog of the page. The image comes as `url` (fetched
    safely: http or https, no private address, at most 3 redirects, 10 s, a
    200 answer with an image of at most 10 MiB), as `data` (base64 or a data
    URL) or as a multipart file; the body may be up to 10 MiB. JPEG, PNG,
    GIF, WebP and BMP are taken; the gateway turns the image upright by its
    EXIF, puts transparency on white, makes it at most 2560 px on its longer
    side and uploads it as a JPEG. A failed upload (no photo kept, HTTP 405,
    no answer, VK failing inside) is made again, up to 5 uploads in all,
    2 to 5 s apart, each at a fresh upload server. Answers within about 45 s: 10 s to fetch, up to 5 s
    waiting for the gateway's image slots, a few seconds to make the image,
    25 s for VK. Many photo requests at once answer `upload_failed` at once.

    Args:
        body (PhotoBody): Exactly one of `url` and `data`.
        body (PhotoUpload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PhotoResponse]
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
    body: PhotoBody | PhotoUpload | Unset = UNSET,
) -> ErrorResponse | PhotoResponse | None:
    """Upload a photo once for every chat of the page

     Makes a VK photo of an image and answers its `attachment`, which a send
    takes in any dialog of the page. The image comes as `url` (fetched
    safely: http or https, no private address, at most 3 redirects, 10 s, a
    200 answer with an image of at most 10 MiB), as `data` (base64 or a data
    URL) or as a multipart file; the body may be up to 10 MiB. JPEG, PNG,
    GIF, WebP and BMP are taken; the gateway turns the image upright by its
    EXIF, puts transparency on white, makes it at most 2560 px on its longer
    side and uploads it as a JPEG. A failed upload (no photo kept, HTTP 405,
    no answer, VK failing inside) is made again, up to 5 uploads in all,
    2 to 5 s apart, each at a fresh upload server. Answers within about 45 s: 10 s to fetch, up to 5 s
    waiting for the gateway's image slots, a few seconds to make the image,
    25 s for VK. Many photo requests at once answer `upload_failed` at once.

    Args:
        body (PhotoBody): Exactly one of `url` and `data`.
        body (PhotoUpload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PhotoResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PhotoBody | PhotoUpload | Unset = UNSET,
) -> Response[ErrorResponse | PhotoResponse]:
    """Upload a photo once for every chat of the page

     Makes a VK photo of an image and answers its `attachment`, which a send
    takes in any dialog of the page. The image comes as `url` (fetched
    safely: http or https, no private address, at most 3 redirects, 10 s, a
    200 answer with an image of at most 10 MiB), as `data` (base64 or a data
    URL) or as a multipart file; the body may be up to 10 MiB. JPEG, PNG,
    GIF, WebP and BMP are taken; the gateway turns the image upright by its
    EXIF, puts transparency on white, makes it at most 2560 px on its longer
    side and uploads it as a JPEG. A failed upload (no photo kept, HTTP 405,
    no answer, VK failing inside) is made again, up to 5 uploads in all,
    2 to 5 s apart, each at a fresh upload server. Answers within about 45 s: 10 s to fetch, up to 5 s
    waiting for the gateway's image slots, a few seconds to make the image,
    25 s for VK. Many photo requests at once answer `upload_failed` at once.

    Args:
        body (PhotoBody): Exactly one of `url` and `data`.
        body (PhotoUpload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PhotoResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PhotoBody | PhotoUpload | Unset = UNSET,
) -> ErrorResponse | PhotoResponse | None:
    """Upload a photo once for every chat of the page

     Makes a VK photo of an image and answers its `attachment`, which a send
    takes in any dialog of the page. The image comes as `url` (fetched
    safely: http or https, no private address, at most 3 redirects, 10 s, a
    200 answer with an image of at most 10 MiB), as `data` (base64 or a data
    URL) or as a multipart file; the body may be up to 10 MiB. JPEG, PNG,
    GIF, WebP and BMP are taken; the gateway turns the image upright by its
    EXIF, puts transparency on white, makes it at most 2560 px on its longer
    side and uploads it as a JPEG. A failed upload (no photo kept, HTTP 405,
    no answer, VK failing inside) is made again, up to 5 uploads in all,
    2 to 5 s apart, each at a fresh upload server. Answers within about 45 s: 10 s to fetch, up to 5 s
    waiting for the gateway's image slots, a few seconds to make the image,
    25 s for VK. Many photo requests at once answer `upload_failed` at once.

    Args:
        body (PhotoBody): Exactly one of `url` and `data`.
        body (PhotoUpload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PhotoResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
