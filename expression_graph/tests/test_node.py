#!/usr/bin/python3

from fractions import Fraction
from expression_graph.expression_node import ExpressionNode
from expression_graph.operator_node import OperatorNode, IntegralOperatorNode, \
    RationalOperatorNode, RealOperatorNode
from expression_graph.value_node import ValueNode, IntegralValueNode, \
    RationalValueNode, RealValueNode

import unittest

class OperatorNodeTest(unittest.TestCase):
    def testSimpleOperatorEvaluation(self):
        lnode = IntegralNode(2)
        rnode = IntegralNode(2)
        opnode = OperatorNode(Operator('+'), lnode, rnode)
        self.assertEqual(4, opnode.eval())

class IntegralNodeTest(unittest.TestCase):
    def testSimpleNodeEvaluation(self):
        node = IntegralNode(2)
        self.assertEqual(2, node.eval())

if __name__ == '__main__':
    unittest.main()
