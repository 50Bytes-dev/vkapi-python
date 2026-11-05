from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageOutcomeEvent")


@_attrs_define
class MessageOutcomeEvent:
    """Whether a send with a `ref` that answered `send_failed` arrived. Sent once,
    a minute or more after the send, when VK told.

        Attributes:
            type_ (Literal['MessageOutcome']):
            ref (str): The send's `ref` Example: order-123-ready.
            chat_id (int): The send's `chatId` Example: 2000000001.
            delivered (bool): true when VK has the message in the dialog
            max_user_id (int): The VK id of the owner's page (the name is kept from maxapi) Example: 123456789.
            user_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_name (str): The account name Example: retail-12-vk-34.
            event_timestamp (int): Unix time in seconds, set when the event happened; a retry keeps it Example: 1793001234.
            message_id (str | Unset): VK's message id, as a string (2.0.0); only when delivered Example: 12030.
    """

    type_: Literal["MessageOutcome"]
    ref: str
    chat_id: int
    delivered: bool
    max_user_id: int
    user_id: str
    instance_id: str
    instance_name: str
    event_timestamp: int
    message_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        ref = self.ref

        chat_id = self.chat_id

        delivered = self.delivered

        max_user_id = self.max_user_id

        user_id = self.user_id

        instance_id = self.instance_id

        instance_name = self.instance_name

        event_timestamp = self.event_timestamp

        message_id = self.message_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "ref": ref,
                "chatId": chat_id,
                "delivered": delivered,
                "maxUserID": max_user_id,
                "userID": user_id,
                "instanceID": instance_id,
                "instanceName": instance_name,
                "eventTimestamp": event_timestamp,
            }
        )
        if message_id is not UNSET:
            field_dict["messageId"] = message_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["MessageOutcome"], d.pop("type"))
        if type_ != "MessageOutcome":
            raise ValueError(f"type must match const 'MessageOutcome', got '{type_}'")

        ref = d.pop("ref")

        chat_id = d.pop("chatId")

        delivered = d.pop("delivered")

        max_user_id = d.pop("maxUserID")

        user_id = d.pop("userID")

        instance_id = d.pop("instanceID")

        instance_name = d.pop("instanceName")

        event_timestamp = d.pop("eventTimestamp")

        message_id = d.pop("messageId", UNSET)

        message_outcome_event = cls(
            type_=type_,
            ref=ref,
            chat_id=chat_id,
            delivered=delivered,
            max_user_id=max_user_id,
            user_id=user_id,
            instance_id=instance_id,
            instance_name=instance_name,
            event_timestamp=event_timestamp,
            message_id=message_id,
        )

        message_outcome_event.additional_properties = d
        return message_outcome_event

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
