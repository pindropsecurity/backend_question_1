#!/usr/bin/python

from numbers import Number


class InvalidOperator(Exception):
    pass


class InvalidNode(Exception):
    pass


class InvalidNumber(Exception):
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


class OperatorNode(Node):
    """
    OperatorNode has a value of +, -, /, or *
    calculate() will return the value of the tree under the node
    """
    operators = ["+", "-", "/", "*"]

    def __init__(self, val):
        if val not in self.operators:
            raise InvalidOperator("Invalid Operator. Must be one of [+ - / *]")
        else:
            super(OperatorNode, self).__init__(val)


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


    pass
