#!/usr/bin/python3

from fractions import Fraction
from ..expression_graph import ExpressionGraph, \
    LeftmostEvaluatingExpressionGraph, EmptyExpressionException, \
    IncompleteExpressionException

from unittest import TestCase

class ExpressionGraphTest(TestCase):
    def testEmptyExpression(self):
        self.assertRaises(EmptyExpressionException, LeftmostEvaluatingExpressionGraph)
    
    def testSingleValueExpression(self):
        graph = LeftmostEvaluatingExpressionGraph(2)
        self.assertEqual('2', str(graph))
        self.assertEqual(2, graph.eval())

    def testSimpleExpression(self):
        graph = LeftmostEvaluatingExpressionGraph(2, '+', 2)
        self.assertEqual('2 + 2', str(graph))
        self.assertEqual(4, graph.eval())

    def testCompoundExpression(self):
        graph = LeftmostEvaluatingExpressionGraph(2, '+', 2, '-', 6)
        self.assertEqual('2 + 2 - 6', str(graph))
        self.assertEqual(-2, graph.eval())

    def testDivisionExpression(self):
        graph = LeftmostEvaluatingExpressionGraph(4, '/', 2)
        self.assertEqual('4 / 2', str(graph))
        self.assertEqual(Fraction(4, 2), graph.eval())

    def testFourValueExpression(self):
        graph = LeftmostEvaluatingExpressionGraph(2, '+', 2, '-', 6, '*', 4)
        self.assertEqual('2 + 2 - 6 * 4', str(graph))
        self.assertEqual(-8, graph.eval())
        
    def testExtendedExpression(self):
        graph = LeftmostEvaluatingExpressionGraph(2, '+', 2, '-', 6, '*', 4, '/', 2)
        self.assertEqual('2 + 2 - 6 * 4 / 2', str(graph))
        self.assertEqual(-4, graph.eval())

    def testCaptureIncompleteExpression(self):
        self.assertRaises(IncompleteExpressionException, LeftmostEvaluatingExpressionGraph, 2, '+', 2, '-', 6, '*', 4, '/')


    def testExtendedWithFractionalResultExpression(self):
        graph = LeftmostEvaluatingExpressionGraph(2, '+', 2, '-', 6, '*', 4, '/', 13)
        self.assertEqual('2 + 2 - 6 * 4 / 13', str(graph))
        self.assertEqual(Fraction(-8, 13), graph.eval())


    def testExtendedWithRealResultExpression(self):
        graph = LeftmostEvaluatingExpressionGraph(2, '+', 2.5, '-', 6, '*', 4, '/', 13)
        self.assertEqual('2 + 2.5 - 6 * 4 / 13', str(graph))
        result = ((2 + 2.5 - 6) * 4) / 13
        self.assertEqual(result, graph.eval())



if __name__ == '__main__':
    unittest.main()
