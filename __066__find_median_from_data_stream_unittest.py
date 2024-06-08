import unittest
from __066__find_median_from_data_stream import MedianFinder

class TestMedianFinder(unittest.TestCase):
    def setUp(self):
        self.median_finder = MedianFinder()

        self.median_finder.addNum(2)
        self.median_finder.addNum(1)
        self.median_finder.addNum(10)


    def test_median_finder(self):
        self.assertEqual(2, self.median_finder.findMedian())

        self.median_finder.addNum(3)
        self.assertEqual(2.5, self.median_finder.findMedian())


if __name__ == '__main__':
    unittest.main()
