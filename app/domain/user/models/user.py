from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import BaseEntity
from app.domain.user.enums.login_type import LoginType
from app.domain.user.enums.role import Role


class User(BaseEntity):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=True)
    password = Column(String, nullable=True)
    nickname = Column(String(20), nullable=False)
    login_type = Column(Enum(LoginType), nullable=False)
    phone_number = Column(String(20), nullable=False)
    provider_id = Column(String, nullable=True)
    refresh_token = Column(String, nullable=True)
    role = Column(Enum(Role), nullable=False)

    # 1:1 관계 (User ↔ UserOnboarding)
    onboarding = relationship(
        "UserOnboarding",
        uselist=False,
        back_populates="user",
        cascade="all, delete-orphan",
    )

    # ---------- 비즈니스 로직 메서드 ----------
    def update_refresh_token(self, refresh_token: str):
        self.refresh_token = refresh_token

    def clear_refresh_token(self):
        self.refresh_token = None

    def update_password(self, password: str):
        self.password = password
