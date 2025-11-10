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
from app.common.exception.handler import general_exception_handler

from app.domain.ai.router.ai_router import router as ai_router

logger = get_logger(__name__)

# ✅ FastAPI 인스턴스 설정 (Swagger 포함)
app = FastAPI(
    title="Roome AI Recommendation API 🧠",
    version="1.0.0",
    description="잇타(It's TIME) 8기 2팀 Roome AI 서버의 Swagger 문서입니다.",
    docs_url="/swagger-ui/index.html",  # Swagger UI 경로
    redoc_url="/redoc",  # ReDoc 경로
    openapi_url="/api-docs",  # OpenAPI 스키마 경로
    debug=False,
)

# ✅ AI 추천 API 라우터 등록
app.include_router(ai_router)

# ✅ 예외 핸들러 등록
app.add_exception_handler(StarletteHTTPException, general_exception_handler)
app.add_exception_handler(RequestValidationError, general_exception_handler)
app.add_exception_handler(GeneralException, general_exception_handler)


# ✅ 루트 엔드포인트
@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return success_response(
        status=SuccessStatus.SUCCESS_200, data={"message": "Welcome to Roome AI!"}
    )


# ✅ 헬스체크
@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))  # DB 연결 확인 쿼리
    return success_response(
        status=SuccessStatus.SUCCESS_200, data={"message": "Database connection OK!"}
    )
