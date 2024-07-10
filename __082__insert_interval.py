'''
    57. Insert Interval
    You are given an array of non-overlapping intervals intervals where intervals[i] = [start-i, end-i] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
    You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

    Insert newInterval into intervals such that intervals is still sorted in ascending order by start-i and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

    Return intervals after the insertion.

    Note that you don't need to modify intervals in-place. You can make a new array and return it.

    Constraints:
        0 <= intervals.length <= 10^4
        intervals[i].length == 2
        0 <= start-i <= end-i <= 10^5
        intervals is sorted by start-i in ascending order.
        newInterval.length == 2
        0 <= start <= end <= 10^5

    #LeetCode: https://leetcode.com/problems/insert-interval/

    Time Complexity: O(n)

    Space Complexity: O(n)
'''

def insert_interval(intervals, new_interval):
    result = []

    for i in range(len(intervals)):
        # If the new_interval comes before the current, no overlapping.
        if new_interval[1] < intervals[i][0]:
            result.append(new_interval)
            return result + intervals[i:]
        # If the new_interval comes after the current, no overlapping.
        # The new_interval is not appended yet, cause it might overlap with future intervals.
        elif new_interval[0] > intervals[i][1]:
            result.append(intervals[i])
        # Overlapping case.
        # # Update the interval to take the minimum start, and maximum end.
        else:
            new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]

    # At this point if the function never returned, that means the new_interval is not appended.
    result.append(new_interval)

    return result