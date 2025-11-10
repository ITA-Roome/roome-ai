from enum import Enum


class SpaceType(str, Enum):
    ROOM = "ROOM"
    ONE_ROOM = "ONE_ROOM"
    KITCHEN = "KITCHEN"
    BATHROOM = "BATHROOM"
    BEDROOM = "BEDROOM"
    ENTRANCE = "ENTRANCE"
