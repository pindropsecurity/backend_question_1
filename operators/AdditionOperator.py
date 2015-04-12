__author__ = 'andy'
from Operator import Operator


class AdditionOperator(Operator):

    def calculate(self, left, right):
        return left + right