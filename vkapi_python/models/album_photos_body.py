from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlbumPhotosBody")


@_attrs_define
class AlbumPhotosBody:
    """
    Attributes:
        photos (list[str]): 1 to 100 photos, `photo<owner_id>_<id>[_<access_key>]`, of the page and of the communities
            it manages Example: ['photo-210132800_457239475', 'photo1127016903_456243480'].
    """

    photos: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        photos = self.photos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "photos": photos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        photos = cast(list[str], d.pop("photos"))

        album_photos_body = cls(
            photos=photos,
        )

        album_photos_body.additional_properties = d
        return album_photos_body

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
