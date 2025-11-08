from typing import Generic, TypeVar, Type, List, Optional
from sqlalchemy.orm import Session
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def get(self, db: Session, id: int) -> Optional[T]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session) -> List[T]:
        return db.query(self.model).all()

    def create(self, db: Session, obj_in: T) -> T:
        db_obj = self.model(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, obj_in: T) -> T:
        for field, value in obj_in.dict().items():
            setattr(obj_in, field, value)
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)
        return obj_in

    def delete(self, db: Session, id: int) -> None:
        obj = db.query(self.model).filter(self.model.id == id).first()
        if obj:
            db.delete(obj)
            db.commit()
