from typing import Generic, TypeVar, Type, List, Optional
from sqlalchemy.orm import Session
from app.db.base_class import (
    BaseEntity,
)  # <- 네 프로젝트의 BaseEntity (SQLAlchemy Base)

T = TypeVar("T", bound=BaseEntity)


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def get(self, db: Session, id: int) -> Optional[T]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session) -> List[T]:
        return db.query(self.model).all()

    def create(self, db: Session, obj_in: dict) -> T:
        """딕셔너리 형태 입력 → SQLAlchemy 객체 생성"""
        db_obj = self.model(**obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: T, update_data: dict) -> T:
        """기존 객체(db_obj)에 update_data 딕셔너리로 값 덮어쓰기"""
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, id: int) -> None:
        obj = db.query(self.model).filter(self.model.id == id).first()
        if obj:
            db.delete(obj)
            db.commit()
