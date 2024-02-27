'''
    424. Longest Repeating Character Replacement
    You are given a string s and an integer k.
    You can choose any character of the string and change it to any other uppercase English character.
    You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter you can get after performing the above operations

    Constraints:
        1 <= s.length <= 10^5
        s consists of only uppercase English letters.
        0 <= k <= s.length

    #LeetCode: https://leetcode.com/problems/longest-repeating-character-replacement/description/

    Time Complexity: O(26 * n) ==> O(n)

    Space Complexity: O(n)
'''
def character_replacement(s,k):
    char_count = {}
    result = 0

    l = 0
    for r in range(len(s)):
        char_count[s[r]] = 1 + char_count.get(s[r], 0)

        #current window is not valid if the length - most_frequent_element is larger than k,
        #that means k replacements are not sufficient to make all characters the same(repeating)
        #if window invalid, then update the frequency map of that character where the left pointer is pointing
        # then move for one position to the right
        if (r - l + 1) - max(char_count.values()) > k:
            char_count[s[l]] -= 1
            l += 1

        result = max(result, r - l + 1)

    return result