import unittest
import tree

class TestTreeFunction(unittest.TestCase):
    def test_basicPlus(self):
        self.assertEqual(tree.tree('+ 1 2'), 3, 'incorrect addition of + 1 2')

    def test_basicMinus(self):
        self.assertEqual(tree.tree('- 1 2'), -1, 'incorrect subtraction of - 1 2')

    def test_basicMult(self):
        self.assertEqual(tree.tree('* 4 2'), 8, 'incorrect multiplication of * 4 2')

    def test_basicDiv(self):
        self.assertEqual(tree.tree('/ 4 2'), 2, 'incorrect division of / 4 -2')

    def test_badOperator(self):
        with self.assertRaises(AssertionError):
            tree.operate('%', 4, 2)

    def test_PlusmoreThan2(self):
        self.assertEqual(tree.tree('+ 1 2 3 4'), 10, 'incorrect addition of + 1 2 3 4')

    def test_MinusmoreThan2(self):
        self.assertEqual(tree.tree('- 1 2 3 4'), -8, 'incorrect addition of + 1 2 3 4')

    def test_MultsmoreThan2(self):
        self.assertEqual(tree.tree('* 1 2 3 4'), 24, 'incorrect addition of + 1 2 3 4')

    def test_DivmoreThan2(self):
        self.assertEqual(tree.tree('/ 1000 10 10'), 10, 'incorrect addition of + 1000 10 10')

    def test_PlusHeight2(self):
        self.assertEqual(tree.tree('+ 2 4 + 1 2'), 9, 'incorrect addition of + 2 4 + 1 2')

    def test_PlusHeight3BalPlusMin(self):
        self.assertEqual(tree.tree('+ 3 + 2 - 3 4'), 4, 'incorrect addition of + + 1 2 + 3 4')

    def test_PlusHeight3LeftBad(self):
        with self.assertRaises(StopIteration):
            tree.tree('+ + + 1 2 3')

    def test_PlusHeight2LeftBad(self):
        with self.assertRaises(StopIteration):
            tree.tree('+ + 1 2')

    def test_PlusHeight2Bal(self):
        with self.assertRaises(StopIteration):
            tree.tree('+ + 1 2 3 + 1 2')

    def test_BadLeaf(self):
        with self.assertRaises(EOFError):
            tree.tree('+ 1 *')

    def test_BadFirstLeaf(self):
        with self.assertRaises(EOFError):
            tree.tree('+ * 1')

unittest.main()
