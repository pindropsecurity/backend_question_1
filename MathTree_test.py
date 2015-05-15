import unittest
from MathTree import Node, BranchNode, LeafNode

class NodeTestCase(unittest.TestCase):
  def setUp(self):
    self.child_node_A = Node('-3.14')
    self.child_node_B = Node(2)
    self.parent_node = Node('+')
    self.root_node = Node('+',(Node(3),Node(1)),Node('-',Node(5),Node(2)))

  def test_BranchNode_Instantiation(self):
    self.assertTrue(isinstance(self.parent_node, BranchNode))

  def test_LeafNode_Instantiate(self):
    self.assertTrue(isinstance(self.child_node_A, LeafNode))
    self.assertTrue(isinstance(self.child_node_B, LeafNode))
    self.assertFalse(isinstance(self.child_node_A, BranchNode))
    self.assertFalse(isinstance(self.child_node_B, BranchNode))

  def test_addChild(self):
    with self.assertRaises(AttributeError):
      self.child_node_A.addChild(Node('3'))

    newChild_C, newChild_D = Node('1'), Node('-')
    newParent = Node('+',[newChild_C])
    newParent.addChild(newChild_D)
    self.assertTrue(newChild_D in newParent.children)
    self.assertTrue(newChild_C in newParent.children)

  def test_LeafNode_values(self):
    self.assertEqual(str(self.child_node_A),'(-3.14)')
    self.assertEqual(self.child_node_A(),-3.14)

  def test_BranchNode_values(self):
    self.assertEqual(str(self.root_node),"""((3.0)+(1.0)+((5.0)-(2.0)))""")

  def test_LeafNode_call(self):
    self.assertEqual(self.child_node_A(),-3.14)

  def test_BranchNode_call(self):
    self.assertEqual(self.root_node(),7)
    with self.assertRaises(ValueError):
      self.parent_node()

  # def test_addChild(self):
  #   self.assertEqual(len(self.parent_node),5)

  # def test_str_cast(self):
  #   self.assertEqual(str(self.parent_node),"((3)+(-12.18)+((4)-(2)))")

if __name__ == "__main__":
  unittest.main()
