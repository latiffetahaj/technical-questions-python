'''
    217. Contains Duplicate
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    #LeetCode: https://leetcode.com/problems/contains-duplicate/description/

    Time Complexity: O(n)

    Space Complexity: O(n)
'''

def contains_duplicate(nums):

    if nums == None:
        return None
    hash_map = set()

    for element in nums:
        if element in hash_map:
            return True
        else:
            hash_map.add(element)

    return False