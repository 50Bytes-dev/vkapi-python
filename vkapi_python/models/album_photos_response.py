from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.album_photo import AlbumPhoto


T = TypeVar("T", bound="AlbumPhotosResponse")


@_attrs_define
class AlbumPhotosResponse:
    """With `album`: `album`, `ownerId`, `albumId`, `total`, `offset`, `count`,
    `photos`. With `ownerId`: `ownerId`, `total`, `offset`, `count`,
    `photos`. With `photos`: `photos` and `missing`.

        Attributes:
            success (bool):  Example: True.
            photos (list[AlbumPhoto]):
            album (str | Unset):  Example: -210132800_312370605.
            owner_id (int | Unset):  Example: -210132800.
            album_id (int | Unset):  Example: 312370605.
            total (int | Unset): VK's count of them all (the album's, or the owner's) Example: 1000.
            offset (int | Unset):
            count (int | Unset): How many photos this page has Example: 50.
            next_offset (int | Unset): The `offset` to ask for next; absent on the last page Example: 50.
            missing (list[str] | Unset): With `photos`, those VK does not give (deleted, never there, or closed to the
                page), as asked Example: ['photo1127016903_1'].
    """

    success: bool
    photos: list[AlbumPhoto]
    album: str | Unset = UNSET
    owner_id: int | Unset = UNSET
    album_id: int | Unset = UNSET
    total: int | Unset = UNSET
    offset: int | Unset = UNSET
    count: int | Unset = UNSET
    next_offset: int | Unset = UNSET
    missing: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        photos = []
        for photos_item_data in self.photos:
            photos_item = photos_item_data.to_dict()
            photos.append(photos_item)

        album = self.album

        owner_id = self.owner_id

        album_id = self.album_id

        total = self.total

        offset = self.offset

        count = self.count

        next_offset = self.next_offset

        missing: list[str] | Unset = UNSET
        if not isinstance(self.missing, Unset):
            missing = self.missing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "photos": photos,
            }
        )
        if album is not UNSET:
            field_dict["album"] = album
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if album_id is not UNSET:
            field_dict["albumId"] = album_id
        if total is not UNSET:
            field_dict["total"] = total
        if offset is not UNSET:
            field_dict["offset"] = offset
        if count is not UNSET:
            field_dict["count"] = count
        if next_offset is not UNSET:
            field_dict["nextOffset"] = next_offset
        if missing is not UNSET:
            field_dict["missing"] = missing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.album_photo import AlbumPhoto

        d = dict(src_dict)
        success = d.pop("success")

        photos = []
        _photos = d.pop("photos")
        for photos_item_data in _photos:
            photos_item = AlbumPhoto.from_dict(photos_item_data)

            photos.append(photos_item)

        album = d.pop("album", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        album_id = d.pop("albumId", UNSET)

        total = d.pop("total", UNSET)

        offset = d.pop("offset", UNSET)

        count = d.pop("count", UNSET)

        next_offset = d.pop("nextOffset", UNSET)

        missing = cast(list[str], d.pop("missing", UNSET))

        album_photos_response = cls(
            success=success,
            photos=photos,
            album=album,
            owner_id=owner_id,
            album_id=album_id,
            total=total,
            offset=offset,
            count=count,
            next_offset=next_offset,
            missing=missing,
        )

        album_photos_response.additional_properties = d
        return album_photos_response

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
