from sqlalchemy import Enum
from enum import Enum as PyEnum


class Gender(str, PyEnum):
    FEMALE = "여성"
    MALE = "남성"
    OTHER = "기타"
