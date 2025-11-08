from enum import Enum


class TagType(str, Enum):
    COLOR = "COLOR"
    MATERIAL = "MATERIAL"
    FEATURE = "FEATURE"
    PRODUCT_TYPE = "PRODUCT_TYPE"
    SIZE = "SIZE"
    USAGE = "USAGE"
    STYLE = "STYLE"
    MOOD = "MOOD"
