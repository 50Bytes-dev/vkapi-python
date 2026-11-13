from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.group_settings_response_settings import GroupSettingsResponseSettings


T = TypeVar("T", bound="GroupSettingsResponse")


@_attrs_define
class GroupSettingsResponse:
    """
    Attributes:
        success (bool):  Example: True.
        owner_id (int):  Example: -210132800.
        community_id (int):  Example: 210132800.
        settings (GroupSettingsResponseSettings): VK's answer to `groups.getSettings` as VK wrote it Example: {'title':
            'Тестовое сообщество', 'description': '', 'wall': 1, 'photos': 1, 'main_section': 0}.
    """

    success: bool
    owner_id: int
    community_id: int
    settings: GroupSettingsResponseSettings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        owner_id = self.owner_id

        community_id = self.community_id

        settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "ownerId": owner_id,
                "communityId": community_id,
                "settings": settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_settings_response_settings import GroupSettingsResponseSettings

        d = dict(src_dict)
        success = d.pop("success")

        owner_id = d.pop("ownerId")

        community_id = d.pop("communityId")

        settings = GroupSettingsResponseSettings.from_dict(d.pop("settings"))

        group_settings_response = cls(
            success=success,
            owner_id=owner_id,
            community_id=community_id,
            settings=settings,
        )

        group_settings_response.additional_properties = d
        return group_settings_response

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
