from sqlalchemy import Enum
from enum import Enum as PyEnum


class TagType(str, PyEnum):
    COLOR = "COLOR"
    MATERIAL = "MATERIAL"
    FEATURE = "FEATURE"
    PRODUCT_TYPE = "PRODUCT_TYPE"
    SIZE = "SIZE"
    USAGE = "USAGE"
    STYLE = "STYLE"
    MOOD = "MOOD"
