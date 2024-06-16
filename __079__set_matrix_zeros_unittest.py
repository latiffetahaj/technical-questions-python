import unittest
from __079__set_matrix_zeros import set_matrix_zeros

class TestMatrixZeros(unittest.TestCase):
    def setUp(self):
        self.input_1 = [[1,1,1],
                        [1,0,1],
                        [1,1,1]]

        self.output_1 = [[1,0,1],
                        [0,0,0],
                        [1,0,1]]

        self.input_2 = [[0,1,2,0],
                        [3,4,5,2],
                        [1,3,1,5]]


        self.output_2 = [[0,0,0,0],
                        [0,4,5,0],
                        [0,3,1,0]]


    def test_matrix_zeros(self):
        self.assertEqual(self.output_1, set_matrix_zeros(self.input_1))

        self.assertEqual(self.output_2, set_matrix_zeros(self.input_2))



if __name__ == '__main__':
    unittest.main()

