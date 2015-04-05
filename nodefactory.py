class ParentDoesNotExist(Exception):
    pass


class SiblingDoesNotExist(Exception):
    pass


class InvalidMathNode(Exception):
    pass


class Node(list):
    """
    A Node is a nothing more than a list that tracks a little extra information about where it exists
    in relation to other nodes
    """
    position = 0
    depth = 0
    def __init__(self, value, children=[], parent=None, *args, **kwargs):
        self.value = value
        for child in self.children:
            self.add_child(child)
        self.parent = parent
        super(list, self).__init__(*args, **kwargs)
    
    def add_child(self, node):
        node.parent = self
        node.position = len(self)
        node.depth = self.depth + 1
        self.append(node)


class Tree(object):
    """
    Acts as a 'container' for Node objects, to be organized in a tree structure with a single base node.
    """
    def __init__(self, root):
        if type(root) != Node:
            raise TypeError('root must be of type Node')
        self.root = root
        self.reset()
    
    def reset(self):
        self.current = self.root
    
    def move_to(self, node):
        """Wrapper for moving current pointer"""
        self.current = node
    
    def move_up(self):
        """Move to the parent node if it exists"""
        if type(self.current.parent) != Node:
            raise ParentDoesNotExist('Parent node does not exist')
        self.move_to(self.current.parent)
    
    def next(self):
        """Move to the next sibling of the current node, if it exists"""
        proposed_position = self.current.position + 1
        try:
            proposed_current = self.current.parent[proposed_position]
        except IndexError:
            #: if next sibling doesn't exist
            self.handle_sibling_error(self.current.depth, proposed_position)
        except TypeError:
            #: if parent is None
            self.handle_sibling_error(self.current.depth, proposed_position)
        else:
            self.move_to(proposed_current)
        return self.current
    
    def previous(self):
        """Move to the previous sibling of the current node, if it exists"""
        if self.current.position == 0:
            self.handle_sibling_error(self.current.depth, -1)
        self.move_to(self.current.parent[self.current.position - 1])
        return self.current
    
    def handle_sibling_error(self, depth, position):
        raise SiblingDoesNotExist('Node does not exist at depth: %d, position: %d' % (depth, position))


class MathNode(Node):
    """
    Node with rules limiting what values it may represent
    """
    nodetype = 'operator'
    def __init__(self, value, *args, **kwargs):
        valid_operators = ['-', '+', '/', '*']
        is_valid = False
        if value in valid_operators:
            is_valid = True
        else:
            try:
                if value.real == value:
                    self.nodetype = 'number'
                    is_valid = True
            except AttributeError:
                is_valid = False
        if not is_valid:
            raise InvalidMathNode('value must be math expression or real number')
        
        super(list, self).__init__(value, *args, **kwargs)
