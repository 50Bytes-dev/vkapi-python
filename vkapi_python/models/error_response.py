from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """The error body of every call. `401` has no `code`. An answer of a call
    that reaches VK may also carry `upstreamCode` and the page's pause.

        Attributes:
            success (bool):
            error (str): A fixed English text per case; never VK's text. Do not branch on it. Example: VK did not confirm
                the message; it may have been delivered.
            code (str | Unset): The machine code; absent on 401. Generic: `INVALID_INPUT`,
                `INTERNAL_ERROR`, `NOT_FOUND`. Login: `login_unavailable`,
                `login_rate_limited`, `code_required`, `code_not_required`,
                `already_logged_in`, `invalid_code`, `login_expired`,
                `login_rejected`, `login_failed`, `login_limited`. Delivery: `not_connected`,
                `invalid_target`, `address_not_found`, `address_refused`,
                `send_rejected`, `message_rejected`, `attachment_rejected`,
                `send_failed`. Other calls: `page_paused`, `page_busy`, `vk_error`,
                `response_too_large`. Photo:
                `invalid_image`, `fetch_failed`, `upload_failed`. Albums (2.2.0):
                `album_refused`, `album_full`. Comments (2.3.0): `comment_refused`.
                Communities (2.4.0): `group_refused`. Example: send_failed.
            upstream_code (str | Unset): The VK error number behind the answer as a string (`"984"`), or `"busy"`. Absent
                when VK did not answer with an error, and on a pause that was already there. Example: 984.
            retry_after_ms (int | Unset): With `send_rejected` "busy" and `page_busy`: in how many milliseconds
                the call may come again (the send in flight, the page's queue of VK
                calls). With `login_limited` and `login_rate_limited` (2.1.0): when a
                login may start, or a code go, again. Example: 2400.
            paused (bool | Unset): Present (true) only when the page is paused; stop choosing every connection of this page.
            pause_reason (str | Unset): Why sending from the page is paused: `captcha` (VK error 14 the gateway
                did not solve), `spam` (7, 9, 17, 29, 983, 984) or `access_denied` (15). Example: spam.
            captcha_solve_error (str | Unset): Why the gateway did not solve VK's captcha (solving on): on a pause it
                set for the captcha, on any call (since 2.0.3; before, on a send), or
                on a refusal with `upstreamCode` "14" and no pause. `timeout`, `bot`,
                `page_changed`, `failed`, `rejected` (VK asked again after the answer,
                or a second captcha came in the same operation) or `not_tried` (no
                `redirect_uri` or `captcha_sid`, the captcha page not on a VK host, or
                the OAuth call of the token refresh, whose captcha is not solved). `bot` (VK's antibot answered BOT and
                offered nothing else) and `page_changed` mean the solver may need a new
                browser recording; a slider VK offered with no time left to drag it is
                `timeout`, and a slider answer VK did not take is `failed`. Example: timeout.
            rejected_attachments (list[str] | Unset): With `attachment_rejected`, the photos VK does not give the page, or
                refuses it on an album call Example: ['photo-12345_457239001_ak11'].
            attachment (str | Unset): `POST /album/photo` (2.2.0): a failure after a copy of the photo was
                made: the copy, in the album without its caption (the caption failed),
                or in the page's saved photos (the move failed and the gateway could
                not delete the copy; in the album when VK's answer was lost) Example: photo1127016903_457239200.
            saved (str | Unset): `POST /album/photo` (2.5.0), on every failure but `INVALID_INPUT`:
                what became of the photo. "no": nothing of the call is in the album.
                "maybe": `photos.save` of the upload or `photos.move` of the copy went
                out and its answer was lost (no answer, cut, VK's 1, 10, 13 or 995); the
                photo may be in the album. "yes": the photo is in the album without
                its caption (`attachment`). Example: maybe.
            stage (str | Unset): `POST /album/photo` (2.5.0): the step that failed. `fetch` (the url,
                or the image of a `photo` on VK's servers), `source` (`photos.getById`
                of a `photo` going into a community's album), `prepare` (the JPEG, or
                the gateway busy with other photos), `server`
                (`photos.getUploadServer`), `upload` (the file posted), `save`
                (`photos.save`), `copy` (`photos.copy`), `move` (`photos.move`),
                `caption` (`photos.edit` of the copy's caption). Absent without a
                connected login, and on a page paused before the first VK call. Example: save.
            copy_removed (bool | Unset): `POST /album/photo` (2.5.0), after VK refused to move the copy into
                the album: true, the copy is deleted from the page's saved photos (no
                `attachment`); false, it stays there (`attachment`)
            deleted (list[str] | Unset): `POST /album/photo/delete` (2.5.0): VK refused the delete and the gateway's
                read of the photos afterwards answered: the photos VK no longer gives
            kept (list[str] | Unset): With `deleted`, the photos VK still gives
            checked (bool | Unset): Whether the gateway could look after a write whose outcome VK did
                not tell. `POST /album/photo` (2.5.0), with `saved` "maybe": true,
                the gateway looked at the album once (`photos.get`) and did not find
                the photo for sure; false, it could not look (no time, the page
                paused, VK did not answer the look); with `saved` "yes": true, the
                look found the copy whose move was lost and its caption failed.
                `POST /album/photo/delete` (2.5.0): true when the gateway read the
                photos after the failed delete (`deleted` and `kept`), false when
                that read failed too, or gave none of the photos after a refusal
                (gone, or no longer the page's: VK answers both alike)
            repeated (bool | Unset): `POST /album/photo` (2.5.0): present (true) when the answer is that
                of an earlier call with the same `ref`: its stored answer as it was,
                or the answer to a first call cut by a stop of the gateway or still
                running
            pending (bool | Unset): `POST /album/photo` (2.5.0): present (true) when the first call with
                the same `ref` was still running when this repeat's request ended;
                repeat later for its answer
    """

    success: bool
    error: str
    code: str | Unset = UNSET
    upstream_code: str | Unset = UNSET
    retry_after_ms: int | Unset = UNSET
    paused: bool | Unset = UNSET
    pause_reason: str | Unset = UNSET
    captcha_solve_error: str | Unset = UNSET
    rejected_attachments: list[str] | Unset = UNSET
    attachment: str | Unset = UNSET
    saved: str | Unset = UNSET
    stage: str | Unset = UNSET
    copy_removed: bool | Unset = UNSET
    deleted: list[str] | Unset = UNSET
    kept: list[str] | Unset = UNSET
    checked: bool | Unset = UNSET
    repeated: bool | Unset = UNSET
    pending: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        error = self.error

        code = self.code

        upstream_code = self.upstream_code

        retry_after_ms = self.retry_after_ms

        paused = self.paused

        pause_reason = self.pause_reason

        captcha_solve_error = self.captcha_solve_error

        rejected_attachments: list[str] | Unset = UNSET
        if not isinstance(self.rejected_attachments, Unset):
            rejected_attachments = self.rejected_attachments

        attachment = self.attachment

        saved = self.saved

        stage = self.stage

        copy_removed = self.copy_removed

        deleted: list[str] | Unset = UNSET
        if not isinstance(self.deleted, Unset):
            deleted = self.deleted

        kept: list[str] | Unset = UNSET
        if not isinstance(self.kept, Unset):
            kept = self.kept

        checked = self.checked

        repeated = self.repeated

        pending = self.pending

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "error": error,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code
        if retry_after_ms is not UNSET:
            field_dict["retryAfterMs"] = retry_after_ms
        if paused is not UNSET:
            field_dict["paused"] = paused
        if pause_reason is not UNSET:
            field_dict["pauseReason"] = pause_reason
        if captcha_solve_error is not UNSET:
            field_dict["captchaSolveError"] = captcha_solve_error
        if rejected_attachments is not UNSET:
            field_dict["rejectedAttachments"] = rejected_attachments
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if saved is not UNSET:
            field_dict["saved"] = saved
        if stage is not UNSET:
            field_dict["stage"] = stage
        if copy_removed is not UNSET:
            field_dict["copyRemoved"] = copy_removed
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if kept is not UNSET:
            field_dict["kept"] = kept
        if checked is not UNSET:
            field_dict["checked"] = checked
        if repeated is not UNSET:
            field_dict["repeated"] = repeated
        if pending is not UNSET:
            field_dict["pending"] = pending

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        error = d.pop("error")

        code = d.pop("code", UNSET)

        upstream_code = d.pop("upstreamCode", UNSET)

        retry_after_ms = d.pop("retryAfterMs", UNSET)

        paused = d.pop("paused", UNSET)

        pause_reason = d.pop("pauseReason", UNSET)

        captcha_solve_error = d.pop("captchaSolveError", UNSET)

        rejected_attachments = cast(list[str], d.pop("rejectedAttachments", UNSET))

        attachment = d.pop("attachment", UNSET)

        saved = d.pop("saved", UNSET)

        stage = d.pop("stage", UNSET)

        copy_removed = d.pop("copyRemoved", UNSET)

        deleted = cast(list[str], d.pop("deleted", UNSET))

        kept = cast(list[str], d.pop("kept", UNSET))

        checked = d.pop("checked", UNSET)

        repeated = d.pop("repeated", UNSET)

        pending = d.pop("pending", UNSET)

        error_response = cls(
            success=success,
            error=error,
            code=code,
            upstream_code=upstream_code,
            retry_after_ms=retry_after_ms,
            paused=paused,
            pause_reason=pause_reason,
            captcha_solve_error=captcha_solve_error,
            rejected_attachments=rejected_attachments,
            attachment=attachment,
            saved=saved,
            stage=stage,
            copy_removed=copy_removed,
            deleted=deleted,
            kept=kept,
            checked=checked,
            repeated=repeated,
            pending=pending,
        )

        error_response.additional_properties = d
        return error_response

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
