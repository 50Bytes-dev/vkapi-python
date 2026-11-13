from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.community_vk import CommunityVk


T = TypeVar("T", bound="Community")


@_attrs_define
class Community:
    """A community (2.4.0): the gateway's fields, read from VK's object, and
    the object itself as VK wrote it (`vk`). A gateway field is absent when
    VK gives none.

        Attributes:
            owner_id (int): The community's id negated, as the album calls take an owner Example: -210132800.
            community_id (int): The community's id, as VK names it Example: 210132800.
            name (str): Empty for an id of no community (VK gives an empty one) Example: Тестовое сообщество.
            screen_name (str):  Example: club210132800.
            type_ (str): VK's `group`, `page` or `event` Example: page.
            is_closed (int): VK's `is_closed`; 0 open, 1 closed, 2 private
            vk (CommunityVk): VK's community object as VK wrote it: every field VK gives, of mixed
                types (`is_business` a string "0", `est_date` "0.0", flags 0/1 or
                true/false), and fields VK adds without notice Example: {'id': 210132800, 'name': 'Тестовое сообщество',
                'screen_name': 'club210132800', 'is_closed': 0, 'type': 'page', 'is_admin': 1, 'admin_level': 3, 'is_member': 1,
                'members_count': 2}.
            is_admin (bool | Unset): Whether the page manages it; absent when VK does not say (a private community) Example:
                True.
            admin_level (int | Unset): The page's role when it manages the community; VK's 1 moderator, 2 editor, 3
                administrator Example: 3.
            is_member (bool | Unset): Whether the page is a member; absent when VK does not say Example: True.
            deactivated (str | Unset): VK's word for a community it closed, such as `banned`
            photo (str | Unset): The address of a 200 px photo, else of a 100 px one Example: https://sun9-....
    """

    owner_id: int
    community_id: int
    name: str
    screen_name: str
    type_: str
    is_closed: int
    vk: CommunityVk
    is_admin: bool | Unset = UNSET
    admin_level: int | Unset = UNSET
    is_member: bool | Unset = UNSET
    deactivated: str | Unset = UNSET
    photo: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        community_id = self.community_id

        name = self.name

        screen_name = self.screen_name

        type_ = self.type_

        is_closed = self.is_closed

        vk = self.vk.to_dict()

        is_admin = self.is_admin

        admin_level = self.admin_level

        is_member = self.is_member

        deactivated = self.deactivated

        photo = self.photo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ownerId": owner_id,
                "communityId": community_id,
                "name": name,
                "screenName": screen_name,
                "type": type_,
                "isClosed": is_closed,
                "vk": vk,
            }
        )
        if is_admin is not UNSET:
            field_dict["isAdmin"] = is_admin
        if admin_level is not UNSET:
            field_dict["adminLevel"] = admin_level
        if is_member is not UNSET:
            field_dict["isMember"] = is_member
        if deactivated is not UNSET:
            field_dict["deactivated"] = deactivated
        if photo is not UNSET:
            field_dict["photo"] = photo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.community_vk import CommunityVk

        d = dict(src_dict)
        owner_id = d.pop("ownerId")

        community_id = d.pop("communityId")

        name = d.pop("name")

        screen_name = d.pop("screenName")

        type_ = d.pop("type")

        is_closed = d.pop("isClosed")

        vk = CommunityVk.from_dict(d.pop("vk"))

        is_admin = d.pop("isAdmin", UNSET)

        admin_level = d.pop("adminLevel", UNSET)

        is_member = d.pop("isMember", UNSET)

        deactivated = d.pop("deactivated", UNSET)

        photo = d.pop("photo", UNSET)

        community = cls(
            owner_id=owner_id,
            community_id=community_id,
            name=name,
            screen_name=screen_name,
            type_=type_,
            is_closed=is_closed,
            vk=vk,
            is_admin=is_admin,
            admin_level=admin_level,
            is_member=is_member,
            deactivated=deactivated,
            photo=photo,
        )

        community.additional_properties = d
        return community

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
