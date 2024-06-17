import unittest
from __080__counting_bits import counting_bits

class TestCountingBits(unittest.TestCase):
    def test_counting_bits(self):
        self.assertEqual([0,1,1], counting_bits(2))
        self.assertEqual([0,1,1,2,1,2], counting_bits(5))
        self.assertEqual([0], counting_bits(0))


if __name__ == '__main__':
    unittest.main()