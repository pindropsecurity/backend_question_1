#!/usr/bin/python3

class ExpressionNode(object):

    def __init__(self, node):
        self._node = node

    def eval(self):
        pass

    def __str__(self):
        return str(self._node)
