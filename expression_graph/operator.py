#!/usr/bin/python3

from fractions import Fraction

class UnsupportedOperatorException(Exception):
    pass

class Operator(str):
    # class constants representing the possible values of an Operator
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'

    operators = [ADD, SUBTRACT, MULTIPLY, DIVIDE]
    
    def __init__(self, operator):
        if operator not in Operator.operators:
            raise UnsupportedOperatorException('{0} is not a supported operator.'
                                               .format(operator))
        else:
            self._operator = operator

    def apply(self, operand, operahend):
        return self.operation.get(self._operator)(operand, operahend)
        
    def symbol(self):
        return self._operator


    
class IntegralOperator(Operator):
    operation = {Operator.ADD: int.__add__,
                 Operator.SUBTRACT: int.__sub__,
                 Operator.MULTIPLY: int.__mul__,
                 Operator.DIVIDE: Fraction}

    def __init__(self, operator):
        super().__init__(operator)


        
class RationalOperator(Operator):
    operation = {Operator.ADD: Fraction.__add__,
                 Operator.SUBTRACT: Fraction.__sub__,
                 Operator.MULTIPLY: Fraction.__mul__,
                 Operator.DIVIDE: Fraction.__truediv__}

    def __init__(self, operator):
        super().__init__(operator)


        
class RealOperator(Operator):
    operation = {Operator.ADD: float.__add__,
                 Operator.SUBTRACT: float.__sub__,
                 Operator.MULTIPLY: float.__mul__,
                 Operator.DIVIDE: float.__truediv__}
    
    def __init__(self, operator):
        super().__init__(operator)
