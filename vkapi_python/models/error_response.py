from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """The error body of every call. `401` has no `code`. A send or chat list
    answer may also carry `upstreamCode` and the page's pause.

        Attributes:
            success (bool):
            error (str): A fixed English text per case; never VK's text. Do not branch on it. Example: VK did not confirm
                the message; it may have been delivered.
            code (str | Unset): The machine code; absent on 401. Generic: `INVALID_INPUT`,
                `INTERNAL_ERROR`. Login: `login_unavailable`, `login_rate_limited`,
                `code_required`, `code_not_required`, `already_logged_in`,
                `invalid_code`, `login_expired`, `login_rejected`, `login_failed`.
                Delivery: `not_connected`, `invalid_target`, `address_not_found`,
                `address_refused`, `send_rejected`, `message_rejected`, `send_failed`.
                Chat list: `page_paused`, `vk_error`. Example: send_failed.
            upstream_code (str | Unset): The VK error number behind the answer as a string (`"984"`), or `"busy"`. Absent
                when VK did not answer with an error. Example: 984.
            paused (bool | Unset): Present (true) only when the page is paused; stop choosing every connection of this page.
            pause_reason (str | Unset): Why sending from the page is paused: `captcha` (VK error 14 the gateway
                did not solve), `spam` (7, 9, 17, 29, 983, 984) or `access_denied` (15). Example: spam.
            captcha_solve_error (str | Unset): Why the gateway did not solve the captcha that paused the page on a send
                (solving on): `timeout`, `bot`, `page_changed`, `failed`, `rejected` (VK
                asked again after the answer) or `not_tried` (no `captcha_sid`, or the
                captcha page was not on a VK host). `bot` and `page_changed` mean the
                solver needs a new browser recording. Example: timeout.
    """

    success: bool
    error: str
    code: str | Unset = UNSET
    upstream_code: str | Unset = UNSET
    paused: bool | Unset = UNSET
    pause_reason: str | Unset = UNSET
    captcha_solve_error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        error = self.error

        code = self.code

        upstream_code = self.upstream_code

        paused = self.paused

        pause_reason = self.pause_reason

        captcha_solve_error = self.captcha_solve_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "error": error,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code
        if paused is not UNSET:
            field_dict["paused"] = paused
        if pause_reason is not UNSET:
            field_dict["pauseReason"] = pause_reason
        if captcha_solve_error is not UNSET:
            field_dict["captchaSolveError"] = captcha_solve_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        error = d.pop("error")

        code = d.pop("code", UNSET)

        upstream_code = d.pop("upstreamCode", UNSET)

        paused = d.pop("paused", UNSET)

        pause_reason = d.pop("pauseReason", UNSET)

        captcha_solve_error = d.pop("captchaSolveError", UNSET)

        error_response = cls(
            success=success,
            error=error,
            code=code,
            upstream_code=upstream_code,
            paused=paused,
            pause_reason=pause_reason,
            captcha_solve_error=captcha_solve_error,
        )

        error_response.additional_properties = d
        return error_response

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
