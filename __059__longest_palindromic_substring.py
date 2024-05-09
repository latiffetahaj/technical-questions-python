'''
    5. Longest Palindromic Substring
    Given a string s, return the longest palindromic substring in s.
    A string is palindromic if it reads the same forward and backward.


    Constraints:
        1 <= s.length <= 1000
        s consists of lowercase English letters.


    #LeetCode: https://leetcode.com/problems/longest-palindromic-substring/description/

    Time Complexity: O(n ^ 2)
    Space Complexity: O(1)
'''
# The same idea as in question 58 applies here. As we find all the palindromic substrings, we keep track of starting and ending index of the
# largest one.
# Then, we use these two indexes to slice the given input and return the correct result.

def longest_palindromic_substring(s):
    st_idx = 0
    end_idx = 0
    length = 0

    for i in range(len(s)):
        # Odd lengths.
        l = i
        r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > length:
                length = r - l + 1
                st_idx = l
                end_idx = r
            l -= 1
            r += 1

        # Even lengths.
        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > length:
                length = r - l + 1
                st_idx = l
                end_idx = r
            l -= 1
            r += 1

    return s[st_idx: end_idx + 1]
