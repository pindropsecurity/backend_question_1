__author__ = 'andy'

import unittest
import math
from operators import DivisionOperator


class TestDivision(unittest.TestCase):

    def test_divide_by_zero(self):
        operator = DivisionOperator.DivisionOperator()

        output = operator.calculate(1, 0)

        self.assertTrue(math.isnan(output))

    def test_divide_complex(self):
        operator = DivisionOperator.DivisionOperator()

        left = complex(8, 1)
        right = complex(2, -1)

        output = operator.calculate(left, right)

        self.assertEqual(3, output.real)
        self.assertEqual(2, output.imag)

    def test_divide_real_by_complex(self):
        operator = DivisionOperator.DivisionOperator()

        left = 1
        right = complex(1, 1)

        output = operator.calculate(left, right)

        self.assertAlmostEqual(0.5, output.real)
        self.assertAlmostEqual(-0.5, output.imag)