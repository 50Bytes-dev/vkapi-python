from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlbumPhotoMoveResponse")


@_attrs_define
class AlbumPhotoMoveResponse:
    """
    Attributes:
        success (bool):  Example: True.
        album (str):  Example: -210132800_312370605.
        moved (int): How many photos went into the album (all asked) Example: 1.
    """

    success: bool
    album: str
    moved: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        album = self.album

        moved = self.moved

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "album": album,
                "moved": moved,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        album = d.pop("album")

        moved = d.pop("moved")

        album_photo_move_response = cls(
            success=success,
            album=album,
            moved=moved,
        )

        album_photo_move_response.additional_properties = d
        return album_photo_move_response

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
