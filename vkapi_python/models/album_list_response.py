from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.album import Album


T = TypeVar("T", bound="AlbumListResponse")


@_attrs_define
class AlbumListResponse:
    """
    Attributes:
        success (bool):  Example: True.
        owner_id (int): Whose albums these are Example: -210132800.
        offset (int): Where this page starts
        count (int): How many albums this page has Example: 1.
        albums (list[Album]):
        next_offset (int | Unset): Present when `count` was asked and a full page came; the `offset` to ask for next. VK
            gives no total, so that page may be empty Example: 50.
    """

    success: bool
    owner_id: int
    offset: int
    count: int
    albums: list[Album]
    next_offset: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        owner_id = self.owner_id

        offset = self.offset

        count = self.count

        albums = []
        for albums_item_data in self.albums:
            albums_item = albums_item_data.to_dict()
            albums.append(albums_item)

        next_offset = self.next_offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "ownerId": owner_id,
                "offset": offset,
                "count": count,
                "albums": albums,
            }
        )
        if next_offset is not UNSET:
            field_dict["nextOffset"] = next_offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.album import Album

        d = dict(src_dict)
        success = d.pop("success")

        owner_id = d.pop("ownerId")

        offset = d.pop("offset")

        count = d.pop("count")

        albums = []
        _albums = d.pop("albums")
        for albums_item_data in _albums:
            albums_item = Album.from_dict(albums_item_data)

            albums.append(albums_item)

        next_offset = d.pop("nextOffset", UNSET)

        album_list_response = cls(
            success=success,
            owner_id=owner_id,
            offset=offset,
            count=count,
            albums=albums,
            next_offset=next_offset,
        )

        album_list_response.additional_properties = d
        return album_list_response

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
