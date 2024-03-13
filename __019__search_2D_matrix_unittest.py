import unittest
from __19__search_2D_matrix import search_2D_matrix

class TestSearch2DMatrix(unittest.TestCase):
    def test_target_found(self):
        self.assertTrue(search_2D_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
        self.assertTrue(search_2D_matrix([[1,2,3,4],[7,8,9,10],[20,30,40,50]], 50))

    def test_target_not_found(self):
        self.assertFalse(search_2D_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))
        self.assertFalse(search_2D_matrix([[1,2,3,4],[7,8,9,10],[20,30,40,50]], -3))



if __name__ == '__main__':
    unittest.main()