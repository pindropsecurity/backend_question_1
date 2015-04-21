''' This module is an implementation of expression tree described by
    backend_quesion_1.  The specification for this can be found at:
    
    https://github.com/pindropsecurity/backend_question_1'''

class ExprTreeError(Exception):
	'''base error class for this module'''
	
	def __init__(self, s=""):
		Exception.__init__(self)
		self.msg = s;

	def __str__(self):
		return self.msg;


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

class NodeError(ExprTreeError):
	'''Exception class which indicates a violation of invariants
	   in base class Node.'''

	def __init__(self, msg=""):
		ExprTreeError.__init__(self, msg)

class Node:
	'''fundamental element of expression tree.    
       intended as 'abstract base class'
	   optionally records line on which element originated.'''
	
	def __init__(self, line=None):
		if not (line is None or isinstance(line,int)):
			raise NodeError("%s: line number must be an int (not %s)" %\
				(self.__class__.__name__, line.__class__.__name__))
		
		self.line = line
            
	def location(self):
		'''returns location in source data, if present.
		   otherwise returns empty string'''
		   
		if self.line is None: 
			return "" 
		else: 
			return 'line %s:' %  (self.line + 1)

	def evaluate(self):
		return 0
		
class Num(Node):
	
	def __init__(self, tok=None, line=None):
		Node.__init__(self, line=line)
		
if __name__ == "__main__":
	
	try:
		x = Node(line=10)
		print "%s value: %d" % (x.location(), x.evaluate()) 
		
		y = Node(line="")
		
	except ExprTreeError as e:
		print "error: %s" % e
		
	



   
