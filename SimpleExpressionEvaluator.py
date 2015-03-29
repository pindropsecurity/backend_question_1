#!/usr/bin/python3

from fractions import Fraction
from expression_graph.expression_graph import ExpressionGraph, \
    LeftmostEvaluatingExpressionGraph, EmptyExpressionException, \
    IncompleteExpressionException
from expression_graph.operator import Operator

def simpleExpressionEvaluator(expression):
    expr_strs = expression.split(' ')
    expr_nodes = list()
    if len(expr_strs) > 0 and expression != '':
        for n in expr_strs:
            node = None
            if n in Operator.operators:
                node = n
            else:
                try:
                    node = int(n)
                except ValueError as e:
                    try:
                        node = float(n)
                    except ValueError as e2:
                        print('{0} is not a valid value for the expression parser'.format(n))
            expr_nodes.append(node)
    print(expr_nodes)
    return LeftmostEvaluatingExpressionGraph(*expr_nodes)


if __name__ == '__main__':
    print(simpleExpressionEvaluator('5').eval())
    print(simpleExpressionEvaluator('2 + 2').eval())
    print(simpleExpressionEvaluator('2 + 2.5').eval())
    print(simpleExpressionEvaluator('2 + 2.5 * 23 / 42 - 8').eval())
    print(simpleExpressionEvaluator('4 / 7').eval())
    print(simpleExpressionEvaluator('4 / 7.1').eval())
    print(simpleExpressionEvaluator('4 / 2').eval())
    
    try:
       print(simpleExpressionEvaluator('').eval())
    except EmptyExpressionException as e:
        print('empty expression')
    
    try:
        print(simpleExpressionEvaluator('4 /').eval())
    except IncompleteExpressionException as e:
        print('incomplete expression')

    
