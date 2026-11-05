from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wall_photo import WallPhoto


T = TypeVar("T", bound="WallPost")


@_attrs_define
class WallPost:
    """
    Attributes:
        post (str): The post id, as asked Example: -12345_678.
        found (bool): false when VK did not give the post (deleted, hidden, a wrong id)
        photos (list[WallPhoto] | Unset):
    """

    post: str
    found: bool
    photos: list[WallPhoto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        post = self.post

        found = self.found

        photos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.photos, Unset):
            photos = []
            for photos_item_data in self.photos:
                photos_item = photos_item_data.to_dict()
                photos.append(photos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "post": post,
                "found": found,
            }
        )
        if photos is not UNSET:
            field_dict["photos"] = photos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wall_photo import WallPhoto

        d = dict(src_dict)
        post = d.pop("post")

        found = d.pop("found")

        _photos = d.pop("photos", UNSET)
        photos: list[WallPhoto] | Unset = UNSET
        if _photos is not UNSET:
            photos = []
            for photos_item_data in _photos:
                photos_item = WallPhoto.from_dict(photos_item_data)

                photos.append(photos_item)

        wall_post = cls(
            post=post,
            found=found,
            photos=photos,
        )

        wall_post.additional_properties = d
        return wall_post

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
