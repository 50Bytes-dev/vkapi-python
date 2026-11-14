from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="AlbumPhotoUpload")


@_attrs_define
class AlbumPhotoUpload:
    """
    Attributes:
        album (str): `<owner_id>_<album_id>`, at most 16 KiB Example: -210132800_312370605.
        file (File): The image file
        caption (str | Unset): At most 2048 characters
        ref (str | Unset): 2.5.0, as in the JSON body; the file's bytes stand for the photo
    """

    album: str
    file: File
    caption: str | Unset = UNSET
    ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        album = self.album

        file = self.file.to_tuple()

        caption = self.caption

        ref = self.ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "album": album,
                "file": file,
            }
        )
        if caption is not UNSET:
            field_dict["caption"] = caption
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("album", (None, str(self.album).encode(), "text/plain")))

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.caption, Unset):
            files.append(("caption", (None, str(self.caption).encode(), "text/plain")))

        if not isinstance(self.ref, Unset):
            files.append(("ref", (None, str(self.ref).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        album = d.pop("album")

        file = File(payload=BytesIO(d.pop("file")))

        caption = d.pop("caption", UNSET)

        ref = d.pop("ref", UNSET)

        album_photo_upload = cls(
            album=album,
            file=file,
            caption=caption,
            ref=ref,
        )

        album_photo_upload.additional_properties = d
        return album_photo_upload

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
