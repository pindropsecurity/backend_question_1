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

    def test_calculate_tree1(self):
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

        self.assertEquals(float(root_node.calculate()), float(12))

    def test_calculate_tree2(self):
        """
                +
              /  \
             3   -       3 + 10 = 13
               /  \
              +    5     15 - 5 = 10
            /  \
           -  10         5 + 10 = 15
         /  \
        9    +           9 - 4 = 5
           /  \
         -     6         -2 + 6 = 4
        / \
       2  4              2 - 4 = -2

        """
        root_node = OperatorNode("+")
        a = NumberNode(3)
        b = OperatorNode("-")
        c = OperatorNode("+")
        d = NumberNode(5)
        e = OperatorNode("-")
        f = NumberNode(10)
        g = NumberNode(9)
        h = OperatorNode("+")
        i = OperatorNode("-")
        j = NumberNode(6)
        k = NumberNode(2)
        l = NumberNode(4)

        root_node.add_child(a)
        root_node.add_child(b)

        b.add_child(c)
        b.add_child(d)

        c.add_child(e)
        c.add_child(f)

        e.add_child(g)
        e.add_child(h)

        h.add_child(i)
        h.add_child(j)

        i.add_child(k)
        i.add_child(l)

        self.assertEquals(float(root_node.calculate()), float(13))

    def test_calculate_tree3(self):
        """
                -
              /  \
             3   *       3 - 150 = -147
               /  \
              *    5     30 * 5 = 150
            /  \
         (div)  10       3 * 10 = 30
         /  \
        9    3           9 / 3 = 3

        """
        root_node = OperatorNode("-")
        a = NumberNode(3)
        b = OperatorNode("*")
        c = OperatorNode("*")
        d = NumberNode(5)
        e = OperatorNode("/")
        f = NumberNode(10)
        g = NumberNode(9)
        h = NumberNode(3)

        root_node.add_child(a)
        root_node.add_child(b)

        b.add_child(c)
        b.add_child(d)

        c.add_child(e)
        c.add_child(f)

        e.add_child(g)
        e.add_child(h)

        self.assertEquals(float(root_node.calculate()), float(-147))

    def test_calculate_tree4(self):
        """
              (div)
              /  \
             3   *       3 / 150 = -147
               /  \
              *    5     30 * 5 = 150
            /  \
         (div)  10       3 * 10 = 30
         /  \
        9    3           9 / 3 = 3

        """
        root_node = OperatorNode("/")
        a = NumberNode(3)
        b = OperatorNode("*")
        c = OperatorNode("*")
        d = NumberNode(5)
        e = OperatorNode("/")
        f = NumberNode(10)
        g = NumberNode(9)
        h = NumberNode(3)

        root_node.add_child(a)
        root_node.add_child(b)

        b.add_child(c)
        b.add_child(d)

        c.add_child(e)
        c.add_child(f)

        e.add_child(g)
        e.add_child(h)

        self.assertEquals(float(root_node.calculate()), 0.02)

    def test_create_tree_from_dict(self):
        #        +
        #       / \
        #      2   -                           2 + -40 = -38
        #         /  \
        #        4    +                     4 - 44 = -40
        #            /  \
        #           -     *                -1 + 45 = 44
        #          / \   / \
        #         7   8 9   5          7 - 8 = -1   9 * 5 = 45

        tree_dict = {"+": [2, {"-": [4, {"+": [{"-": [7, 8]}, {"*": [9, 5]}]}]}]}
        tree = Tree(tree_dict)
        self.assertEquals(float(tree.calculate()), float(-38))

if __name__ == '__main__':
    unittest.main()