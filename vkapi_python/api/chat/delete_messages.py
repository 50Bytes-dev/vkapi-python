from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_body import DeleteBody
from ...models.delete_response import DeleteResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: DeleteBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat/delete",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DeleteResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

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
) -> Response[DeleteResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DeleteBody,
) -> Response[DeleteResponse | ErrorResponse]:
    """Delete the page's messages for everyone

     Deletes up to 100 of the page's messages in one dialog for everyone,
    with a status per message. The gateway reads them first
    (`messages.getById`): one not there or of another dialog is
    `not_found`, one past 24 hours `too_old`, and neither goes to
    `messages.delete` with `delete_for_all` (VK ignores `peer_id` and the
    24 hours with message ids). A paused page
    answers `send_rejected` with the pause, as a send does. Within 8 s.

    Args:
        body (DeleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteResponse | ErrorResponse]
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
    body: DeleteBody,
) -> DeleteResponse | ErrorResponse | None:
    """Delete the page's messages for everyone

     Deletes up to 100 of the page's messages in one dialog for everyone,
    with a status per message. The gateway reads them first
    (`messages.getById`): one not there or of another dialog is
    `not_found`, one past 24 hours `too_old`, and neither goes to
    `messages.delete` with `delete_for_all` (VK ignores `peer_id` and the
    24 hours with message ids). A paused page
    answers `send_rejected` with the pause, as a send does. Within 8 s.

    Args:
        body (DeleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DeleteBody,
) -> Response[DeleteResponse | ErrorResponse]:
    """Delete the page's messages for everyone

     Deletes up to 100 of the page's messages in one dialog for everyone,
    with a status per message. The gateway reads them first
    (`messages.getById`): one not there or of another dialog is
    `not_found`, one past 24 hours `too_old`, and neither goes to
    `messages.delete` with `delete_for_all` (VK ignores `peer_id` and the
    24 hours with message ids). A paused page
    answers `send_rejected` with the pause, as a send does. Within 8 s.

    Args:
        body (DeleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DeleteBody,
) -> DeleteResponse | ErrorResponse | None:
    """Delete the page's messages for everyone

     Deletes up to 100 of the page's messages in one dialog for everyone,
    with a status per message. The gateway reads them first
    (`messages.getById`): one not there or of another dialog is
    `not_found`, one past 24 hours `too_old`, and neither goes to
    `messages.delete` with `delete_for_all` (VK ignores `peer_id` and the
    24 hours with message ids). A paused page
    answers `send_rejected` with the pause, as a send does. Within 8 s.

    Args:
        body (DeleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
