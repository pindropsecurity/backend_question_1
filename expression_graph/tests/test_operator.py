#!/usr/bin/python3

from fractions import Fraction
from expression_graph.operator import Operator, IntegralOperator, \
    RationalOperator, RealOperator, UnsupportedOperatorException

import unittest

class IntegralOperatorTest(unittest.TestCase):
    def testSimpleApplication(self):
        addop = IntegralOperator('+')
        self.assertEqual(4, addop.apply(2, 2))

    def testUnsupportedOperator(self):
        self.assertRaises(UnsupportedOperatorException,
                          IntegralOperator, '**')

    def testDivisionPromoteToFraction(self):
        divop = IntegralOperator('/')
        quotient = divop.apply(4, 6)
        self.assertEqual(type(quotient), Fraction)
        self.assertEqual(Fraction(2, 3), quotient)

        
class RationalOperatorTest(unittest.TestCase):
    def testSimpleApplication(self):
        addop = RationalOperator('+')
        self.assertEqual(1, addop.apply(Fraction(1, 2), Fraction(1, 2)))
        
    def testUnsupportedOperator(self):
        self.assertRaises(UnsupportedOperatorException,
                          RationalOperator, '**')

        
        
class RealOperatorTest(unittest.TestCase):
    def testSimpleApplication(self):
        addop = RealOperator('+')
        self.assertEqual(4.0, addop.apply(2.0, 2.0))
        
    def testUnsupportedOperator(self):
        self.assertRaises(UnsupportedOperatorException,
                          RealOperator, '**')

        
if __name__ == '__main__':
    unittest.main()
