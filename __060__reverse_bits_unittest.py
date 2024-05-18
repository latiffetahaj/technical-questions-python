import unittest
from __060__reverse_bits import reverse_bits

class TestReverseBits(unittest.TestCase):

    def test_reverse_bits(self):
        self.assertEqual('0b10011', reverse_bits(0b11001))

        self.assertEqual('0b1', reverse_bits(0b1))

        self.assertEqual('0b100111', reverse_bits(0b111001))


if __name__ == '__main__':
    unittest.main()