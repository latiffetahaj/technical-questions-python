'''
    53. Maximum Subarray
    Given an integer array nums, find the subarray with the largest sum, and return its sum.

    Constraints:
        1 <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4


    #LeetCode: https://leetcode.com/problems/maximum-subarray/

    Time Complexity: O(n)
    Space Complexity: O(1)
'''
# The solution uses Kadane's Algorithm.
# This is also a dynamic programming algorithm.
# Each i-th positon tells the maximum sum of the subarray ending at that position.
# The recurrence relation is as follows:
# nums[i] = max(nums[i], nums[i] + nums[i - 1])

def max_sum_subarray(nums):
    max_sum = nums[0]

    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i - 1])
        max_sum = max(nums[i], max_sum)

    return max_sum
