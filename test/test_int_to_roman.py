from converters import convert_int_to_roman
from unittest import TestCase


class TestIntToRoman(TestCase):

    def test1(self):
        result = convert_int_to_roman(9)
        self.assertEqual(result, 'ix')

    def test2(self):
        result = convert_int_to_roman(4)
        self.assertEqual(result, 'iv')

    def test3(self):
        result = convert_int_to_roman(2018)
        self.assertEqual(result, 'mmxviii')

    def test4(self):
        with self.assertRaises(ValueError):
            result = convert_int_to_roman(0)

    def test5(self):
        with self.assertRaises(ValueError):
            convert_int_to_roman(-1)

    def test6(self):
        with self.assertRaises(ValueError):
            convert_int_to_roman(10000)
