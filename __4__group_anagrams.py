'''
    49. Group Anagrams
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Constraints:
    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

    #LeetCode: https://leetcode.com/problems/group-anagrams/description/

    Time Complexity: O (n * m)

    Space Complexity: O(n * m), where n - nr of strings, m - length of each string
'''

from collections import defaultdict

def groupAnagrams(strs):
    if strs is None:
        return None

    result = defaultdict(list)

    for s in strs:
        count = [0] * 26 #a...z

        for c in s:
            count[ord(c) - ord("a")] += 1

        result[tuple(count)].append(s)

    return list(result.values())
