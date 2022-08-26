from converters.enumeration.roman_numbers import RomanNumber


def convert_roman_to_int(s: str) -> int:
    if len(s) == 0:
        return 0

    s_enum = enumerate(s.lower())
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
