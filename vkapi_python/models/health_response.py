from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HealthResponse")


@_attrs_define
class HealthResponse:
    """
    Attributes:
        success (bool): false when the database does not answer Example: True.
        status (str): `ok`, or `degraded` when the database does not answer Example: ok.
        version (str):  Example: 1.4.1.
        uptime_seconds (int):  Example: 12345.
        db_ok (bool):  Example: True.
        goroutines (int):  Example: 12.
        mem_alloc_mb (int):  Example: 9.
        timestamp (int): Unix time in seconds Example: 1793001234.
    """

    success: bool
    status: str
    version: str
    uptime_seconds: int
    db_ok: bool
    goroutines: int
    mem_alloc_mb: int
    timestamp: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status

        version = self.version

        uptime_seconds = self.uptime_seconds

        db_ok = self.db_ok

        goroutines = self.goroutines

        mem_alloc_mb = self.mem_alloc_mb

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "status": status,
                "version": version,
                "uptime_seconds": uptime_seconds,
                "db_ok": db_ok,
                "goroutines": goroutines,
                "mem_alloc_mb": mem_alloc_mb,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        status = d.pop("status")

        version = d.pop("version")

        uptime_seconds = d.pop("uptime_seconds")

        db_ok = d.pop("db_ok")

        goroutines = d.pop("goroutines")

        mem_alloc_mb = d.pop("mem_alloc_mb")

        timestamp = d.pop("timestamp")

        health_response = cls(
            success=success,
            status=status,
            version=version,
            uptime_seconds=uptime_seconds,
            db_ok=db_ok,
            goroutines=goroutines,
            mem_alloc_mb=mem_alloc_mb,
            timestamp=timestamp,
        )

        health_response.additional_properties = d
        return health_response

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
