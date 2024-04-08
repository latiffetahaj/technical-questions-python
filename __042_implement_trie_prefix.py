'''
    208. Implement Trie (Prefix Tree)
    A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
    There are various applications of this data structure, such as autocomplete and spellchecker.

    Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

    Constraints:
        1 <= word.length, prefix.length <= 2000
        word and prefix consist only of lowercase English letters.
        At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

    #LeetCode: https://leetcode.com/problems/implement-trie-prefix-tree/description/
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self,word):
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.word = True

    def search(self,word):
        current = self.root

        for c in word:
            if c not in current.children:
                return False

            current = current.children[c]

        return current.word


    def startsWith(self,prefix):
        current = self.root

        for c in prefix:
            if c not in current.children:
                return False

            current = current.children[c]

        return True

