#!/usr/bin/python3
from fractions import Fraction
from expression_graph.operator import IntegralOperator, RationalOperator, \
    RealOperator

import unittest

class IntegralOperatorTest(unittest.TestCase):
    def testSimpleApplication(self):
        addop = IntegralOperator('+')
        self.assertEqual(4, addop.apply(2, 2))


        
class RationalOperatorTest(unittest.TestCase):
    def testSimpleApplication(self):
        addop = RationalOperator('+')
        self.assertEqual(1, addop.apply(Fraction(1, 2), Fraction(1, 2)))


        
class RealOperatorTest(unittest.TestCase):
    def testSimpleApplication(self):
        addop = RealOperator('+')
        self.assertEqual(4.0, addop.apply(2.0, 2.0))


        
if __name__ == '__main__':
    unittest.main()
