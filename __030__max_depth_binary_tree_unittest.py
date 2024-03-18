import unittest
from __030__max_depth_binary_tree import max_depth
from __030__max_depth_binary_tree import max_depth_BFS
from __000__binary_tree_implementation import BinaryTree


class TestMaxDepthTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()
        self.tree.list_to_binary_tree([3,9,20,None,None,15,7])


    def test_max_depth(self):
        root = self.tree.get_root()

        self.assertEqual(3,max_depth(root))

        #when node is None
        self.assertEqual(0,max_depth(None))

    def test_max_depth_BFS(self):
        root = self.tree.get_root()

        self.assertEqual(3,max_depth_BFS(root))





if __name__ == '__main__':
    unittest.main()