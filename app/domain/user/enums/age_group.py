from sqlalchemy import Enum
from enum import Enum as PyEnum


class AgeGroup(str, PyEnum):
    TEENAGER = "10대"
    TWENTIES = "20대"
    THIRTIES = "30대"
    FORTIES = "40대"
    FIFTIES = "50대"
    SIXTIES = "60대"
