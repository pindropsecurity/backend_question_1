import re

numberForm = re.compile("^-?\d*\.?\d*$")
operationForm = re.compile("^[+-/*/]$")

class Node(object):
  """A general Node class used in the creation of its subclasses, BranchNode and 
    LeafNode. *children should only be included in the instantiation of 
    BranchNodes""" 
  def __new__(cls, value, *children):
    strValue = str(value)
    if operationForm.match(strValue):
      obj = super().__new__(BranchNode)
      return obj
    elif numberForm.match(strValue):
      obj = super().__new__(LeafNode)
      return obj
    else:
      raise ValueError("""'value' must be a real number, or a string
                        representing a real number or operator (+-/*)""")
  def __verify__(self):
    pass
  def __str__(self):
    pass
  def __call__(self):
    if self.__verify__():
      return eval(str(self))
    else:
      raise ValueError("""Each Branch Node needs at least 2 sub-Nodes in order
                        to be correctly evaluated.""")

class BranchNode(Node):
  """A sublcass of Node, this class should never be called directly. To create 
    BranchNode, call Node(value, *children), where value should be a single 
    character string of +, -, *, or /. children is an optional parameter which
    is a list of all subnodes for this node."""
  def __init__(self, value, *children):
    if operationForm.match(value):
      self.value = value
    else:
      raise ValueError("""'value' must an operator (+-*/) for instantiating a
                        BranchNode. For mixed Node instantiation, please use
                        Node(value, *children).""")
    self.children = []
    for arg in children:
      if isinstance(arg, list) | isinstance(arg, tuple):
        for child in arg:
          self.addChild(child)
      else:
        self.addChild(arg)

  def addChild(self, child):
    if not isinstance(child, Node):
      raise TypeError("""Child node must be subclass of type Node
                        i.e. BranchNode or LeafNode""")
    else:
      self.children.append(child)

  def __str__(self):
    newStr = "(" + str(self.children[0])
    for childValue in self.children[1:]:
      newStr += "{}{}".format(self.value,childValue)
    return newStr + ")"

  def __verify__(self):
    if len(self.children) > 1:
      verified = True
      for child in self.children:
        verified = (verified & child.__verify__())
      return verified
    else:
      return False


class LeafNode(Node):
  """A subclass of Node, this class should never be called directly. To create
    a LeafNode, call Node(value), where 'value' is a either an int, float, or
    string representaiton of a real number. All values will be converted to
    a float format. Every branch of nodes in a Node treem should be terminated
    with a LeafNode."""
  def __init__(self, value, *children):
    strValue = str(value)
    if numberForm.match(strValue):
      self.value = float(value)
    else:
      raise ValueError("""'value' must be a real number for instantiating a
                        LeafNode. For mixed Node instantiation, please use
                        Node(value, *children).""")
    if len(children) > 0:
      raise TypeError("""A LeafNode cannot have children nodes.""")

  def __str__(self):
    return "({})".format(self.value)

  def __verify__(self):
    return True
