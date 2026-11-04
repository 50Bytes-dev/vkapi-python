from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QRGeneratedEvent")


@_attrs_define
class QRGeneratedEvent:
    """A QR login started, or VK expired the QR and the gateway issued a new one
    (1.4.0: with the QR). Show `qrcode`, or draw your own QR of `qrLink`.

        Attributes:
            type_ (Literal['QRGenerated']):
            qrcode (str): A 256x256 PNG data URI of `qrLink`, the same image `GET /session/qr` serves Example:
                data:image/png;base64,iVBORw0KGgo....
            qr_link (str): VK's login link the QR encodes Example: https://qr.vk.ru/ca?q=....
            user_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_name (str): The account name Example: retail-12-vk-34.
            event_timestamp (int): Unix time in seconds, set when the event happened; a retry keeps it Example: 1793001234.
    """

    type_: Literal["QRGenerated"]
    qrcode: str
    qr_link: str
    user_id: str
    instance_id: str
    instance_name: str
    event_timestamp: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        qrcode = self.qrcode

        qr_link = self.qr_link

        user_id = self.user_id

        instance_id = self.instance_id

        instance_name = self.instance_name

        event_timestamp = self.event_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "qrcode": qrcode,
                "qrLink": qr_link,
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
        type_ = cast(Literal["QRGenerated"], d.pop("type"))
        if type_ != "QRGenerated":
            raise ValueError(f"type must match const 'QRGenerated', got '{type_}'")

        qrcode = d.pop("qrcode")

        qr_link = d.pop("qrLink")

        user_id = d.pop("userID")

        instance_id = d.pop("instanceID")

        instance_name = d.pop("instanceName")

        event_timestamp = d.pop("eventTimestamp")

        qr_generated_event = cls(
            type_=type_,
            qrcode=qrcode,
            qr_link=qr_link,
            user_id=user_id,
            instance_id=instance_id,
            instance_name=instance_name,
            event_timestamp=event_timestamp,
        )

        qr_generated_event.additional_properties = d
        return qr_generated_event

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
