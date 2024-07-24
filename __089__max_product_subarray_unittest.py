import unittest
from __089__max_product_subarray import max_product_subarray

class TestMaxProductSubArray(unittest.TestCase):
    def test_max_product_subarray(self):
        self.assertEqual(6, max_product_subarray([2,3,-2,4]))
        self.assertEqual(-2, max_product_subarray([-2]))
        self.assertEqual(0, max_product_subarray([-2, 0]))

if __name__ == '__main__':
    unittest.main()