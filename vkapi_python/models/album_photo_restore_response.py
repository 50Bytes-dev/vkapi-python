from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.album_photo import AlbumPhoto


T = TypeVar("T", bound="AlbumPhotoRestoreResponse")


@_attrs_define
class AlbumPhotoRestoreResponse:
    """
    Attributes:
        success (bool):  Example: True.
        attachment (str):  Example: photo-210132800_457239475.
        photo (AlbumPhoto | Unset): A photo as VK gives it to `GET /album/photos` and `POST /album/photo/restore`.
        checked (bool | Unset): Present (false) when the read after the restore failed; `photo` is then absent
    """

    success: bool
    attachment: str
    photo: AlbumPhoto | Unset = UNSET
    checked: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        attachment = self.attachment

        photo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.photo, Unset):
            photo = self.photo.to_dict()

        checked = self.checked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "attachment": attachment,
            }
        )
        if photo is not UNSET:
            field_dict["photo"] = photo
        if checked is not UNSET:
            field_dict["checked"] = checked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.album_photo import AlbumPhoto

        d = dict(src_dict)
        success = d.pop("success")

        attachment = d.pop("attachment")

        _photo = d.pop("photo", UNSET)
        photo: AlbumPhoto | Unset
        if isinstance(_photo, Unset):
            photo = UNSET
        else:
            photo = AlbumPhoto.from_dict(_photo)

        checked = d.pop("checked", UNSET)

        album_photo_restore_response = cls(
            success=success,
            attachment=attachment,
            photo=photo,
            checked=checked,
        )

        album_photo_restore_response.additional_properties = d
        return album_photo_restore_response

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
