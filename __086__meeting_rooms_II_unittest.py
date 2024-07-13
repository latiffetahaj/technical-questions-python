import unittest
from __086__meeting_rooms_II import min_meeting_rooms, min_meeting_rooms_II

class TestMinMeetingRooms(unittest.TestCase):

    def test_min_meeting_rooms(self):
        self.assertEqual(0, min_meeting_rooms([]))
        self.assertEqual(2, min_meeting_rooms([[0,40],[5,10],[15,20]]))
        self.assertEqual(1, min_meeting_rooms([[4,9]]))


    def test_min_meeting_rooms_II(self):
        self.assertEqual(0, min_meeting_rooms_II([]))
        self.assertEqual(2, min_meeting_rooms_II([[0,40],[5,10],[15,20]]))
        self.assertEqual(1, min_meeting_rooms_II([[4,9]]))


if __name__ == '__main__':
    unittest.main()