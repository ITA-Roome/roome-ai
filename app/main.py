from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.common.status.success_status import SuccessStatus
from app.common.status.error_status import ErrorStatus
from app.common.response import success_response
from app.common.response import error_response

app = FastAPI(title="Roome AI")


@app.get("/")
def read_root():
    return success_response(
        status=SuccessStatus.SUCCESS_200, data={"message": "Welcome to Roome AI!"}
    )


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))  # 간단한 쿼리로 DB 연결 확인
    return error_response(status=ErrorStatus.INTERNAL_SERVER_ERROR)
