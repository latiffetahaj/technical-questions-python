'''
    136. Single Number
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.


    Constraints:
        1 <= nums.length <= 3 * 10^4
        -3 * 10^4 <= nums[i] <= 3 * 10^4
        Each element in the array appears twice except for one element which appears only once.


    #LeetCode: https://leetcode.com/problems/single-number/

    Time Complexity: O(n)
    Space Complexity: O(1)
'''

def single_number(nums):
    result = 0

    for n in nums:
        result = result ^ n

    return result