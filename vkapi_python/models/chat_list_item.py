from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatListItem")


@_attrs_define
class ChatListItem:
    """
    Attributes:
        chat_id (int): VK's peer_id: a person's id, 2000000000 + a group chat's id, or a
            community's id negated. A person or a group chat goes to
            `POST /chat/send/text` as is; a community does not. Example: 2000000001.
        type_ (str): VK's peer type: `user`, `chat`, `group` or `email` Example: chat.
        local_id (int): VK's local_id; the chat's own number for a chat Example: 1.
        title (str): The chat's title, the person's or the community's name; empty when VK gives none Example: Тестим
            лимиты 1.
        can_write (bool): Whether the page may write there
        unread_count (int):
        members_count (int | Unset): A group chat's member count Example: 3.
        state (str | Unset): The page's state in a group chat: `in`, `kicked`, `left` Example: in.
        is_channel (bool | Unset): Present (true) when a group chat is a community channel
        cant_write_reason (int | Unset): VK's reason code when the page may not write (18, 900, 902, 917, ...) Example:
            917.
        last_message_id (int | Unset): The last message's id Example: 12030.
        last_message_date (int | Unset): The last message's unix time; a search gives none Example: 1793789474.
        photo (str | Unset): A 100 px picture, when VK has one Example: https://sun9-1.userapi.com/photo.jpg.
    """

    chat_id: int
    type_: str
    local_id: int
    title: str
    can_write: bool
    unread_count: int
    members_count: int | Unset = UNSET
    state: str | Unset = UNSET
    is_channel: bool | Unset = UNSET
    cant_write_reason: int | Unset = UNSET
    last_message_id: int | Unset = UNSET
    last_message_date: int | Unset = UNSET
    photo: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        type_ = self.type_

        local_id = self.local_id

        title = self.title

        can_write = self.can_write

        unread_count = self.unread_count

        members_count = self.members_count

        state = self.state

        is_channel = self.is_channel

        cant_write_reason = self.cant_write_reason

        last_message_id = self.last_message_id

        last_message_date = self.last_message_date

        photo = self.photo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
                "type": type_,
                "localId": local_id,
                "title": title,
                "canWrite": can_write,
                "unreadCount": unread_count,
            }
        )
        if members_count is not UNSET:
            field_dict["membersCount"] = members_count
        if state is not UNSET:
            field_dict["state"] = state
        if is_channel is not UNSET:
            field_dict["isChannel"] = is_channel
        if cant_write_reason is not UNSET:
            field_dict["cantWriteReason"] = cant_write_reason
        if last_message_id is not UNSET:
            field_dict["lastMessageId"] = last_message_id
        if last_message_date is not UNSET:
            field_dict["lastMessageDate"] = last_message_date
        if photo is not UNSET:
            field_dict["photo"] = photo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId")

        type_ = d.pop("type")

        local_id = d.pop("localId")

        title = d.pop("title")

        can_write = d.pop("canWrite")

        unread_count = d.pop("unreadCount")

        members_count = d.pop("membersCount", UNSET)

        state = d.pop("state", UNSET)

        is_channel = d.pop("isChannel", UNSET)

        cant_write_reason = d.pop("cantWriteReason", UNSET)

        last_message_id = d.pop("lastMessageId", UNSET)

        last_message_date = d.pop("lastMessageDate", UNSET)

        photo = d.pop("photo", UNSET)

        chat_list_item = cls(
            chat_id=chat_id,
            type_=type_,
            local_id=local_id,
            title=title,
            can_write=can_write,
            unread_count=unread_count,
            members_count=members_count,
            state=state,
            is_channel=is_channel,
            cant_write_reason=cant_write_reason,
            last_message_id=last_message_id,
            last_message_date=last_message_date,
            photo=photo,
        )

        chat_list_item.additional_properties = d
        return chat_list_item

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
