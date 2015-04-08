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


class InvalidTree(Exception):
    """ The tree dictionary didn't have the proper structure """
    pass


class NoChildren(Exception):
    """ Tried to calculate node with no children """
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
    calculate() will return the value of all nodes under the root node.
    """
    operators = ["+", "-", "/", "*"]

    def __init__(self, val):
        if val not in self.operators:
            raise InvalidOperator("Invalid Operator. Must be in set(+ - / *)")
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
        if len(self.children) < 2:
            raise NoChildren("Must have at least two children NumberNodes to calculate")

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
        result = eval(expr)
        return NumberNode(result)


class NumberNode(Node):
    """
    A node that stores a number instead of an operator.
    """
    def __init__(self, val):
        if not isinstance(val, Number):
            raise InvalidNumber("Value must be a number")
        super(NumberNode, self).__init__(val)

    def __int__(self):
        return int(self.val)

    def __float__(self):
        return float(self.val)


class Tree(OperatorNode):
    """
    Create a Tree object from a dictionary.
    """
    def __init__(self, tree_dict):
        if len(tree_dict.keys()) > 1:
            raise InvalidTree("Tree can only have one root node")
        super(Tree, self).__init__(tree_dict.keys()[0])
        for node in self.tree(tree_dict).children:
            self.add_child(node)

    def tree(self, tree):
        def walk_tree(new_tree):
            op_node = OperatorNode(new_tree.keys()[0])
            for item in new_tree[new_tree.keys()[0]]:
                if isinstance(item, dict):
                    op_node.add_child(walk_tree(item))
                else:
                    op_node.add_child(NumberNode(item))
            return op_node

        root = tree.keys()[0]
        root_node = OperatorNode(root)
        for child in tree[root]:
            if isinstance(child, dict):
                root_node.add_child(walk_tree(child))
            else:
                root_node.add_child(NumberNode(child))

        return root_node