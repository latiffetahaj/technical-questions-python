import unittest
from __085__meeting_rooms import can_attend_meetings

class TestCanAttendMeetings(unittest.TestCase):
    def test_attend_meetings(self):
        self.assertTrue(can_attend_meetings([[1, 2], [2, 3], [5, 6]]))
        self.assertFalse(can_attend_meetings([[1, 3], [2, 4]]))
        self.assertTrue(can_attend_meetings([[1,2]]))


if __name__ == '__main__':
    unittest.main()