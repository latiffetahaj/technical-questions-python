'''
    125. Valid Palindrome
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
    Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    #LeetCode: https://leetcode.com/problems/valid-palindrome/

    Time Complexity: O(n)

    Space Complexity: O(1)
'''

def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if not s[i].isalnum() and not s[j].isalnum():
            i += 1
            j -= 1
        elif not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1

    return True