import unittest
from __061__nr_of_1_bits import hamming_weight

class TestHammingWeight(unittest.TestCase):

    def test_hamming_weight(self):
        self.assertEqual(3, hamming_weight(0b110001))
        self.assertEqual(1, hamming_weight(0b1000000000))
        self.assertEqual(5, hamming_weight(0b10011011))
        self.assertEqual(0, hamming_weight(0b00000))


if __name__ == '__main__':
    unittest.main()