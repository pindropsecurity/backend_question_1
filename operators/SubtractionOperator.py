__author__ = 'andy'
from Operator import Operator


class SubtractionOperator(Operator):

    def calculate(self, left, right):
        return left - right
