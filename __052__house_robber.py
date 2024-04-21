'''
    198. House Robber
    You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

    Constraints:
        1 <= nums.length <= 100
        0 <= nums[i] <= 400


    #LeetCode: https://leetcode.com/problems/house-robber/description/

    Time Complexity: O(n) where n = nums.length
    Space Complexity: O(1)
'''
# At each house, we have to make some choices,
# If we're at house i, we can't rob i + 1, the only two possibilites are to rob house at i + 2 or i + 3.
# We pick the choice that maximizes the amount.
# Looking back, the expression that relates these choices would be:

# house[i] = house[i] + max(house[i - 2], house[i - 3])

# So we update the house array based on this equation, and keep track of the max amount

# This is a dynamic programming apporach were subproblems help us solve the bigger problem.

def rob_houses(nums):
    amount = 0

    for i in range(len(nums)):

        house_1 = nums[i - 2] if i - 2 >= 0 else 0
        house_2 = nums[i - 3] if i - 3 >= 0 else 0

        nums[i] = nums[i] + max(house_1, house_2)
        amount = max(nums[i], amount)

    return amount