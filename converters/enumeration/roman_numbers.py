from enum import Enum
import typing


class RomanNumber(Enum):
    i = 1
    v = 5
    x = 10
    l = 50
    c = 100
    d = 500
    m = 1000


def _get_roman_list() -> typing.List[RomanNumber]:
    return [
        RomanNumber.m,
        RomanNumber.d,
        RomanNumber.c,
        RomanNumber.l,
        RomanNumber.x,
        RomanNumber.v,
        RomanNumber.i,
    ]
