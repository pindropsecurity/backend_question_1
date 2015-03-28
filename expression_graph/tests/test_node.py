#!/usr/bin/python3

from fractions import Fraction
from expression_graph.expression_node import ExpressionNode
from expression_graph.operator_node import OperatorNode
from expression_graph.value_node import ValueNode, IntegralValueNode, \
    RationalValueNode, RealValueNode
from expression_graph.operator import Operator

import unittest

class OperatorNodeTest(unittest.TestCase):
    def testSimpleOperatorEvaluation(self):
        lnode = IntegralValueNode(2)
        rnode = IntegralValueNode(2)
        opnode = OperatorNode(Operator('+'), lnode, rnode)
        self.assertEqual(4, opnode.eval())

class IntegralNodeTest(unittest.TestCase):
    def testSimpleNodeEvaluation(self):
        node = IntegralValueNode(2)
        self.assertEqual(2, node.eval())

if __name__ == '__main__':
    unittest.main()
