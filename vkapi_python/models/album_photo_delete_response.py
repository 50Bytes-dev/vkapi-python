from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlbumPhotoDeleteResponse")


@_attrs_define
class AlbumPhotoDeleteResponse:
    """
    Attributes:
        success (bool):  Example: True.
        deleted (list[str]): The photos VK no longer gives, as asked Example: ['photo-210132800_457239475'].
        kept (list[str]): The photos VK still gives after the delete (another owner's, for one)
        checked (bool | Unset): Present (false) when the read after the delete failed; `deleted` and `kept` are then
            empty
        unchecked (list[str] | Unset): With `checked` false, every photo asked
    """

    success: bool
    deleted: list[str]
    kept: list[str]
    checked: bool | Unset = UNSET
    unchecked: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        deleted = self.deleted

        kept = self.kept

        checked = self.checked

        unchecked: list[str] | Unset = UNSET
        if not isinstance(self.unchecked, Unset):
            unchecked = self.unchecked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "deleted": deleted,
                "kept": kept,
            }
        )
        if checked is not UNSET:
            field_dict["checked"] = checked
        if unchecked is not UNSET:
            field_dict["unchecked"] = unchecked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        deleted = cast(list[str], d.pop("deleted"))

        kept = cast(list[str], d.pop("kept"))

        checked = d.pop("checked", UNSET)

        unchecked = cast(list[str], d.pop("unchecked", UNSET))

        album_photo_delete_response = cls(
            success=success,
            deleted=deleted,
            kept=kept,
            checked=checked,
            unchecked=unchecked,
        )

        album_photo_delete_response.additional_properties = d
        return album_photo_delete_response

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
