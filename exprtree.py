''' This module is an implementation of expression tree described by
    backend_quesion_1.  The specification for this can be found at:
    
    https://github.com/pindropsecurity/backend_question_1
    
    I am using this exercise to also (partially) restore my knowledge
    of python, a language in which I stopped actively programming in
    June 2011 - almost 4 years ago.
    
    Please excuse my obsession with line numbers.  If I have time,
    exprtree will parse an expression string, when run as a program.
    Unittests have been split into a different module.'''
    
import numbers
import operator


class ExprTreeError(Exception):
	'''base error class for this module'''
	
	def __init__(self, s=''):
		Exception.__init__(self)
		self.msg = s;

	def __str__(self):
		return self.msg;


class NodeError(ExprTreeError):
	'''Exception class which indicates a violation of invariants
	   in base class Node.'''

	def __init__(self, msg=''):
		ExprTreeError.__init__(self, msg)

class Node:
	'''fundamental element of expression tree.    
       intended as base class to be specialized in all cases of instantiation.
	   optionally records line on which element originated.'''
	
	def __init__(self, tok, line=None):				
		if not (line is None or isinstance(line,int)):
			raise NodeError('%sif specified, line number must be an int (not %s)' %\
				(self.__class__.__name__, line.__class__.__name__))
		else:
			self.line = line
		
		if tok is None:
			raise NodeError('%svalue of Node cannot be None' %\
				(self.location()))
				
		self.tok = tok
			
	def __str__(self):
		'''returns string representation of expression as defined by
		   contents of node and children'''
		return self.token()
			
	def token(self):
		if self.tok is None:
			return ''
		else:
			return str(self.tok)


	def location(self):
		'''returns location in source data, if present.
		   otherwise returns empty string'''
		   
		if self.line is None: 
			return '' 
		else: 
			return 'line %s: ' %  (self.line + 1)

	def evaluate(self):
		'''compute the value of node per it's type and contents.
		   base class method intended to serve as specification of protocol'''
		raise NodeError('%sattempt to employ unspecialized evaluation (class %s)' %\
			(self.location(), self.__class__.__name__))

		
class Num(Node):
	'''Num represents a number term in the expression.'''
	
	def __init__(self, tok, line=None):
		Node.__init__(self, tok=tok, line=line)
		if not isinstance(self.tok, numbers.Real):
			raise NodeError("%s%s is not a real number" %\
				(self.location(), self.tok))
		
	def evaluate(self):
		return self.tok;


class OperationError(ExprTreeError):
	'''Exception class which indicates a violation of invariants
	   in class Operation.'''

	def __init__(self, msg=''):
		ExprTreeError.__init__(self, msg)

class Operation(Node):
	'''class Operation represents the application of a common operator to
	   a successiive pair of numbers. e.g. a - b - c - ......
	   In effect, the result value is accumulated.'''
	   
	def __init__(self, tok, line=None):
		Node.__init__(self, tok=tok, line=line)
		self.operands = []
		self.op = None
			
	def __str__(self):
		'''returns string representation of expression as defined by
		   operator (token) and operands (child nodes)'''
		
		if self.operands:
			return self.token().join([str(child) for child in self.operands])
		else:
			return self.token();
			
	def operate(self, lhs, rhs):
		'''performs mathematical binary operation upon to real numbers'''
		raise OperationError('%sattempt to employ unspecialized operation (class %s)' %\
			(self.location(), self.__class__.__name__))
	
	def add(self, operand):
		'''adds an operand to the operation.'''
		if not (isinstance(operand, Num) or isinstance(operand, Operation)):
			raise NodeError('%sattempt to add invalid operator of type %s' %\
				(self.location(), operand.__class__.__name__))
				
		self.operands.append(operand);
		
	def evaluate(self):
		if not self.operands:
			raise OperationError("%soperation '%s' has no operands" %\
				(self.location(), self.token()))
		elif len(self.operands) == 1:
			raise OperationError("%soperation '%s' has insufficient operands (%s)" %\
				(self.location(), self.token(), str(self)))
				
		result = self.operands[0].evaluate()
		for rhs in self.operands[1:]:
			result = self.operate(result, rhs)
			
		return result
		
class Subtract(Operation):
	'''Implements subtraction'''
	
	def __init__(self, line=None):
		Operation.__init__(self, '-', line=line)
		
	def operate(self, lhs, rhs):
		return lhs - rhs.evaluate()
		
class Add(Operation):
	'''Implements addition'''
	
	def __init__(self, line=None):
		Operation.__init__(self, '+', line=line)
		
	def operate(self, lhs, rhs):
		return lhs + rhs.evaluate()
		
class Multiply(Operation):
	'''Implements multiplication'''
	
	def __init__(self, line=None):
		Operation.__init__(self, '*', line=line)
		
	def operate(self, lhs, rhs):
		return lhs * rhs.evaluate()
		
class DivideByZero(OperationError):
	'''Error to flag divide by zero in expression tree'''
	
	def __init__(self, opNode, divisorNode):
		ExprTreeError.__init__(self,
			"%sdivide by zero caused by subexpression" % (opNode.location()))
		
		if divisorNode.location():
			self.msg += " at %s'%s'" % \
				(divisorNode.location(), divisorNode.token()) 

class Divide(Operation):
	'''Implements division'''
	
	def __init__(self, line=None):
		Operation.__init__(self, '+', line=line)
		
	def operate(self, lhs, rhs):
		divisor = rhs.evaluate()
		if not divisor:
			raise DivideByZero(self, rhs)
			
		return lhs / divisor

	def add(self, operand):
		'''specialization of method rejects zero
		   TODO: should test for zero be more robust since floating point
		   is involved?  seems like a python novice question ...'''
		if len(self.operands) > 0 \
			and isinstance(operand, Num) \
			and not operand.evaluate():
			raise OperationError('%sdivide by zero' % (operand.location()))
		else:
			Operation.add(self, operand)		
		
class Tree:
	'''Tree which defines simple mathematical expression.
	   
	   Tree consists of nodes which represent either real numbers or 
	   the mathematical operations, addition (+), subtraction (-), 
	   multiplication (*), or division (/).  Contiguous operations of
	   the same type (e.g. 1 - 2 - 3), may be aggregated into a 
	   single operation node.
	   
	   An instance of a tree may describe a syntactically incorrect 
	   expression such an expresion term (i.e. number) may have been
	   omitted.'''

'''
if __name__ == '__main__':
	
	try:
		x = Node(tok='543', line=10)
		print '%s value: %d' % (x.location(), x.evaluate()) 
		
		y = Node(tok=543)
		
	except ExprTreeError as e:
		print 'error: %s' % e
'''	
	



   
