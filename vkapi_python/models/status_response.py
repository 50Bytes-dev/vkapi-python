from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusResponse")


@_attrs_define
class StatusResponse:
    """
    Attributes:
        success (bool):  Example: True.
        connected (bool): A stored VK login the account has not disconnected, and either the
            page is paused or the last check of the login did not fail on the
            network.
        authenticated (bool): A VK token is stored, even when disconnected
        logged_in (bool): The same as `connected` (kept from maxapi)
        max_user_id (int): The VK id of the stored login's page; 0 when no token is stored Example: 123456789.
        name (str | Unset): The page's name, as VK last gave it (after the login, then on each check); only with a
            stored token Example: Иван Петров.
        photo (str | Unset): The page's 100 px photo, as VK last gave it; only with a stored token Example:
            https://sun9-1.userapi.com/photo.jpg.
        paused (bool | Unset): Only for a stored, connected login. Read it before `connected`.
        pause_reason (str | Unset): Why sending from the page is paused: `captcha` (VK error 14 the gateway
            did not solve), `spam` (7, 9, 17, 29, 983, 984) or `access_denied` (15). Example: spam.
        upstream_code (str | Unset): Only while paused; the VK error that paused the page, as a string Example: 14.
        captcha_solve_error (str | Unset): Why the gateway did not solve the captcha that paused the page on a send
            (solving on): `timeout`, `bot`, `page_changed`, `failed`, `rejected` (VK
            asked again after the answer) or `not_tried` (no `captcha_sid`, or the
            captcha page was not on a VK host). `bot` and `page_changed` mean the
            solver needs a new browser recording. Example: timeout.
        captcha_image (str | Unset): Only while paused for a captcha, for the account VK gave it to, once
            downloaded and for 5 minutes: a `data:image/(png|jpeg|gif);base64,...`
            URI. Answer it with `POST /session/resume` `captchaKey`. Example: data:image/png;base64,iVBORw0KGgo....
    """

    success: bool
    connected: bool
    authenticated: bool
    logged_in: bool
    max_user_id: int
    name: str | Unset = UNSET
    photo: str | Unset = UNSET
    paused: bool | Unset = UNSET
    pause_reason: str | Unset = UNSET
    upstream_code: str | Unset = UNSET
    captcha_solve_error: str | Unset = UNSET
    captcha_image: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        connected = self.connected

        authenticated = self.authenticated

        logged_in = self.logged_in

        max_user_id = self.max_user_id

        name = self.name

        photo = self.photo

        paused = self.paused

        pause_reason = self.pause_reason

        upstream_code = self.upstream_code

        captcha_solve_error = self.captcha_solve_error

        captcha_image = self.captcha_image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "connected": connected,
                "authenticated": authenticated,
                "loggedIn": logged_in,
                "maxUserID": max_user_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if photo is not UNSET:
            field_dict["photo"] = photo
        if paused is not UNSET:
            field_dict["paused"] = paused
        if pause_reason is not UNSET:
            field_dict["pauseReason"] = pause_reason
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code
        if captcha_solve_error is not UNSET:
            field_dict["captchaSolveError"] = captcha_solve_error
        if captcha_image is not UNSET:
            field_dict["captchaImage"] = captcha_image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        connected = d.pop("connected")

        authenticated = d.pop("authenticated")

        logged_in = d.pop("loggedIn")

        max_user_id = d.pop("maxUserID")

        name = d.pop("name", UNSET)

        photo = d.pop("photo", UNSET)

        paused = d.pop("paused", UNSET)

        pause_reason = d.pop("pauseReason", UNSET)

        upstream_code = d.pop("upstreamCode", UNSET)

        captcha_solve_error = d.pop("captchaSolveError", UNSET)

        captcha_image = d.pop("captchaImage", UNSET)

        status_response = cls(
            success=success,
            connected=connected,
            authenticated=authenticated,
            logged_in=logged_in,
            max_user_id=max_user_id,
            name=name,
            photo=photo,
            paused=paused,
            pause_reason=pause_reason,
            upstream_code=upstream_code,
            captcha_solve_error=captcha_solve_error,
            captcha_image=captcha_image,
        )

        status_response.additional_properties = d
        return status_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
