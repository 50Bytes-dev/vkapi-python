from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.album import Album


T = TypeVar("T", bound="AlbumResponse")


@_attrs_define
class AlbumResponse:
    """
    Attributes:
        success (bool):  Example: True.
        album (Album | Unset): An album as VK gives it. The settings come only when VK gives them: a
            page's privacy to the page that owns it, a community's switches to the
            page that manages it.
    """

    success: bool
    album: Album | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        album: dict[str, Any] | Unset = UNSET
        if not isinstance(self.album, Unset):
            album = self.album.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if album is not UNSET:
            field_dict["album"] = album

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.album import Album

        d = dict(src_dict)
        success = d.pop("success")

        _album = d.pop("album", UNSET)
        album: Album | Unset
        if isinstance(_album, Unset):
            album = UNSET
        else:
            album = Album.from_dict(_album)

        album_response = cls(
            success=success,
            album=album,
        )

        album_response.additional_properties = d
        return album_response

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
