import unittest
from __000__binary_tree_implementation import BinaryTree
from __033__subtree_of_another_tree import is_sub_tree_BFS, is_sub_tree_DFS

class TestIsSubTree(unittest.TestCase):
    def setUp(self):
        self.tree_1 = BinaryTree()
        self.tree_2 = BinaryTree()
        self.tree_3 = BinaryTree()

        self.tree_1.list_to_binary_tree([1,2,10,12,22])
        self.tree_2.list_to_binary_tree([1,2,3,4,5])
        self.tree_3.list_to_binary_tree([2,12,22])

    def test_is_sub_tree(self):
        root_1 = self.tree_1.get_root()
        root_2 = self.tree_2.get_root()
        root_3 = self.tree_3.get_root()

        self.assertFalse(is_sub_tree_DFS(root_2,root_3))
        self.assertFalse(is_sub_tree_BFS(root_2,root_3))

        self.assertTrue(is_sub_tree_DFS(root_1,root_3))
        self.assertTrue(is_sub_tree_BFS(root_1,root_3))


if __name__ == '__main__':
    unittest.main()