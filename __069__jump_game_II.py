'''
    45. Jump Game II
    You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
    Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
            0 <= j <= nums[i] and
            i + j < n
    Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

    Constraints:
        1 <= nums.length <= 10^4
        0 <= nums[i] <= 1000
        It's guaranteed that you can reach nums[n - 1].

    A clarification:
    This questions asks to return the minimum number of jumps to reach the last index.
    At i-th index, the max_jump that you can make is i + nums[i].

    #LeetCode: https://leetcode.com/problems/jump-game-ii/

    Time Complexity: O(n)
    Space Complexity: O(1)
'''
# The idea is to follow a BFS algorithm.
# Starting from nums[0], find the maximum jump that we can make from index 0, then the level will be from [index 1, max_jump].
# We accomplish this by keeping a left and right pointer to determine the level.
# In each level, the min_step is incremeneted by one.

def min_jump(nums):
    res = 0
    l = r = 0

    # r needs to be less than the last index, because if r == last_index, then the goal is accomplished.
    while r < len(nums) - 1:
        farthest = 0
        # Find what's the max jump that we can make from the current level.
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])

        # Update the next level pointers accordingly.
        l = r + 1
        r = farthest

        res += 1

    return res