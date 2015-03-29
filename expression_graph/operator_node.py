#!/usr/bin/python3

from fractions import Fraction
from .operator import Operator, IntegralOperator, RationalOperator, RealOperator
from .expression_node import ExpressionNode
from .value_node import ValueNode, IntegralValueNode, RationalValueNode, \
    RealValueNode

class UnsupportedNodeTypeException(Exception):
    pass

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
            print(type(lnode))
            raise InvalidValueException('{0} is not a valid node'.format(lnode))
        elif not isinstance(rnode, ExpressionNode):
            raise InvalidValueException('{0} is not a valid node'.format(rnode))
        else:
            super().__init__(operator)
            self._lnode = lnode
            self._rnode = rnode

    def eval(self):
        opsym = str(self._node)
        lvalue = self._lnode.eval()
        rvalue = self._rnode.eval()
        lvalue_type = type(lvalue)
        rvalue_type = type(rvalue)

        effective_operator = self._node
        effective_lvalue = lvalue
        effective_rvalue = rvalue

        # this part is a bit concerning to me, as it scales poorly and is
        # quite brittle. I'll try to find a more elegant solution later.
        
        if lvalue_type == float:
            effective_operator = RealOperator(opsym)
            if rvalue_type == Fraction:
                effective_rvalue = rvalue.numerator() // rvalue.denominator()
            elif rvalue_type == int:
                effective_rvalue = float(rvalue)
            elif rvalue_type == float:
                pass
            else:
                raise UnsupportedNodeTypeException('{0} is not a supported node type'.format(lvalue_type))
            
        elif lvalue_type == Fraction:
            if rvalue_type == float:
                effective_operator = RealOperator(opsym)
                effective_lvalue = lvalue.numerator() // lvalue.denominator()
            elif rvalue_type in [int, Fraction]:
                effective_operator = RationalOperator(opsym)
            else:
                raise UnsupportedNodeTypeException('{0} is not a supported node type'.format(lvalue_type))
            
        elif lvalue_type == int:
            if rvalue_type == float:
                effective_operator = RealOperator(opsym)
                effective_lvalue = float(lvalue)
            elif rvalue_type == Fraction:
                effective_operator = RationalOperator(opsym)
            elif rvalue_type == int:
                effective_operator = IntegralOperator(opsym)
            else:
                raise UnsupportedNodeTypeException('{0} is not a supported node type'.format(rvalue_type))                
        else:
            raise UnsupportedNodeTypeException('{0} is not a supported node type'.format(lvalue_type))
                
        return effective_operator.apply(effective_lvalue, effective_rvalue)

    
    def __str__(self):
        s = str(self._lnode) + ' ' + str(self._node) + ' ' + str(self._rnode)
        return s
        
    def depth(self):
        return 1 + max(self._lnode.depth(), self._rnode.depth())
