from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

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
        text (str | Unset): The message; may be empty when there are attachments. Example: Заказ 123 готов к выдаче.
        attachments (list[str] | Unset): Up to 10 VK attachments, as `POST /media/photo` and `POST
            /wall/photos` give them (`photo<owner_id>_<id>[_<access_key>]`). They
            go with any dialog of the page.
        dont_parse_links (bool | Unset): No link preview (VK's `dont_parse_links`)
        ref (str | Unset): Optional caller's id of the message, at most 128 bytes. A send answered
            `send_failed` with a `ref` is confirmed later by a `MessageOutcome`
            event carrying it, when the account is subscribed to it. Example: order-123-ready.
        notify (bool | Unset): Read and ignored (kept from maxapi).
        reply_to (int | Unset): Read and ignored (kept from maxapi).
        phone (str | Unset): Not supported (VK has no lookup by phone); a body without a valid `chatId` answers
            `invalid_target`.
    """

    chat_id: int
    text: str | Unset = UNSET
    attachments: list[str] | Unset = UNSET
    dont_parse_links: bool | Unset = UNSET
    ref: str | Unset = UNSET
    notify: bool | Unset = UNSET
    reply_to: int | Unset = UNSET
    phone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        text = self.text

        attachments: list[str] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments

        dont_parse_links = self.dont_parse_links

        ref = self.ref

        notify = self.notify

        reply_to = self.reply_to

        phone = self.phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if dont_parse_links is not UNSET:
            field_dict["dontParseLinks"] = dont_parse_links
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

        text = d.pop("text", UNSET)

        attachments = cast(list[str], d.pop("attachments", UNSET))

        dont_parse_links = d.pop("dontParseLinks", UNSET)

        ref = d.pop("ref", UNSET)

        notify = d.pop("notify", UNSET)

        reply_to = d.pop("replyTo", UNSET)

        phone = d.pop("phone", UNSET)

        send_text_body = cls(
            chat_id=chat_id,
            text=text,
            attachments=attachments,
            dont_parse_links=dont_parse_links,
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
