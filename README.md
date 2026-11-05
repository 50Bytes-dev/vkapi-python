# vkapi-python
A client library for accessing VKAPI (https://github.com/50Bytes-dev/vkapi), the gateway that holds the login into a
personal VK page and works from it: it sends messages with a text and up to 10 photos to people and to group chats,
lists the page's conversations and the members of its chats, uploads a photo once for every chat, takes the photos
of wall posts by id and deletes the page's messages for everyone. vkapi and maxapi share one contract; this package
follows vkapi's version (2.0.2).

The package is generated from the gateway's OpenAPI schema (`static/api/spec.yml` in vkapi; the gateway serves it at
`/api/spec.yml`, with the Swagger UI at `/api/`). The full contract, with every code and when it comes, is
[`API.md`](https://github.com/50Bytes-dev/vkapi/blob/main/API.md).

## Clients
The gateway takes two tokens, each in its own header and without `Bearer`:

```python
import httpx

from vkapi_python import AuthenticatedClient, Client

# /admin/*: the admin token (VKAPI_ADMIN_TOKEN) in the Authorization header
admin = AuthenticatedClient(base_url="http://localhost:5558", token="<admin token>", prefix="")

# /session/* and /chat/*: the account token in the token header
account = AuthenticatedClient(
    base_url="http://localhost:5558",
    token="<account token>",
    auth_header_name="token",
    prefix="",
    timeout=httpx.Timeout(10.0),
)

# /health takes no token
public = Client(base_url="http://localhost:5558")
```

A send answers within 7.5 s (9 s when the gateway solves a captcha), and a status or connect that checks the login
with VK takes up to 8-9 s: httpx's default timeout of 5 s is too short for the account client. A photo upload
(`api.media.upload_photo`) takes up to about 35 s: give its client a longer timeout.

## Calls
Every operation is a module under `vkapi_python.api.<tag>` with four functions: `sync`, `sync_detailed`, `asyncio`
and `asyncio_detailed`. `sync` returns the parsed body, which for an error is an `ErrorResponse`; `sync_detailed`
returns a `Response` with `status_code` and `parsed`.

| Module | Call |
|---|---|
| `api.health.get_health` | `GET /health` |
| `api.admin.add_user` | `POST /admin/users` |
| `api.admin.edit_user` | `PUT /admin/users/{userid}` |
| `api.admin.delete_user` | `DELETE /admin/users/{userid}` |
| `api.session.connect` | `POST /session/connect` |
| `api.session.get_qr` | `GET /session/qr` |
| `api.session.submit_code` | `POST /session/code` |
| `api.session.get_status` | `GET /session/status` |
| `api.session.resume` | `POST /session/resume` |
| `api.session.disconnect` | `POST /session/disconnect` |
| `api.chat.send_text` | `POST /chat/send/text` |
| `api.chat.list_chats` | `GET /chat/list` |
| `api.chat.chat_info` | `GET /chat/info` |
| `api.chat.chat_members` | `GET /chat/members` |
| `api.chat.delete_messages` | `POST /chat/delete` |
| `api.media.upload_photo` | `POST /media/photo` |
| `api.wall.wall_photos` | `POST /wall/photos` |

Fields the gateway leaves out are `UNSET` (`from vkapi_python.types import UNSET`), which is falsy. Errors carry a
machine `code`; it is absent on 401, which means the token is unknown or the account was deleted.

### Create and delete an account

```python
from vkapi_python.api.admin import add_user, delete_user
from vkapi_python.models import AddUserBody

created = add_user.sync(
    client=admin,
    body=AddUserBody(
        name="shop-12-vk",
        webhook="https://shop.example/webhook/vk?secret=s3cr3t",
        events="Sync,QRAuthorized,AuthExpired,Disconnected,QRGenerated,QRScanned,QRCodeRequired,QRExpired,MessageOutcome,Paused,Resumed",
    ),
)
print(created.id, created.token)  # the token goes into the account client

delete_user.sync(client=admin, userid=created.id)
```

### Log in: connect, QR, code

```python
from vkapi_python.api.session import connect, get_qr, get_status, submit_code
from vkapi_python.models import CodeBody, ConnectBody, ErrorResponse, EventType

res = connect.sync(
    client=account,
    body=ConnectBody(
        subscribe=[EventType.SYNC, EventType.QRGENERATED, EventType.QRSCANNED, EventType.QRCODEREQUIRED,
                   EventType.QRAUTHORIZED, EventType.QREXPIRED, EventType.AUTHEXPIRED, EventType.MESSAGEOUTCOME],
    ),
)
if isinstance(res, ErrorResponse):
    raise RuntimeError(f"{res.code}: {res.error}")  # login_unavailable, not_connected, login_rate_limited, ...

if not res.already_connected:
    # The QR comes in the QRGenerated webhook (see "Parse a webhook"); reading it here is optional and keeps
    # nothing alive: the login runs until VK, the owner or the account ends it.
    qr = get_qr.sync(client=account)
    if isinstance(qr, ErrorResponse):
        if qr.code == "code_required":  # VK asks for a confirmation code after the scan
            submit_code.sync(client=account, body=CodeBody(code="123456"))
        elif qr.code == "already_logged_in":  # the login completed
            pass
        else:  # login_expired, login_rejected, login_failed: connect again
            ...
    else:
        show_qr(qr.qrcode, scanned=qr.scanned)  # your code: qrcode is a PNG data URI

status = get_status.sync(client=account)
if status.paused:  # read paused before connected
    print("paused:", status.pause_reason, status.upstream_code)
print("connected:", status.connected, "VK page:", status.max_user_id)
```

A paused page is resumed with `api.session.resume`; `body=ResumeBody(captcha_key="...")` carries the owner's answer
to `status.captcha_image`, if there is one.

### Send a message to a person or a group chat

```python
from vkapi_python.api.chat import send_text
from vkapi_python.models import ErrorResponse, SendTextBody

# A person: the VK user id
res = send_text.sync(
    client=account,
    body=SendTextBody(chat_id=987654321, text="Заказ 123 готов к выдаче", ref="order-123"),
)

# A group chat: 2000000000 + the chat's number as this page sees it (vk.ru/im/convo/2000000001),
# with photos (up to 10); the text may then be empty
res = send_text.sync(
    client=account,
    body=SendTextBody(
        chat_id=2000000001,
        text="Платье, 1200 ₽",
        attachments=["photo1127016903_457239017_9b0e3c1a2f"],
        dont_parse_links=True,
    ),
)

if isinstance(res, ErrorResponse):
    if res.code == "send_failed":
        # The outcome is unknown: never resend. With a ref, a MessageOutcome webhook tells later.
        ...
    elif res.code == "send_rejected" and res.upstream_code == "busy":
        # Nothing was sent: come again in res.retry_after_ms milliseconds.
        ...
    elif res.code == "attachment_rejected":
        # VK refused a photo: upload it anew and send again.
        ...
    else:
        # Nothing was sent: not_connected, invalid_target, address_refused, address_not_found,
        # message_rejected, send_rejected (see res.upstream_code; res.paused and res.pause_reason when paused).
        ...
else:
    print("sent:", res.message_id)  # a string; keep it to delete the message
```

### Photos

```python
from vkapi_python.api.media import upload_photo
from vkapi_python.api.wall import wall_photos
from vkapi_python.models import PhotoBody, WallPhotosBody

# Once per page: the attachment goes to any of its chats
photo = upload_photo.sync(client=account, body=PhotoBody(url="https://example.com/photo.jpg"))
print(photo.attachment, photo.width, photo.height)  # or an ErrorResponse: invalid_image, fetch_failed, upload_failed

# The photos of wall posts by id; a post VK does not give is found=False: upload its photos instead
posts = wall_photos.sync(client=account, body=WallPhotosBody(posts=["-12345_678"]))
for post in posts.posts:
    print(post.post, post.found, [p.attachment for p in post.photos or []])
```

### Delete for everyone

```python
from vkapi_python.api.chat import delete_messages
from vkapi_python.models import DeleteBody

res = delete_messages.sync(client=account, body=DeleteBody(chat_id=2000000001, message_ids=["12031"]))
for r in res.results:
    print(r.message_id, r.status)  # deleted, too_old (VK refused: error 924), forbidden, not_found
```

### List and search the page's chats

```python
from vkapi_python.api.chat import chat_info, chat_members, list_chats
from vkapi_python.types import UNSET

# All conversations, page by page
offset = 0
while True:
    page = list_chats.sync(client=account, offset=offset, count=50)
    for chat in page.items:
        print(chat.chat_id, chat.type_, chat.title, "can write:", chat.can_write)
    if page.next_offset is UNSET:
        break
    offset = page.next_offset

# Group chats and channels only
chats = list_chats.sync(client=account, type_=["chat", "channel"], count=200)

# Search by title or name, group chats only; VK finds at most 255
found = list_chats.sync(client=account, q="лимиты", type_=["chat"], count=20)

# The last message of each, its text included, and given chats by id
page = list_chats.sync(client=account, include=["lastMessage"], count=20)
info = chat_info.sync(client=account, chat_id=[2000000001, 2000000002])  # info.items, info.missing

# The first 200 members of each group chat and channel, and all members of one chat page by page
page = list_chats.sync(client=account, type_=["chat"], include=["participants"], count=50)
offset = 0
while True:
    members = chat_members.sync(client=account, chat_id=2000000001, offset=offset)
    for m in members.items:
        print(m.id, m.name, "admin:", m.is_admin)
    if members.next_offset is UNSET:
        break
    offset = members.next_offset
```

The gateway sets no bounds of its own beyond VK's (one call's most: 200 conversations, 100 ids, 200 members): how much
to ask for is the project's to decide. A list with `include=participants` takes 0.5 s more per conversation.

