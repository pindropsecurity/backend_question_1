import unittest
import tree

class TestTreeFunction(unittest.TestCase):
    def test_basicPlus(self):
        self.assertEqual(tree.tree('+ 1 2'), 3, 'incorrect addition of + 1 2')

    def test_basicMinus(self):
        self.assertEqual(tree.tree('- 1 2'), -1, 'incorrect subtraction of - 1 2')

    def test_basicMult(self):
        self.assertEqual(tree.tree('* 4 2'), 8, 'incorrect multiplication of * 4 2')

    #def test_basicDiv(self):
        #self.assertEqual(tree.tree('/ 4 -2'), -2, 'incorrect division of / 4 -2')

    def test_badOperator(self):
        with self.assertRaises(AssertionError):
            tree.operate('%', 4, 2)

    def test_PlusmoreThan2(self):
        self.assertEqual(tree.tree('+ 1 2 3 4'), 10, 'incorrect addition of + 1 2 3 4')

    def test_MinusmoreThan2(self):
        self.assertEqual(tree.tree('- 1 2 3 4'), -8, 'incorrect addition of + 1 2 3 4')

    def test_MultsmoreThan2(self):
        self.assertEqual(tree.tree('* 1 2 3 4'), 24, 'incorrect addition of + 1 2 3 4')

    #def test_DivmoreThan2(self):
        #self.assertEqual(tree.tree('/ 1000 -10 -10'), 10, 'incorrect addition of + 1000 -10 -10')

    def test_PlusHeight2(self):
        self.assertEqual(tree.tree('+ 2 4 + 1 2'), 9, 'incorrect addition of + 1000 -10 -10')

unittest.main()
