import unittest
from __075__course_schedule import can_finish


class TestCourseSchedule(unittest.TestCase):
    def test_course_schedule(self):
        self.assertTrue(can_finish(2, [[1,0]]))
        self.assertFalse(can_finish(2, [[1,0], [0,1]]))


if __name__ == '__main__':
    unittest.main()