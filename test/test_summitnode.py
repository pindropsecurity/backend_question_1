__author__ = 'Greg'

import unittest

from summit.node import SummitNode
from summit.exceptions import InvalidOperator, NotEnoughChildren


class TestSummitNode(unittest.TestCase):
    """
    Test the basic structure of an SummitNode
    """

    def test_interface(self):
        """
        Expect an SummitNode to have 2 args in addition to self.

        operator : one of [+,-,*,/]
        children : a list of two or more SummitNodes or Real Numbers

        SummitNode('+', [1,2,3])

        """

        with self.assertRaises(TypeError):
            SummitNode()

        with self.assertRaises(TypeError):
            SummitNode('foo')

        with self.assertRaises(InvalidOperator):
            SummitNode('foo', [])

        with self.assertRaises(NotEnoughChildren):
            SummitNode('+', [1])

    def test_basic_evaluation(self):
        """
        Test to make sure the most basic case will work.

        Given:
            operator = '+'
            children = [1,1]
            expect SummitNode.value = 2
        """

        sm = SummitNode('+', [1, 1])
        self.assertEqual(sm.value, 2)

    def test_div_by_zero(self):
        """
        Test to make sure that the proper exception for division by zero is thrown.
        """

        with self.assertRaises(ZeroDivisionError):
            SummitNode('/', [1, 0])

    def test_two_tier(self):
        """
        Test the expanded evaluation capability for nested SummitNodes.

        Given :

        node1 =
            operator = '+'
            children = [1, 2]
        node2 =
            operator = '+'
            children = [3, node1]

        expect node2.value = 6
        """

        node1 = SummitNode('+', [1, 2])
        node2 = SummitNode('+', [3, node1])

        self.assertEqual(node2.value, 6)