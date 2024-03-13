'''
    242. Valid Anagram
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    #LeetCode: https://leetcode.com/problems/valid-anagram/description/

    Time Complexity: O(s + t)

    Space Complexity: O(s + t)
'''


def isAnagram(s,t):
    if s == None or t == None:
        return False

    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}

    for i in range(len(s)):
        s_map[s[i]] = 1 + s_map.get(s[i], 0)
        t_map[t[i]] = 1 + t_map.get(t[i], 0)

    for i in range(len(s)):
        if s[i] in s_map and s[i] in t_map:
            if s_map[s[i]] != t_map[s[i]]:
                return False
        else:
            return False

    return True





