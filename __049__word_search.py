'''
    79. Word Search
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once.

    Constraints:
        m == board.length
        n = board[i].length
        1 <= m, n <= 6
        1 <= word.length <= 15
        board and word consists of only lowercase and uppercase English letters.


    #LeetCode: https://leetcode.com/problems/word-search/description/

    Time Complexity: O(n * m * word.length)
    Space Complexity: O(word.length) The number of calls in the call stack are at most word.length
'''

def has_word(grid, word):
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == word[0]:
                if dfs(grid, word, visited, i, j, ROWS, COLS, 0):
                    return True

    return False


# We follow a DFS algorithm to search for the given word in the grid.
def dfs(grid, word, visited, r, c, ROWS, COLS, i):
    # When the end of word is reached.
    if i >= len(word):
        return True

    if (not (r >= 0 and r < ROWS) # Out of bounds row check.
        or not (c >= 0 and c < COLS) # Out of bounds column check.
        or (r,c) in visited # If already visited.
        or grid[r][c] != word[i]): # If the characters don't match.
        return False

    visited.add((r,c))

    neighbors = [[r - 1,c], [r + 1, c], [r, c - 1], [r, c + 1]]

    for new_r, new_c in neighbors:
        if dfs(grid, word, visited, new_r, new_c, ROWS, COLS, i + 1):
            return True

    # When all the neighbors of current position return false, remove this position from the set and look for other paths.
    visited.remove((r,c))
    return False

