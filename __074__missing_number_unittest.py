import unittest
from __074__missing_number import missing_number

class TestMissingNumber(unittest.TestCase):
    def test_missing_number(self):
        self.assertEqual(2, missing_number([0,1,3]))
        self.assertEqual(3, missing_number([0,1,2]))
        self.assertEqual(0, missing_number([2,1]))



if __name__ == '__main__':
    unittest.main()