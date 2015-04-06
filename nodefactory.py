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
        for child in self:
            self.add_child(child)
        self.parent = parent
        super(Node, self).__init__(*args, **kwargs)
    
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
        if not isinstance(root, Node):
            raise TypeError('root must be of a Node or subclass of Node')
        self.root = root
        self.reset()
    
    def reset(self):
        self.current = self.root
    
    def move_to(self, node):
        """Wrapper for moving current pointer"""
        self.current = node
    
    def move_up(self):
        """Move to the parent node if it exists"""
        if not isinstance(self.current.parent, Node):
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
        
        super(MathNode, self).__init__(value, *args, **kwargs)


def _get_total(math_mode, left, right):
    if left == None:
        return right
    total = left
    if math_mode == '-':
        total -= right
    elif math_mode == '+':
        total += right
    elif math_mode == '/':
        total /= right
    elif math_mode == '*':
        total *= right
    return total


def math_tree_calculator(node, total=None, math_mode=None):
    if node.nodetype == 'operator':
        for child in node:
            print child.nodetype
            if child.nodetype == 'number':
                total = _get_total(node.value, total, child.value)
            else:
                total = _get_total(node.value, total, math_tree_calculator(child))
    else:
        total = _get_total(math_mode, total, node.value)
    return total


def node_pretty_print(node, indent=0):
    rjust_indent = indent
    if indent:
        rjust_indent = indent * 3
    print '{}'.format(node.value).rjust(rjust_indent, ' ')
    for child in node:
        node_pretty_print(child, indent + 1)


def dict_to_math_node(d):
    node = MathNode(d['value'])
    if 'children' in d:
        for child in d['children']:
            child_node = dict_to_math_node(child)
            node.add_child(child_node)
    return node


def list_to_math_tree(l):
    return dict_to_math_node(l[0])
