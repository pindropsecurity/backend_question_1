__author__ = 'andy'
import unittest
import math
from operators import AdditionOperator


class TestAddition(unittest.TestCase):

    def test_one_plus_one(self):
        operator = AdditionOperator.AdditionOperator()
        output = operator.calculate(1,1)

        self.assertEqual(2, output)

    def test_one_plus_negative(self):
        operator = AdditionOperator.AdditionOperator()
        output = operator.calculate(1,-2)

        self.assertEqual(-1, output)

    def test_adding_complex_number(self):
        operator = AdditionOperator.AdditionOperator()
        left = complex(1, 1)
        right = complex(1, 1)

        output = operator.calculate(left, right)
        self.assertEqual(2, output.real)
        self.assertEqual(2, output.imag)

    def test_adding_complex_number(self):
        operator = AdditionOperator.AdditionOperator()
        left = 1
        right = complex(1, 1)

        output = operator.calculate(left, right)
        self.assertEqual(2, output.real)
        self.assertEqual(1, output.imag)

    def test_nan_addition(self):
        operator = AdditionOperator.AdditionOperator()
        left = 1
        right = float("nan")

        output = operator.calculate(left, right)
        self.assertTrue(math.isnan(output))