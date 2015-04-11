__author__ = 'andy'
from operators import Operator
from TreeLeaf import TreeLeaf


class TreeNode(TreeLeaf):

    def __init__(self, operator):
        if not isinstance(operator, Operator.Operator):
            raise ValueError("Initialized value is not an operator")
        self.operator = operator
        self.leafs = [];

    def add_leaf(self, leaf):
        if not isinstance(leaf, TreeLeaf):
            raise ValueError("The provided value is not a leaf")
        elif leaf is None:
            raise ValueError("Cannot accept a null leaf")

        self.leafs.append(leaf)

    def add_all_leafs(self, leaf_list):
        for leaf in leaf_list:
            self.add_leaf(leaf)

    def get_value(self):
        size = len(self.leafs)

        if size < 2:
            raise ValueError("Not enough values in list to perform calculation")

        result = None
        for i in range(size - 1):
            if i == 0:
                left_hand = self.leafs[0].get_value()
                right_hand = self.leafs[1].get_value()

                result = self.operator.calculate(left_hand, right_hand)
            else:
                right_hand = self.leafs[i + 1].get_value()

                result = self.operator.calculate(result, right_hand)

        return result