from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PhotoBody")


@_attrs_define
class PhotoBody:
    """Exactly one of `url` and `data`.

    Attributes:
        url (str | Unset): An http or https address of the image Example: https://sun9-1.userapi.com/impg/photo.jpg.
        data (str | Unset): The image as base64 or a base64 data URL Example: data:image/png;base64,iVBORw0KGgo....
    """

    url: str | Unset = UNSET
    data: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        data = d.pop("data", UNSET)

        photo_body = cls(
            url=url,
            data=data,
        )

        photo_body.additional_properties = d
        return photo_body

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
