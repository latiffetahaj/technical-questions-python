'''
    211. Design Add and Search Words Data Structure
    Design a data structure that supports adding new words and finding if a string matches any previously added string.

    Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

    Constraints:
        1 <= word.length <= 25
        word in addWord consists of lowercase English letters.
        word in search consist of '.' or lowercase English letters.
        There will be at most 2 dots in word for search queries.
        At most 10^4 calls will be made to addWord and search.

    #LeetCode: https://leetcode.com/problems/design-add-and-search-words-data-structure/

    Time Complexity: addWord(): O(n) where n = word.length
                    search(): O(26*26*n) because there are at most 2 dots in word.

    Space Complexity: O(n) where n = word.length
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.isWord = True

    def search(self, word):

        return self.dfs(0, self.root, word)




    def dfs(self, w_idx, current, word):

        for i in range(w_idx, len(word)):
            if word[i] == '.':
                for child in current.children.values():
                    if self.dfs(i + 1, child, word):
                        return True

                return False
            else:
                if word[i] not in current.children:
                    return False

                current = current.children[word[i]]

        return current.isWord




