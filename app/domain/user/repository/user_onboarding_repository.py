from app.domain.user.models.user_onboarding import UserOnboarding
from app.domain.user.models.user import User
from app.db.base_repository import BaseRepository


class UserOnboardingRepository(BaseRepository[UserOnboarding]):
    def __init__(self):
        super().__init__(UserOnboarding)

    def find_by_user_id(self, db, user_id: int) -> UserOnboarding | None:
        return (
            db.query(UserOnboarding).filter(UserOnboarding.user_id == user_id).first()
        )
