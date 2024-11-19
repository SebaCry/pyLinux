import unittest
from src.calculator import sum, sustract, multiply, division

class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        assert sum(2,3) == 5

    def test_sustract(self):
        assert sustract(10, 5) == 5

    def test_multiply(self):
        assert multiply(10, 34) == 340

    def test_division(self):
        result = division(10,2)
        expected = 5
        assert result == expected
