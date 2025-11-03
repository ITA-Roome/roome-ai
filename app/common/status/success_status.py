from enum import Enum
from app.common.base.base_status import BaseStatus


class SuccessStatus(Enum):
    # Common
    SUCCESS_200 = ("COMM_200", 200, "성공입니다.")
    SUCCESS_201 = ("COMM_201", 201, "성공입니다.")
    SUCCESS_204 = ("COMM_204", 204, "성공입니다.")

    def __init__(self, code: str, http_status: int, message: str):
        self.code = code
        self.http_status = http_status
        self.message = message
