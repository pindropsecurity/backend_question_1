from operator import add, sub, mul, div
from stack import Stack
from tree import Tree

operator_map = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}


def build_tree(math_exp_string):
    """
    This method is used to build a tree from given input mathematical expression.
    
    Following consideration has been taken
    1. higher order operations are given with complete parenthesis ex. 1 - (2*3)
    2. add left and right parenthesis if not given ex. (1 - (2 * 3))
    3. for divide by zero raise a nice error message

    """
    stack = Stack()
    current_node = Tree()

    if not math_exp_string.startswith('(') and not math_exp_string.endswith(')'):
        math_exp_string = '(' + math_exp_string + ')'

    for token in math_exp_string:
        if not token.strip():
            continue

        if token == '(':
            current_node.add_child()
            stack.push(current_node)
            current_node = current_node.get_newborn_child()

        elif token == ')':
            if stack.size():
                current_node = stack.pop()

        elif token in operator_map.keys():
            if current_node.get_val():
                if current_node.get_val() == token:
                    current_node.add_child()
                    stack.push(current_node)
                    current_node = current_node.get_newborn_child()
                else:
                    parent = Tree(token)
                    parent.update_child(current_node)
                    parent.add_child()
                    stack.push(parent)
                    current_node = parent.get_newborn_child()
            else:
                current_node.set_val(token)
                current_node.add_child()
                stack.push(current_node)
                current_node = current_node.get_newborn_child()

        else:
            try:
                current_node.set_val(int(token))
            except ValueError, e:
                current_node.set_val(token)
            current_node = stack.pop()

    return current_node


def do_math_operation(op, left_value, right_value):
    try:
        return op(left_value, right_value)
    except (TypeError, ValueError) as err:
        print err.message
        return 0
    except ZeroDivisionError, err:
        print err.message


def evaluate(node):
    """
    tree traversal method to evaluate the expression
    """

    children = node.get_children()
    if children:
        result = do_math_operation(
            operator_map[node.get_val()], 
            evaluate(children[0]), 
            evaluate(children[1])
        )
        for child in children[2:]:
            return do_math_operation(
                operator_map[node.get_val()], 
                result, 
                evaluate(child)
            )
        return result
    else:
        return node.get_val()


if __name__ == '__main__':
    input_string_list = [
        '1 - 2 - 3',         
        '1 - 2 - 3 + (4 * 5) - 2',
        '(2 * 5) - (2 / 2) + 3'
    ]
    
    for input_string in input_string_list:
        root_node = build_tree(input_string)
        print 'root val ', root_node.get_val()
        print '%s = %d' % (input_string, evaluate(root_node))
