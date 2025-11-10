from app.domain.user.repository.user_repository import UserRepository
from app.domain.user.repository.user_onboarding_repository import (
    UserOnboardingRepository,
)
from sqlalchemy.orm import Session
from app.domain.user.models.user import User


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.onboarding_repository = UserOnboardingRepository()

    def get_user(self, db: Session, user_id: int) -> User | None:
        return self.user_repository.get(db, user_id)

    def get_user_onboarding(self, db: Session, user_id: int):
        return self.onboarding_repository.find_by_user_id(db, user_id)
