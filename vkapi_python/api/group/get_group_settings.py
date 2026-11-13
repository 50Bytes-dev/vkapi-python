from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.group_settings_response import GroupSettingsResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    group_id: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["groupId"] = group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/group/settings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GroupSettingsResponse | None:
    if response.status_code == 200:
        response_200 = GroupSettingsResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | GroupSettingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group_id: int,
) -> Response[ErrorResponse | GroupSettingsResponse]:
    r"""The settings of a community the page manages

     The settings of a community the page manages (`groups.getSettings`), as
    VK wrote them: about 40 KB, most of it the tree of categories. Of a
    community the page does not manage VK answers 15 \"only group admin\":
    `group_refused`, no pause. One VK call, within 8 s (2.4.0).

    Args:
        group_id (int):  Example: -210132800.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GroupSettingsResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group_id: int,
) -> ErrorResponse | GroupSettingsResponse | None:
    r"""The settings of a community the page manages

     The settings of a community the page manages (`groups.getSettings`), as
    VK wrote them: about 40 KB, most of it the tree of categories. Of a
    community the page does not manage VK answers 15 \"only group admin\":
    `group_refused`, no pause. One VK call, within 8 s (2.4.0).

    Args:
        group_id (int):  Example: -210132800.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GroupSettingsResponse
    """

    return sync_detailed(
        client=client,
        group_id=group_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group_id: int,
) -> Response[ErrorResponse | GroupSettingsResponse]:
    r"""The settings of a community the page manages

     The settings of a community the page manages (`groups.getSettings`), as
    VK wrote them: about 40 KB, most of it the tree of categories. Of a
    community the page does not manage VK answers 15 \"only group admin\":
    `group_refused`, no pause. One VK call, within 8 s (2.4.0).

    Args:
        group_id (int):  Example: -210132800.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GroupSettingsResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group_id: int,
) -> ErrorResponse | GroupSettingsResponse | None:
    r"""The settings of a community the page manages

     The settings of a community the page manages (`groups.getSettings`), as
    VK wrote them: about 40 KB, most of it the tree of categories. Of a
    community the page does not manage VK answers 15 \"only group admin\":
    `group_refused`, no pause. One VK call, within 8 s (2.4.0).

    Args:
        group_id (int):  Example: -210132800.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GroupSettingsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            group_id=group_id,
        )
    ).parsed
