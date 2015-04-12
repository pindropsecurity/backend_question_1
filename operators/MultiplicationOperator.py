__author__ = 'andy'
from Operator import Operator


class MultiplicationOperator(Operator):

    def calculate(self, left, right):
        return left * right
