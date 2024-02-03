'''
    1. Two Sum
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    #LeetCode: https://leetcode.com/problems/two-sum/description/

    Time Complexity: O(n)

    Space Complexity: O(n)
'''

'''
    From the given problem, each input guarantees exactly one solution, so there is no need to handle edge cases
'''
def two_sum(nums, target):
    hash_map = {}

    for index, number in enumerate(nums):
        remainder = target - number
        if remainder in hash_map:
            return [hash_map[remainder], index]

        hash_map[number] = index











    # hash_map = {}

    # for index, nr in enumerate(nums):
    #     remainder = target - nr

    #     if remainder in hash_map:
    #         return [hash_map[remainder], index]

    #     hash_map[nr] = index

