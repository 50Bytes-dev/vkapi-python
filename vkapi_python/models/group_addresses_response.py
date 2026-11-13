from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_addresses_response_addresses_item import GroupAddressesResponseAddressesItem


T = TypeVar("T", bound="GroupAddressesResponse")


@_attrs_define
class GroupAddressesResponse:
    """
    Attributes:
        success (bool):  Example: True.
        owner_id (int):  Example: -210132800.
        community_id (int):  Example: 210132800.
        total (int): VK's count of them all
        offset (int):
        count (int): How many addresses this page has
        addresses (list[GroupAddressesResponseAddressesItem]): VK's address objects as VK wrote them
        next_offset (int | Unset): The `offset` to ask for next; absent on the last page
    """

    success: bool
    owner_id: int
    community_id: int
    total: int
    offset: int
    count: int
    addresses: list[GroupAddressesResponseAddressesItem]
    next_offset: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        owner_id = self.owner_id

        community_id = self.community_id

        total = self.total

        offset = self.offset

        count = self.count

        addresses = []
        for addresses_item_data in self.addresses:
            addresses_item = addresses_item_data.to_dict()
            addresses.append(addresses_item)

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
                "addresses": addresses,
            }
        )
        if next_offset is not UNSET:
            field_dict["nextOffset"] = next_offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_addresses_response_addresses_item import GroupAddressesResponseAddressesItem

        d = dict(src_dict)
        success = d.pop("success")

        owner_id = d.pop("ownerId")

        community_id = d.pop("communityId")

        total = d.pop("total")

        offset = d.pop("offset")

        count = d.pop("count")

        addresses = []
        _addresses = d.pop("addresses")
        for addresses_item_data in _addresses:
            addresses_item = GroupAddressesResponseAddressesItem.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        next_offset = d.pop("nextOffset", UNSET)

        group_addresses_response = cls(
            success=success,
            owner_id=owner_id,
            community_id=community_id,
            total=total,
            offset=offset,
            count=count,
            addresses=addresses,
            next_offset=next_offset,
        )

        group_addresses_response.additional_properties = d
        return group_addresses_response

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
