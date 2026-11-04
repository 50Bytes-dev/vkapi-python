from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_list_item import ChatListItem


T = TypeVar("T", bound="ChatListResponse")


@_attrs_define
class ChatListResponse:
    """
    Attributes:
        success (bool):  Example: True.
        offset (int): Where this page starts
        count (int): How many items this page has Example: 2.
        items (list[ChatListItem]):
        total (int | Unset): List only (absent with `q`); VK's count of the conversations under the filter Example: 12.
        next_offset (int | Unset): Present when another page follows; the `offset` to ask for next Example: 2.
    """

    success: bool
    offset: int
    count: int
    items: list[ChatListItem]
    total: int | Unset = UNSET
    next_offset: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        offset = self.offset

        count = self.count

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        total = self.total

        next_offset = self.next_offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "offset": offset,
                "count": count,
                "items": items,
            }
        )
        if total is not UNSET:
            field_dict["total"] = total
        if next_offset is not UNSET:
            field_dict["nextOffset"] = next_offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_list_item import ChatListItem

        d = dict(src_dict)
        success = d.pop("success")

        offset = d.pop("offset")

        count = d.pop("count")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ChatListItem.from_dict(items_item_data)

            items.append(items_item)

        total = d.pop("total", UNSET)

        next_offset = d.pop("nextOffset", UNSET)

        chat_list_response = cls(
            success=success,
            offset=offset,
            count=count,
            items=items,
            total=total,
            next_offset=next_offset,
        )

        chat_list_response.additional_properties = d
        return chat_list_response

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
