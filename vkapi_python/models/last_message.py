from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LastMessage")


@_attrs_define
class LastMessage:
    """A conversation's last message; only with `include=lastMessage`.

    Attributes:
        message_id (str):  Example: 12030.
        date (int):  Example: 1793789474.
        from_id (int):  Example: 1127016903.
        out (bool): Sent by the page
        text (str):  Example: Привет.
        cmid (str | Unset):  Example: 77.
        attachments (int | Unset): How many attachments it has Example: 2.
    """

    message_id: str
    date: int
    from_id: int
    out: bool
    text: str
    cmid: str | Unset = UNSET
    attachments: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        date = self.date

        from_id = self.from_id

        out = self.out

        text = self.text

        cmid = self.cmid

        attachments = self.attachments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageId": message_id,
                "date": date,
                "fromId": from_id,
                "out": out,
                "text": text,
            }
        )
        if cmid is not UNSET:
            field_dict["cmid"] = cmid
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_id = d.pop("messageId")

        date = d.pop("date")

        from_id = d.pop("fromId")

        out = d.pop("out")

        text = d.pop("text")

        cmid = d.pop("cmid", UNSET)

        attachments = d.pop("attachments", UNSET)

        last_message = cls(
            message_id=message_id,
            date=date,
            from_id=from_id,
            out=out,
            text=text,
            cmid=cmid,
            attachments=attachments,
        )

        last_message.additional_properties = d
        return last_message

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
