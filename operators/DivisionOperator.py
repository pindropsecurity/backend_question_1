__author__ = 'andy'
from Operator import Operator


class DivisionOperator(Operator):

    def __init__(self):
        self.data = []

    def calculate(self, left, right):
        if right == 0:
            return float('nan')
        else:
            return left / float(right)
