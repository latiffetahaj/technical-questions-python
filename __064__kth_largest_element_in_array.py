'''
    215. Kth Largest Element in an Array
    Given an integer array nums and an integer k, return the kth largest element in the array.
    Note that it is the kth largest element in the sorted order, not the kth distinct element.
    Can you solve it without sorting?

    Constraints:
        1 <= k <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4


    #LeetCode: https://leetcode.com/problems/kth-largest-element-in-an-array/

    Time Complexity: O(n)
    Space Complexity: O(1)
'''
import heapq

def find_kth_largest(nums, k):
    heapq.heapify(nums)

    while len(nums) > k:
        heapq.heappop(nums)

    return nums[0]