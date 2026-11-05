from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PausedEvent")


@_attrs_define
class PausedEvent:
    """The page is paused (2.0.0): sent to every account of the page subscribed
    to it, whichever account met the stop signal. No captcha in it.

        Attributes:
            type_ (Literal['Paused']):
            max_user_id (int): The VK id of the owner's page (the name is kept from maxapi) Example: 123456789.
            pause_reason (str): Why sending from the page is paused: `captcha` (VK error 14 the gateway
                did not solve), `spam` (7, 9, 17, 29, 983, 984) or `access_denied` (15). Example: spam.
            upstream_code (str): The VK error that paused the page Example: 984.
            user_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_name (str): The account name Example: retail-12-vk-34.
            event_timestamp (int): Unix time in seconds, set when the event happened; a retry keeps it Example: 1793001234.
            captcha_solve_error (str | Unset): Why the gateway did not solve VK's captcha (solving on): on a pause it
                set for the captcha, on any call (since 2.0.3; before, on a send), or
                on a refusal with `upstreamCode` "14" and no pause. `timeout`, `bot`,
                `page_changed`, `failed`, `rejected` (VK asked again after the answer,
                or a second captcha came in the same operation) or `not_tried` (no
                `redirect_uri` or `captcha_sid`, the captcha page not on a VK host, or
                the OAuth call of the token refresh, whose captcha is not solved). `bot` (VK's antibot answered BOT and
                offered nothing else) and `page_changed` mean the solver may need a new
                browser recording; a slider VK offered with no time left to drag it is
                `timeout`, and a slider answer VK did not take is `failed`. Example: timeout.
    """

    type_: Literal["Paused"]
    max_user_id: int
    pause_reason: str
    upstream_code: str
    user_id: str
    instance_id: str
    instance_name: str
    event_timestamp: int
    captcha_solve_error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        max_user_id = self.max_user_id

        pause_reason = self.pause_reason

        upstream_code = self.upstream_code

        user_id = self.user_id

        instance_id = self.instance_id

        instance_name = self.instance_name

        event_timestamp = self.event_timestamp

        captcha_solve_error = self.captcha_solve_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "maxUserID": max_user_id,
                "pauseReason": pause_reason,
                "upstreamCode": upstream_code,
                "userID": user_id,
                "instanceID": instance_id,
                "instanceName": instance_name,
                "eventTimestamp": event_timestamp,
            }
        )
        if captcha_solve_error is not UNSET:
            field_dict["captchaSolveError"] = captcha_solve_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["Paused"], d.pop("type"))
        if type_ != "Paused":
            raise ValueError(f"type must match const 'Paused', got '{type_}'")

        max_user_id = d.pop("maxUserID")

        pause_reason = d.pop("pauseReason")

        upstream_code = d.pop("upstreamCode")

        user_id = d.pop("userID")

        instance_id = d.pop("instanceID")

        instance_name = d.pop("instanceName")

        event_timestamp = d.pop("eventTimestamp")

        captcha_solve_error = d.pop("captchaSolveError", UNSET)

        paused_event = cls(
            type_=type_,
            max_user_id=max_user_id,
            pause_reason=pause_reason,
            upstream_code=upstream_code,
            user_id=user_id,
            instance_id=instance_id,
            instance_name=instance_name,
            event_timestamp=event_timestamp,
            captcha_solve_error=captcha_solve_error,
        )

        paused_event.additional_properties = d
        return paused_event

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
