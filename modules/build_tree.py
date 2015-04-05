from stack import Stack
from tree import Tree

def build_tree(math_exp_string):
    stack = Stack()
    current_node = Tree()

    # expecting the math exp would use parenthesis for higher order operator
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
                stack.pop()

        elif token in ('+', '-', '*', '/'):
            if current_node.get_val():
                if current_node.get_val() == token:
                    current_node.add_child()
                    stack.push(current_node)
                    current_node = current_node.get_newborn_child()
                else:
                    parent = Tree(token)
                    parent.add_child(current_node)
                    parent.add_child()
                    stack.push(parent)
                    current_node = parent.get_newborn_child()
            else:
                current_node.set_val(token)
                current_node.add_child()
                stack.push(current_node)
                current_node = current_node.get_newborn_child()

        else:
            current_node.set_val(token)
            current_node = stack.pop()

    return current_node


if __name__ == '__main__':
    input_string = '1 - 2 - 3'
    root_node = build_tree(input_string)
    print root_node.get_val()
    print root_node.get_newborn_child().get_val()

