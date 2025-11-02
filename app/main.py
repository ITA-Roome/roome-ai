from fastapi import FastAPI, Depends
from sqlalchemy.orm  import Session
from app.db.session import get_db

app = FastAPI(title = "Roome AI")

@app.get("/")
def read_root():
    return {"message": "Welcome to Roome AI!"}

@app.get("/health")
def health_check(db:Session = Depends(get_db)):
    db.execute("SELECT 1")  # 간단한 쿼리로 DB 연결 확인
    return {"status": "ok"}