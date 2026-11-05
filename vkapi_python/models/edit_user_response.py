from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EditUserResponse")


@_attrs_define
class EditUserResponse:
    """
    Attributes:
        success (bool):  Example: True.
        id (str):  Example: 6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
        name (str):  Example: retail-12-vk-34.
        events (str): The subscription, its known events only Example: Sync,Paused,Resumed.
    """

    success: bool
    id: str
    name: str
    events: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        id = self.id

        name = self.name

        events = self.events

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "id": id,
                "name": name,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        id = d.pop("id")

        name = d.pop("name")

        events = d.pop("events")

        edit_user_response = cls(
            success=success,
            id=id,
            name=name,
            events=events,
        )

        edit_user_response.additional_properties = d
        return edit_user_response

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
