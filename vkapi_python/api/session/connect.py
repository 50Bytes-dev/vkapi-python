from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connect_body import ConnectBody
from ...models.connect_response import ConnectResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ConnectBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/session/connect",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConnectResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = ConnectResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

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
) -> Response[ConnectResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ConnectBody,
) -> Response[ConnectResponse | ErrorResponse]:
    """Connect the account to VK

     Overwrites the event subscription, then connects the account. A stored
    login is checked with VK and reused (`alreadyConnected` true, `maxUserID`,
    webhook `Sync`); while the page is paused it is reused without a VK call
    (`paused` true, `pauseReason`). Without a usable stored login a QR login
    starts (`alreadyConnected` false, webhook `QRGenerated` with the QR image
    and link; `GET /session/qr` serves the same image). The login lives until
    VK, the owner or the account ends it; reads do not keep it alive.

    Args:
        body (ConnectBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectResponse | ErrorResponse]
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
    body: ConnectBody,
) -> ConnectResponse | ErrorResponse | None:
    """Connect the account to VK

     Overwrites the event subscription, then connects the account. A stored
    login is checked with VK and reused (`alreadyConnected` true, `maxUserID`,
    webhook `Sync`); while the page is paused it is reused without a VK call
    (`paused` true, `pauseReason`). Without a usable stored login a QR login
    starts (`alreadyConnected` false, webhook `QRGenerated` with the QR image
    and link; `GET /session/qr` serves the same image). The login lives until
    VK, the owner or the account ends it; reads do not keep it alive.

    Args:
        body (ConnectBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ConnectBody,
) -> Response[ConnectResponse | ErrorResponse]:
    """Connect the account to VK

     Overwrites the event subscription, then connects the account. A stored
    login is checked with VK and reused (`alreadyConnected` true, `maxUserID`,
    webhook `Sync`); while the page is paused it is reused without a VK call
    (`paused` true, `pauseReason`). Without a usable stored login a QR login
    starts (`alreadyConnected` false, webhook `QRGenerated` with the QR image
    and link; `GET /session/qr` serves the same image). The login lives until
    VK, the owner or the account ends it; reads do not keep it alive.

    Args:
        body (ConnectBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ConnectBody,
) -> ConnectResponse | ErrorResponse | None:
    """Connect the account to VK

     Overwrites the event subscription, then connects the account. A stored
    login is checked with VK and reused (`alreadyConnected` true, `maxUserID`,
    webhook `Sync`); while the page is paused it is reused without a VK call
    (`paused` true, `pauseReason`). Without a usable stored login a QR login
    starts (`alreadyConnected` false, webhook `QRGenerated` with the QR image
    and link; `GET /session/qr` serves the same image). The login lives until
    VK, the owner or the account ends it; reads do not keep it alive.

    Args:
        body (ConnectBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
