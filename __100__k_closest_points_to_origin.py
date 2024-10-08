'''
    973. K Closest Points to Origin
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

    The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).

    You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


    Constraints:
        1 <= k <= points.length <= 10^4
        -10^4 <= xi, yi <= 10^4


    #LeetCode: https://leetcode.com/problems/k-closest-points-to-origin/

    Time Complexity: O(k logn)
    Space Complexity:  O(n)
'''

import heapq

def k_closest(points, k):
    min_heap = []
    result = []

    for x, y in points:
        dist = x ** 2 + y ** 2 # Even without square root, it satisfies the condition.
        min_heap.append([dist, x, y])

    # Heapify rearranges the element based on the first value, in this case the distance.
    heapq.heapify(min_heap)

    # Pop first k elements. This gives the first k points closest to the origin.
    for i in range(k):
        dist, x, y = heapq.heappop(min_heap)
        result.append([x, y])

    return result