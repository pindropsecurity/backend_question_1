#!/usr/bin/python3

from .operator import Operator, IntegralOperator, RationalOperator, RealOperator
from .expression_node import ExpressionNode
from .value_node import ValueNode, IntegralValueNode, RationalValueNode, \
    RealValueNode


class InvalidOperatorException(Exception):
    pass

class InvalidValueException(Exception):
    pass

class OperatorNode(ExpressionNode):
    nodeTypes = [RealValueNode, RationalValueNode, IntegralValueNode]
    
    def __init__(self, operator, lnode, rnode):
        if not isinstance(operator, Operator):
            raise InvalidOperatorException('{0} is not a supported operator'.format(operator))
        elif not isinstance(lnode, ExpressionNode):
            raise InvalidValueException('{0} is not a valid node'.format(lnode))
        elif not isinstance(rnode, ExpressionNode):
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
        
        if lnode_type == RealValueNode:
            effective_operator = RealOperator(self.__operator.symbol())
            if rnode_type == RationalValueNode:
                effective_rvalue = rvalue.numerator() // rvalue.denominator()
            elif rnode_type == IntegralValueNode:
                effective_rvalue = float(rvalue)
            else:
                effective_rvalue = rvalue
        elif lnode_type == RationalValueNode:
            if rnode_type == RealValueNode:
                effective_operator = RealOperator(self.__operator.symbol())
                effective_lvalue = lvalue.numerator() // lvalue.denominator()
            else:
                effective_operator = RationalOperator(self._operator.symbol())
        else:
            if rnode_type == RealValueNode:
                effective_operator = RealOperator(self._operator.symbol())
                effective_lvalue = float(lvalue)
            elif rnode_type == RationalValueNode:
                effective_operator = RationalOperator(self._operator.symbol())
            else:
                effective_operator = IntegralOperator(self._operator.symbol())
        
        return effective_operator.apply(effective_lvalue, effective_rvalue)
        
