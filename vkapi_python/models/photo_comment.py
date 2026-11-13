from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PhotoComment")


@_attrs_define
class PhotoComment:
    """
    Attributes:
        comment_id (int): The comment's id, counted per owner of the photo Example: 1.
        owner_id (int): The photo's owner; with `commentId` it names the comment Example: -210132800.
        from_id (int): The author; a community's id is negative Example: 1127016903.
        date (int): Unix time Example: 1794569084.
        text (str):  Example: Есть размер M?.
        attachments (list[str]): The attachments VK names by owner and id, as a send takes them
        photo (str | Unset): The photo commented on, `photo<owner_id>_<id>` Example: photo-210132800_457239475.
        reply_to_user (int | Unset):
        reply_to_comment (int | Unset):
        sticker_id (int | Unset):
        likes (int | Unset): With `likes`
    """

    comment_id: int
    owner_id: int
    from_id: int
    date: int
    text: str
    attachments: list[str]
    photo: str | Unset = UNSET
    reply_to_user: int | Unset = UNSET
    reply_to_comment: int | Unset = UNSET
    sticker_id: int | Unset = UNSET
    likes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_id = self.comment_id

        owner_id = self.owner_id

        from_id = self.from_id

        date = self.date

        text = self.text

        attachments = self.attachments

        photo = self.photo

        reply_to_user = self.reply_to_user

        reply_to_comment = self.reply_to_comment

        sticker_id = self.sticker_id

        likes = self.likes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commentId": comment_id,
                "ownerId": owner_id,
                "fromId": from_id,
                "date": date,
                "text": text,
                "attachments": attachments,
            }
        )
        if photo is not UNSET:
            field_dict["photo"] = photo
        if reply_to_user is not UNSET:
            field_dict["replyToUser"] = reply_to_user
        if reply_to_comment is not UNSET:
            field_dict["replyToComment"] = reply_to_comment
        if sticker_id is not UNSET:
            field_dict["stickerId"] = sticker_id
        if likes is not UNSET:
            field_dict["likes"] = likes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_id = d.pop("commentId")

        owner_id = d.pop("ownerId")

        from_id = d.pop("fromId")

        date = d.pop("date")

        text = d.pop("text")

        attachments = cast(list[str], d.pop("attachments"))

        photo = d.pop("photo", UNSET)

        reply_to_user = d.pop("replyToUser", UNSET)

        reply_to_comment = d.pop("replyToComment", UNSET)

        sticker_id = d.pop("stickerId", UNSET)

        likes = d.pop("likes", UNSET)

        photo_comment = cls(
            comment_id=comment_id,
            owner_id=owner_id,
            from_id=from_id,
            date=date,
            text=text,
            attachments=attachments,
            photo=photo,
            reply_to_user=reply_to_user,
            reply_to_comment=reply_to_comment,
            sticker_id=sticker_id,
            likes=likes,
        )

        photo_comment.additional_properties = d
        return photo_comment

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
