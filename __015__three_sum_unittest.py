import unittest
from __15__three_sum import three_sum

class TestThreeSum(unittest.TestCase):
    def test_duplicate_solutions(self):
        self.assertEqual([[0,0,0]], three_sum([0,0,0,0,0]))
        self.assertEqual([[-3,1,2]], three_sum([-3,0,2,2,2,1]))
    def test_empty(self):
        self.assertEqual([], three_sum([0,1,2]))
        self.assertEqual([],three_sum([0,-3,2]))



if __name__ == '__main__':
    unittest.main()