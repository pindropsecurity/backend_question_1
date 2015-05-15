import unittest
from MathTree import Node, BranchNode, LeafNode

class NodeTestCase(unittest.TestCase):
  def setUp(self):
    self.child_node_A = Node('-3.14')
    self.child_node_B = Node(2)
    self.parent_node = Node('+')

  def test_BranchNode_Instantiation(self):
    self.assertTrue(isinstance(self.parent_node, BranchNode))

  def test_LeafNode_Instantiate(self):
    self.assertTrue(isinstance(self.child_node_A, LeafNode))
    self.assertTrue(isinstance(self.child_node_B, LeafNode))
    self.assertFalse(isinstance(self.child_node_A, BranchNode))
    self.assertFalse(isinstance(self.child_node_B, BranchNode))

  # def test_addChild(self):
  #   self.assertEqual(len(self.parent_node),5)

  # def test_str_cast(self):
  #   self.assertEqual(str(self.parent_node),"((3)+(-12.18)+((4)-(2)))")

if __name__ == "__main__":
  unittest.main()
