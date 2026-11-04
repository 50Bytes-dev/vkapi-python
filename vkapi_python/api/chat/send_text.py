from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.send_text_body import SendTextBody
from ...models.send_text_response import SendTextResponse
from ...types import Response


def _get_kwargs(
    *,
    body: SendTextBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat/send/text",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SendTextResponse | None:
    if response.status_code == 200:
        response_200 = SendTextResponse.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | SendTextResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SendTextBody,
) -> Response[ErrorResponse | SendTextResponse]:
    """Send a text message

     Sends a text from the account's VK page to a person or a group chat.
    Every error carries a delivery outcome `code`: only `send_failed` (500)
    means the message may have arrived; every other error means nothing was
    sent. Answers within 8 s (9 s when the gateway solves a captcha).

    Args:
        body (SendTextBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SendTextResponse]
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
    body: SendTextBody,
) -> ErrorResponse | SendTextResponse | None:
    """Send a text message

     Sends a text from the account's VK page to a person or a group chat.
    Every error carries a delivery outcome `code`: only `send_failed` (500)
    means the message may have arrived; every other error means nothing was
    sent. Answers within 8 s (9 s when the gateway solves a captcha).

    Args:
        body (SendTextBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SendTextResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SendTextBody,
) -> Response[ErrorResponse | SendTextResponse]:
    """Send a text message

     Sends a text from the account's VK page to a person or a group chat.
    Every error carries a delivery outcome `code`: only `send_failed` (500)
    means the message may have arrived; every other error means nothing was
    sent. Answers within 8 s (9 s when the gateway solves a captcha).

    Args:
        body (SendTextBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SendTextResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SendTextBody,
) -> ErrorResponse | SendTextResponse | None:
    """Send a text message

     Sends a text from the account's VK page to a person or a group chat.
    Every error carries a delivery outcome `code`: only `send_failed` (500)
    means the message may have arrived; every other error means nothing was
    sent. Answers within 8 s (9 s when the gateway solves a captcha).

    Args:
        body (SendTextBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SendTextResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
