import unittest
from tree import Tree


class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()

    def test_add_child(self):
        self.tree.set_val('+')
        self.assertEqual(self.tree.get_val(), '+')

