'''
    704. Binary Search
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
    If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.

    Constraints:
        1 <= nums.length <= 10^4
        -10^4 < nums[i], target < 10^4
        All the integers in nums are unique.
        nums is sorted in ascending order.

    #LeetCode: https://leetcode.com/problems/binary-search/description/

    Time Complexity: O(log(n))

    Space Complexity: O(1)
'''

def binary_search(nums,target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2 #avoids overflow in very large input sizes.

        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
        else:
            return mid

    return -1