'''
    695. Max Area of Island
    You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
    You may assume all four edges of the grid are surrounded by water.
    The area of an island is the number of cells with a value 1 in the island.

    Return the maximum area of an island in grid. If there is no island, return 0..

    Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 50
        grid[i][j] is either 0 or 1.


    #LeetCode: https://leetcode.com/problems/max-area-of-island/

    Time Complexity: O(n x m)
    Space Complexity: O(n x m) for the visited set, same for the call stack of DFS.
'''

def max_area(grid):
    visited = set()
    result = 0

    for r in range(len(grid)):

        for c in range(len(grid[r])):
            if grid[r][c] == 1 and (r, c) not in visited:
                current = dfs(r, c, grid, visited)
                result = max(result, current)

    return result


def dfs(r, c, grid, visited):
    if (r < 0 or r >=len(grid)
        or c < 0 or c >= len(grid[r])
        or (r, c) in visited
        or grid[r][c] == 0):
        return 0

    area = grid[r][c]
    visited.add((r, c))
    neighbors = [[r - 1, c], [r + 1, c], [r, c + 1], [r, c - 1]]

    for n_row, n_col in neighbors:
        area += dfs(n_row, n_col, grid, visited)

    return area