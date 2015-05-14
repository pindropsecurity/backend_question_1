import unittest
from MathTree import Node

class NodeTestCase(unittest.TestCase):
  def setUp(self):
    self.child_node_a = Node('3')
    self.child_node_b = Node('-12.18')
    self.parent_node = Node('+', 
                            (self.child_node_a, self.child_node_b),
                            Node('-',Node('4'),Node('2')),
                            isRoot=True)

  def test_addChild(self):
    self.assertEqual(len(self.parent_node),5)

  def test_str_cast(self):
    self.assertEqual(str(self.parent_node),"(3)+(-12.18)+(4-2)")

if __name__ == "__main__":
  unittest.main()
