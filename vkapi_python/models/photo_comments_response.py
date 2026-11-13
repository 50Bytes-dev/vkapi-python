from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_author import CommentAuthor
    from ..models.photo_comment import PhotoComment


T = TypeVar("T", bound="PhotoCommentsResponse")


@_attrs_define
class PhotoCommentsResponse:
    """
    Attributes:
        success (bool):  Example: True.
        total (int): VK's count of them all Example: 1.
        offset (int):
        count (int): How many comments this page has Example: 1.
        comments (list[PhotoComment]):
        photo (str | Unset): With `photo` Example: photo-210132800_457239475.
        album (str | Unset): With `album`
        owner_id (int | Unset): With `album` or `ownerId`
        next_offset (int | Unset): The `offset` to ask for next; absent on the last page
        profiles (list[CommentAuthor] | Unset): With `extended`, the users among the authors
        groups (list[CommentAuthor] | Unset): With `extended`, the communities among the authors
    """

    success: bool
    total: int
    offset: int
    count: int
    comments: list[PhotoComment]
    photo: str | Unset = UNSET
    album: str | Unset = UNSET
    owner_id: int | Unset = UNSET
    next_offset: int | Unset = UNSET
    profiles: list[CommentAuthor] | Unset = UNSET
    groups: list[CommentAuthor] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        total = self.total

        offset = self.offset

        count = self.count

        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()
            comments.append(comments_item)

        photo = self.photo

        album = self.album

        owner_id = self.owner_id

        next_offset = self.next_offset

        profiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.profiles, Unset):
            profiles = []
            for profiles_item_data in self.profiles:
                profiles_item = profiles_item_data.to_dict()
                profiles.append(profiles_item)

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "total": total,
                "offset": offset,
                "count": count,
                "comments": comments,
            }
        )
        if photo is not UNSET:
            field_dict["photo"] = photo
        if album is not UNSET:
            field_dict["album"] = album
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if next_offset is not UNSET:
            field_dict["nextOffset"] = next_offset
        if profiles is not UNSET:
            field_dict["profiles"] = profiles
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment_author import CommentAuthor
        from ..models.photo_comment import PhotoComment

        d = dict(src_dict)
        success = d.pop("success")

        total = d.pop("total")

        offset = d.pop("offset")

        count = d.pop("count")

        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = PhotoComment.from_dict(comments_item_data)

            comments.append(comments_item)

        photo = d.pop("photo", UNSET)

        album = d.pop("album", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        next_offset = d.pop("nextOffset", UNSET)

        _profiles = d.pop("profiles", UNSET)
        profiles: list[CommentAuthor] | Unset = UNSET
        if _profiles is not UNSET:
            profiles = []
            for profiles_item_data in _profiles:
                profiles_item = CommentAuthor.from_dict(profiles_item_data)

                profiles.append(profiles_item)

        _groups = d.pop("groups", UNSET)
        groups: list[CommentAuthor] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = CommentAuthor.from_dict(groups_item_data)

                groups.append(groups_item)

        photo_comments_response = cls(
            success=success,
            total=total,
            offset=offset,
            count=count,
            comments=comments,
            photo=photo,
            album=album,
            owner_id=owner_id,
            next_offset=next_offset,
            profiles=profiles,
            groups=groups,
        )

        photo_comments_response.additional_properties = d
        return photo_comments_response

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
