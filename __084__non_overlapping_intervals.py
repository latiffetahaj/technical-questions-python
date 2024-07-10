'''
    435. Non-overlapping Intervals
    Given an array of intervals intervals where intervals[i] = [start-i, end-i],
    return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

    Constraints:
        1 <= intervals.length <= 10^5
        intervals[i].length == 2
        -5 * 10^4 <= start-i < end-i <= 5 * 10^4


    #LeetCode: https://leetcode.com/problems/merge-intervals/

    Time Complexity: O(nlogn) to sort.

    Space Complexity: O(1)
'''

def erase_overlapping_intervals(intervals):
    intervals.sort(key = lambda i: i[0])
    res = 0

    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        # Not overlapping case.
        if start >= prev_end:
            prev_end = end
        # When they overlap
        else:
            # Found one interval that needs to be removed.
            res += 1

            # When finding two intervals that overlap, favor the shorter one, and "remove" the larger one, because
            # the larger interval might interfere with more upcoming intervals.
            # In this case we don't remove any intervals, we just update the prev_end to point to the shorter end.
            prev_end = min(end, prev_end)


    return res