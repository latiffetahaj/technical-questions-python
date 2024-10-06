'''
    130. Surrounded Regions
    You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
        Connect: A cell is connected to adjacent cells horizontally or vertically.
        Region: To form a region connect every 'O' cell.
        Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.

    A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

    Constraints:
        m == board.length
        n == board[i].length
        1 <= m, n <= 200
        board[i][j] is 'X' or 'O'.


    #LeetCode: https://leetcode.com/problems/surrounded-regions/

    Time Complexity: O(m x n)
    Space Complexity: O(m x n) worst case scenario on the recursion stack.
'''

# Key idea: REVERSE THINKING, think the opposite.
# Use a DFS to find the unsurrounded regions, mark them with another value different than 'X' or 'O', like 'T' for example.
# To find the unsurrounded regions we call DFS on first row, last row, first column, and last column.
# Then traverse the grid again, all the 'O's left mark them with X because that is a surrounded region.
# All the 'T' mark them back to 'O' because it is an unsurrounded region.

def mark_surrounded_regions(grid):
    ROWS, COLS = len(grid), len(grid[0])

    # Call DFS on first and last column, so move through the rows.
    for r in range(ROWS):
        dfs(r, 0, grid)
        dfs(r, COLS - 1, grid)

    # Call DFS on first and last row, so move through the columns.
    for c in range(COLS):
        dfs(0, c, grid)
        dfs(ROWS - 1, c, grid)




    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 'O':
                grid[r][c] = 'X'

            if grid[r][c] == 'T':
                grid[r][c] = 'O'

def dfs(r, c, grid):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] != 'O':
        return

    grid[r][c] = 'T'

    neighbors = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]

    for n_row, n_col in neighbors:
        dfs(n_row, n_col, grid)