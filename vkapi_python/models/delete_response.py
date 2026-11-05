from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.delete_result import DeleteResult


T = TypeVar("T", bound="DeleteResponse")


@_attrs_define
class DeleteResponse:
    """
    Attributes:
        success (bool):  Example: True.
        chat_id (int):  Example: 2000000001.
        results (list[DeleteResult]):
    """

    success: bool
    chat_id: int
    results: list[DeleteResult]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        chat_id = self.chat_id

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "chatId": chat_id,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_result import DeleteResult

        d = dict(src_dict)
        success = d.pop("success")

        chat_id = d.pop("chatId")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = DeleteResult.from_dict(results_item_data)

            results.append(results_item)

        delete_response = cls(
            success=success,
            chat_id=chat_id,
            results=results,
        )

        delete_response.additional_properties = d
        return delete_response

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
