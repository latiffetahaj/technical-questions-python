import unittest
from __000__binary_tree_implementation import BinaryTree
from __037__validate_binary_search_tree import is_valid_BST


class TestValidBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.tree_1 = BinaryTree()
        self.tree_2 = BinaryTree()

        self.tree_1.list_to_binary_tree([10,8,20,6,9,12,22])

                #      10
                #      / \
                #     /   \
                #    /     \
                #   8      20
                #  / \     / \
                # 6   9   /   \
                #        12   22

        self.tree_2.list_to_binary_tree([5,4,6,None,None,3,7])

                #     5
                #    / \
                #   4   6
                #      / \
                #     3   7

    def test_is_valid_BST(self):
        root_1 = self.tree_1.get_root()
        root_2 = self.tree_2.get_root()

        self.assertTrue(is_valid_BST(root_1))

        self.assertFalse(is_valid_BST(root_2))

if __name__ == '__main__':
    unittest.main()