`type_` of a row is `user`, `chat`, `channel`, `group` or VK's own `email`; a person's row has `user_id`.

An error (`page_paused`, `vk_error`, `not_connected`, `INVALID_INPUT`) comes back as an `ErrorResponse`.

### Parse a webhook

Each event has its model; pick it by `type`. A model refuses a body of another type with `ValueError`. There are
thirteen events; since 1.4.0 the login can be followed from them alone, and since 2.0.0 `PausedEvent` and
`ResumedEvent` tell every account of a page about its pause (`pause_reason`, `upstream_code`,
`captcha_solve_error`), so the status need not be polled for it:

| Event | Fields besides `type`, `user_id`, `instance_id`, `instance_name`, `event_timestamp` |
|---|---|
| `QRGeneratedEvent` | `qrcode`: the QR as a PNG data URI (the same as `get_qr`); `qr_link`: VK's login link it encodes, to draw your own QR. Sent on the login's start and on every new QR |
| `QRScannedEvent` | none: the owner scanned the QR |
| `QRCodeRequiredEvent` | none: VK asks for the confirmation code (once per login); send it with `submit_code` |
| `QRAuthorizedEvent` | `max_user_id`; `auth_token`: **the VK access token of the login, full access to the owner's VK page** |
| `QRExpiredEvent` | `reason`: `login_expired`, `login_rejected` or `login_failed` |

