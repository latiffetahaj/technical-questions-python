import unittest
from __063__kth_largest_element_in_stream import KthLargest

class TestKthLargest(unittest.TestCase):
    def setUp(self):
        self.kth_largest = KthLargest(2, [3,4,1,2,5])


    def test_add(self):
        # Adding 1 to the stream.
        # The stream in sorted order is 1,1,2,3,4,5
        # And the second largest is 4.
        self.assertEqual(4, self.kth_largest.add(1))

        # The stream in sorted order is 1,1,2,3,4,5, 6
        # And the second largest is 5.
        self.assertEqual(5, self.kth_largest.add(8))


if __name__ == '__main__':
    unittest.main()