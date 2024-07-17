'''
    1143. Longest Common Subsequence
    Given two strings text1 and text2, return the length of their longest common subsequence.
    If there is no common subsequence, return 0.

    A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".
    A common subsequence of two strings is a subsequence that is common to both strings.

    Constraints:
        1 <= text1.length, text2.length <= 1000
        text1 and text2 consist of only lowercase English characters.


    #LeetCode: https://leetcode.com/problems/longest-common-subsequence/

    Time Complexity: O(n x m), where n = text1.length, m = text2.length

    Space Complexity: O(n x m)
'''
# The main idea behing this approach:
#    a b c
# a  x x x
# b  x x x

# Given this small example to find the longest common subsequence between abc and ac. We initialize a grid of 0s of (n + 1) by (m + 1)
#    a b c
# a  0 0 0 0
# b  0 0 0 0
#    0 0 0 0
# We start working from the bottom to top.
# Two cases only:
# If the characters at [i][j] position match, that means we found a common character so the math follows as:
# [i][j] = 1 + [i + 1][j + 1], so we look at the diagonal on the bottom right.
# Else:
# [i][j] = max([i][j + 1], [i + 1][j]), we take the max value from the right and down.

def longest_common_subsequence(text1, text2):
    dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):

        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]


# Since we are using only the information of the row below, we can reduce the space complexity to O(2m) => O(m)

def longest_common_subsequence_II(text1, text2):
    dp = [0] * (len(text2) + 1)

    for i in range(len(text1) - 1, -1, -1):

        temp = [0] * (len(text2) + 1)

        for j in range(len(text2) - 1, -1, - 1):
            if text1[i] == text2[j]:
                temp[j] = 1 + dp[j + 1]
            else:
                temp[j] = max(temp[j + 1], dp[j])

        dp = temp

    return dp[0]