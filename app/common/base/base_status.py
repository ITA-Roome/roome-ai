from typing import Protocol


class BaseStatus(Protocol):
    code: str
    http_status: int
    message: str
