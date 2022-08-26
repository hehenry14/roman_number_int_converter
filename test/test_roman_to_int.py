from unittest import TestCase

from converters import convert_roman_to_int


class TestRomanToInt(TestCase):

    def test_1(self):
        result = convert_roman_to_int('ix')
        self.assertEqual(result, 9)

    def test_2(self):
        result = convert_roman_to_int('iv')
        self.assertEqual(result, 4)

    def test_3(self):
        result = convert_roman_to_int('mmxviii')
        self.assertEqual(result, 2018)

    def test_4(self):
        result = convert_roman_to_int('XI')
        self.assertEqual(result, 11)
