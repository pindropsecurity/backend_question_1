''' This module is an implementation of expression tree described by
    backend_quesion_1.  The specification for this can be found at:
    
    https://github.com/pindropsecurity/backend_question_1
    
    I am using this exercise to also (partially) restore my knowledge
    of python, a language in which I stopped actively programming in
    June 2011 - almost 4 years ago.
    
    Please excuse my obsession with line numbers.  If I have time,
    exprtree will parse an expression string, when run as a program.
    Unittests have been split into a different module.'''

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
	
	def __init__(self, line=None):
		if not (line is None or isinstance(line,int)):
			raise NodeError('%sline number must be an int (not %s)' %\
				(self.__class__.__name__, line.__class__.__name__))
		
		self.line = line
            
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
	'''Num represents a number term in the expression.
	
	   NOTE: this class under development and is not usable in its current
	   state. DO NOT USE IT.
	   '''	
	def __init__(self, tok=None, line=None):
		Node.__init__(self, line=line)
		raise NodeError(
			'I told you not to use class %s!' % (self.__class__.__name__))

class Operation(Node):
	'''class Operation represents the application of a successive pair
	   of numbers to a common operator. e.g. a - b - c - ......

	   NOTE: this class under development and is not usable in its current
	   state. DO NOT USE IT.'''

	def __init__(self, tok=None, line=None):
		Node.__init__(self, line=line)
		raise NodeError(
			'I told you not to use class %s!' % (self.__class__.__name__))
		
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


if __name__ == '__main__':
	
	try:
		x = Node(line=10)
		print '%s value: %d' % (x.location(), x.evaluate()) 
		
		y = Node(line='')
		
	except ExprTreeError as e:
		print 'error: %s' % e
		
	



   
