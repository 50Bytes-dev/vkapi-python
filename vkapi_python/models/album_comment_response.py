from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlbumCommentResponse")


@_attrs_define
class AlbumCommentResponse:
    """
    Attributes:
        success (bool):  Example: True.
        comment_id (int):  Example: 1.
        owner_id (int): The photo's owner; with `commentId` it names the comment Example: -210132800.
        photo (str):  Example: photo-210132800_457239475.
    """

    success: bool
    comment_id: int
    owner_id: int
    photo: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        comment_id = self.comment_id

        owner_id = self.owner_id

        photo = self.photo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "commentId": comment_id,
                "ownerId": owner_id,
                "photo": photo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        comment_id = d.pop("commentId")

        owner_id = d.pop("ownerId")

        photo = d.pop("photo")

        album_comment_response = cls(
            success=success,
            comment_id=comment_id,
            owner_id=owner_id,
            photo=photo,
        )

        album_comment_response.additional_properties = d
        return album_comment_response

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
