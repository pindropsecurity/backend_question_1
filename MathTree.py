import re

numberForm = re.compile("^-?\d*\.?\d*$")
operationForm = re.compile("^[+-/*/]$")

class Node(object):
  def __new__(cls, value, *children):
    strValue = str(value)
    if operationForm.match(strValue):
      obj = super().__new__(BranchNode)
      obj.__init__(value, *children)
      return obj
    elif numberForm.match(strValue):
      obj = super().__new__(LeafNode)
      obj.__init__(value, *children)
      return obj
    else:
      raise ValueError("""'value' must be a real number, or a string
                        representing a real number or operator (+-/*)""")

class BranchNode(object):
  children = []

  def __init__(self, value, *children, isRoot=False):
    if operationForm.match(value):
      self.value = value
    else:
      raise ValueError("""'value' must an operator (+-*/) for instantiating a
                        BranchNode. For mixed Node instantiation, please use
                        Node(value, *children).""")
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

class LeafNode(Node):
  def __init__(self, value, *children):
    strValue = str(value)
    if numberForm.match(strValue):
      self.value = float(value)
    else:
      raise ValueError("""'value' must be a real number for instantiating a
                        LeafNode. For mixed Node instantiation, please use
                        Node(value, *children).""")
    if len(children) > 0:
      raise TypeError("""A LeafNode cannot have child nodes.""")
