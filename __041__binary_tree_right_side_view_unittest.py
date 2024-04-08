import unittest
from __000__binary_tree_implementation import BinaryTree
from __041__binary_tree_right_side_view import binary_tree_right_side_view

class TestBinaryTreeRightSideView(unittest.TestCase):
    def setUp(self):
        self.tree_1 = BinaryTree()
        self.tree_1.list_to_binary_tree([10,8,20,6,9,None,None])

                #      10
                #      / \
                #     /   \
                #    /     \
                #   8      20
                #  / \
                # 6   9
                #

    def test_right_side_view(self):
        root = self.tree_1.get_root()

        self.assertEqual([10,20,9],binary_tree_right_side_view(root))


if __name__ == '__main__':
    unittest.main()
