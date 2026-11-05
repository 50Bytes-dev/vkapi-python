from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chat_list_item import ChatListItem


T = TypeVar("T", bound="ChatInfoResponse")


@_attrs_define
class ChatInfoResponse:
    """
    Attributes:
        success (bool):  Example: True.
        items (list[ChatListItem]):
        missing (list[int]): The ids asked that VK did not give the page Example: [2000000099].
    """

    success: bool
    items: list[ChatListItem]
    missing: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        missing = self.missing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "items": items,
                "missing": missing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_list_item import ChatListItem

        d = dict(src_dict)
        success = d.pop("success")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ChatListItem.from_dict(items_item_data)

            items.append(items_item)

        missing = cast(list[int], d.pop("missing"))

        chat_info_response = cls(
            success=success,
            items=items,
            missing=missing,
        )

        chat_info_response.additional_properties = d
        return chat_info_response

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
