import unittest
from __8__encode_decode import encode, decode

class TestEncodeDecode(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(["123","456","789","10","11"],decode(encode(["123","456","789","10","11"])))

    def test_with_spaces(self):
        self.assertEqual(["Strings with spaces are tricky","Another one with spaces","This also has spaces"],
                        decode(encode(["Strings with spaces are tricky","Another one with spaces","This also has spaces"])))

    def test_empty(self):
        self.assertEqual([],decode(encode([])))
        self.assertEqual([""],decode(encode([""])))

    def test_short_inputs(self):
        self.assertEqual(["we","say",":","yes"], decode(encode(["we","say",":","yes"])))
        self.assertEqual(['###'], decode(encode(['###'])))



if __name__ == '__main__':
    unittest.main()