'''
    212. Word Search II
    Given an m x n board of characters and a list of strings words, return all words on the board.
    Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once in a word.

    Constraints:
        m == board.length
        n == board[i].length
        1 <= m, n <= 12
        board[i][j] is a lowercase English letter.
        1 <= words.length <= 3 * 10^4
        1 <= words[i].length <= 10
        words[i] consists of lowercase English letters.
        All the strings of words are unique.


    #LeetCode: https://leetcode.com/problems/word-search-ii/


    Time Complexity: O(n x m * 4 ^ (n x m))
    Space Complexity: O(10 * words.length) to built the Trie, O(n x m) on the call stack.
'''

from __000__trie_implementation import Trie


# The algorithm is to built a trie, and then do a DFS on each cell of the board.
# Trie helps to search for all words simultaneously.
def find_words(words, board):
    trie = Trie()
    visit = set()
    res = []

    for w in words:
        trie.insert(w)

    for r in range(len(board)):
        for c in range(len(board[r])):
            dfs(r, c, "", board, visit, res, trie.root)

    return res



def dfs(r, c, word, board, visit, res, node):
    if (r < 0 or r >= len(board)
        or c < 0 or c >= len(board[r])
        or (r, c) in visit
        or board[r][c] not in node.children):
        return

    visit.add((r, c))
    word += board[r][c]
    node = node.children[board[r][c]]

    if node.word:
        res.append(word)
        # Avoid adding the same word twice.
        node.word = False

    dfs(r - 1, c, word, board, visit, res, node)
    dfs(r + 1, c, word, board, visit, res, node)
    dfs(r, c - 1, word, board, visit, res, node)
    dfs(r, c + 1, word, board, visit, res, node)

    visit.remove((r, c))