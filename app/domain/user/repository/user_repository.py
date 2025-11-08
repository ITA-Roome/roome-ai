from app.db.base_repository import BaseRepository
from app.domain.user.models.user import User
from sqlalchemy.orm import Session
from typing import Optional


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User)

    def find_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def find_by_nickname(self, db: Session, nickname: str) -> Optional[User]:
        return db.query(User).filter(User.nickname == nickname).first()

    def find_by_phone(self, db: Session, phone_number: str) -> Optional[User]:
        return db.query(User).filter(User.phone_number == phone_number).first()
