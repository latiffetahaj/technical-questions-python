'''
    703. Kth Largest Element in a Stream
    Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Implement KthLargest class:

    KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


    Constraints:
        1 <= k <= 10^4
        0 <= nums.length <= 10^4
        -10^4 <= nums[i] <= 10^4
        -10^4 <= val <= 10^4
        At most 10^4 calls will be made to add.
        It is guaranteed that there will be at least k elements in the array when you search for the kth element.


    #LeetCode: https://leetcode.com/problems/kth-largest-element-in-a-stream/

    Time Complexity: O(1) to find the kth-largest element in a stream.
                    O(n) to initialize the heap of size n + O(log(n-k)) pops from the heap, overall O(n).

    Space Complexity: O(n) where n is the input size.
'''
import heapq

# The core idea is to use a min heap data structure of size k.
# In this way, to find the kth largest element in a stream will be an O(1)
class KthLargest:

    def __init__(self, k, nums):
        self.min_heap = nums
        self.k = k

        #Heapify the input array
        heapq.heapify(self.min_heap)

        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)


    def add(self, val):
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]