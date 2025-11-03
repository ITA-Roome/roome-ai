# app/common/exception/handler.py
from fastapi import Request
from app.common.response import error_response
from app.common.status.error_status import ErrorStatus
from app.common.exception.general_exception import GeneralException


# General Exception Handler
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.common.response import error_response
from app.common.status.error_status import ErrorStatus
from app.common.exception.general_exception import GeneralException


# 400~500 General Exception Handler
async def general_exception_handler(request: Request, exc: Exception):

    print(f"Exception occurred: {exc}")  # 로그 남기기
    # 1. GeneralException (개발자가 직접 raise)
    if isinstance(exc, GeneralException):
        return error_response(status=exc.status, data=exc.data)

    # 2. FastAPI의 기본 HTTPException (404, 405 등)
    if isinstance(exc, StarletteHTTPException):
        status_map = {
            400: ErrorStatus.BAD_REQUEST,
            401: ErrorStatus.UNAUTHORIZED,
            403: ErrorStatus.FORBIDDEN,
            404: ErrorStatus.NOT_FOUND,
            405: ErrorStatus.METHOD_NOT_ALLOWED,
        }
        mapped_status = status_map.get(exc.status_code, ErrorStatus.BAD_REQUEST)
        return error_response(status=mapped_status, data={"detail": exc.detail})

    # 3. RequestValidationError (422 등)
    if isinstance(exc, RequestValidationError):
        return error_response(
            status=ErrorStatus.BAD_REQUEST,
            data={"errors": exc.errors()},
        )

    # 4. 나머지 모든 예외 (예기치 못한 500)
    return error_response(
        status=ErrorStatus.INTERNAL_SERVER_ERROR,
        data={"detail": str(exc)},
    )
