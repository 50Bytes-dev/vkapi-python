from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddUserBody")


@_attrs_define
class AddUserBody:
    """
    Attributes:
        name (str | Unset): Account name. VK shows the login to the owner as `VKAPI_DEVICE_NAME`,
            a space and this name. Not validated. Example: retail-12-vk-34.
        webhook (str | Unset): Where events go, used exactly as given (`?secret=` included). Empty means no events.
            Example: https://retail.example/api/messenger/webhook/34?secret=s3cr3t.
        events (str | Unset): Comma-separated event subscription of `EventType` names; other names, maxapi's `All`
            included,
            are dropped, so `All` subscribes to nothing. `POST /session/connect` overwrites it with `subscribe`. Example:
            Sync,QRAuthorized,AuthExpired,Disconnected,QRGenerated,QRScanned,QRCodeRequired,QRExpired,MessageOutcome.
    """

    name: str | Unset = UNSET
    webhook: str | Unset = UNSET
    events: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        webhook = self.webhook

        events = self.events

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if webhook is not UNSET:
            field_dict["webhook"] = webhook
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        webhook = d.pop("webhook", UNSET)

        events = d.pop("events", UNSET)

        add_user_body = cls(
            name=name,
            webhook=webhook,
            events=events,
        )

        add_user_body.additional_properties = d
        return add_user_body

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
