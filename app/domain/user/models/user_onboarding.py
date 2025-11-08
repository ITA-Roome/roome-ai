from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import BaseEntity
from app.domain.user.enums.age_group import AgeGroup
from app.domain.user.enums.gender import Gender
from app.domain.user.enums.mood_type import MoodType
from app.domain.user.enums.space_type import SpaceType
from app.domain.user.enums.login_type import LoginType
from app.domain.user.enums.role import Role


class UserOnboarding(BaseEntity):
    __tablename__ = "user_onboarding"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    age_group = Column(Enum(AgeGroup), nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    mood_type = Column(Enum(MoodType), nullable=False)
    space_type = Column(Enum(SpaceType), nullable=False)

    user = relationship("User", back_populates="onboarding")

    # ---------- 업데이트 메서드 ----------
    def update(
        self,
        age_group: AgeGroup,
        gender: Gender,
        mood_type: MoodType,
        space_type: SpaceType,
    ):
        self.age_group = age_group
        self.gender = gender
        self.mood_type = mood_type
        self.space_type = space_type
