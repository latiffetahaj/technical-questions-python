'''
    139. Word Break
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

    Note that the same word in the dictionary may be reused multiple times in the segmentation.

    Constraints:
        1 <= s.length <= 300
        1 <= wordDict.length <= 1000
        1 <= wordDict[i].length <= 20
        s and wordDict[i] consist of only lowercase English letters.
        All the strings of wordDict are unique.


    #LeetCode: https://leetcode.com/problems/word-break/description/

    Time Complexity: O(n * m) where n - length of the input string, m - number of words in the dictionary.
    Space Complexity: O(1)
'''

# Iterate over the input from the end.
    # Reason why traversing from the end.
    # Example: s = "starssta". word_dict = ['sta', 'stars'].
    # If sta is matched first from the left, then the remaining portion of the string 'rssta' will not match to any of the words in dictionary.
    # Therefore to avoid this, we traverse from the end.

# Then, for each position in the input, iterate over the dictionary.
# Calculate the length of the current word, then check if s[i - length + 1: i + 1] portion of the string matches any words from the dictionary.

def word_break(s, word_dict):

    i = len(s) - 1
    while i >= 0:

        is_matched = False

        for word in word_dict:
            current_length = len(word)

            # The last portion of the string should match at least one of the words from the dictionary.
            # When it matches, decrease i, and break
            if s[i - current_length + 1: i + 1] == word:
                is_matched = True
                i = i - current_length
                break

        # When none of the words matched the last portion of the string, return False immediately.
        if not is_matched:
            return False


    return True