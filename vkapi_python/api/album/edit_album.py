from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_edit_body import AlbumEditBody
from ...models.album_response import AlbumResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AlbumEditBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/album/edit",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlbumResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AlbumResponse.from_dict(response.json())

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
) -> Response[AlbumResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AlbumEditBody,
) -> Response[AlbumResponse | ErrorResponse]:
    """Edit an album of the page or of a community it manages

     Changes the fields given; a field left out is kept. A community album's
    two switches go together in VK (one given alone sets the other to 0), so
    an edit with one of them reads the album first and sends the other with
    its own value. The album is read back after the edit: when only that read
    fails, the answer is `success` without `album`, and the edit is done. Two
    VK calls, three with one switch alone, within 8 s.

    Args:
        body (AlbumEditBody): The album and at least one field; a field left out is kept.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumResponse | ErrorResponse]
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
    body: AlbumEditBody,
) -> AlbumResponse | ErrorResponse | None:
    """Edit an album of the page or of a community it manages

     Changes the fields given; a field left out is kept. A community album's
    two switches go together in VK (one given alone sets the other to 0), so
    an edit with one of them reads the album first and sends the other with
    its own value. The album is read back after the edit: when only that read
    fails, the answer is `success` without `album`, and the edit is done. Two
    VK calls, three with one switch alone, within 8 s.

    Args:
        body (AlbumEditBody): The album and at least one field; a field left out is kept.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AlbumEditBody,
) -> Response[AlbumResponse | ErrorResponse]:
    """Edit an album of the page or of a community it manages

     Changes the fields given; a field left out is kept. A community album's
    two switches go together in VK (one given alone sets the other to 0), so
    an edit with one of them reads the album first and sends the other with
    its own value. The album is read back after the edit: when only that read
    fails, the answer is `success` without `album`, and the edit is done. Two
    VK calls, three with one switch alone, within 8 s.

    Args:
        body (AlbumEditBody): The album and at least one field; a field left out is kept.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AlbumEditBody,
) -> AlbumResponse | ErrorResponse | None:
    """Edit an album of the page or of a community it manages

     Changes the fields given; a field left out is kept. A community album's
    two switches go together in VK (one given alone sets the other to 0), so
    an edit with one of them reads the album first and sends the other with
    its own value. The album is read back after the edit: when only that read
    fails, the answer is `success` without `album`, and the edit is done. Two
    VK calls, three with one switch alone, within 8 s.

    Args:
        body (AlbumEditBody): The album and at least one field; a field left out is kept.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
