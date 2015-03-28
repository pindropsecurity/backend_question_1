#!/usr/bin/python3

from .expression_node import ExpressionNode

class NodeValueTypeException(Exception):
    pass


class ValueNode(ExpressionNode):
    def __init__(self, value):
        self._value = value

    def eval(self):
        return self._value

    
class IntegralValueNode(ValueNode):
    def __init__(self, value):
        if type(value) is not int:
            raise NodeValueTypeException("{0} is not an integer".format(value))
        else:
            super().__init__(value)

class RationalValueNode(ValueNode):
    def __init__(self, value):
        if type(value) is not Fraction:
            raise NodeValueTypeException("{0} is not a fraction".format(value))
        else:
            super().__init__(value)

class RealValueNode(ValueNode):
    def __init__(self, value):
        if type(value) is not float:
            raise NodeValueTypeException("{0} is not a float".format(value))
        else:
            super().__init__(value)
