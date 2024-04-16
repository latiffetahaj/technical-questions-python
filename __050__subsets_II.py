'''
    90. Subsets II
    Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.

    Constraints:
        1 <= nums.length <= 10
        -10 <= nums[i] <= 10


    #LeetCode: https://leetcode.com/problems/subsets-ii/description/

    Time Complexity: O(2 ^ n)
    Space Complexity: O(2 ^ n)
'''

def subsets_II(nums):

    # Sorting the input makes it easier to skip duplicates
    nums.sort()
    result = []
    current = []

    generate_subsets(nums,result,current,0)

    return result

def generate_subsets(nums, result, current, starting_index):

    # Append the current subset.
    result.append(current.copy())

    # Base case.
    if starting_index >= len(nums):
        return

    i = starting_index
    while i < len(nums):
        current.append(nums[i])

        # Recursive call on the i + 1
        generate_subsets(nums, result, current, i + 1)

        # Remove the current element for the future subsets.
        current.pop()

        # Skip duplicates
        while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        # Increment i for the next iteration.
        i += 1

    return

