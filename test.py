#!/usr/bin/python

from nodefactory import list_to_math_tree, math_tree_calculator, node_pretty_print, create_random_mathnodetree


def unittest(l, expected_result):
    node_tree = list_to_math_tree(l)
    node_pretty_print(node_tree)
    print '---'
    total = math_tree_calculator(node_tree)
    print 'Total: {}'.format(total)
    print 'Expected total: {}'.format(expected_result)
    assert total == expected_result
    print '---------'


test_1_list = [
    {
        'value': '*',
        'children': [
            {
                'value': 3
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
    """Normal, 2 levels deep"""
    unittest(test_1_list, 42)


test_2_list = [
    {
        'value': '-',
        'children': []
    }
]


def test_2():
    """Missing children"""
    unittest(test_2_list, None)


test_3_list = [
    {
        'value': '+',
        'children': [
            {
                'value': '*'
            }
        ]
    }
]


def test_3():
    """Non-numeric value in leaf node"""
    unittest(test_3_list, None)


test_4_list = [
    {
        'value': '*',
        'children': [
            {
                'value': 3,
            },
            {
                'value': 5,
                'children': [
                    {
                        'value': 6
                    },
                    {
                        'value': 9
                    },
                    {
                        'value': '/',
                        'children': [
                            {
                                'value': 8
                            }
                        ]
                    }
                ]
            },
            {
                'value': '+',
                'children': [
                    {
                        'value': 4
                    },
                    {
                        'value': 2
                    }
                ]
            },
            {
                'value': 2,
            },
        ]
    }
]


def test_4():
    """Children in numeric nodes"""
    unittest(test_4_list, 180)


test_5_list = [
    {
        'value': '+',
        'children': [
            {
                'value': 2.0
            },
            {
                'value': '*',
                'children': [
                    {
                        'value': 2
                    },
                    {
                        'value': '+',
                        'children': [
                            {
                                'value': 1
                            },
                            {
                                'value': 2
                            }
                        ]
                    }
                ]
            },
            {
                'value': '/',
                'children': [
                    {
                        'value': 5.0
                    },
                    {
                        'value': 2
                    }
                ]
            },
            {
                'value': '-',
                'children': [
                    {
                        'value': 10
                    },
                    {
                        'value': 5
                    }
                ]
            }
        ]
    }
]


def test_5():
    """Every operator"""
    unittest(test_5_list, 15.5)


test_6_list = [
    {
        'value': '+',
        'children': [
            {
                'value': '+',
                'children': [
                    {
                        'value': '+',
                        'children': [
                            {
                                'value': '+',
                                'children': [
                                    {
                                        'value': 10
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                'value': '+',
                'children': [
                    {
                        'value': '+',
                        'children': [
                            {
                                'value': 4
                            }
                        ]
                    }
                ]
            }
        ]
    }
]


def test_6():
    """Lots of levels"""
    unittest(test_6_list, 14)


def do_optional_test():
    do_test = raw_input('Generate random tree and calculate? (y/n) ')
    if do_test == 'y':
        random_node = create_random_mathnodetree()
        node_pretty_print(random_node)
        total = math_tree_calculator(random_node)
        print 'Total: {}'.format(total)


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    do_optional_test()
    
