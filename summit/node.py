__author__ = 'Greg'
from summit.exceptions import InvalidOperator


class SummitNode(object):
    """
    A SummitNode represents a mathematical operator and children "nodes" that are, at minimum, a pair of real numbers
     in which the operator is applied to. A more complex tree is possible by, instead of providing terminated leafs of
      real numbers, you may insert another SummitNode as one, or all children.

    Operations allowed:
        '+' : Perform Addition of all children
        '-' : Perform Subtraction across all children
        '/' : Perform Division across all children
        '*' : Perform Multiplication across all children

    Limitations:
        * There must be a minimum of 2 children per SummitNode instance, fewer means there is nothing to do, silly.
        * All children must terminate as Real Numbers.
        * You may only perform the operators in the list above (see: Operations allowed)
        * Division by 0 (Zero) is / will always be fatal, tread carefully!


    Example::

        sm = SummitNode('+', [1,2,3])
        > print(sm.value)
        6


    """

    __slots__ = ['operator', 'children', 'value']

    def __init__(self, operator, children):
        self.operator = operator
        self._validate_operator()
        self.children = children

    def _validate_operator(self):
        """
        Validate given operator with the allowed operators list

        :raises ~summit.exceptions.InvalidOperator
        """
        op_list = ['+', '-', '*', '/']
        if self.operator not in op_list:
            raise InvalidOperator('Please provide one of the following operators [ %s ]' % str(op_list))
