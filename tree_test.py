import unittest
import tree

class TestTreeFunction(unittest.TestCase):
    def test_hello(self):
        kk = tree.tree('+ 1 2')
        self.assertEqual(tree.tree('+ 1 2'), 3, 'incorrect addition of + 1 2')

unittest.main()
