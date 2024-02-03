import unittest
from __5__top_k_frequent_elements import top_k_elements

class TestTopKElements(unittest.TestCase):
    def test(self):
        self.assertEqual([3,4], top_k_elements([1,1,1,2,2,3,3,3,3,3,4,4,4,4],2))

    def test_one_element(self):
        self.assertEqual([5],top_k_elements([1,1,5,5,5],1))


if __name__ == '__main__':
    unittest.main()