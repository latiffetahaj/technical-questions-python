import unittest
from __000__binary_tree_implementation import BinaryTree, TreeNode
from __035__lowest_common_ancestor_BST import lca_BST_iterative, lca_BST_recursive
from drawtree import draw_bst

class TestLowestCommonAncestor(unittest.TestCase):
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




    def test_LCA(self):
        draw_bst([10,8,20,6,9,12,22])
        root = self.tree_1.get_root()

        p = TreeNode(8)
        q = TreeNode(20)
        self.assertEqual(10, lca_BST_recursive(root,p,q))
        self.assertEqual(10, lca_BST_iterative(root,p,q))



if __name__ == '__main__':
    unittest.main()
