from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WallPhoto")


@_attrs_define
class WallPhoto:
    """
    Attributes:
        attachment (str):  Example: photo-12345_457239001_ak11.
        width (int | Unset): The largest size VK has Example: 2560.
        height (int | Unset):  Example: 1706.
        url (str | Unset): The address of its largest copy of at most 2560 px on the longer side on
            VK's servers, what an upload keeps (2.2.0); absent when VK gives none. `POST /album/photo` takes it as `url` to
            put the photo into a
            community's album without asking VK for the photo (`photos.getById`) Example: https://sun9-1.userapi.com/....
    """

    attachment: str
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachment = self.attachment

        width = self.width

        height = self.height

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attachment": attachment,
            }
        )
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attachment = d.pop("attachment")

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        url = d.pop("url", UNSET)

        wall_photo = cls(
            attachment=attachment,
            width=width,
            height=height,
            url=url,
        )

        wall_photo.additional_properties = d
        return wall_photo

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
