from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CommunityVk")


@_attrs_define
class CommunityVk:
    """VK's community object as VK wrote it: every field VK gives, of mixed
    types (`is_business` a string "0", `est_date` "0.0", flags 0/1 or
    true/false), and fields VK adds without notice

        Example:
            {'id': 210132800, 'name': 'Тестовое сообщество', 'screen_name': 'club210132800', 'is_closed': 0, 'type': 'page',
                'is_admin': 1, 'admin_level': 3, 'is_member': 1, 'members_count': 2}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        community_vk = cls()

        community_vk.additional_properties = d
        return community_vk

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
