from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.community import Community


T = TypeVar("T", bound="GroupInfoResponse")


@_attrs_define
class GroupInfoResponse:
    """
    Attributes:
        success (bool):  Example: True.
        communities (list[Community]): In VK's order; an id of no community is an empty one
    """

    success: bool
    communities: list[Community]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        communities = []
        for communities_item_data in self.communities:
            communities_item = communities_item_data.to_dict()
            communities.append(communities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "communities": communities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.community import Community

        d = dict(src_dict)
        success = d.pop("success")

        communities = []
        _communities = d.pop("communities")
        for communities_item_data in _communities:
            communities_item = Community.from_dict(communities_item_data)

            communities.append(communities_item)

        group_info_response = cls(
            success=success,
            communities=communities,
        )

        group_info_response.additional_properties = d
        return group_info_response

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
