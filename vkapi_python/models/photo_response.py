from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.page_photos import PagePhotos


T = TypeVar("T", bound="PhotoResponse")


@_attrs_define
class PhotoResponse:
    """
    Attributes:
        success (bool):  Example: True.
        attachment (str): The photo for `attachments` of a send, in any dialog of the page Example:
            photo1127016903_457239017_9b0e3c1a2f.
        width (int): The photo's width as uploaded Example: 1280.
        height (int):  Example: 960.
        page_photos (PagePhotos | Unset): The photo work of the VK page, as this gateway did it for all the
            page's accounts (since 2.5.0): in `GET /session/status` with a stored
            token, and in the 200 answers of `POST /media/photo` and
            `POST /album/photo` with that call counted. Only calls VK did count.
            Another gateway on the same page is not seen. VK's real limits are
            unknown: the gateway refuses nothing by these numbers, the caller
            paces. Left out when the gateway's database fails to give them.

            - `uploads`: new photos VK saved, `photos.save` (`POST /album/photo`)
              and `photos.saveMessagesPhoto` (`POST /media/photo`), one pool of
              VK's flood control;
            - `copies`: `photos.copy`, a VK photo copied into the page's own
              album;
            - `captions`: `photos.edit`, the caption of a copy and
              `POST /album/photo/edit`.
    """

    success: bool
    attachment: str
    width: int
    height: int
    page_photos: PagePhotos | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        attachment = self.attachment

        width = self.width

        height = self.height

        page_photos: dict[str, Any] | Unset = UNSET
        if not isinstance(self.page_photos, Unset):
            page_photos = self.page_photos.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "attachment": attachment,
                "width": width,
                "height": height,
            }
        )
        if page_photos is not UNSET:
            field_dict["pagePhotos"] = page_photos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_photos import PagePhotos

        d = dict(src_dict)
        success = d.pop("success")

        attachment = d.pop("attachment")

        width = d.pop("width")

        height = d.pop("height")

        _page_photos = d.pop("pagePhotos", UNSET)
        page_photos: PagePhotos | Unset
        if isinstance(_page_photos, Unset):
            page_photos = UNSET
        else:
            page_photos = PagePhotos.from_dict(_page_photos)

        photo_response = cls(
            success=success,
            attachment=attachment,
            width=width,
            height=height,
            page_photos=page_photos,
        )

        photo_response.additional_properties = d
        return photo_response

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
