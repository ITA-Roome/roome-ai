from sqlalchemy import Enum
from enum import Enum as PyEnum


class LoginType(str, PyEnum):
    EMAIL = "EMAIL"
    GOOGLE = "GOOGLE"
    KAKAO = "KAKAO"
