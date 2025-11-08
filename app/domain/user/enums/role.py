from sqlalchemy import Enum
from enum import Enum as PyEnum


class Role(str, PyEnum):
    USER = "일반 사용자"
    ADMIN = "관리자"
