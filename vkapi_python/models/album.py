from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Album")


@_attrs_define
class Album:
    """An album as VK gives it. The settings come only when VK gives them: a
    page's privacy to the page that owns it, a community's switches to the
    page that manages it.

        Attributes:
            album (str): The album as the album calls take it, `<owner_id>_<album_id>` Example: -210132800_312370605.
            owner_id (int): The page's id, a community's id negated, or another user's id Example: -210132800.
            album_id (int): The album's id; negative for a system album Example: 312370605.
            title (str):  Example: Платья.
            description (str):  Example: Новинки недели.
            size (int): How many photos it holds Example: 12.
            can_upload (bool): Whether the page may add photos. VK's word for a community's album; true for the page's own
                albums but its system ones; false for another user's Example: True.
            system (bool): A system album (a negative `albumId`), which takes no edit and no photo
            created (int | Unset): Unix time; absent when VK gives none Example: 1794550000.
            updated (int | Unset): Unix time; absent when VK gives none Example: 1794553600.
            thumb (str | Unset): The cover's address, when VK gives one Example: https://sun9-1.userapi.com/....
            privacy_view (list[str] | Unset): A page's album, to its owner. Who sees it, in the words `POST /album/create`
                takes Example: ['all'].
            privacy_comment (list[str] | Unset): A page's album, to its owner. Who comments, in the words `POST
                /album/create` takes Example: ['friends'].
            upload_by_admins_only (bool | Unset): A community's album, to a page that manages the community. Only the
                managers upload Example: True.
            comments_disabled (bool | Unset): A community's album, to a page that manages the community. Comments are off
    """

    album: str
    owner_id: int
    album_id: int
    title: str
    description: str
    size: int
    can_upload: bool
    system: bool
    created: int | Unset = UNSET
    updated: int | Unset = UNSET
    thumb: str | Unset = UNSET
    privacy_view: list[str] | Unset = UNSET
    privacy_comment: list[str] | Unset = UNSET
    upload_by_admins_only: bool | Unset = UNSET
    comments_disabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        album = self.album

        owner_id = self.owner_id

        album_id = self.album_id

        title = self.title

        description = self.description

        size = self.size

        can_upload = self.can_upload

        system = self.system

        created = self.created

        updated = self.updated

        thumb = self.thumb

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
                "ownerId": owner_id,
                "albumId": album_id,
                "title": title,
                "description": description,
                "size": size,
                "canUpload": can_upload,
                "system": system,
            }
        )
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if thumb is not UNSET:
            field_dict["thumb"] = thumb
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

        owner_id = d.pop("ownerId")

        album_id = d.pop("albumId")

        title = d.pop("title")

        description = d.pop("description")

        size = d.pop("size")

        can_upload = d.pop("canUpload")

        system = d.pop("system")

        created = d.pop("created", UNSET)

        updated = d.pop("updated", UNSET)

        thumb = d.pop("thumb", UNSET)

        privacy_view = cast(list[str], d.pop("privacyView", UNSET))

        privacy_comment = cast(list[str], d.pop("privacyComment", UNSET))

        upload_by_admins_only = d.pop("uploadByAdminsOnly", UNSET)

        comments_disabled = d.pop("commentsDisabled", UNSET)

        album = cls(
            album=album,
            owner_id=owner_id,
            album_id=album_id,
            title=title,
            description=description,
            size=size,
            can_upload=can_upload,
            system=system,
            created=created,
            updated=updated,
            thumb=thumb,
            privacy_view=privacy_view,
            privacy_comment=privacy_comment,
            upload_by_admins_only=upload_by_admins_only,
            comments_disabled=comments_disabled,
        )

        album.additional_properties = d
        return album

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
