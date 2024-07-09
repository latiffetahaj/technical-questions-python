import unittest
from __081_sum_of_two_integers import sum_two_integers

class TestSumTwoIntegers(unittest.TestCase):
    def test_sum_two_integers(self):
        self.assertEqual(-1, sum_two_integers(-2, 1))
        self.assertEqual(0, sum_two_integers(3, -3))
        self.assertEqual(-5, sum_two_integers(-2, -3))
        self.assertEqual(6, sum_two_integers(2, 4))


if __name__ == '__main__':
    unittest.main()