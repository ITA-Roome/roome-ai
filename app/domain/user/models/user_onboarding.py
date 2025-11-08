from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import BaseEntity
from enum import Enum
from app.domain.user.models.user import (
    AgeGroup,
    Gender,
    MoodType,
    SpaceType,
)


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
