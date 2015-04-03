import unittest
import tree

class TestTreeFunction(unittest.TestCase):
    def test_basicPlus(self):
        self.assertEqual(tree.tree('+ 1 2'), 3, 'incorrect addition of + 1 2')

    def test_basicMinus(self):
        self.assertEqual(tree.tree('- 1 2'), -1, 'incorrect addition of + 1 2')

    def test_basicMult(self):
        self.assertEqual(tree.tree('* 4 2'), 8, 'incorrect addition of + 1 2')

    def test_basicDiv(self):
        self.assertEqual(tree.tree('/ 4 2'), 2, 'incorrect addition of + 1 2')

    def test_badOperator(self):
        with self.assertRaises(AssertionError):
            tree.operate('%', 4, 2)

    def test_moreThan2(self):
        self.assertEqual(tree.tree('+ 1 2 3 4'), 10, 'incorrect addition of + 1 2')

unittest.main()
