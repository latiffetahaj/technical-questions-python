import unittest
from __000__binary_tree_implementation import BinaryTree
from __029__invert_binary_tree import invert_binary_tree

from drawtree import draw_level_order

class TestInverBinaryTree(unittest.TestCase):
    def setUp(self):
        self.binary_tree = BinaryTree()
        self.binary_tree.list_to_binary_tree([2,1,3])

        draw_level_order('{2,1,3}')

    def test_invert_binary_tree(self):
        root = self.binary_tree.get_root()

        invert_binary_tree(root)

        self.assertEqual([2,3,1], self.binary_tree.binary_tree_to_list())

        draw_level_order('{2,3,1}')



if __name__ == '__main__':
    unittest.main()
