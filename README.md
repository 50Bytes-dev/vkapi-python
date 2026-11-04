# vkapi-python
A client library for accessing VKAPI (https://github.com/50Bytes-dev/vkapi), the gateway that holds the login
into a personal VK page and sends text messages from it to people and to group chats.

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

A send answers within 8 s (9 s when the gateway solves a captcha), and a status or connect that checks the login
with VK takes up to 8-9 s: httpx's default timeout of 5 s is too short for the account client.

## Calls
Every operation is a module under `vkapi_python.api.<tag>` with four functions: `sync`, `sync_detailed`, `asyncio`
and `asyncio_detailed`. `sync` returns the parsed body, which for an error is an `ErrorResponse`; `sync_detailed`
returns a `Response` with `status_code` and `parsed`.

| Module | Call |
|---|---|
| `api.health.get_health` | `GET /health` |
| `api.admin.add_user` | `POST /admin/users` |
| `api.admin.delete_user` | `DELETE /admin/users/{userid}` |
| `api.session.connect` | `POST /session/connect` |
| `api.session.get_qr` | `GET /session/qr` |
| `api.session.submit_code` | `POST /session/code` |
| `api.session.get_status` | `GET /session/status` |
| `api.session.resume` | `POST /session/resume` |
| `api.session.disconnect` | `POST /session/disconnect` |
| `api.chat.send_text` | `POST /chat/send/text` |
| `api.chat.list_chats` | `GET /chat/list` |

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
        events="Sync,QRAuthorized,AuthExpired,Disconnected,QRGenerated,QRScanned,QRExpired,MessageOutcome",
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
        subscribe=[EventType.SYNC, EventType.QRAUTHORIZED, EventType.AUTHEXPIRED, EventType.QREXPIRED,
                   EventType.MESSAGEOUTCOME],
    ),
)
if isinstance(res, ErrorResponse):
    raise RuntimeError(f"{res.code}: {res.error}")  # login_unavailable, not_connected, login_rate_limited, ...

if not res.already_connected:
    # Poll the QR every few seconds while it is shown: the reads keep the login alive.
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

### Send a text to a person or a group chat

```python
from vkapi_python.api.chat import send_text
from vkapi_python.models import ErrorResponse, SendTextBody

# A person: the VK user id
res = send_text.sync(
    client=account,
    body=SendTextBody(chat_id=987654321, text="Заказ 123 готов к выдаче", ref="order-123"),
)

# A group chat: 2000000000 + the chat's number as this page sees it (vk.ru/im/convo/2000000001)
res = send_text.sync(client=account, body=SendTextBody(chat_id=2000000001, text="Новый заказ 124"))

if isinstance(res, ErrorResponse):
    if res.code == "send_failed":
        # The outcome is unknown: never resend. With a ref, a MessageOutcome webhook tells later.
        ...
    else:
        # Nothing was sent: not_connected, invalid_target, address_refused, address_not_found,
        # message_rejected, send_rejected (see res.upstream_code; res.paused and res.pause_reason when paused).
        ...
else:
    print("sent:", res.message_id)
```

### List and search the page's chats

```python
from vkapi_python.api.chat import list_chats
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

# Group chats only
chats = list_chats.sync(client=account, filter_="chats", count=200)

# Search by title or name; VK finds at most 255
found = list_chats.sync(client=account, q="лимиты", count=20)
```

An error (`page_paused`, `vk_error`, `not_connected`, `INVALID_INPUT`) comes back as an `ErrorResponse`.

### Parse a webhook

Each event has its model; pick it by `type`. A model refuses a body of another type with `ValueError`.

```python
from vkapi_python.models import (
    AuthExpiredEvent, DisconnectedEvent, LoggedOutEvent, MessageOutcomeEvent, QRAuthorizedEvent,
    QRExpiredEvent, QRGeneratedEvent, QRScannedEvent, ReconnectingEvent, SyncEvent,
)

EVENTS = {
    "QRGenerated": QRGeneratedEvent, "QRScanned": QRScannedEvent, "QRAuthorized": QRAuthorizedEvent,
    "QRExpired": QRExpiredEvent, "Sync": SyncEvent, "AuthExpired": AuthExpiredEvent,
    "Disconnected": DisconnectedEvent, "Reconnecting": ReconnectingEvent, "LoggedOut": LoggedOutEvent,
    "MessageOutcome": MessageOutcomeEvent,
}


def parse_event(body: dict):
    return EVENTS[body["type"]].from_dict(body)


event = parse_event(request_json)  # the webhook's JSON body
if isinstance(event, MessageOutcomeEvent):
    print(event.ref, "delivered" if event.delivered else "not delivered", event.message_id)
elif isinstance(event, AuthExpiredEvent):
    print("login lost:", event.reason)  # token_revoked, page_blocked, refresh_failed
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

`templates/client.py.jinja` overrides the generator's client template in one respect: `token` and the headers (which carry the token once a request is made) are left out of the clients' `repr`, so a client in a log or a traceback does not show the token. When the generator is upgraded, copy its new `client.py.jinja` and redo that change.
