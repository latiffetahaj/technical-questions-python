import unittest
from __003__two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test(self):
        self.assertEqual([1,2], two_sum([3,2,4],6))
        self.assertEqual([0,1], two_sum([2,7,11,15],9))
        self.assertEqual([0,3], two_sum([-2,0,2,10],8))


if __name__=='__main__':
	unittest.main()