import unittest
from __100__k_closest_points_to_origin import k_closest

class TestKClosest(unittest.TestCase):
    def test_k_closest(self):
        self.assertEqual([[-2,2]], k_closest([[1,3],[-2,2]], 1))

        self.assertEqual([[3,3],[-2,4]], k_closest([[3,3],[5,-1],[-2,4]], 2))

        self.assertEqual([[0,0]], k_closest([[1,2], [-2, 2], [2,3], [0,0]], 1))

if __name__ == '__main__':
    unittest.main()