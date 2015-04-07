#!/usr/bin/python

from numbers import Number


class InvalidOperator(Exception):
    """ An invalid operator was passed """
    pass


class InvalidNode(Exception):
    """ The node was created with no value """
    pass


class InvalidNumber(Exception):
    """ The node was not passed a number """
    pass


class Node(object):
    """
    Object with basic Node properties that will be extended with OperatorNode and NumberNode.
    Can contain any arbitrary number of Nodes.
    """
    def __init__(self, val):
        if val == "":
            raise InvalidNode("Node cannot be empty")

        self.val = val
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()


class OperatorNode(Node):
    """
    OperatorNode has a value of +, -, /, or *
    calculate() will return the value of the tree under the node
    """
    operators = ["+", "-", "/", "*"]

    def __init__(self, val):
        if val not in self.operators:
            raise InvalidOperator("Invalid Operator. Must be one of set(+ - / *)")

        self._operator = val
        super(OperatorNode, self).__init__(val)

    @property
    def operator(self):
        return self._operator

    def calculate(self):
        """
        Recursively walk through all children in OperatorNode and solve until only
        a NumberNode is left.
        """
        def calculate_all_children(children, operator):
            num_children = []
            for node in children:
                if isinstance(node, OperatorNode):
                    num_children.append(calculate_all_children(node.children, node.operator))
                else:
                    num_children.append(node)
            return self.solve_expression(num_children, operator)

        return calculate_all_children(self.children, self.operator)

    def solve_expression(self, number_nodes, operator):
        """
        Create an expression to calculate with eval()
        """
        expr = (" %s " % operator).join([str(float(n)) for n in number_nodes])
        print expr
        result = eval(expr)
        print result
        return NumberNode(result)


class NumberNode(Node):
    """
    A node that stores a number instead of an operator.
    """
    def __init__(self, val):
        if not isinstance(val, Number):
            raise InvalidNumber

        super(NumberNode, self).__init__(val)

    def __int__(self):
        return int(self.val)

    def __float__(self):
        return float(self.val)

