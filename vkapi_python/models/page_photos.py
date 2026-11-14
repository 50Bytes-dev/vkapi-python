from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.photo_work_window import PhotoWorkWindow


T = TypeVar("T", bound="PagePhotos")


@_attrs_define
class PagePhotos:
    """The photo work of the VK page, as this gateway did it for all the
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

        Attributes:
            uploads (PhotoWorkWindow): A count by whole minutes of the gateway's clock, coarse by up to a
                minute
            copies (PhotoWorkWindow): A count by whole minutes of the gateway's clock, coarse by up to a
                minute
            captions (PhotoWorkWindow): A count by whole minutes of the gateway's clock, coarse by up to a
                minute
    """

    uploads: PhotoWorkWindow
    copies: PhotoWorkWindow
    captions: PhotoWorkWindow
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uploads = self.uploads.to_dict()

        copies = self.copies.to_dict()

        captions = self.captions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploads": uploads,
                "copies": copies,
                "captions": captions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.photo_work_window import PhotoWorkWindow

        d = dict(src_dict)
        uploads = PhotoWorkWindow.from_dict(d.pop("uploads"))

        copies = PhotoWorkWindow.from_dict(d.pop("copies"))

        captions = PhotoWorkWindow.from_dict(d.pop("captions"))

        page_photos = cls(
            uploads=uploads,
            copies=copies,
            captions=captions,
        )

        page_photos.additional_properties = d
        return page_photos

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
