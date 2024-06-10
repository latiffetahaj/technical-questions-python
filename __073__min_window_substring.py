'''
    76. Minimum Window Substring
    Given two strings s and t of lengths m and n respectively,
    return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
    If there is no such substring, return the empty string "".
    The testcases will be generated such that the answer is unique.
    Return the length of the longest substring containing the same letter you can get after performing the above operations

    Constraints:
        m == s.length
        n == t.length
        1 <= m, n <= 10^5
        s and t consist of uppercase and lowercase English letters.

    #LeetCode: https://leetcode.com/problems/minimum-window-substring/

    Time Complexity: O(m + n)

    Space Complexity: O(m + n)
'''
# The idea is to keep track of two hashmaps. One from the sliding window, the other with frequencies of the characters in t.
# To make the comparison of the hashmaps faster, we keep two variables that hold the number of unique characters in t and in window.

def min_window(s, t):
    countT = {}
    window = {}

    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    max_w_size = len(s) + 1
    need = len(countT)
    have = 0
    l = 0
    start = 0
    end = 0

    for r in range(len(s)):
        c = s[r]

        window[c] = 1 + window.get(c, 0)

        # This means that one character requirement is fulfilled so increment have by one.
        if c in countT and countT[c] == window[c]:
            have += 1

        while have == need:
            # If a smaller window found.
            if r - l + 1 < max_w_size:
                start = l
                end = r

                max_w_size = r - l + 1

            # Remove the character where left pointer is from the window.
            window[s[l]] -= 1

            # If the requirement for this character are not being met, decrease have by one.
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1

            l += 1

    # If the max window has still the inital value, that means the t isn't found in s.
    if max_w_size == len(s) + 1:
        return ""
    else:
        return s[start: end + 1]
