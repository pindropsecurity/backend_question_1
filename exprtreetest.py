'''Unit tests for exprtree.py'''

import unittest
import exprtree

class NodeBehavior(unittest.TestCase):
	'''verifies base class, Node, expected behavior'''

	def testEnforceIntLine(self):
		'''base class node should not allow non-integer for line number'''
		self.assertRaises(exprtree.ExprTreeError, exprtree.Node, None, '')
		
	def testLocation(self):
		'''location should print empty string in absense of line number'''
		x = exprtree.Node(tok='')
		self.assertEqual(x.location(), '')
		
		x = exprtree.Node(tok='', line=0)
		self.assertEqual(x.location(), 'line 1: ')
		
	def testRejectUnspecializedEvaluation(self):
		'''method evaluate should never be called from base class, Node,
		   which should throw exception in such an instance'''
		   
		class UnspecializedNode(exprtree.Node):
			''' tests lack of specialization of method, evaluate'''
			
			def __init__(self):
				exprtree.Node.__init__(self, tok='')
				
		x = UnspecializedNode()
		self.assertRaises(exprtree.NodeError, x.evaluate)
		   
class NumBehavior(unittest.TestCase):
	'''verifies class, Num, expected behavior'''
	
	def testAllowReal(self):
		'''instantiation of class Num should accept which are real numbers'''
		x = exprtree.Num(float(54))

	def testEnforceReal(self):
		'''instantiation of class Num should reject tokens which are not
		   real numbers'''
		self.assertRaises(exprtree.NodeError, exprtree.Num, "")
		
	def testEvaluate(self):
		'''instance of class Num should evaluate to the value with which
		   it was initialized'''
		value = 3.14159265
		x = exprtree.Num(value)
		self.assertEqual(x.evaluate(), value)
		
class OperationBehavior(unittest.TestCase):
	'''verifies class, Operation, expected behavior'''
	
	def testAcceptNumOperand(self):
		'''an instance of class Operation should accept a number as an operand'''
		
		op = exprtree.Operation('-')
		op.add(exprtree.Num(42))

	def testAcceptOperationOperand(self):
		'''an instance of class Operation should accept another instance
		   of class Operation as an operand'''
		
		op = exprtree.Operation('-')
		op.add(exprtree.Operation('+'))

	def testRejectUnspecializedEvaluation(self):
		'''method Operation.evaluate should never be called from 
		   base class, Node, which should throw exception 
		   in such an instance'''
		   
		class UnspecializedOp(exprtree.Operation):
			''' tests lack of specialization of method, evaluate'''
			
			def __init__(self):
				exprtree.Operation.__init__(self, tok='-')
				
		op = UnspecializedOp()
		op.add(exprtree.Num(50))
		op.add(exprtree.Num(42))
		self.assertRaises(exprtree.OperationError, op.evaluate)

if __name__ == '__main__':
	unittest.main()
	
	
