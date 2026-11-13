from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlbumReorderBody")


@_attrs_define
class AlbumReorderBody:
    """The album and exactly one of `before` and `after`, an album of the same owner.

    Attributes:
        album (str): `<owner_id>_<album_id>`, the page's own or a community's, not a system album Example:
            -210132800_312370605.
        before (str | Unset): The album it goes right before, `<owner_id>_<album_id>` Example: -210132800_312370606.
        after (str | Unset): The album it goes right after, `<owner_id>_<album_id>`
    """

    album: str
    before: str | Unset = UNSET
    after: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        album = self.album

        before = self.before

        after = self.after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "album": album,
            }
        )
        if before is not UNSET:
            field_dict["before"] = before
        if after is not UNSET:
            field_dict["after"] = after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        album = d.pop("album")

        before = d.pop("before", UNSET)

        after = d.pop("after", UNSET)

        album_reorder_body = cls(
            album=album,
            before=before,
            after=after,
        )

        album_reorder_body.additional_properties = d
        return album_reorder_body

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
