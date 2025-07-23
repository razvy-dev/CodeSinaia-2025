import unittest
from roman_converter import roman_converter_to_arab as roman_converter
from roman_converter import arab_to_roman_converter as arab_converter

class TestInvalidInput(unittest.TestCase):
    # ======== Step 1 ======== no input, return None
    def test_no_input(self):
        self.assertEqual(roman_converter(None), None)
        self.assertEqual(arab_converter(None), None)

    def test_num_str(self):
        self.assertEqual(roman_converter("123"), None)
        self.assertEqual(arab_converter("123"), None)

    def test_num_vir(self):
        self.assertEqual(roman_converter(12.34), None)
        self.assertEqual(arab_converter(12.34), None)
    
    def test_range_min(self):
        self.assertEqual(arab_converter(0), None)
        self.assertEqual(roman_converter("0"), None)
    
    def test_range_max(self):
        self.assertEqual(roman_converter("MMMM"), None)
        self.assertEqual(arab_converter(4000), None)   

class TestOnes(unittest.TestCase):
    # ======== Step 2 ======== ones
    def test_ones(self):
        self.assertEqual(roman_converter("I"), 1)
        self.assertEqual(roman_converter("V"), 5)
        self.assertEqual(roman_converter("X"), 10)
        self.assertEqual(roman_converter("L"), 50)
        self.assertEqual(roman_converter("C"), 100)
        self.assertEqual(roman_converter("D"), 500)
        self.assertEqual(roman_converter("M"), 1000)

    def test_two(self):
        self.assertEqual(roman_converter("II"), 2)
        self.assertEqual(roman_converter("XX"), 20)
        self.assertEqual(roman_converter("CC"), 200)
        self.assertEqual(roman_converter("MM"), 2000)
    
    def test_three(self):
        self.assertEqual(roman_converter("III"), 3)
        self.assertEqual(roman_converter("XXX"), 30)
        self.assertEqual(roman_converter("CCC"), 300)
        self.assertEqual(roman_converter("MMM"), 3000)

    def test_composed(self):
        # ======== Step 3 ======== composed numbers for roman to arab
        self.assertEqual(roman_converter("IV"), 4)
        self.assertEqual(roman_converter("IX"), 9)
        self.assertEqual(roman_converter("XL"), 40)
        self.assertEqual(roman_converter("XC"), 90)
        self.assertEqual(roman_converter("CD"), 400)
        self.assertEqual(roman_converter("CM"), 900)
        # ======== Step 4 ======== composed numbers for arab to roman

class TestComposedNumbers(unittest.TestCase):
    def test_composed_numbers(self):
        self.assertEqual(arab_converter(4), "IV")
        self.assertEqual(arab_converter(9), "IX")
        self.assertEqual(arab_converter(40), "XL")
        self.assertEqual(arab_converter(90), "XC")
        self.assertEqual(arab_converter(400), "CD")
        self.assertEqual(arab_converter(900), "CM")
