__author__ = 'andy'
from Operator import Operator


class DivisionOperator(Operator):

    def calculate(self, left, right):
        if right == 0:
            return float('nan')
        elif isinstance(right, int):
            return left / float(right)
        else:
            return left/right
