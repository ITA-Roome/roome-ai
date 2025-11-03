from enum import Enum
from app.common.base.base_status import BaseStatus


class ErrorStatus(Enum):
    # Common
    BAD_REQUEST = ("COMM_400", 400, "잘못된 요청입니다.")
    UNAUTHORIZED = ("COMM_401", 401, "인증이 필요합니다.")
    FORBIDDEN = ("COMM_403", 403, "접근 권한이 없습니다.")
    NOT_FOUND = ("COMM_404", 404, "요청한 자원을 찾을 수 없습니다.")
    METHOD_NOT_ALLOWED = ("COMM_405", 405, "허용되지 않은 메소드입니다.")
    CONFLICT = ("COMM_409", 409, "충돌이 발생했습니다.")
    INTERNAL_SERVER_ERROR = ("COMM_500", 500, "서버 내부 오류입니다.")

    def __init__(self, code: str, http_status: int, message: str):
        self.code = code
        self.http_status = http_status
        self.message = message
