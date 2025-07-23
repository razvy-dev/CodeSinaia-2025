import unittest
from TODO_number_to_words import number_to_words

class TestInput(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(number_to_words(None))
    def test_type(self):
        self.assertRaises(TypeError, number_to_words, "string")
        self.assertRaises(TypeError, number_to_words, 3.14)
        self.assertRaises(TypeError, number_to_words, [1, 2, 3])
        self.assertRaises(TypeError, number_to_words, {1: "one"})

class TestUnderTen(unittest.TestCase):
    def test_under_ten(self):
        self.assertEqual(number_to_words(0), "zero")
        self.assertEqual(number_to_words(1), "one")
        self.assertEqual(number_to_words(2), "two")
        self.assertEqual(number_to_words(3), "three")
        self.assertEqual(number_to_words(4), "four")
        self.assertEqual(number_to_words(5), "five")
        self.assertEqual(number_to_words(6), "six")
        self.assertEqual(number_to_words(7), "seven")
        self.assertEqual(number_to_words(8), "eight")
        self.assertEqual(number_to_words(9), "nine")

class TestTenToTwenty(unittest.TestCase):
    def test_ten_to_twenty(self):
        self.assertEqual(number_to_words(10), "ten")
        self.assertEqual(number_to_words(11), "eleven")
        self.assertEqual(number_to_words(12), "twelve")
        self.assertEqual(number_to_words(13), "thirteen")
        self.assertEqual(number_to_words(14), "fourteen")
        self.assertEqual(number_to_words(15), "fifteen")
        self.assertEqual(number_to_words(16), "sixteen")
        self.assertEqual(number_to_words(17), "seventeen")
        self.assertEqual(number_to_words(18), "eighteen")
        self.assertEqual(number_to_words(19), "nineteen")

class TestTens(unittest.TestCase):
    def test_tens(self):
        self.assertEqual(number_to_words(20), "twenty")
        self.assertEqual(number_to_words(30), "thirty")
        self.assertEqual(number_to_words(40), "forty")
        self.assertEqual(number_to_words(50), "fifty")
        self.assertEqual(number_to_words(60), "sixty")
        self.assertEqual(number_to_words(70), "seventy")
        self.assertEqual(number_to_words(80), "eighty")
        self.assertEqual(number_to_words(90), "ninety")

class TestUpToUndred(unittest.TestCase):
    def test_up_to_hundred(self):
        self.assertEqual(number_to_words(21), "twenty one")
        self.assertEqual(number_to_words(22), "twenty two")
        self.assertEqual(number_to_words(35), "thirty five")
        self.assertEqual(number_to_words(99), "ninety nine")
        self.assertEqual(number_to_words(100), "one hundred")

