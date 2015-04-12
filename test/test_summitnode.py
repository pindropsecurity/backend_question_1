__author__ = 'Greg'

import unittest

from summit.node import SummitNode
from summit.exceptions import InvalidOperator


class TestSummitNodeStructure(unittest.TestCase):
    """
    Test the basic structure of an OpNode
    """

    def test_interface(self):
        """
        Expect an OpNode to have 2 args in addition to self.

        operator : one of [+,-,*,/]
        children : a list of two or more SummitNodes or Real Numbers

        SummitNode('+', [1,2,3])

        """

        with self.assertRaises(TypeError):
            SummitNode()  # noqa

        with self.assertRaises(TypeError):
            SummitNode('foo')  # noqa

        with self.assertRaises(InvalidOperator):
            SummitNode('foo', [])