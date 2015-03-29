#!/usr/bin/python3

from fractions import Fraction
from .operator import Operator, IntegralOperator, RationalOperator, \
    RealOperator, UnsupportedOperatorException
from .operator_node import OperatorNode, UnsupportedNodeTypeException, \
    InvalidOperatorException, InvalidValueException
from .expression_node import ExpressionNode
from .value_node import ValueNode, IntegralValueNode, RationalValueNode, \
    RealValueNode, NodeValueTypeException

class InvalidGraphException(Exception):
    pass

class EmptyExpressionException(Exception):
    pass

class IncompleteExpressionException(Exception):
    pass

class ExpressionGraph(object):
    """ Class to represent an evaluable arithmetic expression as a graph.""" 
    def __init__(self, graph):
        if not isinstance(graph, ExpressionNode) and not isinstance(graph, ExpressionGraph):
            raise InvalidGraphException()
        else:
            self._graph = graph

    def depth(self):
        if isinstance(self._graph, ExpressionNode):
            return self._graph.depth()
        else:
            return self._graph._node.depth()
        
    def __str__(self):
        if isinstance(self._graph, ExpressionNode):
            return str(self._graph)
        else:
            return str(self._graph._node)


class LeftmostEvaluatingExpressionGraph(ExpressionGraph):
    """ Class to represent an evaluable arithmetic expression as a graph."""    
    def __init__(self, *elements, **kwargs):
        head = None
        if 'head' in kwargs.keys():
            head = kwargs['head']
        
        if elements is None or (head is None and len(elements) == 0):
            raise EmptyExpressionException()
        
        self._node = None
        self._graph = None
        lnode = None
        opnode = None
        rnode = None
        next_element = IterableIndex(elements, IncompleteExpressionException)

        # In order to get the desired order of operations, we need
        # to built the graph bottom up, with a left skew - that is,
        # the left-most elements must be built first, then the
        # elements to the right are built in such a way that the final
        # graph goes down (possibly) multiple levels to the left,
        # but only one level to the right.
        
        if head is None:
            lvalue = elements[next_element.value()]
            lnode = assignValueNodeType(lvalue)
            try:
                next_element.iterate()
            except IncompleteExpressionException as e:
                # in this instance, it means that there is only a
                # single element in the expression, which is the value
                # of the expression
                self._node = lnode
                self._graph = self
                return
                
            lnode = assignValueNodeType(lvalue)
            
        # head is not empty       
        else:
            lnode = head

        opvalue = elements[next_element.value()]
        next_element.iterate()

        rvalue = elements[next_element.value()]
        rnode = assignValueNodeType(rvalue)

        self._node = OperatorNode(Operator(opvalue), lnode, rnode)
        
        try:
            next_element.iterate()
            remainder_start = next_element.value()
            remaining_elements = elements[remainder_start:]
            super().__init__(LeftmostEvaluatingExpressionGraph(*remaining_elements, head=self._node))
        except IncompleteExpressionException as e:
            super().__init__(self._node)


    def eval(self):
        """ Evaluate the graph. This works because only the rightmost node of 
            the graph is actually exposed as the handle of the graph,
            so all nodes are guaranteed to be evaluated in the correct order."""
        print(self)
        if isinstance(self._graph, ExpressionNode):
            return self._graph.eval()
        else:
            return self._graph._node.eval()
        
def assignValueNodeType(value):
    """ Utility function to map a value to its correct ValueNode type. """
    val_type = type(value)
    if val_type not in [int, Fraction, float]:
        raise NodeValueTypeException('{0} is not a valid value for a node'.format(value))
    else:
        if val_type == int:
            return IntegralValueNode(value)
        elif val_type == Fraction:
            return RationalValueNode(value)
        else:
            return RealValueNode(value)

        
class IterableIndex(object):
    """utility class for an index that automatically checks whether
       it has overrun the end of the list it is bound to, and throws the 
       correct exception when it does."""

    def __init__(self, iterated_list, raised_exception):
        self._index = 0
        self._iterated_list = iterated_list
        self._raised_exception = raised_exception

    def value(self):
        return self._index

    def iterate(self):
        self._index += 1
        if self._index >= len(self._iterated_list):
            raise self._raised_exception()
    
        
    
