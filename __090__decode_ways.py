'''
    91. Decode Ways
    You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

            "1" -> 'A'
            "2" -> 'B'
            ...
            "25" -> 'Y'
            "26" -> 'Z'

    However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

    For example, "11106" can be decoded into:
            "AAJF" with the grouping (1, 1, 10, 6)
            "KJF" with the grouping (11, 10, 6)
            The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
            Note: there may be strings that are impossible to decode.

    Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.



    Constraints:
        1 <= s.length <= 100
        s contains only digits and may contain leading zero(s).


    #LeetCode: https://leetcode.com/problems/decode-ways/

    Time Complexity: O(n)

    Space Complexity: O(n)
'''
# Dp array will hold the number of ways to decode the string s at index i.
def num_decodings(s):
    dp = [0] * (len(s) + 1)

    dp[-1] = 1

    for i in range(len(s) - 1, -1, -1):
        if s[i] != '0':
            dp[i] = dp[i + 1]

            # If current and next character make up a number >0 and <= 26.
            if (i + 1) < len(s) and int(s[i: i + 2]) <= 26:
                dp[i] += dp[i + 2]

    return dp[0]