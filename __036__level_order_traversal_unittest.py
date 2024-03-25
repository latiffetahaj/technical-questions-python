import unittest
from __000__binary_tree_implementation import BinaryTree, TreeNode
from __036__level_order_traversal import level_order_traversal

class TestLevelOrderTraversal(unittest.TestCase):
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

    def test_level_order_traversal(self):
        root = self.tree_1.get_root()

        self.assertEqual([[10],[8,20],[6,9,12,22]], level_order_traversal(root))

        #testing None root
        self.assertEqual([], level_order_traversal(None))

        #when tree contains only root node
        new_root = TreeNode(2)

        self.assertEqual([[2]],level_order_traversal(new_root))


if __name__ == '__main__':
    unittest.main()