'''
    Meeting Schedule
    Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
    determine if a person could add all meetings to their schedule without any conflicts.

    Note:
        (0,8),(8,10) is not considered a conflict at 8.

    Constraints:
        0 <= intervals.length <= 500
        0 <= intervals[i].start < intervals[i].end <= 1,000,000


    #LeetCode: https://leetcode.com/problems/meeting-rooms/

    Time Complexity: O(nlogn) to sort.

    Space Complexity: O(1)
'''

def can_attend_meetings(intervals):
    intervals.sort(key = lambda i: i[0])

    for i in range(1, len(intervals)):
        current_start = intervals[i][0]
        prev_end = intervals[i - 1][1]

        # When overlap is found.
        if current_start < prev_end:
            return False

    return True