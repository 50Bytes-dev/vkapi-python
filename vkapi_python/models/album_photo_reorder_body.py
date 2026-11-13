from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlbumPhotoReorderBody")


@_attrs_define
class AlbumPhotoReorderBody:
    """The photo and exactly one of `before` and `after`, a photo of the same album.

    Attributes:
        photo (str): `photo<owner_id>_<id>[_<access_key>]`, the page's or a community's Example:
            photo-210132800_457239475.
        before (str | Unset): The photo it goes right before Example: photo-210132800_457239476.
        after (str | Unset): The photo it goes right after
    """

    photo: str
    before: str | Unset = UNSET
    after: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        photo = self.photo

        before = self.before

        after = self.after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "photo": photo,
            }
        )
        if before is not UNSET:
            field_dict["before"] = before
        if after is not UNSET:
            field_dict["after"] = after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        photo = d.pop("photo")

        before = d.pop("before", UNSET)

        after = d.pop("after", UNSET)

        album_photo_reorder_body = cls(
            photo=photo,
            before=before,
            after=after,
        )

        album_photo_reorder_body.additional_properties = d
        return album_photo_reorder_body

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
