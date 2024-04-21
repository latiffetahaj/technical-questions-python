import unittest
from __055__coin_change import coin_change

class TestCoinChange(unittest.TestCase):

    def test_coin_change(self):
        self.assertEqual(3, coin_change([1,2,5], 11))

        self.assertEqual(-1, coin_change([2,3], 1))

        self.assertEqual(2, coin_change([1,2,4,5],8))



if __name__ == '__main__':
    unittest.main()