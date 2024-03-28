import unittest
from __040__binary_tree_max_path_sum import max_path_sum
from __000__binary_tree_implementation import BinaryTree

class TestMaxPathSum(unittest.TestCase):
    def setUp(self):
        self.tree_1 = BinaryTree()

        self.tree_1.list_to_binary_tree([-10,9,20,None,None,15,7])
        #  -10
        #   / \
        #  9  20
        #     / \
        #    15  7

    def test_max_path_sum(self):
        root = self.tree_1.get_root()
        self.assertEqual(42, max_path_sum(root))




if __name__ == '__main__':
    unittest.main()

