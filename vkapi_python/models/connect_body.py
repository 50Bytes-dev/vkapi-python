from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_type import EventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectBody")


@_attrs_define
class ConnectBody:
    """
    Attributes:
        subscribe (list[EventType] | Unset): The event subscription; overwrites the stored one. Unknown types are
            dropped, duplicates kept once. Example: ['Sync', 'QRAuthorized', 'AuthExpired', 'Disconnected', 'QRGenerated',
            'QRScanned', 'QRCodeRequired', 'QRExpired', 'MessageOutcome'].
        immediate (bool | Unset): Read and ignored (kept from maxapi).
    """

    subscribe: list[EventType] | Unset = UNSET
    immediate: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscribe: list[str] | Unset = UNSET
        if not isinstance(self.subscribe, Unset):
            subscribe = []
            for subscribe_item_data in self.subscribe:
                subscribe_item = subscribe_item_data.value
                subscribe.append(subscribe_item)

        immediate = self.immediate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscribe is not UNSET:
            field_dict["subscribe"] = subscribe
        if immediate is not UNSET:
            field_dict["immediate"] = immediate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _subscribe = d.pop("subscribe", UNSET)
        subscribe: list[EventType] | Unset = UNSET
        if _subscribe is not UNSET:
            subscribe = []
            for subscribe_item_data in _subscribe:
                subscribe_item = EventType(subscribe_item_data)

                subscribe.append(subscribe_item)

        immediate = d.pop("immediate", UNSET)

        connect_body = cls(
            subscribe=subscribe,
            immediate=immediate,
        )

        connect_body.additional_properties = d
        return connect_body

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
