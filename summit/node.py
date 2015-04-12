__author__ = 'Greg'

from summit.exceptions import InvalidOperator, NotEnoughChildren, RealNumberExpected


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
        """
        Configures the SummitNode object with provided operator and children and requests validation
        of the provided arguments.

        :param operator: A string containing one of the following arithmetic operators ['+', '-', '*', '/']
        :type operator: string
        :param children: A list of two or more elements comprised of a mixture of real numbers and or SummitNodes
        :type children: list
        """
        self.operator = operator
        self._validate_operator()

        self.children = children
        self._validate_children()

        self.value = self._evaluate()


    def _validate_operator(self):
        """
        Validate given operator with the allowed operators list

        :raises ~summit.exceptions.InvalidOperator: If operator not in allowed list
        """
        op_list = ['+', '-', '*', '/']
        if self.operator not in op_list:
            raise InvalidOperator('Please provide one of the following operators [ %s ]' % str(op_list))

    def _validate_children(self):
        """
        Validate that at least two children were provided

        :raises ~summit.exceptions.NotEnoughChildren: If fewer than two children were provided.
        """
        child_count = len(self.children)
        if child_count < 2:
            raise NotEnoughChildren('Expected two or more children, %d provided' % child_count)

    @staticmethod
    def _get_child_value(child):
        if isinstance(child, SummitNode):
            return child.value
        else:
            try:
                tmp_val = float(child)
                return tmp_val
            except ValueError:
                raise RealNumberExpected

    def _evaluate(self):
        """
        Evaluate the children against the provided operator, sets self.value
        """

        op_map = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }

        operation = op_map[self.operator]
        start_val = None
        for child in self.children:
            subject = self._get_child_value(child)
            if start_val is None:
                # Set basis for operation, need a value to work against!
                start_val = subject
                continue
            start_val = operation(start_val, subject)
        return start_val
