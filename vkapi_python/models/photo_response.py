from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PhotoResponse")


@_attrs_define
class PhotoResponse:
    """
    Attributes:
        success (bool):  Example: True.
        attachment (str): The photo for `attachments` of a send, in any dialog of the page Example:
            photo1127016903_457239017_9b0e3c1a2f.
        width (int): The photo's width as uploaded Example: 1280.
        height (int):  Example: 960.
    """

    success: bool
    attachment: str
    width: int
    height: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        attachment = self.attachment

        width = self.width

        height = self.height

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "attachment": attachment,
                "width": width,
                "height": height,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        attachment = d.pop("attachment")

        width = d.pop("width")

        height = d.pop("height")

        photo_response = cls(
            success=success,
            attachment=attachment,
            width=width,
            height=height,
        )

        photo_response.additional_properties = d
        return photo_response

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
