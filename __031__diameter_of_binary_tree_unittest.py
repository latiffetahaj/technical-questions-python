import unittest
from __031__diameter_of_binary_tree import diameter_binary_tree
from __000__binary_tree_implementation import BinaryTree

class TestDiameterBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree_1 = BinaryTree()
        self.tree = BinaryTree()

        self.tree.list_to_binary_tree([1,2,3,4,5])
        self.tree_1.list_to_binary_tree([1,2])


    def test_diameter_binary_tree(self):
        root = self.tree.get_root()
        root_1 = self.tree_1.get_root()

        self.assertEqual(3,diameter_binary_tree(root))
        self.assertEqual(1,diameter_binary_tree(root_1))


if __name__ == '__main__':
    unittest.main()