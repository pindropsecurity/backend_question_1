import unittest

from summit.node import SummitNode
from summit.exceptions import InvalidOperator, NotEnoughChildren, \
    RealNumberExpected

__author__ = 'Greg'


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
        Test to make sure that the proper exception for division by zero is
        thrown.
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

    def check_dynamic_equal(self, op, args):
        sm = SummitNode(op, args[0])
        self.assertEqual(sm.value, args[1],
                         'Evaluating : Op [%s] | values %s | expected [%d]'
                         % (op, str(args[0]), args[1]))

    def test_all_operators_good(self):
        """
        Test all operators available for simple a case.
        """
        op_map = {
            "+": ([1, 1], 2),
            "-": ([1, 1], 1),
            "*": ([2, 3], 6),
            "/": ([4, 2], 2)
        }

        for op, args in op_map.items():
            yield self.check_dynamic_equal(op, args)

    def test_float_division(self):
        """
        Test float division directly
        """
        sm = SummitNode('/', [4.5, 2])
        self.assertEqual(sm.value, 2.25)
        self.assertIsInstance(sm.value, float)

    def test_unreal_value(self):
        """
        Test to make sure that only real numbers are usable
        """

        with self.assertRaises(RealNumberExpected):
            # Throw a monkey wrench in the works (object)
            SummitNode('+', [1, object])

        with self.assertRaises(RealNumberExpected):
            # Make sure that strings don't work either
            SummitNode('+', [1, 'Wrench'])

    def test_more_complex_evaluation(self):
        """
        Test evaluation of a complex set that includes all operators
        """

        node1 = SummitNode('+', [1, 1])  # 2
        node2 = SummitNode('-', [10, 2])  # 8
        node3 = SummitNode('*', [2, 2, 2])  # 8
        node4 = SummitNode('/', [node2, node1])  # 4
        node5 = SummitNode('*', [node4, node3])  # 32

        self.assertEqual(node5.value, 32)
