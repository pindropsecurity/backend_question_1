import unittest
from modules.tree_manipulation import build_tree, evaluate
from modules.tree import Tree

class TestBuildTree(unittest.TestCase):
    def setUp(self):
        self.input_string_list = [
            ('1 - 2 - 3', -4),         
            ('1 - 2 - 3 + (4 * 5) - 2', 14),
            ('(2 * 5) - (2 / 2) + 3', 12)
        ]


    def test_build_tree(self):
        for input_string_tup in self.input_string_list:
            input_string, _ = input_string_tup
            root_node = build_tree(input_string)
            self.assertIsInstance(root_node, Tree)
            self.assertIsNotNone(root_node.get_val())


    def test_evaluate(self):
        for input_string_tup in self.input_string_list:
            input_string, expected_result = input_string_tup
            root_node = build_tree(input_string)
            self.assertEqual(evaluate(root_node), expected_result)


