from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentAuthor")


@_attrs_define
class CommentAuthor:
    """
    Attributes:
        id (int): A user's id, or a community's id negated Example: 1127016903.
        name (str):  Example: Надежда Ушакова.
        screen_name (str | Unset):
        photo (str | Unset): The address of a 100 px photo
    """

    id: int
    name: str
    screen_name: str | Unset = UNSET
    photo: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        screen_name = self.screen_name

        photo = self.photo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if screen_name is not UNSET:
            field_dict["screenName"] = screen_name
        if photo is not UNSET:
            field_dict["photo"] = photo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        screen_name = d.pop("screenName", UNSET)

        photo = d.pop("photo", UNSET)

        comment_author = cls(
            id=id,
            name=name,
            screen_name=screen_name,
            photo=photo,
        )

        comment_author.additional_properties = d
        return comment_author

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
