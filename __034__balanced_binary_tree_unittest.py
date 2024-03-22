import unittest
from __000__binary_tree_implementation import BinaryTree
from __034__balanced_binary_tree import is_balanced

class TestIsBalanced(unittest.TestCase):
    def setUp(self):
        self.tree_1 = BinaryTree()
        self.tree_2 = BinaryTree()

        self.tree_1.list_to_binary_tree([1,2,10,12,22])
        self.tree_2.list_to_binary_tree([1,2,None,4,5])


    def test_is_balanced(self):
        root_1 = self.tree_1.get_root()
        root_2 = self.tree_2.get_root()

        self.assertTrue(is_balanced(root_1))
        self.assertFalse(is_balanced(root_2))

        self.assertTrue(is_balanced(None))


if __name__ == '__main__':
    unittest.main()