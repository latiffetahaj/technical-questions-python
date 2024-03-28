import unittest
from __000__binary_tree_implementation import BinaryTree
from __039__k_th_smallest_element_BST import kth_smallest_iterative_dfs
class TestKthSmallest(unittest.TestCase):
    def setUp(self):
        self.tree_1 = BinaryTree()
        self.tree_1.list_to_binary_tree([10,8,20,6,9,12,22])

                #      10
                #      / \
                #     /   \
                #    /     \
                #   8      20
                #  / \     / \
                # 6   9   /   \
                #        12   22

    def test_kth_smallest(self):
        root = self.tree_1.get_root()

        self.assertEqual(12,kth_smallest_iterative_dfs(root,5))



if __name__ == '__main__':
    unittest.main()

