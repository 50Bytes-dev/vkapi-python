from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlbumPhoto")


@_attrs_define
class AlbumPhoto:
    """A photo as VK gives it to `GET /album/photos` and `POST /album/photo/restore`.

    Attributes:
        attachment (str): The photo as a send takes it, with `_<access_key>` when VK gives one Example:
            photo-210132800_457239475.
        owner_id (int):  Example: -210132800.
        photo_id (int):  Example: 457239475.
        caption (str):  Example: Платье, 1200 ₽.
        album (str | Unset): Its album, `<owner_id>_<album_id>`, when VK tells it Example: -210132800_312370605.
        album_id (int | Unset): Its album's id; negative for a system album (`-6` profile, `-7` wall, `-15` saved)
            Example: 312370605.
        date (int | Unset): Unix time Example: 1794550000.
        width (int | Unset): The largest size VK has Example: 1280.
        height (int | Unset):  Example: 960.
        url (str | Unset): The address of its largest copy of at most 2560 px, as on `POST /wall/photos` Example:
            https://sun9-1.userapi.com/....
        latitude (float | Unset): The place VK keeps of the photo, when it keeps one Example: 55.7558.
        longitude (float | Unset):  Example: 37.6173.
        likes (int | Unset): With `extended`
        comments (int | Unset): With `extended`
        reposts (int | Unset): With `extended`
        tags (int | Unset): With `extended`
        can_comment (bool | Unset): With `extended`, when VK gives it
    """

    attachment: str
    owner_id: int
    photo_id: int
    caption: str
    album: str | Unset = UNSET
    album_id: int | Unset = UNSET
    date: int | Unset = UNSET
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    url: str | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    likes: int | Unset = UNSET
    comments: int | Unset = UNSET
    reposts: int | Unset = UNSET
    tags: int | Unset = UNSET
    can_comment: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachment = self.attachment

        owner_id = self.owner_id

        photo_id = self.photo_id

        caption = self.caption

        album = self.album

        album_id = self.album_id

        date = self.date

        width = self.width

        height = self.height

        url = self.url

        latitude = self.latitude

        longitude = self.longitude

        likes = self.likes

        comments = self.comments

        reposts = self.reposts

        tags = self.tags

        can_comment = self.can_comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attachment": attachment,
                "ownerId": owner_id,
                "photoId": photo_id,
                "caption": caption,
            }
        )
        if album is not UNSET:
            field_dict["album"] = album
        if album_id is not UNSET:
            field_dict["albumId"] = album_id
        if date is not UNSET:
            field_dict["date"] = date
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if url is not UNSET:
            field_dict["url"] = url
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if likes is not UNSET:
            field_dict["likes"] = likes
        if comments is not UNSET:
            field_dict["comments"] = comments
        if reposts is not UNSET:
            field_dict["reposts"] = reposts
        if tags is not UNSET:
            field_dict["tags"] = tags
        if can_comment is not UNSET:
            field_dict["canComment"] = can_comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attachment = d.pop("attachment")

        owner_id = d.pop("ownerId")

        photo_id = d.pop("photoId")

        caption = d.pop("caption")

        album = d.pop("album", UNSET)

        album_id = d.pop("albumId", UNSET)

        date = d.pop("date", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        url = d.pop("url", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        likes = d.pop("likes", UNSET)

        comments = d.pop("comments", UNSET)

        reposts = d.pop("reposts", UNSET)

        tags = d.pop("tags", UNSET)

        can_comment = d.pop("canComment", UNSET)

        album_photo = cls(
            attachment=attachment,
            owner_id=owner_id,
            photo_id=photo_id,
            caption=caption,
            album=album,
            album_id=album_id,
            date=date,
            width=width,
            height=height,
            url=url,
            latitude=latitude,
            longitude=longitude,
            likes=likes,
            comments=comments,
            reposts=reposts,
            tags=tags,
            can_comment=can_comment,
        )

        album_photo.additional_properties = d
        return album_photo

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
