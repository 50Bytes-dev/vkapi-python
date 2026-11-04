from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.message_response import MessageResponse
from ...types import Response


def _get_kwargs(
    userid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/admin/users/{userid}".format(
            userid=quote(str(userid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | MessageResponse | None:
    if response.status_code == 200:
        response_200 = MessageResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | MessageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    userid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | MessageResponse]:
    """Delete an account

     Stops the account's QR login, deletes the account with its VK login, and
    makes its token answer 401 at once. Succeeds for an unknown id too. No
    webhook is sent. The session stays open in VK, and the page's pause is
    kept.

    Args:
        userid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MessageResponse]
    """

    kwargs = _get_kwargs(
        userid=userid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    userid: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | MessageResponse | None:
    """Delete an account

     Stops the account's QR login, deletes the account with its VK login, and
    makes its token answer 401 at once. Succeeds for an unknown id too. No
    webhook is sent. The session stays open in VK, and the page's pause is
    kept.

    Args:
        userid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MessageResponse
    """

    return sync_detailed(
        userid=userid,
        client=client,
    ).parsed


async def asyncio_detailed(
    userid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | MessageResponse]:
    """Delete an account

     Stops the account's QR login, deletes the account with its VK login, and
    makes its token answer 401 at once. Succeeds for an unknown id too. No
    webhook is sent. The session stays open in VK, and the page's pause is
    kept.

    Args:
        userid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MessageResponse]
    """

    kwargs = _get_kwargs(
        userid=userid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    userid: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | MessageResponse | None:
    """Delete an account

     Stops the account's QR login, deletes the account with its VK login, and
    makes its token answer 401 at once. Succeeds for an unknown id too. No
    webhook is sent. The session stays open in VK, and the page's pause is
    kept.

    Args:
        userid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MessageResponse
    """

    return (
        await asyncio_detailed(
            userid=userid,
            client=client,
        )
    ).parsed
