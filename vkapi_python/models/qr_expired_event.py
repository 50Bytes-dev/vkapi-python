from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QRExpiredEvent")


@_attrs_define
class QRExpiredEvent:
    """A QR login ended without logging in.

    Attributes:
        type_ (Literal['QRExpired']):
        reason (str): `login_expired`, `login_rejected` (declined on the phone), `login_failed` (also when VK has not
            answered the login's poll for 5 minutes, or failed it five times in a row), or `login_limited` (2.1.0: VK
            answered the poll with a flood answer five times in a row) Example: login_expired.
        user_id (str): The account id (`userID` and `instanceID` are the same) Example:
            6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
        instance_id (str): The account id (`userID` and `instanceID` are the same) Example:
            6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
        instance_name (str): The account name Example: retail-12-vk-34.
        event_timestamp (int): Unix time in seconds, set when the event happened; a retry keeps it Example: 1793001234.
        retry_after_ms (int | Unset): With `login_limited` (2.1.0): in how many milliseconds a connect may start a login
            again Example: 240000.
    """

    type_: Literal["QRExpired"]
    reason: str
    user_id: str
    instance_id: str
    instance_name: str
    event_timestamp: int
    retry_after_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        reason = self.reason

        user_id = self.user_id

        instance_id = self.instance_id

        instance_name = self.instance_name

        event_timestamp = self.event_timestamp

        retry_after_ms = self.retry_after_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "reason": reason,
                "userID": user_id,
                "instanceID": instance_id,
                "instanceName": instance_name,
                "eventTimestamp": event_timestamp,
            }
        )
        if retry_after_ms is not UNSET:
            field_dict["retryAfterMs"] = retry_after_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["QRExpired"], d.pop("type"))
        if type_ != "QRExpired":
            raise ValueError(f"type must match const 'QRExpired', got '{type_}'")

        reason = d.pop("reason")

        user_id = d.pop("userID")

        instance_id = d.pop("instanceID")

        instance_name = d.pop("instanceName")

        event_timestamp = d.pop("eventTimestamp")

        retry_after_ms = d.pop("retryAfterMs", UNSET)

        qr_expired_event = cls(
            type_=type_,
            reason=reason,
            user_id=user_id,
            instance_id=instance_id,
            instance_name=instance_name,
            event_timestamp=event_timestamp,
            retry_after_ms=retry_after_ms,
        )

        qr_expired_event.additional_properties = d
        return qr_expired_event

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
