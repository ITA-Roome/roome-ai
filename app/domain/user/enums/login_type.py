from enum import Enum


class LoginType(str, Enum):
    EMAIL = "EMAIL"
    GOOGLE = "GOOGLE"
    KAKAO = "KAKAO"
