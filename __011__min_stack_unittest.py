import unittest
from __011__min_stack import MinStack


class TestMinStack(unittest.TestCase):
    def setUp(self):
        self.minStack = MinStack()
        self.minStack.push(2)
        self.minStack.push(3)
        self.minStack.push(-3)

    def test_top(self):
        self.assertEqual(-3,self.minStack.top())

    def test_get_min(self):
        self.assertEqual(-3,self.minStack.getMin())



if __name__ == '__main__':
    unittest.main()