import unittest
from __20__buy_sell_stock import max_profit


class TestBuySellStock(unittest.TestCase):
    def test_profit_found(self):
        self.assertEqual(5, max_profit([7,1,5,3,6,4]))

    def test_profit_not_found(self):
        self.assertEqual(0, max_profit([7,6,4,3,1]))



if __name__ == '__main__':
    unittest.main()