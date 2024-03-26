import unittest
from __038__construct_tree_preorder_inorder import construct_tree, values_preorder
from __000__binary_tree_implementation import BinaryTree

class TestConstructTree(unittest.TestCase):

    def test_construct_tree(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]

        root = construct_tree(preorder,inorder)
        #built a preorder traversal of this tree, then compare with the preorder array


        self.assertEqual(preorder,values_preorder(root))

if __name__ == '__main__':
    unittest.main()




