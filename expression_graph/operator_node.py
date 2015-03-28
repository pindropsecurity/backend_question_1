#!/usr/bin/python3

from .operator import Operator
from .expression_node import ExpressionNode
from .value_node import ValueNode, IntegralNode, RationalNode, RealNode


class InvalidOperatorException(Exception):
    pass

class InvalidValueException(Exception):
    pass

class OperatorNode(ExpressionNode):
    nodeTypes = [RealNode, RationalNode, IntegralNode]
    
    def __init__(self, operator, lnode, rnode):
        if not isinstance(Operator, operator):
            raise InvalidOperatorException('{0} is not a supported operator'.format(operator))
        elif not isinstance(ExpressionNode, lval):
            raise InvalidValueException('{0} is not a valid node'.format(lnode))
        elif not isinstance(ExpressionNode, rval):
            raise InvalidValueException('{0} is not a valid node'.format(rnode))
        else:
            self._operator = operator
            self._lnode = lnode
            self._rnode = rnode

    def eval(self):
        lvalue = self._lnode.eval()
        rvalue = self._rnode.eval()
        lnode_type = type(self._lnode)
        rnode_type = type(self._rnode)

        effective_operator = self._operator
        effective_lvalue = lvalue
        effective_rvalue = rvalue

        # this part is a bit concerning to me, as it scales poorly
        # and is quite brittle. I'll try to find a more elegant solution later.
        
        if lnode_type == RealNode:
            effective_operator = RealOperator(self.__operator.symbol())
            if rnode_type == RationalNode:
                effective_rvalue = rvalue.numerator() // rvalue.denominator()
            elif rnode_type == IntegralNode:
                effective_rvalue = float(rvalue)
            else:
                effective_rvalue = rvalue
        elif lnode_type == RationalNode:
            if rnode_type == RealNode:
                effective_operator = RealOperator(self.__operator.symbol())
                effective_lvalue = lvalue.numerator() // lvalue.denominator()
            else:
                effective_operator = RationalOperator(self.__operator.symbol())
        else:
            if rnode_type == RealNode:
                effective_operator = RealOperator(self.__operator.symbol())
                effective_lvalue = float(lvalue)
            elif rnode_type == RationalNode:
                effective_operator = RationalOperator(self.__operator.symbol())
            else:
                effective_operator = IntegralOperator(self.__operator.symbol())
        
        return effective_operator.apply(effective_lvalue, effective_rvalue)
        
