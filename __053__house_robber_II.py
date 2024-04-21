'''
    213. House Robber II
    You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed.
    All houses at this place are arranged in a circle.
    That means the first house is the neighbor of the last one.

    Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

    Constraints:
        1 <= nums.length <= 100
        0 <= nums[i] <= 1000


    #LeetCode: https://leetcode.com/problems/house-robber-ii/description/

    Time Complexity: O(n) where n = nums.length
    Space Complexity: O(1)
'''
from __052__house_robber import rob_houses

# This question is similiar to the house robber 1, solution can be found at __052__house_robber.py
# To avoid stealing two adjacent houses, the first and the last one, we use the solution of house robber 1 two times

# 1: Using input from [0: length - 1, not inclusive] so if the input was of houses from 0 - 9 this would be [0:8]
# 2: Using input from [1: till the end], from the example above [1:]

def rob_houses_II(nums):

    # Include nums[0] to cover the case when length(nums) == 1.

    return max(nums[0], rob_houses(nums[1:]), rob_houses(nums[0: len(nums) - 1]))