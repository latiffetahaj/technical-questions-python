'''
    55. Jump Game
    You are given an integer array nums.
    You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
    Return true if you can reach the last index, or false otherwise.

    Constraints:
        1 <= nums.length <= 10^4
        0 <= nums[i] <= 10^5


    #LeetCode: https://leetcode.com/problems/jump-game/

    Time Complexity: O(n)
    Space Complexity: O(1)
'''
# The algorithm is to traverse from the end, and at each i-th step to check if we can reach the goal from that position.
# If so, shift the goal to that position.
# If at the end goal is at position 0, return True, otherwise return False.
def can_jump(nums):
    goal = len(nums) - 1 # Last index is the goal to reach.

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return goal == 0
