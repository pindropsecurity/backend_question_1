'''Unit tests for exprtree.py'''

import unittest
import exprtree
import math

class NodeBehavior(unittest.TestCase):
	'''verifies base class, Node, expected behavior'''
		
	def testRejectUnspecializedEvaluation(self):
		'''method evaluate should never be called from base class, Node,
		   which should throw exception in such an instance'''
		   
		class UnspecializedNode(exprtree.Node):
			''' tests lack of specialization of method, evaluate'''
			
			def __init__(self):
				exprtree.Node.__init__(self, '')
				
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
		op.addOperand(exprtree.Num(42))

	def testAcceptOperationOperand(self):
		'''an instance of class Operation should accept another instance
		   of class Operation as an operand'''
		
		op = exprtree.Operation('-')
		op.addOperand(exprtree.Operation('+'))

	def testRejectUnspecializedEvaluation(self):
		'''method Operation.evaluate should never be called from 
		   base class, Node, which should throw exception 
		   in such an instance'''
		   
		class UnspecializedOp(exprtree.Operation):
			''' tests lack of specialization of method, evaluate'''
			
			def __init__(self):
				exprtree.Operation.__init__(self, '-')
				
		op = UnspecializedOp()
		op.addOperand(exprtree.Num(50))
		op.addOperand(exprtree.Num(42))
		self.assertRaises(exprtree.OperationError, op.evaluate)
		
	def testInsufficientOperands(self):
		'''class Operation should raise an exception when it holds less 
		   than two operands'''
		   
		sub = exprtree.Subtract()
		self.assertRaises(exprtree.OperationError, sub.evaluate);
		
		sub.addOperand(exprtree.Num(42))
		self.assertRaises(exprtree.OperationError, sub.evaluate);
		
		
class AddBehavior(unittest.TestCase):
	'''verifies class, Add, expected behavior'''
	
	def testSimpleEvaluation(self):
		'''class Add should properly evaluate two operands'''
		op = exprtree.Add()
		op.addOperand(exprtree.Num(42))
		op.addOperand(exprtree.Num(41))
		
		self.assertEquals(83,op.evaluate())

	def testExtendedEvaluation(self):
		'''class Add should properly evaluate two operands'''
		op = exprtree.Add()
		op.addOperand(exprtree.Num(1))
		op.addOperand(exprtree.Num(2))
		op.addOperand(exprtree.Num(3))
		
		self.assertEquals(6, op.evaluate())

class SubtractBehavior(unittest.TestCase):
	'''verifies class, Subtract, expected behavior'''
	
	def testSimpleEvaluation(self):
		'''class Subtract should properly evaluate two operands'''
		op = exprtree.Subtract()
		op.addOperand(exprtree.Num(42))
		op.addOperand(exprtree.Num(41))
		
		self.assertEquals(1,op.evaluate())

	def testExtendedEvaluation(self):
		'''class Subtract should properly evaluate two operands'''
		op = exprtree.Subtract()
		op.addOperand(exprtree.Num(1))
		op.addOperand(exprtree.Num(2))
		op.addOperand(exprtree.Num(3))
		
		self.assertEquals(-4, op.evaluate())

class MultiplyBehavior(unittest.TestCase):
	'''verifies class, Multiply, expected behavior'''
	
	def testSimpleEvaluation(self):
		'''class Multiply should properly evaluate two operands'''
		op = exprtree.Multiply()
		op.addOperand(exprtree.Num(math.pi))
		op.addOperand(exprtree.Num(2.0))
		
		expected = math.pi * 2.0
		self.assertEquals(expected ,op.evaluate())

	def testExtendedEvaluation(self):
		'''class Multiplyevaluate two operands'''
		op = exprtree.Multiply()
		op.addOperand(exprtree.Num(math.pi))
		op.addOperand(exprtree.Num(2.0))
		op.addOperand(exprtree.Num(0.5))
		
		self.assertEquals(math.pi, op.evaluate())

class DivideBehavior(unittest.TestCase):
	'''verifies class, Divide, expected behavior'''
	
	def testSimpleEvaluation(self):
		'''class Divide should properly evaluate two operands'''
		op = exprtree.Divide()
		op.addOperand(exprtree.Num(math.pi))
		op.addOperand(exprtree.Num(2.0))
		
		expected = math.pi / 2.0
		self.assertEquals(expected ,op.evaluate())

	def testExtendedEvaluation(self):
		'''class Divide evaluate two operands'''
		op = exprtree.Divide()
		op.addOperand(exprtree.Num(math.pi))
		op.addOperand(exprtree.Num(2.0))
		op.addOperand(exprtree.Num(0.5))
		
		self.assertEquals(math.pi, op.evaluate())
		
class ExprTreeBehavior(unittest.TestCase):
	'''verifies class, Divide, expected behavior'''
	
	def testDegenerateExpression(self):
		'''expression consisting of lone number should be successfully
		   evaluated'''
		   
		expr = exprtree.ExprTree(exprtree.Num(42))
		self.assertEquals(42, expr.evaluate())

	def testAccumulatedSubtraction(self):
		'''this test implements one of the acceptance criteria as specified
		   in the requirements.  refer to the link provided in the module
		   doc string'''
		   
		op = exprtree.Subtract()
		op.addOperand(exprtree.Num(1))
		op.addOperand(exprtree.Num(2))
		op.addOperand(exprtree.Num(3))
		
		expr = exprtree.ExprTree(op)
		self.assertEquals(-4, expr.evaluate())
		
	def testHetergenousOperations(self):
		'''expression containing valid multiple operations should evaluate successfully.
		
		   expression tree to be tested:
		   
		               +
		   -              *       -42       /
		 83  41   math.pi   2            pi   -2
		 
		 the result should be 42 + 2pi + (-42) + (-pi/2) = 3*pi/2 '''
		   		
		#expr = exprtree.ExprTree(exprtree.Add())
		#expr.root.addOperand(exprtree.Subtract())
		#expr.root.operands

if __name__ == '__main__':
	unittest.main()
	
	
