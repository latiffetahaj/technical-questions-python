import unittest
from __077__rotate_image import rotate_image_90

class TestRotateImage(unittest.TestCase):
    def setUp(self):
        self.input_1 = [[1,2,3],
                        [4,5,6],
                        [7,8,9]]

        self.output_1 = [[7,4,1],
                        [8,5,2],
                        [9,6,3]]


        self.input_2 = [[5,1,9,11],
                        [2,4,8,10],
                        [13,3,6,7],
                        [15,14,12,16]]

        self.output_2 = [[15,13,2,5],
                        [14,3,4,1],
                        [12,6,8,9],
                        [16,7,10,11]]


    def test_rotate_image(self):
        self.assertEqual(self.output_1, rotate_image_90(self.input_1))

        self.assertEqual(self.output_2, rotate_image_90(self.input_2))



if __name__ == '__main__':
    unittest.main()