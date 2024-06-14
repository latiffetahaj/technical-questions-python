import unittest
from __078__spiral_matrix import spiral_matrix

class TestSpiralMatrix(unittest.TestCase):
    def test_spiral_matrix(self):
        self.assertEqual([1,2,3,6,9,8,7,4,5], spiral_matrix([[1,2,3],
                                                            [4,5,6],
                                                            [7,8,9]]))

        self.assertEqual([1], spiral_matrix([[1]]))

        self.assertEqual([1,2,3], spiral_matrix([[1,2,3]]))

        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], spiral_matrix([[1, 2, 3, 4],
                                                                                                                [14, 15, 16, 5],
                                                                                                                [13, 20, 17, 6],
                                                                                                                [12, 19, 18, 7],
                                                                                                                [11, 10, 9, 8]]))

if __name__ == '__main__':
    unittest.main()