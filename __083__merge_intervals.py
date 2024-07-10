'''
    56. Merge Intervals
    Given an array of intervals where intervals[i] = [start-i, end-i],
    merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

    Constraints:
        1 <= intervals.length <= 10^4
        intervals[i].length == 2
        0 <= start-i <= end-i <= 10^4


    #LeetCode: https://leetcode.com/problems/merge-intervals/

    Time Complexity: O(nlogn) to sort.

    Space Complexity: O(n) to store the result.
'''
def merge_intervals(intervals):
    # Sort by the start value in each interval.
    intervals.sort(key = lambda i: i[0])

    output = []
    output.append(intervals[0])

    for i in range(1, len(intervals)):
        # Intervals overlap.
        if intervals[i][0] <= output[-1][1]:
            output[-1][1] = max(intervals[i][1], output[-1][1])
        else:
            output.append(intervals[i])

    return output