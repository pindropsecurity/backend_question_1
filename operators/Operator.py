__author__ = 'andy'


class Operator:

    def __init__(self):
        self.data = []

    def calculate(self, left, right):
        raise NotImplementedError()