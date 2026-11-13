from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlbumCoverBody")


@_attrs_define
class AlbumCoverBody:
    """
    Attributes:
        album (str): `<owner_id>_<album_id>`, the page's own or a community's, not a system album Example:
            -210132800_312370605.
        photo (str): A photo of the album, `photo<owner_id>_<id>[_<access_key>]` Example: photo-210132800_457239475.
    """

    album: str
    photo: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        album = self.album

        photo = self.photo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "album": album,
                "photo": photo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        album = d.pop("album")

        photo = d.pop("photo")

        album_cover_body = cls(
            album=album,
            photo=photo,
        )

        album_cover_body.additional_properties = d
        return album_cover_body

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
