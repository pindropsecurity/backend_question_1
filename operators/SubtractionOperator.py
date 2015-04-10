__author__ = 'andy'
from Operator import Operator


class SubtractionOperator(Operator):

    def __init__(self):
        self.data = []

    def calculate(self, left, right):
        return left - right
