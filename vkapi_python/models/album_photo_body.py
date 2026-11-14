from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlbumPhotoBody")


@_attrs_define
class AlbumPhotoBody:
    """The album, a caption, and exactly one of `url`, `data` and `photo`.

    Attributes:
        album (str): `<owner_id>_<album_id>`, the page's own or a community's, not a system album Example:
            -210132800_312370605.
        caption (str | Unset): At most 2048 characters Example: Платье, 1200 ₽.
        url (str | Unset): An http or https address of the image, fetched as on `POST /media/photo`; for a photo VK has,
            its `url` from `POST /wall/photos` Example: https://sun9-1.userapi.com/....
        data (str | Unset): The image as base64 or a base64 data URL
        photo (str | Unset): A photo VK has, `photo<owner_id>_<id>[_<access_key>]`. Copied into the page's own album;
            into a community's, found with `photos.getById` and uploaded anew Example:
            photo-219994268_457445460_73cdc6dd4c0351c2b9.
        ref (str | Unset): 2.5.0: the caller's key of this photo, at most 128 bytes (empty: none),
            the account's own, held 24 h: a repeat of the call with it gets the
            first call's answer (`repeated`). The same `ref` with another album,
            caption or photo is refused. Not the `ref` of `POST /chat/send/text` Example: sku-1042-photo-1.
    """

    album: str
    caption: str | Unset = UNSET
    url: str | Unset = UNSET
    data: str | Unset = UNSET
    photo: str | Unset = UNSET
    ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        album = self.album

        caption = self.caption

        url = self.url

        data = self.data

        photo = self.photo

        ref = self.ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "album": album,
            }
        )
        if caption is not UNSET:
            field_dict["caption"] = caption
        if url is not UNSET:
            field_dict["url"] = url
        if data is not UNSET:
            field_dict["data"] = data
        if photo is not UNSET:
            field_dict["photo"] = photo
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        album = d.pop("album")

        caption = d.pop("caption", UNSET)

        url = d.pop("url", UNSET)

        data = d.pop("data", UNSET)

        photo = d.pop("photo", UNSET)

        ref = d.pop("ref", UNSET)

        album_photo_body = cls(
            album=album,
            caption=caption,
            url=url,
            data=data,
            photo=photo,
            ref=ref,
        )

        album_photo_body.additional_properties = d
        return album_photo_body

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
