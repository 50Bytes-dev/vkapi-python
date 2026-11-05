from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_user_body import EditUserBody
from ...models.edit_user_response import EditUserResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    userid: str,
    *,
    body: EditUserBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/admin/users/{userid}".format(
            userid=quote(str(userid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EditUserResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = EditUserResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EditUserResponse | ErrorResponse]:
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
    body: EditUserBody,
) -> Response[EditUserResponse | ErrorResponse]:
    """Edit an account

     Changes the fields given: the name (VK shows it with the next login), the
    webhook and the event subscription. A field left out stays. The account token, the login and the
    page stay. The
    answer has no token and no webhook.

    Args:
        userid (str):
        body (EditUserBody): Each field given replaces the account's; each left out stays.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditUserResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        userid=userid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    userid: str,
    *,
    client: AuthenticatedClient,
    body: EditUserBody,
) -> EditUserResponse | ErrorResponse | None:
    """Edit an account

     Changes the fields given: the name (VK shows it with the next login), the
    webhook and the event subscription. A field left out stays. The account token, the login and the
    page stay. The
    answer has no token and no webhook.

    Args:
        userid (str):
        body (EditUserBody): Each field given replaces the account's; each left out stays.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditUserResponse | ErrorResponse
    """

    return sync_detailed(
        userid=userid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    userid: str,
    *,
    client: AuthenticatedClient,
    body: EditUserBody,
) -> Response[EditUserResponse | ErrorResponse]:
    """Edit an account

     Changes the fields given: the name (VK shows it with the next login), the
    webhook and the event subscription. A field left out stays. The account token, the login and the
    page stay. The
    answer has no token and no webhook.

    Args:
        userid (str):
        body (EditUserBody): Each field given replaces the account's; each left out stays.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditUserResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        userid=userid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    userid: str,
    *,
    client: AuthenticatedClient,
    body: EditUserBody,
) -> EditUserResponse | ErrorResponse | None:
    """Edit an account

     Changes the fields given: the name (VK shows it with the next login), the
    webhook and the event subscription. A field left out stays. The account token, the login and the
    page stay. The
    answer has no token and no webhook.

    Args:
        userid (str):
        body (EditUserBody): Each field given replaces the account's; each left out stays.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditUserResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            userid=userid,
            client=client,
            body=body,
        )
    ).parsed
