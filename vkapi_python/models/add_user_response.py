from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddUserResponse")


@_attrs_define
class AddUserResponse:
    """
    Attributes:
        success (bool):  Example: True.
        id (str): The account id, for `DELETE /admin/users/{userid}` Example: 6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
        token (str): The account token, for the `token` header Example: 0b7a9e31-5d2c-4f6a-9e8b-1c2d3e4f5a6b.
        name (str):  Example: retail-12-vk-34.
    """

    success: bool
    id: str
    token: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        id = self.id

        token = self.token

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "id": id,
                "token": token,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        id = d.pop("id")

        token = d.pop("token")

        name = d.pop("name")

        add_user_response = cls(
            success=success,
            id=id,
            token=token,
            name=name,
        )

        add_user_response.additional_properties = d
        return add_user_response

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
