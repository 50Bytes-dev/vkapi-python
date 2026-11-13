from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlbumEditBody")


@_attrs_define
class AlbumEditBody:
    """The album and at least one field; a field left out is kept.

    Attributes:
        album (str): `<owner_id>_<album_id>`, as in the album's link; `album` before it is taken too. The page's own or
            a community's, not a system album Example: -210132800_312370605.
        title (str | Unset): 1 to 128 characters; spaces around it are dropped Example: Платья, осень.
        description (str | Unset): At most 1000 characters
        privacy_view (list[str] | Unset): A page's album only. Who sees it: 1 to 100 of `all`, `friends`,
            `friends_of_friends`, `friends_of_friends_only`, `nobody`, `only_me`,
            `list<id>` (a friend list), `<user_id>`, and `-list<id>` or `-<user_id>`
            to leave one out. Example: ['all'].
        privacy_comment (list[str] | Unset): A page's album only. Who comments: 1 to 100 of `all`, `friends`,
            `friends_of_friends`, `friends_of_friends_only`, `nobody`, `only_me`,
            `list<id>` (a friend list), `<user_id>`, and `-list<id>` or `-<user_id>`
            to leave one out. Example: ['friends'].
        upload_by_admins_only (bool | Unset): A community's album only. Given alone, the gateway sends
            `commentsDisabled` as the album has it
        comments_disabled (bool | Unset): A community's album only. Given alone, the gateway sends `uploadByAdminsOnly`
            as the album has it
    """

    album: str
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    privacy_view: list[str] | Unset = UNSET
    privacy_comment: list[str] | Unset = UNSET
    upload_by_admins_only: bool | Unset = UNSET
    comments_disabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        album = self.album

        title = self.title

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
                "album": album,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
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
        album = d.pop("album")

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        privacy_view = cast(list[str], d.pop("privacyView", UNSET))

        privacy_comment = cast(list[str], d.pop("privacyComment", UNSET))

        upload_by_admins_only = d.pop("uploadByAdminsOnly", UNSET)

        comments_disabled = d.pop("commentsDisabled", UNSET)

        album_edit_body = cls(
            album=album,
            title=title,
            description=description,
            privacy_view=privacy_view,
            privacy_comment=privacy_comment,
            upload_by_admins_only=upload_by_admins_only,
            comments_disabled=comments_disabled,
        )

        album_edit_body.additional_properties = d
        return album_edit_body

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
