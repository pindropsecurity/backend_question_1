'''Unit tests for exprtree.py'''

import unittest
import exprtree

class NodeBehavior(unittest.TestCase):

	def testEnforceIntLine(self):
		'''base class node should not allow non-integer for line number'''
		self.assertRaises(exprtree.ExprTreeError, exprtree.Node, "")
		
	def testLocation(self):
		'''location should print empty string in absense of line number'''
		x = exprtree.Node()
		self.assertEqual(x.location(), "")
		
		x = exprtree.Node(0)
		self.assertEqual(x.location(), "line 1: ")
		
	def testRejectUnspecializedEvaluation(self):
		'''method evaluate should never be called from base class, Node,
		   which should throw exception in such an instance'''
		   
		class UnspecializedNode(exprtree.Node):
			''' tests lack of specialization of method, evaluate'''
			
			def __init__(self):
				exprtree.Node.__init__(self)
				
		x = UnspecializedNode()
		self.assertRaises(exprtree.NodeError, x.evaluate)
		   

if __name__ == '__main__':
	unittest.main()
	
	
