from sqlalchemy import Enum
from enum import Enum as PyEnum


class SpaceType(str, PyEnum):
    ROOM = "방"
    ONE_ROOM = "원룸"
    KITCHEN = "주방"
    BATHROOM = "화장실"
    BEDROOM = "침실"
    ENTRANCE = "현관"
