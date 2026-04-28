from enum import Enum


class Regex(Enum):
    BRAND = (
        r'^[a-zA-Z]{2,20}$',
        'only alphanumeric and 2-20 char ',
    )
    NAME = (
        r'^[A-Z][a-zA-Z]{1,19}$',
        'only alphanumeric and 1-20 char first one is uppercase',
    )

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
