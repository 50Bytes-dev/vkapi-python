from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.page_photos import PagePhotos


T = TypeVar("T", bound="AlbumPhotoResponse")


@_attrs_define
class AlbumPhotoResponse:
    """
    Attributes:
        success (bool):  Example: True.
        attachment (str): The photo, as a send takes it Example: photo-210132800_457239101.
        album (str):  Example: -210132800_312370605.
        photo_id (int):  Example: 457239101.
        owner_id (int): The photo's owner, the album's Example: -210132800.
        album_id (int):  Example: 312370605.
        how (str): `uploaded` (a new upload) or `copied` (a photo VK has, copied into the page's own album) Example:
            uploaded.
        width (int | Unset): The largest size VK keeps; absent on a copy Example: 1280.
        height (int | Unset):  Example: 960.
        checked (bool | Unset): 2.5.0: only when VK's answer to the save or the move was lost and the gateway found the
            photo in the album by its one look (`photos.get`): true
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
        repeated (bool | Unset): 2.5.0: present (true) when this is the stored answer of an earlier call with the same
            `ref`, as it was then (`pagePhotos` too); no VK call was made
    """

    success: bool
    attachment: str
    album: str
    photo_id: int
    owner_id: int
    album_id: int
    how: str
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    checked: bool | Unset = UNSET
    page_photos: PagePhotos | Unset = UNSET
    repeated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        attachment = self.attachment

        album = self.album

        photo_id = self.photo_id

        owner_id = self.owner_id

        album_id = self.album_id

        how = self.how

        width = self.width

        height = self.height

        checked = self.checked

        page_photos: dict[str, Any] | Unset = UNSET
        if not isinstance(self.page_photos, Unset):
            page_photos = self.page_photos.to_dict()

        repeated = self.repeated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "attachment": attachment,
                "album": album,
                "photoId": photo_id,
                "ownerId": owner_id,
                "albumId": album_id,
                "how": how,
            }
        )
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if checked is not UNSET:
            field_dict["checked"] = checked
        if page_photos is not UNSET:
            field_dict["pagePhotos"] = page_photos
        if repeated is not UNSET:
            field_dict["repeated"] = repeated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_photos import PagePhotos

        d = dict(src_dict)
        success = d.pop("success")

        attachment = d.pop("attachment")

        album = d.pop("album")

        photo_id = d.pop("photoId")

        owner_id = d.pop("ownerId")

        album_id = d.pop("albumId")

        how = d.pop("how")

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        checked = d.pop("checked", UNSET)

        _page_photos = d.pop("pagePhotos", UNSET)
        page_photos: PagePhotos | Unset
        if isinstance(_page_photos, Unset):
            page_photos = UNSET
        else:
            page_photos = PagePhotos.from_dict(_page_photos)

        repeated = d.pop("repeated", UNSET)

        album_photo_response = cls(
            success=success,
            attachment=attachment,
            album=album,
            photo_id=photo_id,
            owner_id=owner_id,
            album_id=album_id,
            how=how,
            width=width,
            height=height,
            checked=checked,
            page_photos=page_photos,
            repeated=repeated,
        )

        album_photo_response.additional_properties = d
        return album_photo_response

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
