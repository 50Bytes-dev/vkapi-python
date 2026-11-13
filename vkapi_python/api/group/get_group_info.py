from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.group_info_response import GroupInfoResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    group_ids: list[str],
    fields: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_group_ids = group_ids

    params["groupIds"] = json_group_ids

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/group/info",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GroupInfoResponse | None:
    if response.status_code == 200:
        response_200 = GroupInfoResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | GroupInfoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group_ids: list[str],
    fields: list[str] | Unset = UNSET,
) -> Response[ErrorResponse | GroupInfoResponse]:
    """Communities by id or screen name, with every field VK gives

     Up to 500 communities by id or screen name (`groups.getById`), in VK's
    order, each with the gateway's fields and VK's object as VK wrote it
    (`vk`); by default with every field the gateway knows. VK takes no
    negative id (the gateway makes it positive), drops ids past 500 without
    a word (the gateway refuses more), and fails the whole call with 100
    for one screen name it does not know (`400`). An id of no community
    gives an empty one (no name, the default photo), not an error. A
    screen name VK follows to the community's present one. One VK call,
    within 8 s plus 50 ms a community asked (2.4.0).

    Args:
        group_ids (list[str]):  Example: ['210132800', '-219994268', 'apiclub'].
        fields (list[str] | Unset):  Example: ['members_count', 'counters'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GroupInfoResponse]
    """

    kwargs = _get_kwargs(
        group_ids=group_ids,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group_ids: list[str],
    fields: list[str] | Unset = UNSET,
) -> ErrorResponse | GroupInfoResponse | None:
    """Communities by id or screen name, with every field VK gives

     Up to 500 communities by id or screen name (`groups.getById`), in VK's
    order, each with the gateway's fields and VK's object as VK wrote it
    (`vk`); by default with every field the gateway knows. VK takes no
    negative id (the gateway makes it positive), drops ids past 500 without
    a word (the gateway refuses more), and fails the whole call with 100
    for one screen name it does not know (`400`). An id of no community
    gives an empty one (no name, the default photo), not an error. A
    screen name VK follows to the community's present one. One VK call,
    within 8 s plus 50 ms a community asked (2.4.0).

    Args:
        group_ids (list[str]):  Example: ['210132800', '-219994268', 'apiclub'].
        fields (list[str] | Unset):  Example: ['members_count', 'counters'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GroupInfoResponse
    """

    return sync_detailed(
        client=client,
        group_ids=group_ids,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group_ids: list[str],
    fields: list[str] | Unset = UNSET,
) -> Response[ErrorResponse | GroupInfoResponse]:
    """Communities by id or screen name, with every field VK gives

     Up to 500 communities by id or screen name (`groups.getById`), in VK's
    order, each with the gateway's fields and VK's object as VK wrote it
    (`vk`); by default with every field the gateway knows. VK takes no
    negative id (the gateway makes it positive), drops ids past 500 without
    a word (the gateway refuses more), and fails the whole call with 100
    for one screen name it does not know (`400`). An id of no community
    gives an empty one (no name, the default photo), not an error. A
    screen name VK follows to the community's present one. One VK call,
    within 8 s plus 50 ms a community asked (2.4.0).

    Args:
        group_ids (list[str]):  Example: ['210132800', '-219994268', 'apiclub'].
        fields (list[str] | Unset):  Example: ['members_count', 'counters'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GroupInfoResponse]
    """

    kwargs = _get_kwargs(
        group_ids=group_ids,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group_ids: list[str],
    fields: list[str] | Unset = UNSET,
) -> ErrorResponse | GroupInfoResponse | None:
    """Communities by id or screen name, with every field VK gives

     Up to 500 communities by id or screen name (`groups.getById`), in VK's
    order, each with the gateway's fields and VK's object as VK wrote it
    (`vk`); by default with every field the gateway knows. VK takes no
    negative id (the gateway makes it positive), drops ids past 500 without
    a word (the gateway refuses more), and fails the whole call with 100
    for one screen name it does not know (`400`). An id of no community
    gives an empty one (no name, the default photo), not an error. A
    screen name VK follows to the community's present one. One VK call,
    within 8 s plus 50 ms a community asked (2.4.0).

    Args:
        group_ids (list[str]):  Example: ['210132800', '-219994268', 'apiclub'].
        fields (list[str] | Unset):  Example: ['members_count', 'counters'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GroupInfoResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            group_ids=group_ids,
            fields=fields,
        )
    ).parsed
