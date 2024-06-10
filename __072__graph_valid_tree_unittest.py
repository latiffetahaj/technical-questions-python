import unittest
from __072__graph_valid_tree import is_graph_valid_tree

class TestGraphValidTree(unittest.TestCase):

    def test_graph_valid_tree(self):
        self.assertFalse(is_graph_valid_tree(4, [[0, 1], [0, 3], [1, 2], [2, 3]]))

        self.assertTrue(is_graph_valid_tree(5, [[0, 1], [0, 2], [2, 3], [2, 4]]))


if __name__ == '__main__':
    unittest.main()