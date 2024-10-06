import unittest
from __097__course_schedule_II import find_order

class TestFindOrder(unittest.TestCase):

    def test_find_order(self):

        self.assertEqual([0,1], find_order(2, [[1, 0]]))

        self.assertEqual([0,1,2,3], find_order(4, [[1,0],[2,0],[3,1],[3,2]]))

        self.assertEqual([0], find_order(1, []))


if __name__ == '__main__':
    unittest.main()