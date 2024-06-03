import unittest
from __062__single_number import single_number

class TestSingleNumber(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(3, single_number([1,2,3,1,2]))
        self.assertEqual(1, single_number([1]))
        self.assertEqual(0, single_number([10,20,20,10,0]))



if __name__ == '__main__':
    unittest.main()
