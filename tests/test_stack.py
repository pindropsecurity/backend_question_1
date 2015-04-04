import unittest
from modules.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push('foo')
        self.assertEqual(self.stack.size(), 1)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), None)
