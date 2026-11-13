from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupMembersResponse")


@_attrs_define
class GroupMembersResponse:
    """
    Attributes:
        success (bool):  Example: True.
        owner_id (int):  Example: -210132800.
        community_id (int):  Example: 210132800.
        total (int): VK's count of them all Example: 2.
        offset (int):
        count (int): How many members this page has Example: 2.
        members (list[Any]): As VK wrote them: user ids, or user objects with `fields` or `filter=managers` (with `role`
            and `permissions`) Example: [{'id': 1127016903, 'role': 'administrator', 'permissions': ['ads']}].
        next_offset (int | Unset): The `offset` to ask for next; absent on the last page
    """

    success: bool
    owner_id: int
    community_id: int
    total: int
    offset: int
    count: int
    members: list[Any]
    next_offset: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        owner_id = self.owner_id

        community_id = self.community_id

        total = self.total

        offset = self.offset

        count = self.count

        members = self.members

        next_offset = self.next_offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "ownerId": owner_id,
                "communityId": community_id,
                "total": total,
                "offset": offset,
                "count": count,
                "members": members,
            }
        )
        if next_offset is not UNSET:
            field_dict["nextOffset"] = next_offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        owner_id = d.pop("ownerId")

        community_id = d.pop("communityId")

        total = d.pop("total")

        offset = d.pop("offset")

        count = d.pop("count")

        members = cast(list[Any], d.pop("members"))

        next_offset = d.pop("nextOffset", UNSET)

        group_members_response = cls(
            success=success,
            owner_id=owner_id,
            community_id=community_id,
            total=total,
            offset=offset,
            count=count,
            members=members,
            next_offset=next_offset,
        )

        group_members_response.additional_properties = d
        return group_members_response

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
