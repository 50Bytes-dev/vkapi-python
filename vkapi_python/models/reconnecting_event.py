from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReconnectingEvent")


@_attrs_define
class ReconnectingEvent:
    """Accepted in a subscription (kept from maxapi), never sent.

    Attributes:
        type_ (Literal['Reconnecting']):
        user_id (str): The account id (`userID` and `instanceID` are the same) Example:
            6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
        instance_id (str): The account id (`userID` and `instanceID` are the same) Example:
            6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
        instance_name (str): The account name Example: retail-12-vk-34.
        event_timestamp (int): Unix time in seconds, set when the event happened; a retry keeps it Example: 1793001234.
    """

    type_: Literal["Reconnecting"]
    user_id: str
    instance_id: str
    instance_name: str
    event_timestamp: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        user_id = self.user_id

        instance_id = self.instance_id

        instance_name = self.instance_name

        event_timestamp = self.event_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "userID": user_id,
                "instanceID": instance_id,
                "instanceName": instance_name,
                "eventTimestamp": event_timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["Reconnecting"], d.pop("type"))
        if type_ != "Reconnecting":
            raise ValueError(f"type must match const 'Reconnecting', got '{type_}'")

        user_id = d.pop("userID")

        instance_id = d.pop("instanceID")

        instance_name = d.pop("instanceName")

        event_timestamp = d.pop("eventTimestamp")

        reconnecting_event = cls(
            type_=type_,
            user_id=user_id,
            instance_id=instance_id,
            instance_name=instance_name,
            event_timestamp=event_timestamp,
        )

        reconnecting_event.additional_properties = d
        return reconnecting_event

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
