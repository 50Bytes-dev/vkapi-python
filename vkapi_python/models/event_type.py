from enum import Enum


class EventType(str, Enum):
    AUTHEXPIRED = "AuthExpired"
    DISCONNECTED = "Disconnected"
    LOGGEDOUT = "LoggedOut"
    MESSAGEOUTCOME = "MessageOutcome"
    QRAUTHORIZED = "QRAuthorized"
    QRCODEREQUIRED = "QRCodeRequired"
    QREXPIRED = "QRExpired"
    QRGENERATED = "QRGenerated"
    QRSCANNED = "QRScanned"
    RECONNECTING = "Reconnecting"
    SYNC = "Sync"

    def __str__(self) -> str:
        return str(self.value)
