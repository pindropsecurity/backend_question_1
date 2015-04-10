__author__ = 'andy'
from operators import Operator
from TreeLeaf import TreeLeaf


class TreeNode(TreeLeaf):

    def __init__(self, operator, left, right):
        if not isinstance(left, TreeLeaf):
            raise ValueError("Left hand value must be a tree")

        if not isinstance(left, TreeLeaf):
            raise ValueError("Right hand value must be a tree")

        self.operator = operator
        self.left = left
        self.right = right

    def get_value(self):

        if self.left is None:
            raise ValueError("There is no left hand side to this operator ")
        else:
            left_value = self.left.get_value()

        if self.right is None:
            raise ValueError("There is no right hand side to this operator ")
        else:
            right_value = self.right.get_value()

        return self.operator.calculate(left_value, right_value)