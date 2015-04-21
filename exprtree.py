''' This module is an implementation of expression tree described by
    backend_quesion_1.  The specification for this can be found at:
    
    https://github.com/pindropsecurity/backend_question_1
    
    I am using this exercise to also (partially) restore my knowledge
    of python, a language in which I stopped actively programming in
    June 2011 - almost 4 years ago.'''
    
import numbers
import operator


class ExprTreeError(Exception):
	'''base error class for this module'''
	
	def __init__(self, s=''):
		Exception.__init__(self)
		self.__msg = s;

	def __str__(self):
		return self.msg;


class NodeError(ExprTreeError):
	'''Exception class which indicates a violation of invariants
	   in base class Node.'''

	def __init__(self, msg=''):
		ExprTreeError.__init__(self, msg)

class Node:
	'''fundamental element of expression tree.    
       intended as base class to be specialized in all cases of instantiation.'''
	
	def __init__(self, tok):
		self.__token = None
				
		if tok is None:
			raise NodeError('value of Node cannot be None')
		else:
			self.__token = tok
			
	def __str__(self):
		'''returns string representation of expression as defined by
		   contents of node and children'''
		return str(self.token())
	
	def token(self):
		return self.__token

	def evaluate(self):
		'''compute the value of node per it's type and contents.
		   base class method intended to serve as specification of protocol'''
		raise NodeError('attempt to employ unspecialized evaluation (class %s)' %\
			(self.__class__.__name__))

		
class Num(Node):
	'''Num represents a number term in the expression.'''
	
	def __init__(self, tok):
		try:
		   Node.__init__(self, float(tok))
		except ValueError:
			raise NodeError("value '%s' cannot be converted to a real number" %\
				(str(tok)))
		
	def evaluate(self):
		return self.token();


class OperationError(ExprTreeError):
	'''Exception class which indicates a violation of invariants
	   in class Operation.'''

	def __init__(self, msg=''):
		ExprTreeError.__init__(self, msg)

class Operation(Node):
	'''class Operation represents the application of a common operator to
	   a successiive pair of numbers. e.g. a - b - c - ......
	   In effect, the result value is accumulated.'''
	   
	def __init__(self, tok):
		Node.__init__(self, tok)
		self.__operands = []
			
	def __str__(self):
		'''returns string representation of expression as defined by
		   operator (token) and operands (child nodes)'''
		
		if self.arity() > 1:
			return str(self.token()).join([str(child) for child in self.__operands])
		elif self.arity() == 1:
			return '%s%s' % (str(self.lhs()),self.token());
		else:
			return ''
			
	def operate(self, lhs, rhs):
		'''performs mathematical binary operation upon to real numbers'''
		raise OperationError('attempt to employ unspecialized operation (class %s)' %\
			(self.__class__.__name__))
	
	def addOperand(self, operand):
		'''adds an operand to the operation.'''
		if not (isinstance(operand, Num) or isinstance(operand, Operation)):
			raise NodeError('attempt to add invalid operator of type %s' %\
				(operand.__class__.__name__))
				
		self.__operands.append(operand);
		
	def arity(self):
		return len(self.__operands)
		
	def lhs(self):
		'''returns the first operand (i.e. (l)eft-(h)and-(s)ide'''
		if self.arity():
			return self.__operands[0]
		else:
			raise OperationError("operation '%s' has no left-hand-side" %\
				(str(self.token())))
		
	def evaluate(self):
		if not self.__operands:
			raise OperationError("operation '%s' has no operands" %\
				(str(self.token())))
		elif self.arity() == 1:
			raise OperationError("operation '%s' has insufficient operands (%s)" %\
				(str(self.token()), str(self)))
				
		result = self.lhs().evaluate()
		for rhs in self.__operands[1:]:
			result = self.operate(result, rhs)
			
		return result
		
class Subtract(Operation):
	'''Implements subtraction'''
	
	def __init__(self):
		Operation.__init__(self, '-')
		
	def operate(self, lhs, rhs):
		return lhs - rhs.evaluate()
		
class Add(Operation):
	'''Implements addition'''
	
	def __init__(self):
		Operation.__init__(self, '+')
		
	def operate(self, lhs, rhs):
		return lhs + rhs.evaluate()
		
class Multiply(Operation):
	'''Implements multiplication'''
	
	def __init__(self):
		Operation.__init__(self, '*')
		
	def operate(self, lhs, rhs):
		return lhs * rhs.evaluate()
		
class DivideByZero(OperationError):
	'''Error to flag divide by zero in expression tree'''
	
	def __init__(self, opNode, divisorNode):
		DivideByZero.__init__(self,
			"divide by zero caused by subexpression")

class Divide(Operation):
	'''Implements division'''
	
	def __init__(self):
		Operation.__init__(self, '+')
		
	def operate(self, lhs, rhs):
		divisor = rhs.evaluate()
		if not divisor:
			raise DivideByZero(self, rhs)
			
		return lhs / divisor

	def addOperand(self, operand):
		'''specialization of method rejects zero
		   TODO: should test for zero be more robust since floating point
		   is involved?  seems like a python novice question ...'''
		if self.arity() > 0 \
			and isinstance(operand, Num) \
			and not operand.evaluate():
			raise OperationError('guaranteed divide by zero')
		else:
			Operation.addOperand(self, operand)		
		
		
class ExprTree:
	'''Tree which defines simple mathematical expression.
	   
	   Tree consists of nodes which represent either real numbers or 
	   the mathematical operations, addition (+), subtraction (-), 
	   multiplication (*), or division (/).  Contiguous operations of
	   the same type (e.g. 1 - 2 - 3), may be aggregated into a 
	   single operation node.
	   
	   An instance of a tree may describe a syntactically incorrect 
	   expression such an expresion term (i.e. number) may have been
	   omitted.'''
	   
	def __init__(self, root=Num(0)):
		'''initialize an instance of class ExprTree such that by default,
		   a tree evaluates to zero'''

		self.root = root
		
	def evaluate(self):
		return self.root.evaluate()
		
	def __setattr__(self, name, value):
		if name != "root":
			ExprTree.__setattr__(self, name, value)
			
		if not (isinstance(value, Num) or isinstance(value, Operation)):
			raise NodeError(
				'root node of %s must be either instance of %s' \
				' or a subclass of %s (not an %s)' %\
				(Num.__name__, Operation.__name__, value.__class__.__name__))
				
		self.__dict__["root"] = value
				
    

'''
if __name__ == '__main__':
	
	try:
		x = Node('543')
		print '%s value: %d' % (x.location(), x.evaluate()) 
		
		y = Node(tok=543)
		
	except ExprTreeError as e:
		print 'error: %s' % e
'''	
	



   
