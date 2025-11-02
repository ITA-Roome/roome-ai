from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.common.response import success_response
from app.common.status.success_status import SuccessStatus
from app.common.status.error_status import ErrorStatus
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
from app.common.exception.general_exception import GeneralException
from app.common.exception.handler import (
    general_exception_handler,
)

app = FastAPI(title="Roome AI")

# 400, 401, 403, 404, 405 등 (FastAPI가 내부적으로 발생시키는 모든 HTTP 예외)
app.add_exception_handler(StarletteHTTPException, general_exception_handler)

# 400 ValidationError (요청 바디/쿼리 검증 실패)
app.add_exception_handler(RequestValidationError, general_exception_handler)

# 나머지 모든 예외 (500, 런타임 에러, DB 에러 등)
app.add_exception_handler(GeneralException, general_exception_handler)


@app.get("/")
def read_root():
    return success_response(
        status=SuccessStatus.SUCCESS_200, data={"message": "Welcome to Roome AI!"}
    )


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))  # 간단한 쿼리로 DB 연결 확인
    return GeneralException(status=ErrorStatus.INTERNAL_SERVER_ERROR)
