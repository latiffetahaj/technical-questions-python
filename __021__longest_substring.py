'''
    3. Longest Substring Without Repeating Characters
    Given a string s, find the length of the longest substring without repeating characters.

    Constraints:
        0 <= s.length <= 5 * 10^4
        s consists of English letters, digits, symbols and spaces.

    #LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

    Time Complexity: O(n)

    Space Complexity: O(n)
'''

def length_longest_substring(s):
    max_length = 0
    char_set = set()
    l = 0
    for r in range(len(s)):
        #when encountering a repeating character, remove all the previous character using the left pointer
        #until the current one is not in the char_set

        # a,b,c,d,e,c => when c is encountered remove a,b,c from char_set, then l = 3, s[l] = d
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1

        #then add the current character and recompute the max_length
        char_set.add(s[r])

        #if string is ab, and l = 0, r = 1, total_length of this substring would be r - l + 1 = 1 - 0 + 1 = 2
        max_length = max(max_length, r - l + 1)

    return max_length
