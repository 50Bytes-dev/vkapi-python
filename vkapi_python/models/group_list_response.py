from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.community import Community


T = TypeVar("T", bound="GroupListResponse")


@_attrs_define
class GroupListResponse:
    """
    Attributes:
        success (bool):  Example: True.
        user_id (int): Whose communities these are Example: 1127016903.
        total (int): VK's count of them all, the banned communities VK leaves out of the page included Example: 1.
        offset (int):
        count (int): How many communities this page has Example: 1.
        communities (list[Community]):
        next_offset (int | Unset): `offset` + `count` asked, when that is under `total`; absent on the last page
        last_updated_time (int | Unset): VK's `last_updated_time` (undocumented; absent with a filter) Example:
            1794512003.
    """

    success: bool
    user_id: int
    total: int
    offset: int
    count: int
    communities: list[Community]
    next_offset: int | Unset = UNSET
    last_updated_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        user_id = self.user_id

        total = self.total

        offset = self.offset

        count = self.count

        communities = []
        for communities_item_data in self.communities:
            communities_item = communities_item_data.to_dict()
            communities.append(communities_item)

        next_offset = self.next_offset

        last_updated_time = self.last_updated_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "userId": user_id,
                "total": total,
                "offset": offset,
                "count": count,
                "communities": communities,
            }
        )
        if next_offset is not UNSET:
            field_dict["nextOffset"] = next_offset
        if last_updated_time is not UNSET:
            field_dict["lastUpdatedTime"] = last_updated_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.community import Community

        d = dict(src_dict)
        success = d.pop("success")

        user_id = d.pop("userId")

        total = d.pop("total")

        offset = d.pop("offset")

        count = d.pop("count")

        communities = []
        _communities = d.pop("communities")
        for communities_item_data in _communities:
            communities_item = Community.from_dict(communities_item_data)

            communities.append(communities_item)

        next_offset = d.pop("nextOffset", UNSET)

        last_updated_time = d.pop("lastUpdatedTime", UNSET)

        group_list_response = cls(
            success=success,
            user_id=user_id,
            total=total,
            offset=offset,
            count=count,
            communities=communities,
            next_offset=next_offset,
            last_updated_time=last_updated_time,
        )

        group_list_response.additional_properties = d
        return group_list_response

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
