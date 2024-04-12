'''
    78. Subsets
    Given an integer array nums of unique elements, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.

    Constraints:
        1 <= nums.length <= 10
        -10 <= nums[i] <= 10
        All the numbers of nums are unique.


    #LeetCode: https://leetcode.com/problems/subsets/description/

    Time Complexity: O(2 ^ n)
    Space Complexity: O(2 ^ n)
'''
# The algorithm is as follows:
# In each step, there are two recursive calls.
# One that includes the current number.
# One that doesn't include the current number.

def subsets(nums):
    input_length = len(nums)
    sub_sets = []
    cur_set = []

    helper(0,cur_set,sub_sets,input_length,nums)

    return sub_sets

def helper(i,cur_set, sub_sets,input_length,nums):

    if i >= input_length:
        sub_sets.append(cur_set.copy())
        return

    #include nums[i]
    cur_set.append(nums[i])
    helper(i + 1, cur_set, sub_sets,input_length,nums)

    #exclude nums[i]
    cur_set.pop()
    helper(i + 1, cur_set, sub_sets,input_length,nums)

