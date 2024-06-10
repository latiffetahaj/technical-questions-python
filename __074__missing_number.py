'''
    268. Missing Number
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

    Constraints:
        n == nums.length
        1 <= n <= 104
        0 <= nums[i] <= n
        All the numbers of nums are unique.

    #LeetCode: https://leetcode.com/problems/missing-number/

    Time Complexity: O(n)

    Space Complexity: O(1)
'''
# This solution follows a similar approach to the question __062__ missing number.
# To use the bit manipulation technique:
# We use index values as well to simulate that all the numbers appear twice except one.

def missing_number(nums):
    n = len(nums)

    # We initalize result to n because indexes appear from 0 to n-1.
    # The net effect of XOR twice with the same number is zero, so at the end the result will hold the missing number.
    result = n
    for i in range(n):
        result = result ^ i ^ nums[i]

    return result