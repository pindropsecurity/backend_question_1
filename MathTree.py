import re

class Node(object):
  numberForm = re.compile("^-?\d*\.?\d*$")
  operationForm = re.compile("^[+-/*/]$")
  children = []

  def __init__(self, value, *children, isRoot=False):
    if self.numberForm.match(value):
      self.value = float(value)
      self.isLeaf = True
      if isRoot:
        raise ValueError("Root node must have value '+', '-', '*', or '/'")
    elif self.operationForm.match(value):
      self.value = value
      self.isLeaf = False
      self.isRoot = isRoot
    else:
      raise ValueError("'Value' must be a number string or an operator (+-*/)")
    for arg in children:
      if isinstance(arg, list) | isinstance(arg, tuple):
        for child in arg:
          self.addChild(child)
      else:
        self.addChild(arg)

  def addChild(self, child):
    if not isinstance(child, Node):
      raise TypeError("Child node must be of type Node")
    else:
      self.children.append(child)
      self.isLeaf = False

  def __len__(self):
    total = 0
    if self.isLeaf | (len(self.children) < 1):
      return 1
    for child in self.children:
      total += len(child)
    return total
