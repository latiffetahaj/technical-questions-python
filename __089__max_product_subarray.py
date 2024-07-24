'''
    152. Maximum Product Subarray
    Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

    Note:
        (0,8),(8,10) is not considered a conflict at 8.

    Constraints:
        1 <= nums.length <= 2 * 10^4
        -10 <= nums[i] <= 10
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


    #LeetCode: https://leetcode.com/problems/maximum-product-subarray/description/

    Time Complexity: O(n)

    Space Complexity: O(1)
'''

def max_product_subarray(nums):
    result = nums[0]
    current_min = nums[0]
    current_max = nums[0]

    for i in range(1, len(nums)):
        # Save current max before modifying.
        temp = current_max

        # Include the current_min for cases when current_min * nums[i] > 0, when current_min < 0 and nums[i] < 0.
        current_max = max(nums[i], nums[i] * current_max, nums[i] * current_min)

        # Same reasons as above for current_max, use the temp variable in this case.
        current_min = min(nums[i], nums[i] * current_min, temp * nums[i])

        result = max(current_max, current_min, result)

    return result



