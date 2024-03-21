import unittest
from __000__binary_tree_implementation import BinaryTree
from __032__same_binary_tree import same_tree

class TestSameTree(unittest.TestCase):
    def setUp(self):
        self.tree_1 = BinaryTree()
        self.tree_2 = BinaryTree()
        self.tree_3 = BinaryTree()

        self.tree_1.list_to_binary_tree([1,2,10,12])
        self.tree_2.list_to_binary_tree([1,2,3,4,5])
        self.tree_3.list_to_binary_tree([1,2,10,12])


    def test_same_tree(self):
        root_1 = self.tree_1.get_root()
        root_2 = self.tree_2.get_root()
        root_3 = self.tree_3.get_root()

        self.assertTrue(same_tree(root_1,root_3))
        self.assertFalse(same_tree(root_2,root_3))

        #two null trees are the same
        self.assertTrue(same_tree(None,None))


if __name__ == '__main__':
    unittest.main()