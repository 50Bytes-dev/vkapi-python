from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendTextBody")


@_attrs_define
class SendTextBody:
    """
    Attributes:
        chat_id (int): The recipient. A VK user id, `1 <= chatId < 1900000000` or
            `200000000000 <= chatId < 1000000000000`; or a group chat's peer id,
            `2000000001 <= chatId <= 2100000000` (2e9 + the chat's number as this
            page sees it). Anything else answers `invalid_target`. Example: 987654321.
        text (str): The message. VK refuses an empty text (`send_rejected`). Example: Заказ 123 готов к выдаче.
        ref (str | Unset): Optional caller's id of the message, at most 128 bytes. A send answered
            `send_failed` with a `ref` is confirmed later by a `MessageOutcome`
            event carrying it, when the account is subscribed to it. Example: order-123-ready.
        notify (bool | Unset): Read and ignored (kept from maxapi).
        reply_to (int | Unset): Read and ignored (kept from maxapi).
        phone (str | Unset): Not supported (VK has no lookup by phone); a body without a valid `chatId` answers
            `invalid_target`.
    """

    chat_id: int
    text: str
    ref: str | Unset = UNSET
    notify: bool | Unset = UNSET
    reply_to: int | Unset = UNSET
    phone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        text = self.text

        ref = self.ref

        notify = self.notify

        reply_to = self.reply_to

        phone = self.phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
                "text": text,
            }
        )
        if ref is not UNSET:
            field_dict["ref"] = ref
        if notify is not UNSET:
            field_dict["notify"] = notify
        if reply_to is not UNSET:
            field_dict["replyTo"] = reply_to
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId")

        text = d.pop("text")

        ref = d.pop("ref", UNSET)

        notify = d.pop("notify", UNSET)

        reply_to = d.pop("replyTo", UNSET)

        phone = d.pop("phone", UNSET)

        send_text_body = cls(
            chat_id=chat_id,
            text=text,
            ref=ref,
            notify=notify,
            reply_to=reply_to,
            phone=phone,
        )

        send_text_body.additional_properties = d
        return send_text_body

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
