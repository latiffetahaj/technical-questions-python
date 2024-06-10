import unittest
from __076__nr_connected_components_graph import count_components

class TestCountComponents(unittest.TestCase):
    def test_count_components(self):
        self.assertEqual(1, count_components(3,[[0,1],[0,2]]))
        self.assertEqual(2, count_components(6,[[0,1],[1,2],[2,3],[4,5]] ))


if __name__ == '__main__':
    unittest.main()