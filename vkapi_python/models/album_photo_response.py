from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlbumPhotoResponse")


@_attrs_define
class AlbumPhotoResponse:
    """
    Attributes:
        success (bool):  Example: True.
        attachment (str): The photo, as a send takes it Example: photo-210132800_457239101.
        album (str):  Example: -210132800_312370605.
        photo_id (int):  Example: 457239101.
        owner_id (int): The photo's owner, the album's Example: -210132800.
        album_id (int):  Example: 312370605.
        how (str): `uploaded` (a new upload) or `copied` (a photo VK has, copied into the page's own album) Example:
            uploaded.
        width (int | Unset): The largest size VK keeps; absent on a copy Example: 1280.
        height (int | Unset):  Example: 960.
    """

    success: bool
    attachment: str
    album: str
    photo_id: int
    owner_id: int
    album_id: int
    how: str
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        attachment = self.attachment

        album = self.album

        photo_id = self.photo_id

        owner_id = self.owner_id

        album_id = self.album_id

        how = self.how

        width = self.width

        height = self.height

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "attachment": attachment,
                "album": album,
                "photoId": photo_id,
                "ownerId": owner_id,
                "albumId": album_id,
                "how": how,
            }
        )
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        attachment = d.pop("attachment")

        album = d.pop("album")

        photo_id = d.pop("photoId")

        owner_id = d.pop("ownerId")

        album_id = d.pop("albumId")

        how = d.pop("how")

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        album_photo_response = cls(
            success=success,
            attachment=attachment,
            album=album,
            photo_id=photo_id,
            owner_id=owner_id,
            album_id=album_id,
            how=how,
            width=width,
            height=height,
        )

        album_photo_response.additional_properties = d
        return album_photo_response

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
