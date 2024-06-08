'''
    295. Find Median from Data Stream
    The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
    Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.

    Constraints:
        -10^5 <= num <= 10^5
        There will be at least one element in the data structure before calling findMedian.
        At most 5 * 10^4 calls will be made to addNum and findMedian.


    #LeetCode: https://leetcode.com/problems/find-median-from-data-stream/

    Time Complexity: O(logn) to add a number, O(1) lookup for median.
    Space Complexity: O(n)
'''
import heapq
# The algorithm is to use two heaps. A max heap to store values that are smaller, and a min heap to store values that are larger.
# The heaps are set up this way to keep values that are needed to calculate median closer to each other, O(1) lookup.
class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        # By default push to the max_heap.
        heapq.heappush(self.max_heap, -1 * num)

        # If the top of max_heap is larger than the top of min_heap.
        if self.max_heap and self.min_heap and -1 * self.max_heap[0] > self.min_heap[0]:
            val = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # When two heaps differ in length by more than one.
        if len(self.max_heap) - len(self.min_heap) > 1:
            val = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        if len(self.min_heap) - len(self.max_heap) > 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * val)

    def findMedian(self):
        if len(self.max_heap) > len(self.min_heap):
            return -1 * self.max_heap[0]
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return (-1 * self.max_heap[0] + self.min_heap[0]) / 2
