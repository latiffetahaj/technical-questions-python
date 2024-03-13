import unittest
from __006__product_except_self import product_except_self

class TestProductExceptSelf(unittest.TestCase):
    def test_positive_inputs(self):
        self.assertEqual([24,12,8,6],product_except_self([1,2,3,4]))
        self.assertEqual([2,1], product_except_self([1,2]))


    def test_negative_inputs(self):
        self.assertEqual([0,0,9,0,0],product_except_self([-1,1,0,-3,3]))

    def test_all_zeros(self):
        self.assertEqual([0,0,0],product_except_self([0,0,0]))



if __name__ == '__main__':
    unittest.main()