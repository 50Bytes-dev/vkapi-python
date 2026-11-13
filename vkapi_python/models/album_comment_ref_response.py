from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlbumCommentRefResponse")


@_attrs_define
class AlbumCommentRefResponse:
    """
    Attributes:
        success (bool):  Example: True.
        owner_id (int):  Example: -210132800.
        comment_id (int):  Example: 1.
    """

    success: bool
    owner_id: int
    comment_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        owner_id = self.owner_id

        comment_id = self.comment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "ownerId": owner_id,
                "commentId": comment_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        owner_id = d.pop("ownerId")

        comment_id = d.pop("commentId")

        album_comment_ref_response = cls(
            success=success,
            owner_id=owner_id,
            comment_id=comment_id,
        )

        album_comment_ref_response.additional_properties = d
        return album_comment_ref_response

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
