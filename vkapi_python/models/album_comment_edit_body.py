from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlbumCommentEditBody")


@_attrs_define
class AlbumCommentEditBody:
    """The comment and at least one of `message` and `attachments`.

    Attributes:
        owner_id (int): The commented photo's owner Example: -210132800.
        comment_id (int):  Example: 1.
        message (str | Unset):  Example: Есть размер M и L?.
        attachments (list[str] | Unset): Up to 10, as a send takes them
    """

    owner_id: int
    comment_id: int
    message: str | Unset = UNSET
    attachments: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        comment_id = self.comment_id

        message = self.message

        attachments: list[str] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ownerId": owner_id,
                "commentId": comment_id,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_id = d.pop("ownerId")

        comment_id = d.pop("commentId")

        message = d.pop("message", UNSET)

        attachments = cast(list[str], d.pop("attachments", UNSET))

        album_comment_edit_body = cls(
            owner_id=owner_id,
            comment_id=comment_id,
            message=message,
            attachments=attachments,
        )

        album_comment_edit_body.additional_properties = d
        return album_comment_edit_body

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
