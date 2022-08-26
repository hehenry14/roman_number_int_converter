import typing
from enum import Enum


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


def decode_roman_number(s: str) -> int:
    if len(s) == 0:
        return 0

    s_enum = enumerate(s)
    _, num_str = next(s_enum)
    num = getattr(RomanNumber, num_str)
    result = num.value
    while True:
        try:
            _, next_num_str = next(s_enum)
            next_num = getattr(RomanNumber, next_num_str)
            if next_num.value > num.value:
                result -= num.value
                result += next_num.value - num.value
            else:
                result += next_num.value
            num = next_num
        except StopIteration:
            break

    return result


def _left_side_iter():
    candidates = [1, 10, 100]
    roman_list = _get_roman_list()
    for num in roman_list:
        if num.value in candidates:
            yield num


def encode_roman_number(num_int: int):
    left_iter = _left_side_iter()
    left_side = next(left_iter)
    result = ''
    roman_list = _get_roman_list()

    for num in roman_list:

        if left_side.value >= num.value:
            try:
                if left_side:
                    left_side = next(left_iter)
            except StopIteration:
                left_side = None

        while num.value <= num_int:
            num_int -= num.value
            result += num.name

        if left_side and num.value - left_side.value <= num_int:
            num_int -= num.value - left_side.value
            result += f'{left_side.name}{num.name}'

        if num_int == 0:
            break

    return result


if __name__ == '__main__':
    print(decode_roman_number('v'))
    print(decode_roman_number('iv'))
    print(decode_roman_number('CDXLIII'.lower()))
    print(decode_roman_number('MMXVIII'.lower()))
    print(encode_roman_number(9))
    print(encode_roman_number(11))
    print(encode_roman_number(100))
    print(encode_roman_number(4))
    print(encode_roman_number(2018))
