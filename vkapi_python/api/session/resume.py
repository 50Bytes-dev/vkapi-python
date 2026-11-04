from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.resume_body import ResumeBody
from ...models.resume_response import ResumeResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ResumeBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/session/resume",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ResumeResponse | None:
    if response.status_code == 200:
        response_200 = ResumeResponse.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ResumeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ResumeBody | Unset = UNSET,
) -> Response[ErrorResponse | ResumeResponse]:
    """Resume sending from the page

     Lifts the pause of the account's VK page, for every account logged into
    it; `maxUserID` names the page. A page that is not paused answers the
    same. The body is optional: `captchaKey` is the owner's answer to the
    status's `captchaImage` and goes to VK with the account's next send. No
    VK call.

    Args:
        body (ResumeBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ResumeResponse]
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
    body: ResumeBody | Unset = UNSET,
) -> ErrorResponse | ResumeResponse | None:
    """Resume sending from the page

     Lifts the pause of the account's VK page, for every account logged into
    it; `maxUserID` names the page. A page that is not paused answers the
    same. The body is optional: `captchaKey` is the owner's answer to the
    status's `captchaImage` and goes to VK with the account's next send. No
    VK call.

    Args:
        body (ResumeBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ResumeResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ResumeBody | Unset = UNSET,
) -> Response[ErrorResponse | ResumeResponse]:
    """Resume sending from the page

     Lifts the pause of the account's VK page, for every account logged into
    it; `maxUserID` names the page. A page that is not paused answers the
    same. The body is optional: `captchaKey` is the owner's answer to the
    status's `captchaImage` and goes to VK with the account's next send. No
    VK call.

    Args:
        body (ResumeBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ResumeResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ResumeBody | Unset = UNSET,
) -> ErrorResponse | ResumeResponse | None:
    """Resume sending from the page

     Lifts the pause of the account's VK page, for every account logged into
    it; `maxUserID` names the page. A page that is not paused answers the
    same. The body is optional: `captchaKey` is the owner's answer to the
    status's `captchaImage` and goes to VK with the account's next send. No
    VK call.

    Args:
        body (ResumeBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ResumeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
