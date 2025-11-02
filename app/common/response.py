from typing import Any, Optional, TypeVar
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from app.common.base.base_status import BaseStatus

T = TypeVar("T")


class ApiResponse(BaseModel):
    is_success: bool
    code: str
    message: str
    data: Any = None


# Build Response
def build_response(
    status: BaseStatus, is_success: bool, data: Any = None
) -> JSONResponse:
    return JSONResponse(
        status_code=status.http_status,
        content=ApiResponse(
            is_success=is_success,
            code=status.code,
            message=status.message,
            data=data,
        ).model_dump(),
    )


# Success Response
def success_response(status: BaseStatus, data: Any = None) -> JSONResponse:
    return build_response(status=status, is_success=True, data=data)


# Error Response
def error_response(status: BaseStatus, data: Optional[Any] = None) -> JSONResponse:
    return build_response(status=status, is_success=False, data=data)
