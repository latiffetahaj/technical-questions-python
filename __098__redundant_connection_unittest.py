import unittest
from __098__redundant_connection import find_redundant_connection

class TestRedundantConnection(unittest.TestCase):
    def test_redundant_connection(self):
        self.assertEqual([2,3], find_redundant_connection([[1,2],[1,3],[2,3]]))

        self.assertEqual([1,4], find_redundant_connection([[1,2],[2,3],[3,4],[1,4],[1,5]]))

        self.assertEqual([2,8], find_redundant_connection([[2,7], [7, 1], [7, 8], [8, 4], [8, 6], [6, 3], [2, 8], [3, 4]]))

if __name__ == '__main__':
    unittest.main()