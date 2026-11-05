from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.wall_post import WallPost


T = TypeVar("T", bound="WallPhotosResponse")


@_attrs_define
class WallPhotosResponse:
    """
    Attributes:
        success (bool):  Example: True.
        posts (list[WallPost]):
    """

    success: bool
    posts: list[WallPost]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        posts = []
        for posts_item_data in self.posts:
            posts_item = posts_item_data.to_dict()
            posts.append(posts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "posts": posts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wall_post import WallPost

        d = dict(src_dict)
        success = d.pop("success")

        posts = []
        _posts = d.pop("posts")
        for posts_item_data in _posts:
            posts_item = WallPost.from_dict(posts_item_data)

            posts.append(posts_item)

        wall_photos_response = cls(
            success=success,
            posts=posts,
        )

        wall_photos_response.additional_properties = d
        return wall_photos_response

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
