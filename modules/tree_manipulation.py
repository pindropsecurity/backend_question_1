from operator import add, sub, mul, div
from stack import Stack
from tree import Tree


def build_tree(math_exp_string):
    stack = Stack()
    current_node = Tree()

    # expecting the math exp would use parenthesis for higher order operator i.e. */
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

        elif token in ('+', '-', '*', '/'):
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
                print 'Cannot convert into int:', e.message, ' setting 0 instead'
                current_node.set_val(0)
            current_node = stack.pop()

    return current_node

operation_map = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}


def evaluate(node):
    children = node.get_children()
    if children:
        first_child_val = evaluate(children[0])
        second_child_val = evaluate(children[1])
        result = operation_map[node.get_val()](first_child_val, second_child_val)
        for child in children[2:]:
            child_val = evaluate(child)
            return operation_map[node.get_val()](result, child_val)
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
