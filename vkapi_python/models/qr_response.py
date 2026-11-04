from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QRResponse")


@_attrs_define
class QRResponse:
    """
    Attributes:
        success (bool):  Example: True.
        qrcode (str): A 256x256 PNG data URI of VK's login link Example: data:image/png;base64,iVBORw0KGgo....
        scanned (bool): true once the owner scanned the current QR
    """

    success: bool
    qrcode: str
    scanned: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        qrcode = self.qrcode

        scanned = self.scanned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "qrcode": qrcode,
                "scanned": scanned,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        qrcode = d.pop("qrcode")

        scanned = d.pop("scanned")

        qr_response = cls(
            success=success,
            qrcode=qrcode,
            scanned=scanned,
        )

        qr_response.additional_properties = d
        return qr_response

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
