#!/usr/bin/env python
from __future__ import division

import operator
import sys
import unittest


class Error(Exception):
  """Custom exception for module."""


class Node(object):
  """Node for binary tree.

  The number of children extending from any node is greater than or equal to 2.
  Each node could either be a mathematical operator or a real number.
  Each of the leaf nodes should be (no promises :-)) a real number - Hint :
  Handle error here....
  The mathematical operators come from the set (-, +, /, *)
  If a node is a mathematical operator, the operation should be evaluated
  left-to-right:
  So, if you have a subtraction node with 1, 2 and 3 you would evaluate as
  1 - 2 - 3 = -4. Write a method that calculates the value of such a tree.

  Attributes:
    operator_map: dict: maps operator string to operator method.
    value: str or int, math operator as string, or numerical type.
    left: str or int, math operator as string, or numerical type.
    right: str or int, math operator as string, or numerical type.
  """
  operator_map = {
      '+': operator.add, '-': operator.sub,
      '*': operator.mul, '/': operator.truediv}

  def __init__(self, value=None, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def evaluate(self):
    if self.value in self.operator_map:
      mathematical_operator = self.operator_map[self.value]
      try:
        return mathematical_operator(
            self.left.evaluate(), self.right.evaluate())
      except BaseException as error:
        raise Error('Error: {0}'.format(error.message))
    else:
      return self.value


def parse_expression(math_expression):
  """Parse string as math expression with basic operators.

  Example of the tree parsed from '2 + 3':
    (+)
    / \
  (2) (3)
  Example of the tree parsed from '1 - 2 - 3':
      (-)
      / \
    (-) (3)
    / \
  (1) (2)

  Args:
    math_expression: str, math expression. example: "2 + 3"
  Returns:
    Node object as tree.
  """
  tree = Node()
  math_expression = math_expression.split()

  if len(math_expression) < 3:
    error_msg = 'expected 3 values, got {0}'.format(len(math_expression))
    raise Error(error_msg)

  for value in math_expression:

    if value.isdigit():
      value = int(value)

    if tree.value is None:
      tree.value = value
    elif str(value) in tree.operator_map:
      tree = Node(value, tree)
    elif isinstance(value, int) and str(tree.value) in tree.operator_map:
      tree.right = Node(value)

  return tree


class Tests(unittest.TestCase):
  """Unittests for module."""
  def test_node(self):
    tree = Node('+', Node(2), Node(3))
    expected_value = 5
    self.assertIsInstance(tree, Node)
    self.assertEquals(tree.value, '+')
    self.assertEquals(tree.left.value, 2)
    self.assertEquals(tree.right.value, 3)
    self.assertEquals(tree.evaluate(), expected_value)
    self.assertRaises(Error, Node('+').evaluate)

  def test_parse_expression(self):
    check = parse_expression('2 + 5').evaluate()
    expected_value = 7
    self.assertEquals(check, expected_value)
    check = parse_expression('1 - 2 - 3').evaluate()
    expected_value = -4
    self.assertEquals(check, expected_value)
    check = parse_expression('5 / 2').evaluate()
    expected_value = 2.5
    self.assertAlmostEquals(check, expected_value)
    self.assertRaises(Error, parse_expression, '')


if __name__ == '__main__':
  unittest.main()
