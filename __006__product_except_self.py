'''
    238. Product of Array Except Self

    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    Constraints:
    You must write an algorithm that runs in O(n) time and without using the division operation.

    #LeetCode: https://leetcode.com/problems/product-of-array-except-self/description/

    Time Complexity: O(3n) ==> O(n)

    Space Complexity: O(3n) ==> O(n)

'''

def product_except_self(nums):
    pre_fix = []
    post_fix = []
    result = []

    #calculate the prefix
    total_product = 1
    for n in nums:
        total_product *= n
        pre_fix.append(total_product)

    #print(pre_fix)
    #calculate the postfix from the end
    total_product = 1
    for i in range(len(nums) - 1, -1, -1):
        total_product *= nums[i]
        post_fix.insert(0,total_product)

    #print(post_fix)
    #build the result array
    for i in range(len(nums)):
        left_product = pre_fix[i - 1] if i > 0 else 1
        right_product = post_fix[i + 1] if (i < (len(nums)) - 1) else 1
        result.append(left_product * right_product)

    return result


