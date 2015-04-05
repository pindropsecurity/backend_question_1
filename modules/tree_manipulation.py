import logging
from operator import add, sub, mul, div
from stack import Stack
from tree import Tree
from custom_exceptions import TreeManipulationError, InvalidInput, EvaluationError

operator_map = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

opening_parenthesis = ('(', )
closing_parenthesis = (')', )
parenthesis_map = dict(zip(opening_parenthesis, closing_parenthesis))

def filter_exp_list(exp):
    """
    filter expression string and return a list with all operands, operators and parenthesis
    """
    exp_list = []
    operand = []

    for token in exp:
        if not token.strip():
            continue
        elif token == '(':
            exp_list.append(token)
        elif token in ('+', '-', '*', '/', ')'):
            if operand:
                exp_list.append(''.join(operand))
            exp_list.append(token)
            operand = []
        else:
            operand.append(token)
    
    if operand:
        exp_list.append(''.join(operand))

    # add a outer closed parenthesis
    exp_list.insert(0, '(')
    exp_list.append(')')

    return exp_list


def validate_math_exp(exp):
    """
    this method will check if all opening parenthesis has a corresponding closing parenthesis
    """
    stack = Stack()

    for token in exp:
        if token in opening_parenthesis:
            stack.push(token)
        elif token in closing_parenthesis and parenthesis_map[stack.top()] == token:
            stack.pop()

    return stack.size() == 0


def build_tree(math_exp_string):
    """
    This method is used to build a tree from given input mathematical expression.
    Following consideration has been taken
    1. higher order operations are given with complete parenthesis ex. 1 - (2*3)
    2. add left and right parenthesis if not given ex. (1 - (2 * 3))
    3. print error message for any exception

    """
    if not validate_math_exp(math_exp_string):
        raise InvalidInput('Validation Error, one or more parenthesis are not closed properly')
    
    exp_list = filter_exp_list(math_exp_string)
    stack = Stack()
    current_node = Tree()

    for token in exp_list:

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
                current_node.set_val(float(token))
            except ValueError, e:
                logging.info(e.message)
                current_node.set_val(token)
            current_node = stack.pop()

    return current_node


def do_math_operation(op, left_value, right_value):
    try:
        return op(left_value, right_value)
    except (TypeError, ValueError, ZeroDivisionError, FloatingPointError) as err:
        raise EvaluationError(err)


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
        'A + (  B * C )  ',
        '1 - 2.0 - 3',
        '1 - 2.5 - 3 + (4 * 5) - 2',
        '(2 * 5.5) - (2.0 / 2) + 3'
    ]

    for input_string in input_string_list:
        try:
            root_node = build_tree(input_string)
            print 'Evaluate (%s) = %0.2f' % (input_string, evaluate(root_node))
        except TreeManipulationError, e:
            print e.message
