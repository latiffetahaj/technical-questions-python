'''
    33. Search in Rotated Sorted Array
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that
    the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target,
    return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.

    Constraints:
        1 <= nums.length <= 5000
        -10^4 <= nums[i] <= 10&4
        All values of nums are unique.
        nums is an ascending array that is possibly rotated.
        -10^4 <= target <= 10^4

    #LeetCode: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

    Time Complexity: O(log(n))

    Space Complexity: O(1)
'''

def search_rotated_array(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if target == nums[mid]:
            return mid

        elif nums[low] <= nums[mid]:
            if target >= nums[low] and target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        elif nums[mid] <= nums[high]:
            if target >= nums[mid] and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


