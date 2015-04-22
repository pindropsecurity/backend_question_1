import unittest
from modules.tree import Tree


class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()

    def test_add_child(self):
        self.tree.set_val('+')
        self.assertEqual(self.tree.get_val(), '+')
        
        self.tree.add_child('4')
        self.tree.add_child('5')
        self.assertEqual(self.tree.get_newborn_child().get_val(), '5')

