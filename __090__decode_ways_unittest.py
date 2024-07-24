import unittest
from __090__decode_ways import num_decodings

class TestNumDecodings(unittest.TestCase):
    def test_num_decodings(self):
        self.assertEqual(4, num_decodings('2612'))
        self.assertEqual(0, num_decodings('000'))
        self.assertEqual(1, num_decodings('10'))





if __name__ == '__main__':
    unittest.main()