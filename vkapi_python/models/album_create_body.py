from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlbumCreateBody")


@_attrs_define
class AlbumCreateBody:
    """
    Attributes:
        title (str): 1 to 128 characters; spaces around it are dropped Example: Платья.
        owner_id (int | Unset): Left out (or the page's id), the page's album; a community's id negated, the community's
            (the page must manage it) Example: -210132800.
        description (str | Unset): At most 1000 characters Example: Новинки недели.
        privacy_view (list[str] | Unset): A page's album only. Who sees it: 1 to 100 of `all`, `friends`,
            `friends_of_friends`, `friends_of_friends_only`, `nobody`, `only_me`,
            `list<id>` (a friend list), `<user_id>`, and `-list<id>` or `-<user_id>`
            to leave one out. Example: ['all'].
        privacy_comment (list[str] | Unset): A page's album only. Who comments: 1 to 100 of `all`, `friends`,
            `friends_of_friends`, `friends_of_friends_only`, `nobody`, `only_me`,
            `list<id>` (a friend list), `<user_id>`, and `-list<id>` or `-<user_id>`
            to leave one out. Example: ['friends'].
        upload_by_admins_only (bool | Unset): A community's album only. Only the community's managers upload
        comments_disabled (bool | Unset): A community's album only. Comments are off
    """

    title: str
    owner_id: int | Unset = UNSET
    description: str | Unset = UNSET
    privacy_view: list[str] | Unset = UNSET
    privacy_comment: list[str] | Unset = UNSET
    upload_by_admins_only: bool | Unset = UNSET
    comments_disabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        owner_id = self.owner_id

        description = self.description

        privacy_view: list[str] | Unset = UNSET
        if not isinstance(self.privacy_view, Unset):
            privacy_view = self.privacy_view

        privacy_comment: list[str] | Unset = UNSET
        if not isinstance(self.privacy_comment, Unset):
            privacy_comment = self.privacy_comment

        upload_by_admins_only = self.upload_by_admins_only

        comments_disabled = self.comments_disabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if description is not UNSET:
            field_dict["description"] = description
        if privacy_view is not UNSET:
            field_dict["privacyView"] = privacy_view
        if privacy_comment is not UNSET:
            field_dict["privacyComment"] = privacy_comment
        if upload_by_admins_only is not UNSET:
            field_dict["uploadByAdminsOnly"] = upload_by_admins_only
        if comments_disabled is not UNSET:
            field_dict["commentsDisabled"] = comments_disabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        owner_id = d.pop("ownerId", UNSET)

        description = d.pop("description", UNSET)

        privacy_view = cast(list[str], d.pop("privacyView", UNSET))

        privacy_comment = cast(list[str], d.pop("privacyComment", UNSET))

        upload_by_admins_only = d.pop("uploadByAdminsOnly", UNSET)

        comments_disabled = d.pop("commentsDisabled", UNSET)

        album_create_body = cls(
            title=title,
            owner_id=owner_id,
            description=description,
            privacy_view=privacy_view,
            privacy_comment=privacy_comment,
            upload_by_admins_only=upload_by_admins_only,
            comments_disabled=comments_disabled,
        )

        album_create_body.additional_properties = d
        return album_create_body

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