`auth_token` is a live token of the owner's personal VK page, with access to its messages: whoever has it can act as
the owner. Store it like a password, never log it, and keep the webhook endpoint that receives it private. The model
leaves it out of `repr`. It is the token at login time: the gateway refreshes it later without an event. No other
event carries a secret.

```python
from vkapi_python.models import (
    AuthExpiredEvent, DisconnectedEvent, LoggedOutEvent, MessageOutcomeEvent, PausedEvent, QRAuthorizedEvent,
    QRCodeRequiredEvent, QRExpiredEvent, QRGeneratedEvent, QRScannedEvent, ReconnectingEvent, ResumedEvent,
    SyncEvent,
)

EVENTS = {
    "QRGenerated": QRGeneratedEvent, "QRScanned": QRScannedEvent, "QRCodeRequired": QRCodeRequiredEvent,
    "QRAuthorized": QRAuthorizedEvent, "QRExpired": QRExpiredEvent, "Sync": SyncEvent,
    "AuthExpired": AuthExpiredEvent, "Disconnected": DisconnectedEvent, "Reconnecting": ReconnectingEvent,
    "LoggedOut": LoggedOutEvent, "MessageOutcome": MessageOutcomeEvent,
    "Paused": PausedEvent, "Resumed": ResumedEvent,
}


def parse_event(body: dict):
    return EVENTS[body["type"]].from_dict(body)


event = parse_event(request_json)  # the webhook's JSON body
if isinstance(event, QRGeneratedEvent):
    show_qr(event.qrcode)  # your code; or draw a QR of event.qr_link
elif isinstance(event, QRCodeRequiredEvent):
    ask_for_code()  # your code: then submit_code.sync(client=account, body=CodeBody(code=...))
elif isinstance(event, QRAuthorizedEvent):
    store_secret(event.max_user_id, event.auth_token)  # your code: full access to the owner's VK page
elif isinstance(event, QRExpiredEvent):
    print("login ended:", event.reason)  # login_expired, login_rejected, login_failed
elif isinstance(event, MessageOutcomeEvent):
    print(event.ref, "delivered" if event.delivered else "not delivered", event.message_id)
elif isinstance(event, AuthExpiredEvent):
    print("login lost:", event.reason)  # token_revoked, page_blocked, refresh_failed
elif isinstance(event, PausedEvent):
    print("page paused:", event.pause_reason, event.upstream_code)  # resume with api.session.resume
elif isinstance(event, ResumedEvent):
    print("page resumed:", event.max_user_id)
```

### Async

```python
from vkapi_python.api.session import get_status

async with account as client:
    status = await get_status.asyncio(client=client)
```

## Advanced customizations

`verify_ssl`, `timeout`, `headers`, `httpx_args` and the rest are on the generated `Client` and
`AuthenticatedClient`, see their docstrings. You can also customize the underlying `httpx.Client` or
`httpx.AsyncClient`:

```python
from vkapi_python import AuthenticatedClient


def log_response(response):
    request = response.request
    print(f"{request.method} {request.url} - Status {response.status_code}")


account = AuthenticatedClient(
    base_url="http://localhost:5558",
    token="<account token>",
    auth_header_name="token",
    prefix="",
    httpx_args={"event_hooks": {"response": [log_response]}},
)
```

## Regenerate client
After a change of `../vkapi/static/api/spec.yml`:

```shell
uv sync
./generate.sh
```

`generate.sh` runs `openapi-python-client` from the dev group and moves the generated `vkapi_client` package to
`vkapi_python`. The generator is pinned below 0.29: 0.29 writes code that needs Python 3.11 (`typing.Self`), and the
package supports 3.10.

`templates/client.py.jinja` overrides the generator's client template in one respect: `token` and the headers (which carry the token once a request is made) are left out of the clients' `repr`, so a client in a log or a traceback does not show the token. `templates/model.py.jinja` overrides the generator's model template the same way for the fields that carry a VK token (`auth_token` of `QRAuthorizedEvent`): they are left out of the model's `repr`. When the generator is upgraded, copy its new `client.py.jinja` and `model.py.jinja` and redo these changes.
