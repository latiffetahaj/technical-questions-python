'''
    167. Two Sum II - Input Array Is Sorted
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
    Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
    The tests are generated such that there is exactly one solution.
    You may not use the same element twice.

Your solution must use only constant extra space.
    Constraints:
        2 <= numbers.length <= 3 * 104
        -1000 <= numbers[i] <= 1000
        numbers is sorted in non-decreasing order.
        -1000 <= target <= 1000
        The tests are generated such that there is exactly one solution.


    #LeetCode: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

    Time Complexity: O(n)
    Space Complexity:  O(1)
'''
# A simple two pointer technique.

def two_sum_II(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        current_sum = numbers[l] + numbers[r]
        if current_sum > target:
            # Move the right pointer to decrease the sum.
            r -= 1
        elif current_sum < target:
            # Move the left pointer to increase the sum.
            l += 1
        else:
            # Add 1 to l and r because the input array is 1-indexed.
            return [l + 1, r + 1]