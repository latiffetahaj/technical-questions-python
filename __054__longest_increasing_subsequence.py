'''
    300. Longest Increasing Subsequence
    Given an integer array nums, return the length of the longest strictly increasing subsequence.

    A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

    Constraints:
        1 <= nums.length <= 2500
        -104 <= nums[i] <= 104


    #LeetCode: https://leetcode.com/problems/longest-increasing-subsequence/description/

    Time Complexity: O(n ^ 2) where n = nums.length
    Space Complexity: O(n)
'''
# A dynamic programming approach
# Allocate a new array with the same size as input, this will keep the longest increasing subsequence at each index.
# Initially, the default values are all 1s, because by default each individual element can be a increasing subsequence of length 1.

# Loop through the input array in two ways.
# The outer loop goes from the beginning to the end.
# The inner loop goes from the beginning up to the current index.
# If we find an element that is less than the current element, we update the length as follows.

# LIS (longest increasing subsequence): LIS[i] = max(LIS[i], 1 + LIS[j], where j is the position where nums[j] < nums[i]).

def length_of_LIS(nums):
    LIS = [1] * len(nums)
    result = 1

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

        result = max(result, LIS[i])

    return result
