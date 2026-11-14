from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PhotoWorkWindow")


@_attrs_define
class PhotoWorkWindow:
    """A count by whole minutes of the gateway's clock, coarse by up to a
    minute

        Attributes:
            hour (int): The last 60 minutes Example: 812.
            day (int): The last 24 hours Example: 4120.
    """

    hour: int
    day: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hour = self.hour

        day = self.day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hour": hour,
                "day": day,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hour = d.pop("hour")

        day = d.pop("day")

        photo_work_window = cls(
            hour=hour,
            day=day,
        )

        photo_work_window.additional_properties = d
        return photo_work_window

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
