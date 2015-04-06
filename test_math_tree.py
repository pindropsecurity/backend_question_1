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

    def test_create_tree(self):
        """
                +
              /  \
             3   -
               /  \
              +    5
            /  \
           4  10

           answer: 12

        """
        root_node = OperatorNode("+")
        a_node = NumberNode(3)
        b_node = OperatorNode("-")
        c_node = OperatorNode("+")
        d_node = NumberNode(5)
        e_node = NumberNode(4)
        f_node = NumberNode(10)

        root_node.add_child(a_node)
        root_node.add_child(b_node)

        b_node.add_child(c_node)
        b_node.add_child(d_node)

        c_node.add_child(e_node)
        c_node.add_child(f_node)

        self.assertEquals(root_node.calculate(), 12)


if __name__ == '__main__':
    unittest.main()