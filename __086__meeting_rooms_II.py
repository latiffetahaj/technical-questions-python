'''
    Meeting Schedule II
    Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
    find the minimum number of days required to schedule all meetings without any conflicts.

    Note:
        (0,8),(8,10) is not considered a conflict at 8.

    Constraints:
        0 <= intervals.length <= 500
        0 <= intervals[i].start < intervals[i].end <= 1,000,000


    #LeetCode: https://leetcode.com/problems/meeting-rooms-ii/

    Time Complexity: O(nlogn) to sort.

    Space Complexity: O(n)
'''
# This approach finds the maximum of meetings that conflict at any point
# And this tells the minimum number of days that we need to arrange those meetings so no conflict would occur.
def min_meeting_rooms(intervals):

    startings = sorted([i[0] for i in intervals])
    endings = sorted([i[1] for i in intervals])

    count = result = 0
    s = e = 0

    while s < len(startings):
        # When the meeting starts.
        if startings[s] < endings[e]:
            count += 1
            s += 1
        # When a meeting ends.
        else:
            count -= 1
            e += 1

        result = max(result, count)

    return result

import heapq

# Another approach is to use a min heap, that keeps the endings of the intervals.
# The idea to keep the minimum on top, is to keep track of the meeting conflicts.

# Same time and space complexity as the first solution above.

def min_meeting_rooms_II(intervals):
    if not intervals:
        return 0

    intervals.sort(key = lambda i:i[0])
    result = 1
    endings = []
    heapq.heappush(endings, intervals[0][1])

    for start, end in intervals[1:]:
        # If there's no conflict, pop the minimum ending so far.
        if start >= endings[0]:
            heapq.heappop(endings)
        else:
            # When conflict occurs.
            result += 1

        # Push the new ending to the heap.
        heapq.heappush(endings, end)

    return result


