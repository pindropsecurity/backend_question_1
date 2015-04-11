__author__ = 'andy'
import unittest
from operators import AdditionOperator
from operators import DivisionOperator
from operators import SubtractionOperator
from tree import TreeNode
from tree import TreeLeaf

class TestTreeMath(unittest.TestCase):


    def test_one_plus_one(self):
        operand = AdditionOperator.AdditionOperator()
        left_hand = TreeLeaf.TreeLeaf(1)
        right_hand = TreeLeaf.TreeLeaf(1)

        tree = TreeNode.TreeNode(operand)
        tree.add_leaf(left_hand)
        tree.add_leaf(right_hand)

        self.assertEquals(2, tree.get_value())

    #test 1 + 1/2 = 1.5
    def test_one_plus_one_half(self):
        operand_addition = AdditionOperator.AdditionOperator()
        operand_division = DivisionOperator.DivisionOperator()

        one = TreeLeaf.TreeLeaf(1)
        two = TreeLeaf.TreeLeaf(2)

        division_tree = TreeNode.TreeNode(operand_division);
        division_tree.add_leaf(one)
        division_tree.add_leaf(two)

        addition_tree = TreeNode.TreeNode(operand_addition)
        addition_tree.add_leaf(one)
        addition_tree.add_leaf(division_tree)

        self.assertAlmostEqual(1.5, addition_tree.get_value())

    #test 1-2-3=-4
    def test_stated_example(self):
        subtraction = SubtractionOperator.SubtractionOperator()

        one = TreeLeaf.TreeLeaf(1)
        two = TreeLeaf.TreeLeaf(2)
        three = TreeLeaf.TreeLeaf(3)

        one_minus_two_minus_three = TreeNode.TreeNode(subtraction)
        one_minus_two_minus_three.add_leaf(one)
        one_minus_two_minus_three.add_leaf(two)
        one_minus_two_minus_three.add_leaf(three)

        output = one_minus_two_minus_three.get_value()
        self.assertEqual(-4, output)

