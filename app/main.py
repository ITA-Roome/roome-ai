from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.common.response import success_response
from app.core.logging_config import get_logger
from app.common.status.success_status import SuccessStatus
from app.common.status.error_status import ErrorStatus
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
from app.common.exception.general_exception import GeneralException
from app.common.exception.handler import (
    general_exception_handler,
)

logger = get_logger(__name__)

app = FastAPI(
    title="Roome AI",
    version="1.0.0",
    description="잇타(It's TIME) 8기 2팀 Roome AI 서버의 Swagger 문서입니다.",
    docs_url="/swagger-ui/index.html",  # Swagger UI 경로
    redoc_url="/redoc",  # ReDoc 경로
    openapi_url="/api-docs",  # OpenAPI 스키마 경로
    debug=False,  # 디버그 모드 설정
)


# 400, 401, 403, 404, 405, 409, 500등 (FastAPI가 내부적으로 발생시키는 모든 HTTP 예외)
app.add_exception_handler(StarletteHTTPException, general_exception_handler)
app.add_exception_handler(RequestValidationError, general_exception_handler)
app.add_exception_handler(GeneralException, general_exception_handler)


@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return success_response(
        status=SuccessStatus.SUCCESS_200, data={"message": "Welcome to Roome AI!"}
    )


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))  # 간단한 쿼리로 DB 연결 확인
    return GeneralException(status=ErrorStatus.INTERNAL_SERVER_ERROR)
