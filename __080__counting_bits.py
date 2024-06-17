'''
    338. Counting Bits
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
    ans[i] is the number of 1's in the binary representation of i.

    Constraints:
        0 <= n <= 105

    #LeetCode: https://leetcode.com/problems/counting-bits/

    Time Complexity: O(n)

    Space Complexity: O(n)
'''
# The linear time solution is an dynamic programming solution.
# We build the result as we go. The offset holds the relationship between the current i and previous ones that are calculated.
# The main idea is that everytime we can double the offset, that means a new most significant bit has been encountered.
# 0 - 000
# 1 - 001
# 2 - 010
# 3 - 011
# 4 - 100
# Initially offset = 1
# For 1, nr_one_bits = 1 + dp[0] = 1
# Now from [2,3] offset changes to 2, because they depend on the values, two indexes before.
# From [4,7] offset = 4
# From [8, 16] offest = 8 and so on.

def counting_bits(n):
    dp = [0] * (n + 1)

    offset = 1

    for i in range(1, n + 1):
        # Update the offset only if we can double it.
        if offset * 2 == i:
            offset *= 2

        dp[i] = 1 + dp[i - offset]


    return dp