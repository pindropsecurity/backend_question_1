#!/usr/bin/python

from math_tree import *

import unittest


class TreeGraph(unittest.TestCase):
    def test_create_node(self):
        node = Node("test")
        self.assertEquals(node.val, "test")

    def test_create_node_exception(self):
        self.assertRaises(InvalidNode, Node, "")

    def test_create_operator_node(self):
        node = OperatorNode("+")
        self.assertEquals("+", node.val)

    def test_create_op_node_exception(self):
        self.assertRaises(InvalidOperator, OperatorNode, "a")

    def test_create_number_node(self):
        node = NumberNode(2)
        self.assertEquals(node.val, 2)

    def test_create_number_node_exception(self):
        self.assertRaises(InvalidNumber, NumberNode, "a")


if __name__ == '__main__':
    unittest.main()