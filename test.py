#!/usr/bin/python

from nodefactory import list_to_math_tree, math_tree_calculator, node_pretty_print

def unittest(l, expected_result):
    node_tree = list_to_math_tree(l)
    node_pretty_print(node_tree)
    print '---'
    total = math_tree_calculator(node_tree)
    print 'Total: {}'.format(total)
    print 'Expected total: {}'.format(expected_result)
    assert total == expected_result

test_1_list = [
    {
        'value': '*',
        'children': [
            {
                'value': 3,
                'children': []
            },
            {
                'value': 2
            },
            {
                'value': '+',
                'children': [
                    {
                        'value': 2
                    },
                    {
                        'value': 5
                    }
                ]
            }
        ]
    }
]

def test_1():
    unittest(test_1_list, 42)


if __name__ == '__main__':
    test_1()