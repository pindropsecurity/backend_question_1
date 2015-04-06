#!/usr/bin/python

from math_tree import Node, NumberNode, OperatorNode

import unittest


class TreeGraph(unittest.TestCase):
    def test_create_node(self):
        node = Node("test")
        self.assertEquals(node.val, "test")

    def test_create_operator_node(self):
        node = OperatorNode("+")
        self.assertEquals("+", node.val)

    def test_create_number_node(self):
        node = NumberNode(2)
        self.assertEquals(node.val, 2)


