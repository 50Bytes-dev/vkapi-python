from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlbumCommentBody")


@_attrs_define
class AlbumCommentBody:
    """The photo and at least one of `message`, `attachments` and `stickerId`.

    Attributes:
        photo (str): `photo<owner_id>_<id>[_<access_key>]`, any photo VK lets the page comment on Example:
            photo-210132800_457239475.
        message (str | Unset):  Example: Есть размер M?.
        attachments (list[str] | Unset): Up to 10, as a send takes them
        reply_to_comment (int | Unset): The comment it answers
        sticker_id (int | Unset):
        from_group (bool | Unset): Writes as the community that owns the photo; the photo must be a community's
        guid (str | Unset): At most 256 bytes; VK takes the same comment once however often it is sent
    """

    photo: str
    message: str | Unset = UNSET
    attachments: list[str] | Unset = UNSET
    reply_to_comment: int | Unset = UNSET
    sticker_id: int | Unset = UNSET
    from_group: bool | Unset = UNSET
    guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        photo = self.photo

        message = self.message

        attachments: list[str] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments

        reply_to_comment = self.reply_to_comment

        sticker_id = self.sticker_id

        from_group = self.from_group

        guid = self.guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "photo": photo,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if reply_to_comment is not UNSET:
            field_dict["replyToComment"] = reply_to_comment
        if sticker_id is not UNSET:
            field_dict["stickerId"] = sticker_id
        if from_group is not UNSET:
            field_dict["fromGroup"] = from_group
        if guid is not UNSET:
            field_dict["guid"] = guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        photo = d.pop("photo")

        message = d.pop("message", UNSET)

        attachments = cast(list[str], d.pop("attachments", UNSET))

        reply_to_comment = d.pop("replyToComment", UNSET)

        sticker_id = d.pop("stickerId", UNSET)

        from_group = d.pop("fromGroup", UNSET)

        guid = d.pop("guid", UNSET)

        album_comment_body = cls(
            photo=photo,
            message=message,
            attachments=attachments,
            reply_to_comment=reply_to_comment,
            sticker_id=sticker_id,
            from_group=from_group,
            guid=guid,
        )

        album_comment_body.additional_properties = d
        return album_comment_body

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
