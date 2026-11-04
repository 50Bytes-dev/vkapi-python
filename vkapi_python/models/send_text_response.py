from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SendTextResponse")


@_attrs_define
class SendTextResponse:
    """
    Attributes:
        success (bool):  Example: True.
        message_id (int): VK's message id; 0 when VK answered without one Example: 4711.
        chat_id (int): The request's `chatId` Example: 987654321.
    """

    success: bool
    message_id: int
    chat_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message_id = self.message_id

        chat_id = self.chat_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "messageId": message_id,
                "chatId": chat_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        message_id = d.pop("messageId")

        chat_id = d.pop("chatId")

        send_text_response = cls(
            success=success,
            message_id=message_id,
            chat_id=chat_id,
        )

        send_text_response.additional_properties = d
        return send_text_response

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
