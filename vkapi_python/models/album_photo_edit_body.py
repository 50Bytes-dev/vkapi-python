from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlbumPhotoEditBody")


@_attrs_define
class AlbumPhotoEditBody:
    """The photo and at least one of `caption`, `latitude` with `longitude`, and `deletePlace`.

    Attributes:
        photo (str): `photo<owner_id>_<id>[_<access_key>]`, the page's or a community's Example:
            photo-210132800_457239475.
        caption (str | Unset): At most 2048 characters; an empty one clears it. Left out, the caption stays (the gateway
            reads it first) Example: Платье, 1500 ₽.
        latitude (float | Unset): With `longitude`, the photo's place Example: 55.7558.
        longitude (float | Unset):  Example: 37.6173.
        delete_place (bool | Unset): Removes the photo's place; not with `latitude` and `longitude`
    """

    photo: str
    caption: str | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    delete_place: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        photo = self.photo

        caption = self.caption

        latitude = self.latitude

        longitude = self.longitude

        delete_place = self.delete_place

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "photo": photo,
            }
        )
        if caption is not UNSET:
            field_dict["caption"] = caption
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if delete_place is not UNSET:
            field_dict["deletePlace"] = delete_place

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        photo = d.pop("photo")

        caption = d.pop("caption", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        delete_place = d.pop("deletePlace", UNSET)

        album_photo_edit_body = cls(
            photo=photo,
            caption=caption,
            latitude=latitude,
            longitude=longitude,
            delete_place=delete_place,
        )

        album_photo_edit_body.additional_properties = d
        return album_photo_edit_body

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
