from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

# SQLAlchemy engine creation
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True, # 연결 감지
    pool_size = 10,
    max_overflow = 20,
)

# Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()