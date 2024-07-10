import unittest
from __082__insert_interval import insert_interval

class TestInsertInterval(unittest.TestCase):
    def test_insert_interval(self):
        self.assertEqual([[1,5],[6,9]], insert_interval([[1,3],[6,9]], [2,5]))
        self.assertEqual([[1,2], [3,4]], insert_interval([[3,4]], [1,2]))
        self.assertEqual([[6,7], [8,9]], insert_interval([[6,7]], [8,9]))


if __name__ == '__main__':
    unittest.main()