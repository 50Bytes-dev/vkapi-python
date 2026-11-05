from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Participant")


@_attrs_define
class Participant:
    """
    Attributes:
        id (int): A person's id, or a community's id negated Example: 233333572.
        name (str):  Example: Иван Петров.
        photo (str | Unset):  Example: https://sun9-1.userapi.com/photo.jpg.
        is_admin (bool | Unset):
        is_owner (bool | Unset):
    """

    id: int
    name: str
    photo: str | Unset = UNSET
    is_admin: bool | Unset = UNSET
    is_owner: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        photo = self.photo

        is_admin = self.is_admin

        is_owner = self.is_owner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if photo is not UNSET:
            field_dict["photo"] = photo
        if is_admin is not UNSET:
            field_dict["isAdmin"] = is_admin
        if is_owner is not UNSET:
            field_dict["isOwner"] = is_owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        photo = d.pop("photo", UNSET)

        is_admin = d.pop("isAdmin", UNSET)

        is_owner = d.pop("isOwner", UNSET)

        participant = cls(
            id=id,
            name=name,
            photo=photo,
            is_admin=is_admin,
            is_owner=is_owner,
        )

        participant.additional_properties = d
        return participant

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
