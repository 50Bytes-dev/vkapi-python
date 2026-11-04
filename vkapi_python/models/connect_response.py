from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectResponse")


@_attrs_define
class ConnectResponse:
    """
    Attributes:
        success (bool):  Example: True.
        details (str): A human-readable summary Example: Already connected to VK.
        events (str): The stored subscription, comma-separated Example: Sync,QRAuthorized,AuthExpired.
        already_connected (bool): true when the stored login was reused; false when a QR login started
        max_user_id (int | Unset): The VK id of the owner's page; only with `alreadyConnected` true. The name is kept
            from maxapi. Example: 123456789.
        paused (bool | Unset): Whether sending from the page is paused; only with `alreadyConnected` true.
        pause_reason (str | Unset): Why sending from the page is paused: `captcha` (VK error 14 the gateway
            did not solve), `spam` (7, 9, 17, 29, 983, 984) or `access_denied` (15). Example: spam.
    """

    success: bool
    details: str
    events: str
    already_connected: bool
    max_user_id: int | Unset = UNSET
    paused: bool | Unset = UNSET
    pause_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        details = self.details

        events = self.events

        already_connected = self.already_connected

        max_user_id = self.max_user_id

        paused = self.paused

        pause_reason = self.pause_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "details": details,
                "events": events,
                "alreadyConnected": already_connected,
            }
        )
        if max_user_id is not UNSET:
            field_dict["maxUserID"] = max_user_id
        if paused is not UNSET:
            field_dict["paused"] = paused
        if pause_reason is not UNSET:
            field_dict["pauseReason"] = pause_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        details = d.pop("details")

        events = d.pop("events")

        already_connected = d.pop("alreadyConnected")

        max_user_id = d.pop("maxUserID", UNSET)

        paused = d.pop("paused", UNSET)

        pause_reason = d.pop("pauseReason", UNSET)

        connect_response = cls(
            success=success,
            details=details,
            events=events,
            already_connected=already_connected,
            max_user_id=max_user_id,
            paused=paused,
            pause_reason=pause_reason,
        )

        connect_response.additional_properties = d
        return connect_response

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
