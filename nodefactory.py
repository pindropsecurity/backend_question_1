
class InvalidMathNode(Exception):
    pass


class Node(list):
    """
    A Node is a nothing more than a list that tracks values
    """
    def __init__(self, value, *args, **kwargs):
        self.value = value
        super(Node, self).__init__(*args, **kwargs)


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


def math_tree_calculator(node, total=None, math_mode=None):
    """Recursively loop over an entire 'math node tree', calculate its total value"""
    def _get_total(math_mode, left, right):
        if left == None:
            return right#: Happens if there's no total yet
        elif right == None:
            return left#: Can happen with malformed tree
        total = left
        if math_mode == '-':
            total -= right
        elif math_mode == '+':
            total += right
        elif math_mode == '/':
            total /= float(right)
        elif math_mode == '*':
            total *= right
        return total
    
    if node.nodetype == 'operator':
        for child in node:
            if child.nodetype == 'number':
                total = _get_total(node.value, total, child.value)
            else:
                total = _get_total(node.value, total, math_tree_calculator(child))
    else:
        total = _get_total(math_mode, total, node.value)
    return total


def node_pretty_print(node, indent=0):
    """Prints out nodes for nice display during testing"""
    optional_twig = ''
    optional_branch = ''
    rjust_indent = indent
    if indent:
        rjust_indent = indent * 4
        optional_twig = ' {'
    if len(node):
        optional_branch = '\\'
    print '{}{}'.format(optional_twig, node.value).rjust(rjust_indent, ' ')
    if optional_branch:
        print optional_branch.rjust(rjust_indent + 2)
    for child in node:
        node_pretty_print(child, indent + 1)


def dict_to_math_node(d):
    """Converts dict representations of nodes into actual Node objects"""
    node = MathNode(d['value'])
    if 'children' in d:
        for child in d['children']:
            child_node = dict_to_math_node(child)
            node.append(child_node)
    return node


def list_to_math_tree(l):
    """Wrapper for dict_to_math_node, allows creation of lists that more resemble our actual node trees"""
    return dict_to_math_node(l[0])


def create_random_mathnodetree(depth=0):
    """Creates random node and calculates, for fun, and testing unexpected situations"""
    import random
    do_operator = False
    if depth == 0:
        do_operator = True
    else:
        base_chance = 60
        adjusted_chance = base_chance - (depth * 2)
        randint = random.randint(0, 100)
        if randint <= adjusted_chance:
            do_operator = True
    
    if do_operator:
        value = random.choice(['-', '+', '/', '*'])
    else:
        value = random.randint(1, 40)
    node = MathNode(value=value)
    
    if do_operator:
        if depth == 0:
            #: Make sure we at least go one deep
            child_length = random.randint(1, 6)
        else:
            child_length = random.randint(0, 5)
        for i in range(child_length):
            node.append(create_random_mathnodetree(depth=depth+1))
    return node
