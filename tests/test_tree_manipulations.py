import unittest
from modules.tree_manipulation import build_tree, evaluate
from modules.tree import Tree
from modules.custom_exceptions import InvalidInput, EvaluationError

class TestBuildTree(unittest.TestCase):
    def setUp(self):
        self.input_string_list = [
            ('1 - 2 - 3', -4.00),         
            ('1 - 2 - 3 + (4 * 5) - 2', 14.00),
            ('(2 * 5) - (2 / 2) + 3', 12.00),
        ]


    def test_build_tree(self):
        for input_string_tup in self.input_string_list:
            input_string, _ = input_string_tup
            root_node = build_tree(input_string)
            self.assertIsInstance(root_node, Tree)
            self.assertIsNotNone(root_node.get_val())


    def test_invalid_exp(self):
        input_string_list = ('1 + (3*5', '(2 * 3 - 1')
        for input_string in input_string_list:
            with self.assertRaises(InvalidInput):
                build_tree(input_string)

    def test_evaluate(self):
        for input_string_tup in self.input_string_list:
            input_string, expected_result = input_string_tup
            root_node = build_tree(input_string)
            self.assertEqual(evaluate(root_node), expected_result)


    def test_evaluate_divide_by_zero(self):
        """
        In case of divide by zero it should return None for that operator node
        """
        input_string_list = ('2 / 0', '1 + (2 / 0)')
        for input_string in input_string_list:
            root_node = build_tree(input_string)
            with self.assertRaises(EvaluationError):
                evaluate(root_node)


    def test_evaluate_non_digit_token(self):
        input_string = 'A + (B * C)'
        root_node = build_tree(input_string)
        with self.assertRaises(EvaluationError):
            evaluate(root_node)

