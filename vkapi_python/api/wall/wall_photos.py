from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.wall_photos_body import WallPhotosBody
from ...models.wall_photos_response import WallPhotosResponse
from ...types import Response


def _get_kwargs(
    *,
    body: WallPhotosBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/wall/photos",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WallPhotosResponse | None:
    if response.status_code == 200:
        response_200 = WallPhotosResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | WallPhotosResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WallPhotosBody,
) -> Response[ErrorResponse | WallPhotosResponse]:
    """The photos of wall posts

     The photos of up to 100 wall posts by id (`<owner_id>_<post_id>`), as
    attachments a send takes, in full size and in the post's order, with one
    `wall.getById`. A post VK does not give (deleted, hidden, a wrong id) is
    `found: false`: upload its photos with `POST /media/photo` instead. A
    repost without photos of its own gives the reposted post's. Within 8 s.

    Args:
        body (WallPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WallPhotosResponse]
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
    body: WallPhotosBody,
) -> ErrorResponse | WallPhotosResponse | None:
    """The photos of wall posts

     The photos of up to 100 wall posts by id (`<owner_id>_<post_id>`), as
    attachments a send takes, in full size and in the post's order, with one
    `wall.getById`. A post VK does not give (deleted, hidden, a wrong id) is
    `found: false`: upload its photos with `POST /media/photo` instead. A
    repost without photos of its own gives the reposted post's. Within 8 s.

    Args:
        body (WallPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WallPhotosResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WallPhotosBody,
) -> Response[ErrorResponse | WallPhotosResponse]:
    """The photos of wall posts

     The photos of up to 100 wall posts by id (`<owner_id>_<post_id>`), as
    attachments a send takes, in full size and in the post's order, with one
    `wall.getById`. A post VK does not give (deleted, hidden, a wrong id) is
    `found: false`: upload its photos with `POST /media/photo` instead. A
    repost without photos of its own gives the reposted post's. Within 8 s.

    Args:
        body (WallPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WallPhotosResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: WallPhotosBody,
) -> ErrorResponse | WallPhotosResponse | None:
    """The photos of wall posts

     The photos of up to 100 wall posts by id (`<owner_id>_<post_id>`), as
    attachments a send takes, in full size and in the post's order, with one
    `wall.getById`. A post VK does not give (deleted, hidden, a wrong id) is
    `found: false`: upload its photos with `POST /media/photo` instead. A
    repost without photos of its own gives the reposted post's. Within 8 s.

    Args:
        body (WallPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WallPhotosResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
