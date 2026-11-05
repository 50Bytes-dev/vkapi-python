from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.participant import Participant


T = TypeVar("T", bound="ChatMembersResponse")


@_attrs_define
class ChatMembersResponse:
    """
    Attributes:
        success (bool):  Example: True.
        chat_id (int):  Example: 2000000001.
        total (int): The chat's members in all, as VK counts them Example: 450.
        offset (int):
        count (int): How many in `items` Example: 200.
        items (list[Participant]):
        next_offset (int | Unset): Where the next page starts; absent on the last Example: 200.
    """

    success: bool
    chat_id: int
    total: int
    offset: int
    count: int
    items: list[Participant]
    next_offset: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        chat_id = self.chat_id

        total = self.total

        offset = self.offset

        count = self.count

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_offset = self.next_offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "chatId": chat_id,
                "total": total,
                "offset": offset,
                "count": count,
                "items": items,
            }
        )
        if next_offset is not UNSET:
            field_dict["nextOffset"] = next_offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.participant import Participant

        d = dict(src_dict)
        success = d.pop("success")

        chat_id = d.pop("chatId")

        total = d.pop("total")

        offset = d.pop("offset")

        count = d.pop("count")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Participant.from_dict(items_item_data)

            items.append(items_item)

        next_offset = d.pop("nextOffset", UNSET)

        chat_members_response = cls(
            success=success,
            chat_id=chat_id,
            total=total,
            offset=offset,
            count=count,
            items=items,
            next_offset=next_offset,
        )

        chat_members_response.additional_properties = d
        return chat_members_response

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
