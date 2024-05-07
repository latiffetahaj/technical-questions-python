'''
    647. Palindromic Substrings
    Given a string s, return the number of palindromic substrings in it.
    A string is a palindrome when it reads the same backward as forward.
    A substring is a contiguous sequence of characters within the string.

    Constraints:
        1 <= s.length <= 1000
        s consists of lowercase English letters.


    #LeetCode: https://leetcode.com/problems/palindromic-substrings/description/

    Time Complexity: O(n ^ 2)
    Space Complexity: O(1)
'''
# The algorithm uses a two pointers technique and dynamic programming.
# We start by using one character as a substring center and check if we can expand on both sides.
# This finds all the palindromic substring of odd length.
# To find the even palindromic substrings, we use two characters as a substring center and check if we can expand on both sides.

def count_palindromic_substrings(s):
    count = 0

    for i in range(len(s)):
        # Find odd length palindromic substrings
        l = i
        r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

        # Find even length palindromic substrings
        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

    return count
