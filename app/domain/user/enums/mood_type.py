from sqlalchemy import Enum
from enum import Enum as PyEnum


class MoodType(str, PyEnum):
    COZY = "아늑한"
    SIMPLE = "단순한"
    SNUG = "포근한"
    NEAT = "깔끔한"
    CHIC = "세련된"
    CUTE = "귀여운"
