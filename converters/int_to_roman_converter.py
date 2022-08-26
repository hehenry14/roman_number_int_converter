from converters.enumeration.roman_numbers import _get_roman_list


def _left_side_iter():
    candidates = [1, 10, 100]
    roman_list = _get_roman_list()
    for num in roman_list:
        if num.value in candidates:
            yield num


def convert_int_to_roman(num_int: int):
    if num_int <= 0 or num_int >= 10000:
        raise ValueError(f'number {num_int} is out of range.')

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
